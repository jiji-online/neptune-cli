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


class TimeDuration(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, years=None, weeks=None, seconds=None, minutes=None, hours=None, months=None, days=None):
        """
        TimeDuration - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'years': 'int',
            'weeks': 'int',
            'seconds': 'int',
            'minutes': 'int',
            'hours': 'int',
            'months': 'int',
            'days': 'int'
        }

        self.attribute_map = {
            'years': 'years',
            'weeks': 'weeks',
            'seconds': 'seconds',
            'minutes': 'minutes',
            'hours': 'hours',
            'months': 'months',
            'days': 'days'
        }

        self._years = years
        self._weeks = weeks
        self._seconds = seconds
        self._minutes = minutes
        self._hours = hours
        self._months = months
        self._days = days

    @property
    def years(self):
        """
        Gets the years of this TimeDuration.


        :return: The years of this TimeDuration.
        :rtype: int
        """
        return self._years

    @years.setter
    def years(self, years):
        """
        Sets the years of this TimeDuration.


        :param years: The years of this TimeDuration.
        :type: int
        """
        
        self._years = years

    @property
    def weeks(self):
        """
        Gets the weeks of this TimeDuration.


        :return: The weeks of this TimeDuration.
        :rtype: int
        """
        return self._weeks

    @weeks.setter
    def weeks(self, weeks):
        """
        Sets the weeks of this TimeDuration.


        :param weeks: The weeks of this TimeDuration.
        :type: int
        """
        
        self._weeks = weeks

    @property
    def seconds(self):
        """
        Gets the seconds of this TimeDuration.


        :return: The seconds of this TimeDuration.
        :rtype: int
        """
        return self._seconds

    @seconds.setter
    def seconds(self, seconds):
        """
        Sets the seconds of this TimeDuration.


        :param seconds: The seconds of this TimeDuration.
        :type: int
        """
        
        self._seconds = seconds

    @property
    def minutes(self):
        """
        Gets the minutes of this TimeDuration.


        :return: The minutes of this TimeDuration.
        :rtype: int
        """
        return self._minutes

    @minutes.setter
    def minutes(self, minutes):
        """
        Sets the minutes of this TimeDuration.


        :param minutes: The minutes of this TimeDuration.
        :type: int
        """
        
        self._minutes = minutes

    @property
    def hours(self):
        """
        Gets the hours of this TimeDuration.


        :return: The hours of this TimeDuration.
        :rtype: int
        """
        return self._hours

    @hours.setter
    def hours(self, hours):
        """
        Sets the hours of this TimeDuration.


        :param hours: The hours of this TimeDuration.
        :type: int
        """
        
        self._hours = hours

    @property
    def months(self):
        """
        Gets the months of this TimeDuration.


        :return: The months of this TimeDuration.
        :rtype: int
        """
        return self._months

    @months.setter
    def months(self, months):
        """
        Sets the months of this TimeDuration.


        :param months: The months of this TimeDuration.
        :type: int
        """
        
        self._months = months

    @property
    def days(self):
        """
        Gets the days of this TimeDuration.


        :return: The days of this TimeDuration.
        :rtype: int
        """
        return self._days

    @days.setter
    def days(self, days):
        """
        Sets the days of this TimeDuration.


        :param days: The days of this TimeDuration.
        :type: int
        """
        
        self._days = days

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




