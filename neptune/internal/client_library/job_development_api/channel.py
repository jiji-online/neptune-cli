# -*- coding: utf-8 -*-
#
# Copyright (c) 2016, deepsense.io
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import enum
import logging
import math

from future.builtins import object

from neptune.internal.client_library.job_development_api.channel_params import ChannelParams
from neptune.internal.client_library.job_development_api.channel_type import ChannelType
from neptune.internal.client_library.job_development_api.image import Image
from neptune.internal.common.models.parameters_validation import (
    float_conv,
    of_type_validator,
    one_of_type_validator,
    one_of_validator,
    text_conv,
    validate,
    validate_coordinates
)


class Channel(object):
    """
    A channel is a named series of two-dimensional points belonging to a job.

    Each point’s abscissa (point’s X) is always a floating point number.

    The ordinate’s (point’s Y) type depends on channel’s type, which can be either:

    - Numeric - Y is represented by a floating point number.
    - Text - Y is represented by any text value.
    - Image - Y is represented by an image with name and description.

    The points, called channel’s values, represent a function,
    so X-coordinates have to be unique in a channel.
    Moreover, the points generated by jobs during execution must be in order
    so that the X-coordinates increase.
    """

    MAX_TEXT_VALUE_LENGTH = 1000

    def __init__(self,
                 channel_values_service, _id, name, channel_type, auto_increment_type):
        """
        Create a new Channel.

        .. warning:: For internal use only.

           Use :py:attr:`~neptune.Job.create_channel` instead to create a new channel.

        :param name: A channel name. It must be unique in the scope of a specific job.
        :param channel_type: Type of the channel.
        :type name: unicode
        :type channel_type: neptune.ChannelType
        """
        self._id = _id
        self._name = name
        self._type = channel_type
        self._logger = logging.getLogger(__name__)
        self._channel_values_service = channel_values_service
        self._auto_increment_type = auto_increment_type
        self.collision_count = 0

    def __str__(self):
        return 'Channel(name: {})'.format(self.name)

    def reset(self):
        self._channel_values_service.reset_channel(self)

    def delete(self):
        self._channel_values_service.delete_channel(self)

    @validate_coordinates
    def send(self, x=None, y=None):
        """
        Given values of X and Y, sends a channel value to Neptune.

        :param x: The value of channel value's X-coordinate.
            Values of the x parameter should be strictly increasing for consecutive calls.
        :param y: The value of channel value's Y-coordinate.
            Accepted types: float for :py:attr:`~neptune.series_type.NUMERIC`,
            str/unicode for :py:attr:`~neptune.series_type.TEXT`,
            neptune.Image for :py:attr:`~neptune.series_type.IMAGE`.

            If this parameter is None, the value passed in x parameter is used as Y-coordinate and
            the last X-coordinate incremented by one will be used as X-coordinate

            If Y-coordinate is of type TEXT it will be truncated to no more than 1000 characters.
        """

        if y is None:
            x, y = None, x

        if self.type == ChannelType.NUMERIC:
            self._send_numeric(x, y)
        elif self.type == ChannelType.TEXT:
            self._send_text(x, y)
        elif self.type == ChannelType.IMAGE:
            self._send_image(x, y)

    @validate(x=one_of_type_validator([one_of_validator([None]), float_conv]), y=float_conv)
    def _send_numeric(self, x, y):
        self._validate_and_send(x, y)

    @validate(x=one_of_type_validator([one_of_validator([None]), float_conv]), y=text_conv)
    def _send_text(self, x, y):
        y = y[:self.MAX_TEXT_VALUE_LENGTH]
        self._validate_and_send(x, y)

    @validate(x=one_of_type_validator([one_of_validator([None]), float_conv]),
              y=of_type_validator(Image))
    def _send_image(self, x, y):
        self._validate_and_send(x, y)

    def _validate_and_send(self, x, y):

        if self._check_if_not_supported_value(x):
            self._log_unsupported_value(x, x, y)
        elif self._check_if_not_supported_value(y):
            self._log_unsupported_value(y, x, y)
        else:
            self._channel_values_service.send(self, x, y)

    def _check_if_not_supported_value(self, value):
        return isinstance(value, float) and (math.isinf(value) or math.isnan(value))

    def _log_unsupported_value(self, incorrect_value, x, y):
        self._logger.warning(
            "Value %s is not supported. Point (x=%s, y=%s) cannot be sent to channel '%s'.",
            incorrect_value, repr(x), repr(y), self.name)

    @property
    def id(self):
        """
        Gets id of this Channel.

        :return: The id of this Channel.
        :rtype: uuid
        """
        return self._id

    @property
    def name(self):
        """
        Gets name of this Channel.
        It must be unique in the scope of a specific job.

        :return: A channel name.
        :rtype: str
        """
        return self._name

    @property
    def type(self):
        """
        Gets type of this Channel.

        :return: The type of this Channel.
        :rtype: neptune.ChannelType
        """
        return self._type

    @property
    def auto_increment_type(self):
        """
        Gets auto increment type of this Channel.

        :return: The auto increment type of this Channel.
        :rtype: AutoIncrementType
        """
        return self._auto_increment_type

    def __eq__(self, other):
        return self.__class__ == other.__class__ and \
               self.id == other.id and \
               self.name == other.name and \
               self.type == other.type and \
               self.auto_increment_type == other.auto_increment_type

    def __hash__(self):
        return hash((self.id, self.name, self.type, self.auto_increment_type))


class AutoIncrementType(str, enum.Enum):
    """
    Next natural integer
    """
    Int = 'int'

    """
    Microseconds since channel creation
    """
    Micro = 'micro'


class ChannelFactory(object):

    def __init__(self, api_service, experiment_id, channel_values_service):
        self.__api_service = api_service
        self.__experiment_id = experiment_id
        self.__channel_values_service = channel_values_service
        self.__stdout_channel = None
        self.__stderr_channel = None

    def create(self, name, channel_type=ChannelType.NUMERIC, auto_increment_type=AutoIncrementType.Int):
        swagger_channel = self.__api_service.create_channel(self.__experiment_id, ChannelParams(name, channel_type))
        return self.__channel_from_api_model(swagger_channel, auto_increment_type)

    def get_or_create_stdout_channel(self):
        if self.__stdout_channel is None:
            self.__stdout_channel = self.__create_system_text_channel(name=u'stdout')
        return self.__stdout_channel

    def get_or_create_stderr_channel(self):
        if self.__stderr_channel is None:
            self.__stderr_channel = self.__create_system_text_channel(name=u'stderr')
        return self.__stderr_channel

    def wait_for_threads(self):
        self.__channel_values_service.wait_for_threads()

    def __channel_from_api_model(self, swagger_channel, auto_increment_type):
        return Channel(
            channel_values_service=self.__channel_values_service,
            _id=swagger_channel.id,
            name=swagger_channel.name,
            channel_type=swagger_channel.channel_type,
            auto_increment_type=auto_increment_type
        )

    def __create_system_text_channel(self, name):
        swagger_stderr_channel = self.__api_service.create_system_channel(
            experiment_id=self.__experiment_id, channel_params=ChannelParams(name, ChannelType.TEXT))
        return self.__channel_from_api_model(swagger_stderr_channel, auto_increment_type=AutoIncrementType.Micro)
