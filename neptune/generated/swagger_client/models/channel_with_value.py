# coding: utf-8

"""
Copyright 2016 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems
import re


class ChannelWithValue(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, x=None, y=None, channel_type=None, channel_name=None, channel_id=None):
        """
        ChannelWithValue - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'x': 'float',
            'y': 'str',
            'channel_type': 'ChannelType',
            'channel_name': 'str',
            'channel_id': 'str'
        }

        self.attribute_map = {
            'x': 'x',
            'y': 'y',
            'channel_type': 'channelType',
            'channel_name': 'channelName',
            'channel_id': 'channelId'
        }

        self._x = x
        self._y = y
        self._channel_type = channel_type
        self._channel_name = channel_name
        self._channel_id = channel_id

    @property
    def x(self):
        """
        Gets the x of this ChannelWithValue.


        :return: The x of this ChannelWithValue.
        :rtype: float
        """
        return self._x

    @x.setter
    def x(self, x):
        """
        Sets the x of this ChannelWithValue.


        :param x: The x of this ChannelWithValue.
        :type: float
        """
        
        self._x = x

    @property
    def y(self):
        """
        Gets the y of this ChannelWithValue.


        :return: The y of this ChannelWithValue.
        :rtype: str
        """
        return self._y

    @y.setter
    def y(self, y):
        """
        Sets the y of this ChannelWithValue.


        :param y: The y of this ChannelWithValue.
        :type: str
        """
        
        self._y = y

    @property
    def channel_type(self):
        """
        Gets the channel_type of this ChannelWithValue.


        :return: The channel_type of this ChannelWithValue.
        :rtype: ChannelType
        """
        return self._channel_type

    @channel_type.setter
    def channel_type(self, channel_type):
        """
        Sets the channel_type of this ChannelWithValue.


        :param channel_type: The channel_type of this ChannelWithValue.
        :type: ChannelType
        """
        
        self._channel_type = channel_type

    @property
    def channel_name(self):
        """
        Gets the channel_name of this ChannelWithValue.


        :return: The channel_name of this ChannelWithValue.
        :rtype: str
        """
        return self._channel_name

    @channel_name.setter
    def channel_name(self, channel_name):
        """
        Sets the channel_name of this ChannelWithValue.


        :param channel_name: The channel_name of this ChannelWithValue.
        :type: str
        """
        
        self._channel_name = channel_name

    @property
    def channel_id(self):
        """
        Gets the channel_id of this ChannelWithValue.


        :return: The channel_id of this ChannelWithValue.
        :rtype: str
        """
        return self._channel_id

    @channel_id.setter
    def channel_id(self, channel_id):
        """
        Sets the channel_id of this ChannelWithValue.


        :param channel_id: The channel_id of this ChannelWithValue.
        :type: str
        """
        
        self._channel_id = channel_id

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other



