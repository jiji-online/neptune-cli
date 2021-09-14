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


class ModifyLeaderboardEvent(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, aliases=None, columns=None, grid_search_view=None, numeric_channels=None, operation=None, parameters=None, properties=None, sorted_by=None, system_columns=None, text_channels=None):
        """
        ModifyLeaderboardEvent - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'aliases': 'int',
            'columns': 'int',
            'grid_search_view': 'bool',
            'numeric_channels': 'int',
            'operation': 'str',
            'parameters': 'int',
            'properties': 'int',
            'sorted_by': 'str',
            'system_columns': 'int',
            'text_channels': 'int'
        }

        self.attribute_map = {
            'aliases': 'aliases',
            'columns': 'columns',
            'grid_search_view': 'gridSearchView',
            'numeric_channels': 'numericChannels',
            'operation': 'operation',
            'parameters': 'parameters',
            'properties': 'properties',
            'sorted_by': 'sortedBy',
            'system_columns': 'systemColumns',
            'text_channels': 'textChannels'
        }

        self._aliases = aliases
        self._columns = columns
        self._grid_search_view = grid_search_view
        self._numeric_channels = numeric_channels
        self._operation = operation
        self._parameters = parameters
        self._properties = properties
        self._sorted_by = sorted_by
        self._system_columns = system_columns
        self._text_channels = text_channels

    @property
    def aliases(self):
        """
        Gets the aliases of this ModifyLeaderboardEvent.


        :return: The aliases of this ModifyLeaderboardEvent.
        :rtype: int
        """
        return self._aliases

    @aliases.setter
    def aliases(self, aliases):
        """
        Sets the aliases of this ModifyLeaderboardEvent.


        :param aliases: The aliases of this ModifyLeaderboardEvent.
        :type: int
        """
        
        self._aliases = aliases

    @property
    def columns(self):
        """
        Gets the columns of this ModifyLeaderboardEvent.


        :return: The columns of this ModifyLeaderboardEvent.
        :rtype: int
        """
        return self._columns

    @columns.setter
    def columns(self, columns):
        """
        Sets the columns of this ModifyLeaderboardEvent.


        :param columns: The columns of this ModifyLeaderboardEvent.
        :type: int
        """
        
        self._columns = columns

    @property
    def grid_search_view(self):
        """
        Gets the grid_search_view of this ModifyLeaderboardEvent.


        :return: The grid_search_view of this ModifyLeaderboardEvent.
        :rtype: bool
        """
        return self._grid_search_view

    @grid_search_view.setter
    def grid_search_view(self, grid_search_view):
        """
        Sets the grid_search_view of this ModifyLeaderboardEvent.


        :param grid_search_view: The grid_search_view of this ModifyLeaderboardEvent.
        :type: bool
        """
        
        self._grid_search_view = grid_search_view

    @property
    def numeric_channels(self):
        """
        Gets the numeric_channels of this ModifyLeaderboardEvent.


        :return: The numeric_channels of this ModifyLeaderboardEvent.
        :rtype: int
        """
        return self._numeric_channels

    @numeric_channels.setter
    def numeric_channels(self, numeric_channels):
        """
        Sets the numeric_channels of this ModifyLeaderboardEvent.


        :param numeric_channels: The numeric_channels of this ModifyLeaderboardEvent.
        :type: int
        """
        
        self._numeric_channels = numeric_channels

    @property
    def operation(self):
        """
        Gets the operation of this ModifyLeaderboardEvent.


        :return: The operation of this ModifyLeaderboardEvent.
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        """
        Sets the operation of this ModifyLeaderboardEvent.


        :param operation: The operation of this ModifyLeaderboardEvent.
        :type: str
        """
        allowed_values = ["MOVE_COLUMN", "REMOVE_COLUMN", "ADD_COLUMN", "SORT_COLUMN"]
        if operation not in allowed_values:
            raise ValueError(
                "Invalid value for `operation`, must be one of {0}"
                .format(allowed_values)
            )

        self._operation = operation

    @property
    def parameters(self):
        """
        Gets the parameters of this ModifyLeaderboardEvent.


        :return: The parameters of this ModifyLeaderboardEvent.
        :rtype: int
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """
        Sets the parameters of this ModifyLeaderboardEvent.


        :param parameters: The parameters of this ModifyLeaderboardEvent.
        :type: int
        """
        
        self._parameters = parameters

    @property
    def properties(self):
        """
        Gets the properties of this ModifyLeaderboardEvent.


        :return: The properties of this ModifyLeaderboardEvent.
        :rtype: int
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """
        Sets the properties of this ModifyLeaderboardEvent.


        :param properties: The properties of this ModifyLeaderboardEvent.
        :type: int
        """
        
        self._properties = properties

    @property
    def sorted_by(self):
        """
        Gets the sorted_by of this ModifyLeaderboardEvent.


        :return: The sorted_by of this ModifyLeaderboardEvent.
        :rtype: str
        """
        return self._sorted_by

    @sorted_by.setter
    def sorted_by(self, sorted_by):
        """
        Sets the sorted_by of this ModifyLeaderboardEvent.


        :param sorted_by: The sorted_by of this ModifyLeaderboardEvent.
        :type: str
        """
        
        self._sorted_by = sorted_by

    @property
    def system_columns(self):
        """
        Gets the system_columns of this ModifyLeaderboardEvent.


        :return: The system_columns of this ModifyLeaderboardEvent.
        :rtype: int
        """
        return self._system_columns

    @system_columns.setter
    def system_columns(self, system_columns):
        """
        Sets the system_columns of this ModifyLeaderboardEvent.


        :param system_columns: The system_columns of this ModifyLeaderboardEvent.
        :type: int
        """
        
        self._system_columns = system_columns

    @property
    def text_channels(self):
        """
        Gets the text_channels of this ModifyLeaderboardEvent.


        :return: The text_channels of this ModifyLeaderboardEvent.
        :rtype: int
        """
        return self._text_channels

    @text_channels.setter
    def text_channels(self, text_channels):
        """
        Sets the text_channels of this ModifyLeaderboardEvent.


        :param text_channels: The text_channels of this ModifyLeaderboardEvent.
        :type: int
        """
        
        self._text_channels = text_channels

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



