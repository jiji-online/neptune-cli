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


class ProjectPageDTO(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, default_page=None, id=None, content=None, title=None, removable=None, editable=None):
        """
        ProjectPageDTO - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'default_page': 'bool',
            'id': 'str',
            'content': 'str',
            'title': 'str',
            'removable': 'bool',
            'editable': 'bool'
        }

        self.attribute_map = {
            'default_page': 'defaultPage',
            'id': 'id',
            'content': 'content',
            'title': 'title',
            'removable': 'removable',
            'editable': 'editable'
        }

        self._default_page = default_page
        self._id = id
        self._content = content
        self._title = title
        self._removable = removable
        self._editable = editable

    @property
    def default_page(self):
        """
        Gets the default_page of this ProjectPageDTO.


        :return: The default_page of this ProjectPageDTO.
        :rtype: bool
        """
        return self._default_page

    @default_page.setter
    def default_page(self, default_page):
        """
        Sets the default_page of this ProjectPageDTO.


        :param default_page: The default_page of this ProjectPageDTO.
        :type: bool
        """
        
        self._default_page = default_page

    @property
    def id(self):
        """
        Gets the id of this ProjectPageDTO.


        :return: The id of this ProjectPageDTO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ProjectPageDTO.


        :param id: The id of this ProjectPageDTO.
        :type: str
        """
        
        self._id = id

    @property
    def content(self):
        """
        Gets the content of this ProjectPageDTO.


        :return: The content of this ProjectPageDTO.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """
        Sets the content of this ProjectPageDTO.


        :param content: The content of this ProjectPageDTO.
        :type: str
        """
        
        self._content = content

    @property
    def title(self):
        """
        Gets the title of this ProjectPageDTO.


        :return: The title of this ProjectPageDTO.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this ProjectPageDTO.


        :param title: The title of this ProjectPageDTO.
        :type: str
        """
        
        self._title = title

    @property
    def removable(self):
        """
        Gets the removable of this ProjectPageDTO.


        :return: The removable of this ProjectPageDTO.
        :rtype: bool
        """
        return self._removable

    @removable.setter
    def removable(self, removable):
        """
        Sets the removable of this ProjectPageDTO.


        :param removable: The removable of this ProjectPageDTO.
        :type: bool
        """
        
        self._removable = removable

    @property
    def editable(self):
        """
        Gets the editable of this ProjectPageDTO.


        :return: The editable of this ProjectPageDTO.
        :rtype: bool
        """
        return self._editable

    @editable.setter
    def editable(self, editable):
        """
        Sets the editable of this ProjectPageDTO.


        :param editable: The editable of this ProjectPageDTO.
        :type: bool
        """
        
        self._editable = editable

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




