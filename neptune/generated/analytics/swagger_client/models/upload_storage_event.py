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


class UploadStorageEvent(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, balance=None, files=None, free_quota=None, size=None):
        """
        UploadStorageEvent - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'balance': 'float',
            'files': 'int',
            'free_quota': 'int',
            'size': 'int'
        }

        self.attribute_map = {
            'balance': 'balance',
            'files': 'files',
            'free_quota': 'freeQuota',
            'size': 'size'
        }

        self._balance = balance
        self._files = files
        self._free_quota = free_quota
        self._size = size

    @property
    def balance(self):
        """
        Gets the balance of this UploadStorageEvent.


        :return: The balance of this UploadStorageEvent.
        :rtype: float
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """
        Sets the balance of this UploadStorageEvent.


        :param balance: The balance of this UploadStorageEvent.
        :type: float
        """
        
        self._balance = balance

    @property
    def files(self):
        """
        Gets the files of this UploadStorageEvent.


        :return: The files of this UploadStorageEvent.
        :rtype: int
        """
        return self._files

    @files.setter
    def files(self, files):
        """
        Sets the files of this UploadStorageEvent.


        :param files: The files of this UploadStorageEvent.
        :type: int
        """
        
        self._files = files

    @property
    def free_quota(self):
        """
        Gets the free_quota of this UploadStorageEvent.


        :return: The free_quota of this UploadStorageEvent.
        :rtype: int
        """
        return self._free_quota

    @free_quota.setter
    def free_quota(self, free_quota):
        """
        Sets the free_quota of this UploadStorageEvent.


        :param free_quota: The free_quota of this UploadStorageEvent.
        :type: int
        """
        
        self._free_quota = free_quota

    @property
    def size(self):
        """
        Gets the size of this UploadStorageEvent.


        :return: The size of this UploadStorageEvent.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """
        Sets the size of this UploadStorageEvent.


        :param size: The size of this UploadStorageEvent.
        :type: int
        """
        
        self._size = size

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




