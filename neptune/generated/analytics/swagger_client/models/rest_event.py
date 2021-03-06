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


class RestEvent(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, anonymous_page_view=None, cli_usage=None, click=None, interact_chart=None, modify_leaderboard=None, neptune_crash=None, read_documentation=None, time_spent=None, user_id=None, user_page_view=None):
        """
        RestEvent - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'anonymous_page_view': 'AnonymousPageViewEvent',
            'cli_usage': 'CliUsageEvent',
            'click': 'ClickEvent',
            'interact_chart': 'InteractChartEvent',
            'modify_leaderboard': 'ModifyLeaderboardEvent',
            'neptune_crash': 'NeptuneCrashEvent',
            'read_documentation': 'ReadDocumentationEvent',
            'time_spent': 'TimeSpentEvent',
            'user_id': 'str',
            'user_page_view': 'UserPageViewEvent'
        }

        self.attribute_map = {
            'anonymous_page_view': 'anonymousPageView',
            'cli_usage': 'cliUsage',
            'click': 'click',
            'interact_chart': 'interactChart',
            'modify_leaderboard': 'modifyLeaderboard',
            'neptune_crash': 'neptuneCrash',
            'read_documentation': 'readDocumentation',
            'time_spent': 'timeSpent',
            'user_id': 'userId',
            'user_page_view': 'userPageView'
        }

        self._anonymous_page_view = anonymous_page_view
        self._cli_usage = cli_usage
        self._click = click
        self._interact_chart = interact_chart
        self._modify_leaderboard = modify_leaderboard
        self._neptune_crash = neptune_crash
        self._read_documentation = read_documentation
        self._time_spent = time_spent
        self._user_id = user_id
        self._user_page_view = user_page_view

    @property
    def anonymous_page_view(self):
        """
        Gets the anonymous_page_view of this RestEvent.


        :return: The anonymous_page_view of this RestEvent.
        :rtype: AnonymousPageViewEvent
        """
        return self._anonymous_page_view

    @anonymous_page_view.setter
    def anonymous_page_view(self, anonymous_page_view):
        """
        Sets the anonymous_page_view of this RestEvent.


        :param anonymous_page_view: The anonymous_page_view of this RestEvent.
        :type: AnonymousPageViewEvent
        """
        
        self._anonymous_page_view = anonymous_page_view

    @property
    def cli_usage(self):
        """
        Gets the cli_usage of this RestEvent.


        :return: The cli_usage of this RestEvent.
        :rtype: CliUsageEvent
        """
        return self._cli_usage

    @cli_usage.setter
    def cli_usage(self, cli_usage):
        """
        Sets the cli_usage of this RestEvent.


        :param cli_usage: The cli_usage of this RestEvent.
        :type: CliUsageEvent
        """
        
        self._cli_usage = cli_usage

    @property
    def click(self):
        """
        Gets the click of this RestEvent.


        :return: The click of this RestEvent.
        :rtype: ClickEvent
        """
        return self._click

    @click.setter
    def click(self, click):
        """
        Sets the click of this RestEvent.


        :param click: The click of this RestEvent.
        :type: ClickEvent
        """
        
        self._click = click

    @property
    def interact_chart(self):
        """
        Gets the interact_chart of this RestEvent.


        :return: The interact_chart of this RestEvent.
        :rtype: InteractChartEvent
        """
        return self._interact_chart

    @interact_chart.setter
    def interact_chart(self, interact_chart):
        """
        Sets the interact_chart of this RestEvent.


        :param interact_chart: The interact_chart of this RestEvent.
        :type: InteractChartEvent
        """
        
        self._interact_chart = interact_chart

    @property
    def modify_leaderboard(self):
        """
        Gets the modify_leaderboard of this RestEvent.


        :return: The modify_leaderboard of this RestEvent.
        :rtype: ModifyLeaderboardEvent
        """
        return self._modify_leaderboard

    @modify_leaderboard.setter
    def modify_leaderboard(self, modify_leaderboard):
        """
        Sets the modify_leaderboard of this RestEvent.


        :param modify_leaderboard: The modify_leaderboard of this RestEvent.
        :type: ModifyLeaderboardEvent
        """
        
        self._modify_leaderboard = modify_leaderboard

    @property
    def neptune_crash(self):
        """
        Gets the neptune_crash of this RestEvent.


        :return: The neptune_crash of this RestEvent.
        :rtype: NeptuneCrashEvent
        """
        return self._neptune_crash

    @neptune_crash.setter
    def neptune_crash(self, neptune_crash):
        """
        Sets the neptune_crash of this RestEvent.


        :param neptune_crash: The neptune_crash of this RestEvent.
        :type: NeptuneCrashEvent
        """
        
        self._neptune_crash = neptune_crash

    @property
    def read_documentation(self):
        """
        Gets the read_documentation of this RestEvent.


        :return: The read_documentation of this RestEvent.
        :rtype: ReadDocumentationEvent
        """
        return self._read_documentation

    @read_documentation.setter
    def read_documentation(self, read_documentation):
        """
        Sets the read_documentation of this RestEvent.


        :param read_documentation: The read_documentation of this RestEvent.
        :type: ReadDocumentationEvent
        """
        
        self._read_documentation = read_documentation

    @property
    def time_spent(self):
        """
        Gets the time_spent of this RestEvent.


        :return: The time_spent of this RestEvent.
        :rtype: TimeSpentEvent
        """
        return self._time_spent

    @time_spent.setter
    def time_spent(self, time_spent):
        """
        Sets the time_spent of this RestEvent.


        :param time_spent: The time_spent of this RestEvent.
        :type: TimeSpentEvent
        """
        
        self._time_spent = time_spent

    @property
    def user_id(self):
        """
        Gets the user_id of this RestEvent.


        :return: The user_id of this RestEvent.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this RestEvent.


        :param user_id: The user_id of this RestEvent.
        :type: str
        """
        
        self._user_id = user_id

    @property
    def user_page_view(self):
        """
        Gets the user_page_view of this RestEvent.


        :return: The user_page_view of this RestEvent.
        :rtype: UserPageViewEvent
        """
        return self._user_page_view

    @user_page_view.setter
    def user_page_view(self, user_page_view):
        """
        Sets the user_page_view of this RestEvent.


        :param user_page_view: The user_page_view of this RestEvent.
        :type: UserPageViewEvent
        """
        
        self._user_page_view = user_page_view

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




