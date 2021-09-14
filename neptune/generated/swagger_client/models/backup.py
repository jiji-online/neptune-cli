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


class Backup(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, path=None, size=None, globs=None):
        """
        Backup - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'path': 'str',
            'size': 'int',
            'globs': 'list[str]'
        }

        self.attribute_map = {
            'path': 'path',
            'size': 'size',
            'globs': 'globs'
        }

        self._path = path
        self._size = size
        self._globs = globs

    @property
    def path(self):
        """
        Gets the path of this Backup.


        :return: The path of this Backup.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path of this Backup.


        :param path: The path of this Backup.
        :type: str
        """
        
        self._path = path

    @property
    def size(self):
        """
        Gets the size of this Backup.


        :return: The size of this Backup.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """
        Sets the size of this Backup.


        :param size: The size of this Backup.
        :type: int
        """
        
        self._size = size

    @property
    def globs(self):
        """
        Gets the globs of this Backup.


        :return: The globs of this Backup.
        :rtype: list[str]
        """
        return self._globs

    @globs.setter
    def globs(self, globs):
        """
        Sets the globs of this Backup.


        :param globs: The globs of this Backup.
        :type: list[str]
        """
        
        self._globs = globs

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



