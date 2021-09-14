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


class Organization(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, payment_status=None, avatar_url=None, organization_type=None, avatar_source=None, info=None, id=None, paid=None, created=None):
        """
        Organization - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'payment_status': 'str',
            'avatar_url': 'str',
            'organization_type': 'OrganizationType',
            'avatar_source': 'AvatarSourceEnum',
            'info': 'str',
            'id': 'str',
            'paid': 'bool',
            'created': 'datetime'
        }

        self.attribute_map = {
            'name': 'name',
            'payment_status': 'paymentStatus',
            'avatar_url': 'avatarUrl',
            'organization_type': 'organizationType',
            'avatar_source': 'avatarSource',
            'info': 'info',
            'id': 'id',
            'paid': 'paid',
            'created': 'created'
        }

        self._name = name
        self._payment_status = payment_status
        self._avatar_url = avatar_url
        self._organization_type = organization_type
        self._avatar_source = avatar_source
        self._info = info
        self._id = id
        self._paid = paid
        self._created = created

    @property
    def name(self):
        """
        Gets the name of this Organization.


        :return: The name of this Organization.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Organization.


        :param name: The name of this Organization.
        :type: str
        """
        
        self._name = name

    @property
    def payment_status(self):
        """
        Gets the payment_status of this Organization.


        :return: The payment_status of this Organization.
        :rtype: str
        """
        return self._payment_status

    @payment_status.setter
    def payment_status(self, payment_status):
        """
        Sets the payment_status of this Organization.


        :param payment_status: The payment_status of this Organization.
        :type: str
        """
        
        self._payment_status = payment_status

    @property
    def avatar_url(self):
        """
        Gets the avatar_url of this Organization.


        :return: The avatar_url of this Organization.
        :rtype: str
        """
        return self._avatar_url

    @avatar_url.setter
    def avatar_url(self, avatar_url):
        """
        Sets the avatar_url of this Organization.


        :param avatar_url: The avatar_url of this Organization.
        :type: str
        """
        
        self._avatar_url = avatar_url

    @property
    def organization_type(self):
        """
        Gets the organization_type of this Organization.


        :return: The organization_type of this Organization.
        :rtype: OrganizationType
        """
        return self._organization_type

    @organization_type.setter
    def organization_type(self, organization_type):
        """
        Sets the organization_type of this Organization.


        :param organization_type: The organization_type of this Organization.
        :type: OrganizationType
        """
        
        self._organization_type = organization_type

    @property
    def avatar_source(self):
        """
        Gets the avatar_source of this Organization.


        :return: The avatar_source of this Organization.
        :rtype: AvatarSourceEnum
        """
        return self._avatar_source

    @avatar_source.setter
    def avatar_source(self, avatar_source):
        """
        Sets the avatar_source of this Organization.


        :param avatar_source: The avatar_source of this Organization.
        :type: AvatarSourceEnum
        """
        
        self._avatar_source = avatar_source

    @property
    def info(self):
        """
        Gets the info of this Organization.


        :return: The info of this Organization.
        :rtype: str
        """
        return self._info

    @info.setter
    def info(self, info):
        """
        Sets the info of this Organization.


        :param info: The info of this Organization.
        :type: str
        """
        
        self._info = info

    @property
    def id(self):
        """
        Gets the id of this Organization.


        :return: The id of this Organization.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Organization.


        :param id: The id of this Organization.
        :type: str
        """
        
        self._id = id

    @property
    def paid(self):
        """
        Gets the paid of this Organization.


        :return: The paid of this Organization.
        :rtype: bool
        """
        return self._paid

    @paid.setter
    def paid(self, paid):
        """
        Sets the paid of this Organization.


        :param paid: The paid of this Organization.
        :type: bool
        """
        
        self._paid = paid

    @property
    def created(self):
        """
        Gets the created of this Organization.


        :return: The created of this Organization.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this Organization.


        :param created: The created of this Organization.
        :type: datetime
        """
        
        self._created = created

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




