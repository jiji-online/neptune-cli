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


class UserProfileUpdate(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, biography=None, has_logged_to_cli=None, last_name=None, first_name=None, short_info=None):
        """
        UserProfileUpdate - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'biography': 'str',
            'has_logged_to_cli': 'bool',
            'last_name': 'str',
            'first_name': 'str',
            'short_info': 'str'
        }

        self.attribute_map = {
            'biography': 'biography',
            'has_logged_to_cli': 'hasLoggedToCli',
            'last_name': 'lastName',
            'first_name': 'firstName',
            'short_info': 'shortInfo'
        }

        self._biography = biography
        self._has_logged_to_cli = has_logged_to_cli
        self._last_name = last_name
        self._first_name = first_name
        self._short_info = short_info

    @property
    def biography(self):
        """
        Gets the biography of this UserProfileUpdate.


        :return: The biography of this UserProfileUpdate.
        :rtype: str
        """
        return self._biography

    @biography.setter
    def biography(self, biography):
        """
        Sets the biography of this UserProfileUpdate.


        :param biography: The biography of this UserProfileUpdate.
        :type: str
        """
        
        self._biography = biography

    @property
    def has_logged_to_cli(self):
        """
        Gets the has_logged_to_cli of this UserProfileUpdate.


        :return: The has_logged_to_cli of this UserProfileUpdate.
        :rtype: bool
        """
        return self._has_logged_to_cli

    @has_logged_to_cli.setter
    def has_logged_to_cli(self, has_logged_to_cli):
        """
        Sets the has_logged_to_cli of this UserProfileUpdate.


        :param has_logged_to_cli: The has_logged_to_cli of this UserProfileUpdate.
        :type: bool
        """
        
        self._has_logged_to_cli = has_logged_to_cli

    @property
    def last_name(self):
        """
        Gets the last_name of this UserProfileUpdate.


        :return: The last_name of this UserProfileUpdate.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """
        Sets the last_name of this UserProfileUpdate.


        :param last_name: The last_name of this UserProfileUpdate.
        :type: str
        """
        
        self._last_name = last_name

    @property
    def first_name(self):
        """
        Gets the first_name of this UserProfileUpdate.


        :return: The first_name of this UserProfileUpdate.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """
        Sets the first_name of this UserProfileUpdate.


        :param first_name: The first_name of this UserProfileUpdate.
        :type: str
        """
        
        self._first_name = first_name

    @property
    def short_info(self):
        """
        Gets the short_info of this UserProfileUpdate.


        :return: The short_info of this UserProfileUpdate.
        :rtype: str
        """
        return self._short_info

    @short_info.setter
    def short_info(self, short_info):
        """
        Sets the short_info of this UserProfileUpdate.


        :param short_info: The short_info of this UserProfileUpdate.
        :type: str
        """
        
        self._short_info = short_info

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




