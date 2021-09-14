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


class ChangePricingPlanEvent(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, free_quota=None, pricing_plan=None):
        """
        ChangePricingPlanEvent - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'free_quota': 'int',
            'pricing_plan': 'str'
        }

        self.attribute_map = {
            'free_quota': 'freeQuota',
            'pricing_plan': 'pricingPlan'
        }

        self._free_quota = free_quota
        self._pricing_plan = pricing_plan

    @property
    def free_quota(self):
        """
        Gets the free_quota of this ChangePricingPlanEvent.


        :return: The free_quota of this ChangePricingPlanEvent.
        :rtype: int
        """
        return self._free_quota

    @free_quota.setter
    def free_quota(self, free_quota):
        """
        Sets the free_quota of this ChangePricingPlanEvent.


        :param free_quota: The free_quota of this ChangePricingPlanEvent.
        :type: int
        """
        
        self._free_quota = free_quota

    @property
    def pricing_plan(self):
        """
        Gets the pricing_plan of this ChangePricingPlanEvent.


        :return: The pricing_plan of this ChangePricingPlanEvent.
        :rtype: str
        """
        return self._pricing_plan

    @pricing_plan.setter
    def pricing_plan(self, pricing_plan):
        """
        Sets the pricing_plan of this ChangePricingPlanEvent.


        :param pricing_plan: The pricing_plan of this ChangePricingPlanEvent.
        :type: str
        """
        
        self._pricing_plan = pricing_plan

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




