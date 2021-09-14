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


class PricingPlanUpdate(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, pricing_plan_id=None, private_projects_action=None):
        """
        PricingPlanUpdate - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'pricing_plan_id': 'str',
            'private_projects_action': 'PricingPlanUpdateProjectsAction'
        }

        self.attribute_map = {
            'pricing_plan_id': 'pricingPlanId',
            'private_projects_action': 'privateProjectsAction'
        }

        self._pricing_plan_id = pricing_plan_id
        self._private_projects_action = private_projects_action

    @property
    def pricing_plan_id(self):
        """
        Gets the pricing_plan_id of this PricingPlanUpdate.


        :return: The pricing_plan_id of this PricingPlanUpdate.
        :rtype: str
        """
        return self._pricing_plan_id

    @pricing_plan_id.setter
    def pricing_plan_id(self, pricing_plan_id):
        """
        Sets the pricing_plan_id of this PricingPlanUpdate.


        :param pricing_plan_id: The pricing_plan_id of this PricingPlanUpdate.
        :type: str
        """
        
        self._pricing_plan_id = pricing_plan_id

    @property
    def private_projects_action(self):
        """
        Gets the private_projects_action of this PricingPlanUpdate.


        :return: The private_projects_action of this PricingPlanUpdate.
        :rtype: PricingPlanUpdateProjectsAction
        """
        return self._private_projects_action

    @private_projects_action.setter
    def private_projects_action(self, private_projects_action):
        """
        Sets the private_projects_action of this PricingPlanUpdate.


        :param private_projects_action: The private_projects_action of this PricingPlanUpdate.
        :type: PricingPlanUpdateProjectsAction
        """
        
        self._private_projects_action = private_projects_action

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



