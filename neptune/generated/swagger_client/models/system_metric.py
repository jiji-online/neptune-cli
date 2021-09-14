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


class SystemMetric(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, series=None, name=None, description=None, resource_type=None, min=None, experiment_id=None, id=None, max=None, unit=None):
        """
        SystemMetric - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'series': 'list[str]',
            'name': 'str',
            'description': 'str',
            'resource_type': 'SystemMetricResourceType',
            'min': 'float',
            'experiment_id': 'str',
            'id': 'str',
            'max': 'float',
            'unit': 'str'
        }

        self.attribute_map = {
            'series': 'series',
            'name': 'name',
            'description': 'description',
            'resource_type': 'resourceType',
            'min': 'min',
            'experiment_id': 'experimentId',
            'id': 'id',
            'max': 'max',
            'unit': 'unit'
        }

        self._series = series
        self._name = name
        self._description = description
        self._resource_type = resource_type
        self._min = min
        self._experiment_id = experiment_id
        self._id = id
        self._max = max
        self._unit = unit

    @property
    def series(self):
        """
        Gets the series of this SystemMetric.


        :return: The series of this SystemMetric.
        :rtype: list[str]
        """
        return self._series

    @series.setter
    def series(self, series):
        """
        Sets the series of this SystemMetric.


        :param series: The series of this SystemMetric.
        :type: list[str]
        """
        
        self._series = series

    @property
    def name(self):
        """
        Gets the name of this SystemMetric.


        :return: The name of this SystemMetric.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this SystemMetric.


        :param name: The name of this SystemMetric.
        :type: str
        """
        
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this SystemMetric.


        :return: The description of this SystemMetric.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this SystemMetric.


        :param description: The description of this SystemMetric.
        :type: str
        """
        
        self._description = description

    @property
    def resource_type(self):
        """
        Gets the resource_type of this SystemMetric.


        :return: The resource_type of this SystemMetric.
        :rtype: SystemMetricResourceType
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """
        Sets the resource_type of this SystemMetric.


        :param resource_type: The resource_type of this SystemMetric.
        :type: SystemMetricResourceType
        """
        
        self._resource_type = resource_type

    @property
    def min(self):
        """
        Gets the min of this SystemMetric.


        :return: The min of this SystemMetric.
        :rtype: float
        """
        return self._min

    @min.setter
    def min(self, min):
        """
        Sets the min of this SystemMetric.


        :param min: The min of this SystemMetric.
        :type: float
        """
        
        self._min = min

    @property
    def experiment_id(self):
        """
        Gets the experiment_id of this SystemMetric.


        :return: The experiment_id of this SystemMetric.
        :rtype: str
        """
        return self._experiment_id

    @experiment_id.setter
    def experiment_id(self, experiment_id):
        """
        Sets the experiment_id of this SystemMetric.


        :param experiment_id: The experiment_id of this SystemMetric.
        :type: str
        """
        
        self._experiment_id = experiment_id

    @property
    def id(self):
        """
        Gets the id of this SystemMetric.


        :return: The id of this SystemMetric.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this SystemMetric.


        :param id: The id of this SystemMetric.
        :type: str
        """
        
        self._id = id

    @property
    def max(self):
        """
        Gets the max of this SystemMetric.


        :return: The max of this SystemMetric.
        :rtype: float
        """
        return self._max

    @max.setter
    def max(self, max):
        """
        Sets the max of this SystemMetric.


        :param max: The max of this SystemMetric.
        :type: float
        """
        
        self._max = max

    @property
    def unit(self):
        """
        Gets the unit of this SystemMetric.


        :return: The unit of this SystemMetric.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """
        Sets the unit of this SystemMetric.


        :param unit: The unit of this SystemMetric.
        :type: str
        """
        
        self._unit = unit

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




