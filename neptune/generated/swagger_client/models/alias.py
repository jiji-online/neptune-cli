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


class Alias(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, project_id=None, name=None, channels=None):
        """
        Alias - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'project_id': 'str',
            'name': 'str',
            'channels': 'list[str]'
        }

        self.attribute_map = {
            'id': 'id',
            'project_id': 'projectId',
            'name': 'name',
            'channels': 'channels'
        }

        self._id = id
        self._project_id = project_id
        self._name = name
        self._channels = channels

    @property
    def id(self):
        """
        Gets the id of this Alias.


        :return: The id of this Alias.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Alias.


        :param id: The id of this Alias.
        :type: str
        """
        
        self._id = id

    @property
    def project_id(self):
        """
        Gets the project_id of this Alias.


        :return: The project_id of this Alias.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """
        Sets the project_id of this Alias.


        :param project_id: The project_id of this Alias.
        :type: str
        """
        
        self._project_id = project_id

    @property
    def name(self):
        """
        Gets the name of this Alias.


        :return: The name of this Alias.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Alias.


        :param name: The name of this Alias.
        :type: str
        """
        
        self._name = name

    @property
    def channels(self):
        """
        Gets the channels of this Alias.


        :return: The channels of this Alias.
        :rtype: list[str]
        """
        return self._channels

    @channels.setter
    def channels(self, channels):
        """
        Sets the channels of this Alias.


        :param channels: The channels of this Alias.
        :type: list[str]
        """
        
        self._channels = channels

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




