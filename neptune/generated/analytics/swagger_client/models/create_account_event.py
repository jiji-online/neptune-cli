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


class CreateAccountEvent(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, campaign_name=None, campaign_source=None, email=None, free_credits=None, frontend_id=None, login_method=None, name=None, organization_id=None, pricing_plan=None, session_time=None, trial_period_days=None, username=None):
        """
        CreateAccountEvent - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'campaign_name': 'str',
            'campaign_source': 'str',
            'email': 'str',
            'free_credits': 'int',
            'frontend_id': 'str',
            'login_method': 'str',
            'name': 'str',
            'organization_id': 'str',
            'pricing_plan': 'str',
            'session_time': 'int',
            'trial_period_days': 'int',
            'username': 'str'
        }

        self.attribute_map = {
            'campaign_name': 'campaignName',
            'campaign_source': 'campaignSource',
            'email': 'email',
            'free_credits': 'freeCredits',
            'frontend_id': 'frontendId',
            'login_method': 'loginMethod',
            'name': 'name',
            'organization_id': 'organizationId',
            'pricing_plan': 'pricingPlan',
            'session_time': 'sessionTime',
            'trial_period_days': 'trialPeriodDays',
            'username': 'username'
        }

        self._campaign_name = campaign_name
        self._campaign_source = campaign_source
        self._email = email
        self._free_credits = free_credits
        self._frontend_id = frontend_id
        self._login_method = login_method
        self._name = name
        self._organization_id = organization_id
        self._pricing_plan = pricing_plan
        self._session_time = session_time
        self._trial_period_days = trial_period_days
        self._username = username

    @property
    def campaign_name(self):
        """
        Gets the campaign_name of this CreateAccountEvent.


        :return: The campaign_name of this CreateAccountEvent.
        :rtype: str
        """
        return self._campaign_name

    @campaign_name.setter
    def campaign_name(self, campaign_name):
        """
        Sets the campaign_name of this CreateAccountEvent.


        :param campaign_name: The campaign_name of this CreateAccountEvent.
        :type: str
        """
        
        self._campaign_name = campaign_name

    @property
    def campaign_source(self):
        """
        Gets the campaign_source of this CreateAccountEvent.


        :return: The campaign_source of this CreateAccountEvent.
        :rtype: str
        """
        return self._campaign_source

    @campaign_source.setter
    def campaign_source(self, campaign_source):
        """
        Sets the campaign_source of this CreateAccountEvent.


        :param campaign_source: The campaign_source of this CreateAccountEvent.
        :type: str
        """
        
        self._campaign_source = campaign_source

    @property
    def email(self):
        """
        Gets the email of this CreateAccountEvent.


        :return: The email of this CreateAccountEvent.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this CreateAccountEvent.


        :param email: The email of this CreateAccountEvent.
        :type: str
        """
        
        self._email = email

    @property
    def free_credits(self):
        """
        Gets the free_credits of this CreateAccountEvent.


        :return: The free_credits of this CreateAccountEvent.
        :rtype: int
        """
        return self._free_credits

    @free_credits.setter
    def free_credits(self, free_credits):
        """
        Sets the free_credits of this CreateAccountEvent.


        :param free_credits: The free_credits of this CreateAccountEvent.
        :type: int
        """
        
        self._free_credits = free_credits

    @property
    def frontend_id(self):
        """
        Gets the frontend_id of this CreateAccountEvent.


        :return: The frontend_id of this CreateAccountEvent.
        :rtype: str
        """
        return self._frontend_id

    @frontend_id.setter
    def frontend_id(self, frontend_id):
        """
        Sets the frontend_id of this CreateAccountEvent.


        :param frontend_id: The frontend_id of this CreateAccountEvent.
        :type: str
        """
        
        self._frontend_id = frontend_id

    @property
    def login_method(self):
        """
        Gets the login_method of this CreateAccountEvent.


        :return: The login_method of this CreateAccountEvent.
        :rtype: str
        """
        return self._login_method

    @login_method.setter
    def login_method(self, login_method):
        """
        Sets the login_method of this CreateAccountEvent.


        :param login_method: The login_method of this CreateAccountEvent.
        :type: str
        """
        
        self._login_method = login_method

    @property
    def name(self):
        """
        Gets the name of this CreateAccountEvent.


        :return: The name of this CreateAccountEvent.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CreateAccountEvent.


        :param name: The name of this CreateAccountEvent.
        :type: str
        """
        
        self._name = name

    @property
    def organization_id(self):
        """
        Gets the organization_id of this CreateAccountEvent.


        :return: The organization_id of this CreateAccountEvent.
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """
        Sets the organization_id of this CreateAccountEvent.


        :param organization_id: The organization_id of this CreateAccountEvent.
        :type: str
        """
        
        self._organization_id = organization_id

    @property
    def pricing_plan(self):
        """
        Gets the pricing_plan of this CreateAccountEvent.


        :return: The pricing_plan of this CreateAccountEvent.
        :rtype: str
        """
        return self._pricing_plan

    @pricing_plan.setter
    def pricing_plan(self, pricing_plan):
        """
        Sets the pricing_plan of this CreateAccountEvent.


        :param pricing_plan: The pricing_plan of this CreateAccountEvent.
        :type: str
        """
        
        self._pricing_plan = pricing_plan

    @property
    def session_time(self):
        """
        Gets the session_time of this CreateAccountEvent.


        :return: The session_time of this CreateAccountEvent.
        :rtype: int
        """
        return self._session_time

    @session_time.setter
    def session_time(self, session_time):
        """
        Sets the session_time of this CreateAccountEvent.


        :param session_time: The session_time of this CreateAccountEvent.
        :type: int
        """
        
        self._session_time = session_time

    @property
    def trial_period_days(self):
        """
        Gets the trial_period_days of this CreateAccountEvent.


        :return: The trial_period_days of this CreateAccountEvent.
        :rtype: int
        """
        return self._trial_period_days

    @trial_period_days.setter
    def trial_period_days(self, trial_period_days):
        """
        Sets the trial_period_days of this CreateAccountEvent.


        :param trial_period_days: The trial_period_days of this CreateAccountEvent.
        :type: int
        """
        
        self._trial_period_days = trial_period_days

    @property
    def username(self):
        """
        Gets the username of this CreateAccountEvent.


        :return: The username of this CreateAccountEvent.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this CreateAccountEvent.


        :param username: The username of this CreateAccountEvent.
        :type: str
        """
        
        self._username = username

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



