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


class EditExperimentParams(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, code_access=None, name=None, description=None, tags=None, properties=None, actions=None):
        """
        EditExperimentParams - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'code_access': 'ExperimentCodeAccess',
            'name': 'str',
            'description': 'str',
            'tags': 'list[str]',
            'properties': 'list[KeyValueProperty]',
            'actions': 'list[Action]'
        }

        self.attribute_map = {
            'code_access': 'codeAccess',
            'name': 'name',
            'description': 'description',
            'tags': 'tags',
            'properties': 'properties',
            'actions': 'actions'
        }

        self._code_access = code_access
        self._name = name
        self._description = description
        self._tags = tags
        self._properties = properties
        self._actions = actions

    @property
    def code_access(self):
        """
        Gets the code_access of this EditExperimentParams.


        :return: The code_access of this EditExperimentParams.
        :rtype: ExperimentCodeAccess
        """
        return self._code_access

    @code_access.setter
    def code_access(self, code_access):
        """
        Sets the code_access of this EditExperimentParams.


        :param code_access: The code_access of this EditExperimentParams.
        :type: ExperimentCodeAccess
        """
        
        self._code_access = code_access

    @property
    def name(self):
        """
        Gets the name of this EditExperimentParams.


        :return: The name of this EditExperimentParams.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this EditExperimentParams.


        :param name: The name of this EditExperimentParams.
        :type: str
        """
        
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this EditExperimentParams.


        :return: The description of this EditExperimentParams.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this EditExperimentParams.


        :param description: The description of this EditExperimentParams.
        :type: str
        """
        
        self._description = description

    @property
    def tags(self):
        """
        Gets the tags of this EditExperimentParams.


        :return: The tags of this EditExperimentParams.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this EditExperimentParams.


        :param tags: The tags of this EditExperimentParams.
        :type: list[str]
        """
        
        self._tags = tags

    @property
    def properties(self):
        """
        Gets the properties of this EditExperimentParams.


        :return: The properties of this EditExperimentParams.
        :rtype: list[KeyValueProperty]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """
        Sets the properties of this EditExperimentParams.


        :param properties: The properties of this EditExperimentParams.
        :type: list[KeyValueProperty]
        """
        
        self._properties = properties

    @property
    def actions(self):
        """
        Gets the actions of this EditExperimentParams.


        :return: The actions of this EditExperimentParams.
        :rtype: list[Action]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """
        Sets the actions of this EditExperimentParams.


        :param actions: The actions of this EditExperimentParams.
        :type: list[Action]
        """
        
        self._actions = actions

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




