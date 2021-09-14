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


class RegisteredMemberInfo(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, username=None, avatar_url=None, avatar_source=None, last_name=None, first_name=None):
        """
        RegisteredMemberInfo - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'username': 'str',
            'avatar_url': 'str',
            'avatar_source': 'AvatarSourceEnum',
            'last_name': 'str',
            'first_name': 'str'
        }

        self.attribute_map = {
            'username': 'username',
            'avatar_url': 'avatarUrl',
            'avatar_source': 'avatarSource',
            'last_name': 'lastName',
            'first_name': 'firstName'
        }

        self._username = username
        self._avatar_url = avatar_url
        self._avatar_source = avatar_source
        self._last_name = last_name
        self._first_name = first_name

    @property
    def username(self):
        """
        Gets the username of this RegisteredMemberInfo.


        :return: The username of this RegisteredMemberInfo.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this RegisteredMemberInfo.


        :param username: The username of this RegisteredMemberInfo.
        :type: str
        """
        
        self._username = username

    @property
    def avatar_url(self):
        """
        Gets the avatar_url of this RegisteredMemberInfo.


        :return: The avatar_url of this RegisteredMemberInfo.
        :rtype: str
        """
        return self._avatar_url

    @avatar_url.setter
    def avatar_url(self, avatar_url):
        """
        Sets the avatar_url of this RegisteredMemberInfo.


        :param avatar_url: The avatar_url of this RegisteredMemberInfo.
        :type: str
        """
        
        self._avatar_url = avatar_url

    @property
    def avatar_source(self):
        """
        Gets the avatar_source of this RegisteredMemberInfo.


        :return: The avatar_source of this RegisteredMemberInfo.
        :rtype: AvatarSourceEnum
        """
        return self._avatar_source

    @avatar_source.setter
    def avatar_source(self, avatar_source):
        """
        Sets the avatar_source of this RegisteredMemberInfo.


        :param avatar_source: The avatar_source of this RegisteredMemberInfo.
        :type: AvatarSourceEnum
        """
        
        self._avatar_source = avatar_source

    @property
    def last_name(self):
        """
        Gets the last_name of this RegisteredMemberInfo.


        :return: The last_name of this RegisteredMemberInfo.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """
        Sets the last_name of this RegisteredMemberInfo.


        :param last_name: The last_name of this RegisteredMemberInfo.
        :type: str
        """
        
        self._last_name = last_name

    @property
    def first_name(self):
        """
        Gets the first_name of this RegisteredMemberInfo.


        :return: The first_name of this RegisteredMemberInfo.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """
        Sets the first_name of this RegisteredMemberInfo.


        :param first_name: The first_name of this RegisteredMemberInfo.
        :type: str
        """
        
        self._first_name = first_name

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




