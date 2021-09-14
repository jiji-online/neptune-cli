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


class GroupEntryDTO(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, project_name=None, trashed=None, description=None, tags=None, time_of_creation=None, project_id=None, organization_name=None, id=None, short_id=None, metric=None, organization_id=None, owner=None):
        """
        GroupEntryDTO - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'project_name': 'str',
            'trashed': 'bool',
            'description': 'str',
            'tags': 'list[str]',
            'time_of_creation': 'datetime',
            'project_id': 'str',
            'organization_name': 'str',
            'id': 'str',
            'short_id': 'str',
            'metric': 'Metric',
            'organization_id': 'str',
            'owner': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'project_name': 'projectName',
            'trashed': 'trashed',
            'description': 'description',
            'tags': 'tags',
            'time_of_creation': 'timeOfCreation',
            'project_id': 'projectId',
            'organization_name': 'organizationName',
            'id': 'id',
            'short_id': 'shortId',
            'metric': 'metric',
            'organization_id': 'organizationId',
            'owner': 'owner'
        }

        self._name = name
        self._project_name = project_name
        self._trashed = trashed
        self._description = description
        self._tags = tags
        self._time_of_creation = time_of_creation
        self._project_id = project_id
        self._organization_name = organization_name
        self._id = id
        self._short_id = short_id
        self._metric = metric
        self._organization_id = organization_id
        self._owner = owner

    @property
    def name(self):
        """
        Gets the name of this GroupEntryDTO.


        :return: The name of this GroupEntryDTO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this GroupEntryDTO.


        :param name: The name of this GroupEntryDTO.
        :type: str
        """
        
        self._name = name

    @property
    def project_name(self):
        """
        Gets the project_name of this GroupEntryDTO.


        :return: The project_name of this GroupEntryDTO.
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """
        Sets the project_name of this GroupEntryDTO.


        :param project_name: The project_name of this GroupEntryDTO.
        :type: str
        """
        
        self._project_name = project_name

    @property
    def trashed(self):
        """
        Gets the trashed of this GroupEntryDTO.


        :return: The trashed of this GroupEntryDTO.
        :rtype: bool
        """
        return self._trashed

    @trashed.setter
    def trashed(self, trashed):
        """
        Sets the trashed of this GroupEntryDTO.


        :param trashed: The trashed of this GroupEntryDTO.
        :type: bool
        """
        
        self._trashed = trashed

    @property
    def description(self):
        """
        Gets the description of this GroupEntryDTO.


        :return: The description of this GroupEntryDTO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this GroupEntryDTO.


        :param description: The description of this GroupEntryDTO.
        :type: str
        """
        
        self._description = description

    @property
    def tags(self):
        """
        Gets the tags of this GroupEntryDTO.


        :return: The tags of this GroupEntryDTO.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this GroupEntryDTO.


        :param tags: The tags of this GroupEntryDTO.
        :type: list[str]
        """
        
        self._tags = tags

    @property
    def time_of_creation(self):
        """
        Gets the time_of_creation of this GroupEntryDTO.


        :return: The time_of_creation of this GroupEntryDTO.
        :rtype: datetime
        """
        return self._time_of_creation

    @time_of_creation.setter
    def time_of_creation(self, time_of_creation):
        """
        Sets the time_of_creation of this GroupEntryDTO.


        :param time_of_creation: The time_of_creation of this GroupEntryDTO.
        :type: datetime
        """
        
        self._time_of_creation = time_of_creation

    @property
    def project_id(self):
        """
        Gets the project_id of this GroupEntryDTO.


        :return: The project_id of this GroupEntryDTO.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """
        Sets the project_id of this GroupEntryDTO.


        :param project_id: The project_id of this GroupEntryDTO.
        :type: str
        """
        
        self._project_id = project_id

    @property
    def organization_name(self):
        """
        Gets the organization_name of this GroupEntryDTO.


        :return: The organization_name of this GroupEntryDTO.
        :rtype: str
        """
        return self._organization_name

    @organization_name.setter
    def organization_name(self, organization_name):
        """
        Sets the organization_name of this GroupEntryDTO.


        :param organization_name: The organization_name of this GroupEntryDTO.
        :type: str
        """
        
        self._organization_name = organization_name

    @property
    def id(self):
        """
        Gets the id of this GroupEntryDTO.


        :return: The id of this GroupEntryDTO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this GroupEntryDTO.


        :param id: The id of this GroupEntryDTO.
        :type: str
        """
        
        self._id = id

    @property
    def short_id(self):
        """
        Gets the short_id of this GroupEntryDTO.


        :return: The short_id of this GroupEntryDTO.
        :rtype: str
        """
        return self._short_id

    @short_id.setter
    def short_id(self, short_id):
        """
        Sets the short_id of this GroupEntryDTO.


        :param short_id: The short_id of this GroupEntryDTO.
        :type: str
        """
        
        self._short_id = short_id

    @property
    def metric(self):
        """
        Gets the metric of this GroupEntryDTO.


        :return: The metric of this GroupEntryDTO.
        :rtype: Metric
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        """
        Sets the metric of this GroupEntryDTO.


        :param metric: The metric of this GroupEntryDTO.
        :type: Metric
        """
        
        self._metric = metric

    @property
    def organization_id(self):
        """
        Gets the organization_id of this GroupEntryDTO.


        :return: The organization_id of this GroupEntryDTO.
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """
        Sets the organization_id of this GroupEntryDTO.


        :param organization_id: The organization_id of this GroupEntryDTO.
        :type: str
        """
        
        self._organization_id = organization_id

    @property
    def owner(self):
        """
        Gets the owner of this GroupEntryDTO.


        :return: The owner of this GroupEntryDTO.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """
        Sets the owner of this GroupEntryDTO.


        :param owner: The owner of this GroupEntryDTO.
        :type: str
        """
        
        self._owner = owner

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



