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


class ChartPoint(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, x=None, y=None, miny=None, maxy=None):
        """
        ChartPoint - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'x': 'float',
            'y': 'float',
            'miny': 'float',
            'maxy': 'float'
        }

        self.attribute_map = {
            'x': 'x',
            'y': 'y',
            'miny': 'miny',
            'maxy': 'maxy'
        }

        self._x = x
        self._y = y
        self._miny = miny
        self._maxy = maxy

    @property
    def x(self):
        """
        Gets the x of this ChartPoint.


        :return: The x of this ChartPoint.
        :rtype: float
        """
        return self._x

    @x.setter
    def x(self, x):
        """
        Sets the x of this ChartPoint.


        :param x: The x of this ChartPoint.
        :type: float
        """
        
        self._x = x

    @property
    def y(self):
        """
        Gets the y of this ChartPoint.


        :return: The y of this ChartPoint.
        :rtype: float
        """
        return self._y

    @y.setter
    def y(self, y):
        """
        Sets the y of this ChartPoint.


        :param y: The y of this ChartPoint.
        :type: float
        """
        
        self._y = y

    @property
    def miny(self):
        """
        Gets the miny of this ChartPoint.


        :return: The miny of this ChartPoint.
        :rtype: float
        """
        return self._miny

    @miny.setter
    def miny(self, miny):
        """
        Sets the miny of this ChartPoint.


        :param miny: The miny of this ChartPoint.
        :type: float
        """
        
        self._miny = miny

    @property
    def maxy(self):
        """
        Gets the maxy of this ChartPoint.


        :return: The maxy of this ChartPoint.
        :rtype: float
        """
        return self._maxy

    @maxy.setter
    def maxy(self, maxy):
        """
        Sets the maxy of this ChartPoint.


        :param maxy: The maxy of this ChartPoint.
        :type: float
        """
        
        self._maxy = maxy

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




