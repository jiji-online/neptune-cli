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


class OrganizationCreationParams(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, payments_info=None, organization_type=None):
        """
        OrganizationCreationParams - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'payments_info': 'PaymentsInfo',
            'organization_type': 'OrganizationType'
        }

        self.attribute_map = {
            'name': 'name',
            'payments_info': 'paymentsInfo',
            'organization_type': 'organizationType'
        }

        self._name = name
        self._payments_info = payments_info
        self._organization_type = organization_type

    @property
    def name(self):
        """
        Gets the name of this OrganizationCreationParams.


        :return: The name of this OrganizationCreationParams.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this OrganizationCreationParams.


        :param name: The name of this OrganizationCreationParams.
        :type: str
        """
        
        self._name = name

    @property
    def payments_info(self):
        """
        Gets the payments_info of this OrganizationCreationParams.


        :return: The payments_info of this OrganizationCreationParams.
        :rtype: PaymentsInfo
        """
        return self._payments_info

    @payments_info.setter
    def payments_info(self, payments_info):
        """
        Sets the payments_info of this OrganizationCreationParams.


        :param payments_info: The payments_info of this OrganizationCreationParams.
        :type: PaymentsInfo
        """
        
        self._payments_info = payments_info

    @property
    def organization_type(self):
        """
        Gets the organization_type of this OrganizationCreationParams.


        :return: The organization_type of this OrganizationCreationParams.
        :rtype: OrganizationType
        """
        return self._organization_type

    @organization_type.setter
    def organization_type(self, organization_type):
        """
        Sets the organization_type of this OrganizationCreationParams.


        :param organization_type: The organization_type of this OrganizationCreationParams.
        :type: OrganizationType
        """
        
        self._organization_type = organization_type

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




