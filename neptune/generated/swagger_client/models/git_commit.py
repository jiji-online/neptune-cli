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


class GitCommit(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, author_email=None, parents=None, commit_id=None, message=None, commit_date=None, author_name=None):
        """
        GitCommit - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'author_email': 'str',
            'parents': 'list[str]',
            'commit_id': 'str',
            'message': 'str',
            'commit_date': 'datetime',
            'author_name': 'str'
        }

        self.attribute_map = {
            'author_email': 'authorEmail',
            'parents': 'parents',
            'commit_id': 'commitId',
            'message': 'message',
            'commit_date': 'commitDate',
            'author_name': 'authorName'
        }

        self._author_email = author_email
        self._parents = parents
        self._commit_id = commit_id
        self._message = message
        self._commit_date = commit_date
        self._author_name = author_name

    @property
    def author_email(self):
        """
        Gets the author_email of this GitCommit.


        :return: The author_email of this GitCommit.
        :rtype: str
        """
        return self._author_email

    @author_email.setter
    def author_email(self, author_email):
        """
        Sets the author_email of this GitCommit.


        :param author_email: The author_email of this GitCommit.
        :type: str
        """
        
        self._author_email = author_email

    @property
    def parents(self):
        """
        Gets the parents of this GitCommit.


        :return: The parents of this GitCommit.
        :rtype: list[str]
        """
        return self._parents

    @parents.setter
    def parents(self, parents):
        """
        Sets the parents of this GitCommit.


        :param parents: The parents of this GitCommit.
        :type: list[str]
        """
        
        self._parents = parents

    @property
    def commit_id(self):
        """
        Gets the commit_id of this GitCommit.


        :return: The commit_id of this GitCommit.
        :rtype: str
        """
        return self._commit_id

    @commit_id.setter
    def commit_id(self, commit_id):
        """
        Sets the commit_id of this GitCommit.


        :param commit_id: The commit_id of this GitCommit.
        :type: str
        """
        
        self._commit_id = commit_id

    @property
    def message(self):
        """
        Gets the message of this GitCommit.


        :return: The message of this GitCommit.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this GitCommit.


        :param message: The message of this GitCommit.
        :type: str
        """
        
        self._message = message

    @property
    def commit_date(self):
        """
        Gets the commit_date of this GitCommit.


        :return: The commit_date of this GitCommit.
        :rtype: datetime
        """
        return self._commit_date

    @commit_date.setter
    def commit_date(self, commit_date):
        """
        Sets the commit_date of this GitCommit.


        :param commit_date: The commit_date of this GitCommit.
        :type: datetime
        """
        
        self._commit_date = commit_date

    @property
    def author_name(self):
        """
        Gets the author_name of this GitCommit.


        :return: The author_name of this GitCommit.
        :rtype: str
        """
        return self._author_name

    @author_name.setter
    def author_name(self, author_name):
        """
        Sets the author_name of this GitCommit.


        :param author_name: The author_name of this GitCommit.
        :type: str
        """
        
        self._author_name = author_name

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



