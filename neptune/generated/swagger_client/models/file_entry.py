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


class FileEntry(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, size=None, permissions=None, file_type=None, mtime=None):
        """
        FileEntry - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'size': 'int',
            'permissions': 'str',
            'file_type': 'str',
            'mtime': 'datetime'
        }

        self.attribute_map = {
            'name': 'name',
            'size': 'size',
            'permissions': 'permissions',
            'file_type': 'fileType',
            'mtime': 'mtime'
        }

        self._name = name
        self._size = size
        self._permissions = permissions
        self._file_type = file_type
        self._mtime = mtime

    @property
    def name(self):
        """
        Gets the name of this FileEntry.


        :return: The name of this FileEntry.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this FileEntry.


        :param name: The name of this FileEntry.
        :type: str
        """
        
        self._name = name

    @property
    def size(self):
        """
        Gets the size of this FileEntry.


        :return: The size of this FileEntry.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """
        Sets the size of this FileEntry.


        :param size: The size of this FileEntry.
        :type: int
        """
        
        self._size = size

    @property
    def permissions(self):
        """
        Gets the permissions of this FileEntry.


        :return: The permissions of this FileEntry.
        :rtype: str
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """
        Sets the permissions of this FileEntry.


        :param permissions: The permissions of this FileEntry.
        :type: str
        """
        
        self._permissions = permissions

    @property
    def file_type(self):
        """
        Gets the file_type of this FileEntry.


        :return: The file_type of this FileEntry.
        :rtype: str
        """
        return self._file_type

    @file_type.setter
    def file_type(self, file_type):
        """
        Sets the file_type of this FileEntry.


        :param file_type: The file_type of this FileEntry.
        :type: str
        """
        
        self._file_type = file_type

    @property
    def mtime(self):
        """
        Gets the mtime of this FileEntry.


        :return: The mtime of this FileEntry.
        :rtype: datetime
        """
        return self._mtime

    @mtime.setter
    def mtime(self, mtime):
        """
        Sets the mtime of this FileEntry.


        :param mtime: The mtime of this FileEntry.
        :type: datetime
        """
        
        self._mtime = mtime

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




