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


class TimeSpentEvent(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, actions=None, current_url=None):
        """
        TimeSpentEvent - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'actions': 'int',
            'current_url': 'str'
        }

        self.attribute_map = {
            'actions': 'actions',
            'current_url': 'currentUrl'
        }

        self._actions = actions
        self._current_url = current_url

    @property
    def actions(self):
        """
        Gets the actions of this TimeSpentEvent.


        :return: The actions of this TimeSpentEvent.
        :rtype: int
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """
        Sets the actions of this TimeSpentEvent.


        :param actions: The actions of this TimeSpentEvent.
        :type: int
        """
        
        self._actions = actions

    @property
    def current_url(self):
        """
        Gets the current_url of this TimeSpentEvent.


        :return: The current_url of this TimeSpentEvent.
        :rtype: str
        """
        return self._current_url

    @current_url.setter
    def current_url(self, current_url):
        """
        Sets the current_url of this TimeSpentEvent.


        :param current_url: The current_url of this TimeSpentEvent.
        :type: str
        """
        
        self._current_url = current_url

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




