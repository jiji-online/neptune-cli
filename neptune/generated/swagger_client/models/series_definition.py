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


class SeriesDefinition(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, label=None, channel_name=None, alias_id=None, series_type=None):
        """
        SeriesDefinition - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'label': 'str',
            'channel_name': 'str',
            'alias_id': 'str',
            'series_type': 'SeriesType'
        }

        self.attribute_map = {
            'label': 'label',
            'channel_name': 'channelName',
            'alias_id': 'aliasId',
            'series_type': 'seriesType'
        }

        self._label = label
        self._channel_name = channel_name
        self._alias_id = alias_id
        self._series_type = series_type

    @property
    def label(self):
        """
        Gets the label of this SeriesDefinition.


        :return: The label of this SeriesDefinition.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """
        Sets the label of this SeriesDefinition.


        :param label: The label of this SeriesDefinition.
        :type: str
        """
        
        self._label = label

    @property
    def channel_name(self):
        """
        Gets the channel_name of this SeriesDefinition.


        :return: The channel_name of this SeriesDefinition.
        :rtype: str
        """
        return self._channel_name

    @channel_name.setter
    def channel_name(self, channel_name):
        """
        Sets the channel_name of this SeriesDefinition.


        :param channel_name: The channel_name of this SeriesDefinition.
        :type: str
        """
        
        self._channel_name = channel_name

    @property
    def alias_id(self):
        """
        Gets the alias_id of this SeriesDefinition.


        :return: The alias_id of this SeriesDefinition.
        :rtype: str
        """
        return self._alias_id

    @alias_id.setter
    def alias_id(self, alias_id):
        """
        Sets the alias_id of this SeriesDefinition.


        :param alias_id: The alias_id of this SeriesDefinition.
        :type: str
        """
        
        self._alias_id = alias_id

    @property
    def series_type(self):
        """
        Gets the series_type of this SeriesDefinition.


        :return: The series_type of this SeriesDefinition.
        :rtype: SeriesType
        """
        return self._series_type

    @series_type.setter
    def series_type(self, series_type):
        """
        Sets the series_type of this SeriesDefinition.


        :param series_type: The series_type of this SeriesDefinition.
        :type: SeriesType
        """
        
        self._series_type = series_type

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




