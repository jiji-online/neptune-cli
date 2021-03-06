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


class ModifyFilterEvent(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, conditions=None, name=None, operation=None):
        """
        ModifyFilterEvent - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'conditions': 'int',
            'name': 'str',
            'operation': 'str'
        }

        self.attribute_map = {
            'conditions': 'conditions',
            'name': 'name',
            'operation': 'operation'
        }

        self._conditions = conditions
        self._name = name
        self._operation = operation

    @property
    def conditions(self):
        """
        Gets the conditions of this ModifyFilterEvent.


        :return: The conditions of this ModifyFilterEvent.
        :rtype: int
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """
        Sets the conditions of this ModifyFilterEvent.


        :param conditions: The conditions of this ModifyFilterEvent.
        :type: int
        """
        
        self._conditions = conditions

    @property
    def name(self):
        """
        Gets the name of this ModifyFilterEvent.


        :return: The name of this ModifyFilterEvent.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ModifyFilterEvent.


        :param name: The name of this ModifyFilterEvent.
        :type: str
        """
        
        self._name = name

    @property
    def operation(self):
        """
        Gets the operation of this ModifyFilterEvent.


        :return: The operation of this ModifyFilterEvent.
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        """
        Sets the operation of this ModifyFilterEvent.


        :param operation: The operation of this ModifyFilterEvent.
        :type: str
        """
        
        self._operation = operation

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




