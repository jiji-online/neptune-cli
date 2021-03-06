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


class SeatsDiscount(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, number_of_seats=None, percentage=None, savings=None):
        """
        SeatsDiscount - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'number_of_seats': 'int',
            'percentage': 'float',
            'savings': 'float'
        }

        self.attribute_map = {
            'number_of_seats': 'numberOfSeats',
            'percentage': 'percentage',
            'savings': 'savings'
        }

        self._number_of_seats = number_of_seats
        self._percentage = percentage
        self._savings = savings

    @property
    def number_of_seats(self):
        """
        Gets the number_of_seats of this SeatsDiscount.


        :return: The number_of_seats of this SeatsDiscount.
        :rtype: int
        """
        return self._number_of_seats

    @number_of_seats.setter
    def number_of_seats(self, number_of_seats):
        """
        Sets the number_of_seats of this SeatsDiscount.


        :param number_of_seats: The number_of_seats of this SeatsDiscount.
        :type: int
        """
        
        self._number_of_seats = number_of_seats

    @property
    def percentage(self):
        """
        Gets the percentage of this SeatsDiscount.


        :return: The percentage of this SeatsDiscount.
        :rtype: float
        """
        return self._percentage

    @percentage.setter
    def percentage(self, percentage):
        """
        Sets the percentage of this SeatsDiscount.


        :param percentage: The percentage of this SeatsDiscount.
        :type: float
        """
        
        self._percentage = percentage

    @property
    def savings(self):
        """
        Gets the savings of this SeatsDiscount.


        :return: The savings of this SeatsDiscount.
        :rtype: float
        """
        return self._savings

    @savings.setter
    def savings(self, savings):
        """
        Sets the savings of this SeatsDiscount.


        :param savings: The savings of this SeatsDiscount.
        :type: float
        """
        
        self._savings = savings

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




