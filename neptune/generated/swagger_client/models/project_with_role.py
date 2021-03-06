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


class ProjectWithRole(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, code_access=None, name=None, last_activity=None, star_count=None, avatar_url=None, description=None, experiment_copy_count=None, featured=None, time_of_creation=None, user_role_in_organization=None, organization_name=None, avatar_source=None, leaderboard_entry_count=None, starred_by_me=None, id=None, user_role_in_project=None, background_url=None, project_key=None, organization_id=None, user_count=None, visibility=None, display_class=None):
        """
        ProjectWithRole - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'code_access': 'ProjectCodeAccess',
            'name': 'str',
            'last_activity': 'datetime',
            'star_count': 'int',
            'avatar_url': 'str',
            'description': 'str',
            'experiment_copy_count': 'int',
            'featured': 'bool',
            'time_of_creation': 'datetime',
            'user_role_in_organization': 'OrganizationRole',
            'organization_name': 'str',
            'avatar_source': 'AvatarSourceEnum',
            'leaderboard_entry_count': 'int',
            'starred_by_me': 'bool',
            'id': 'str',
            'user_role_in_project': 'ProjectRole',
            'background_url': 'str',
            'project_key': 'str',
            'organization_id': 'str',
            'user_count': 'int',
            'visibility': 'VisibilityEnum',
            'display_class': 'str'
        }

        self.attribute_map = {
            'code_access': 'codeAccess',
            'name': 'name',
            'last_activity': 'lastActivity',
            'star_count': 'starCount',
            'avatar_url': 'avatarUrl',
            'description': 'description',
            'experiment_copy_count': 'experimentCopyCount',
            'featured': 'featured',
            'time_of_creation': 'timeOfCreation',
            'user_role_in_organization': 'userRoleInOrganization',
            'organization_name': 'organizationName',
            'avatar_source': 'avatarSource',
            'leaderboard_entry_count': 'leaderboardEntryCount',
            'starred_by_me': 'starredByMe',
            'id': 'id',
            'user_role_in_project': 'userRoleInProject',
            'background_url': 'backgroundUrl',
            'project_key': 'projectKey',
            'organization_id': 'organizationId',
            'user_count': 'userCount',
            'visibility': 'visibility',
            'display_class': 'displayClass'
        }

        self._code_access = code_access
        self._name = name
        self._last_activity = last_activity
        self._star_count = star_count
        self._avatar_url = avatar_url
        self._description = description
        self._experiment_copy_count = experiment_copy_count
        self._featured = featured
        self._time_of_creation = time_of_creation
        self._user_role_in_organization = user_role_in_organization
        self._organization_name = organization_name
        self._avatar_source = avatar_source
        self._leaderboard_entry_count = leaderboard_entry_count
        self._starred_by_me = starred_by_me
        self._id = id
        self._user_role_in_project = user_role_in_project
        self._background_url = background_url
        self._project_key = project_key
        self._organization_id = organization_id
        self._user_count = user_count
        self._visibility = visibility
        self._display_class = display_class

    @property
    def code_access(self):
        """
        Gets the code_access of this ProjectWithRole.


        :return: The code_access of this ProjectWithRole.
        :rtype: ProjectCodeAccess
        """
        return self._code_access

    @code_access.setter
    def code_access(self, code_access):
        """
        Sets the code_access of this ProjectWithRole.


        :param code_access: The code_access of this ProjectWithRole.
        :type: ProjectCodeAccess
        """
        
        self._code_access = code_access

    @property
    def name(self):
        """
        Gets the name of this ProjectWithRole.


        :return: The name of this ProjectWithRole.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ProjectWithRole.


        :param name: The name of this ProjectWithRole.
        :type: str
        """
        
        self._name = name

    @property
    def last_activity(self):
        """
        Gets the last_activity of this ProjectWithRole.


        :return: The last_activity of this ProjectWithRole.
        :rtype: datetime
        """
        return self._last_activity

    @last_activity.setter
    def last_activity(self, last_activity):
        """
        Sets the last_activity of this ProjectWithRole.


        :param last_activity: The last_activity of this ProjectWithRole.
        :type: datetime
        """
        
        self._last_activity = last_activity

    @property
    def star_count(self):
        """
        Gets the star_count of this ProjectWithRole.


        :return: The star_count of this ProjectWithRole.
        :rtype: int
        """
        return self._star_count

    @star_count.setter
    def star_count(self, star_count):
        """
        Sets the star_count of this ProjectWithRole.


        :param star_count: The star_count of this ProjectWithRole.
        :type: int
        """
        
        self._star_count = star_count

    @property
    def avatar_url(self):
        """
        Gets the avatar_url of this ProjectWithRole.


        :return: The avatar_url of this ProjectWithRole.
        :rtype: str
        """
        return self._avatar_url

    @avatar_url.setter
    def avatar_url(self, avatar_url):
        """
        Sets the avatar_url of this ProjectWithRole.


        :param avatar_url: The avatar_url of this ProjectWithRole.
        :type: str
        """
        
        self._avatar_url = avatar_url

    @property
    def description(self):
        """
        Gets the description of this ProjectWithRole.


        :return: The description of this ProjectWithRole.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ProjectWithRole.


        :param description: The description of this ProjectWithRole.
        :type: str
        """
        
        self._description = description

    @property
    def experiment_copy_count(self):
        """
        Gets the experiment_copy_count of this ProjectWithRole.


        :return: The experiment_copy_count of this ProjectWithRole.
        :rtype: int
        """
        return self._experiment_copy_count

    @experiment_copy_count.setter
    def experiment_copy_count(self, experiment_copy_count):
        """
        Sets the experiment_copy_count of this ProjectWithRole.


        :param experiment_copy_count: The experiment_copy_count of this ProjectWithRole.
        :type: int
        """
        
        self._experiment_copy_count = experiment_copy_count

    @property
    def featured(self):
        """
        Gets the featured of this ProjectWithRole.


        :return: The featured of this ProjectWithRole.
        :rtype: bool
        """
        return self._featured

    @featured.setter
    def featured(self, featured):
        """
        Sets the featured of this ProjectWithRole.


        :param featured: The featured of this ProjectWithRole.
        :type: bool
        """
        
        self._featured = featured

    @property
    def time_of_creation(self):
        """
        Gets the time_of_creation of this ProjectWithRole.


        :return: The time_of_creation of this ProjectWithRole.
        :rtype: datetime
        """
        return self._time_of_creation

    @time_of_creation.setter
    def time_of_creation(self, time_of_creation):
        """
        Sets the time_of_creation of this ProjectWithRole.


        :param time_of_creation: The time_of_creation of this ProjectWithRole.
        :type: datetime
        """
        
        self._time_of_creation = time_of_creation

    @property
    def user_role_in_organization(self):
        """
        Gets the user_role_in_organization of this ProjectWithRole.


        :return: The user_role_in_organization of this ProjectWithRole.
        :rtype: OrganizationRole
        """
        return self._user_role_in_organization

    @user_role_in_organization.setter
    def user_role_in_organization(self, user_role_in_organization):
        """
        Sets the user_role_in_organization of this ProjectWithRole.


        :param user_role_in_organization: The user_role_in_organization of this ProjectWithRole.
        :type: OrganizationRole
        """
        
        self._user_role_in_organization = user_role_in_organization

    @property
    def organization_name(self):
        """
        Gets the organization_name of this ProjectWithRole.


        :return: The organization_name of this ProjectWithRole.
        :rtype: str
        """
        return self._organization_name

    @organization_name.setter
    def organization_name(self, organization_name):
        """
        Sets the organization_name of this ProjectWithRole.


        :param organization_name: The organization_name of this ProjectWithRole.
        :type: str
        """
        
        self._organization_name = organization_name

    @property
    def avatar_source(self):
        """
        Gets the avatar_source of this ProjectWithRole.


        :return: The avatar_source of this ProjectWithRole.
        :rtype: AvatarSourceEnum
        """
        return self._avatar_source

    @avatar_source.setter
    def avatar_source(self, avatar_source):
        """
        Sets the avatar_source of this ProjectWithRole.


        :param avatar_source: The avatar_source of this ProjectWithRole.
        :type: AvatarSourceEnum
        """
        
        self._avatar_source = avatar_source

    @property
    def leaderboard_entry_count(self):
        """
        Gets the leaderboard_entry_count of this ProjectWithRole.


        :return: The leaderboard_entry_count of this ProjectWithRole.
        :rtype: int
        """
        return self._leaderboard_entry_count

    @leaderboard_entry_count.setter
    def leaderboard_entry_count(self, leaderboard_entry_count):
        """
        Sets the leaderboard_entry_count of this ProjectWithRole.


        :param leaderboard_entry_count: The leaderboard_entry_count of this ProjectWithRole.
        :type: int
        """
        
        self._leaderboard_entry_count = leaderboard_entry_count

    @property
    def starred_by_me(self):
        """
        Gets the starred_by_me of this ProjectWithRole.


        :return: The starred_by_me of this ProjectWithRole.
        :rtype: bool
        """
        return self._starred_by_me

    @starred_by_me.setter
    def starred_by_me(self, starred_by_me):
        """
        Sets the starred_by_me of this ProjectWithRole.


        :param starred_by_me: The starred_by_me of this ProjectWithRole.
        :type: bool
        """
        
        self._starred_by_me = starred_by_me

    @property
    def id(self):
        """
        Gets the id of this ProjectWithRole.


        :return: The id of this ProjectWithRole.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ProjectWithRole.


        :param id: The id of this ProjectWithRole.
        :type: str
        """
        
        self._id = id

    @property
    def user_role_in_project(self):
        """
        Gets the user_role_in_project of this ProjectWithRole.


        :return: The user_role_in_project of this ProjectWithRole.
        :rtype: ProjectRole
        """
        return self._user_role_in_project

    @user_role_in_project.setter
    def user_role_in_project(self, user_role_in_project):
        """
        Sets the user_role_in_project of this ProjectWithRole.


        :param user_role_in_project: The user_role_in_project of this ProjectWithRole.
        :type: ProjectRole
        """
        
        self._user_role_in_project = user_role_in_project

    @property
    def background_url(self):
        """
        Gets the background_url of this ProjectWithRole.


        :return: The background_url of this ProjectWithRole.
        :rtype: str
        """
        return self._background_url

    @background_url.setter
    def background_url(self, background_url):
        """
        Sets the background_url of this ProjectWithRole.


        :param background_url: The background_url of this ProjectWithRole.
        :type: str
        """
        
        self._background_url = background_url

    @property
    def project_key(self):
        """
        Gets the project_key of this ProjectWithRole.


        :return: The project_key of this ProjectWithRole.
        :rtype: str
        """
        return self._project_key

    @project_key.setter
    def project_key(self, project_key):
        """
        Sets the project_key of this ProjectWithRole.


        :param project_key: The project_key of this ProjectWithRole.
        :type: str
        """
        
        self._project_key = project_key

    @property
    def organization_id(self):
        """
        Gets the organization_id of this ProjectWithRole.


        :return: The organization_id of this ProjectWithRole.
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """
        Sets the organization_id of this ProjectWithRole.


        :param organization_id: The organization_id of this ProjectWithRole.
        :type: str
        """
        
        self._organization_id = organization_id

    @property
    def user_count(self):
        """
        Gets the user_count of this ProjectWithRole.


        :return: The user_count of this ProjectWithRole.
        :rtype: int
        """
        return self._user_count

    @user_count.setter
    def user_count(self, user_count):
        """
        Sets the user_count of this ProjectWithRole.


        :param user_count: The user_count of this ProjectWithRole.
        :type: int
        """
        
        self._user_count = user_count

    @property
    def visibility(self):
        """
        Gets the visibility of this ProjectWithRole.


        :return: The visibility of this ProjectWithRole.
        :rtype: VisibilityEnum
        """
        return self._visibility

    @visibility.setter
    def visibility(self, visibility):
        """
        Sets the visibility of this ProjectWithRole.


        :param visibility: The visibility of this ProjectWithRole.
        :type: VisibilityEnum
        """
        
        self._visibility = visibility

    @property
    def display_class(self):
        """
        Gets the display_class of this ProjectWithRole.


        :return: The display_class of this ProjectWithRole.
        :rtype: str
        """
        return self._display_class

    @display_class.setter
    def display_class(self, display_class):
        """
        Sets the display_class of this ProjectWithRole.


        :param display_class: The display_class of this ProjectWithRole.
        :type: str
        """
        
        self._display_class = display_class

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




