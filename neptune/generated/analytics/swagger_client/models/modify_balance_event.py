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


class ModifyBalanceEvent(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, balance=None, balance_change=None, bonus=None, bonus_change=None, info=None, reason=None):
        """
        ModifyBalanceEvent - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'balance': 'float',
            'balance_change': 'float',
            'bonus': 'float',
            'bonus_change': 'float',
            'info': 'str',
            'reason': 'str'
        }

        self.attribute_map = {
            'balance': 'balance',
            'balance_change': 'balanceChange',
            'bonus': 'bonus',
            'bonus_change': 'bonusChange',
            'info': 'info',
            'reason': 'reason'
        }

        self._balance = balance
        self._balance_change = balance_change
        self._bonus = bonus
        self._bonus_change = bonus_change
        self._info = info
        self._reason = reason

    @property
    def balance(self):
        """
        Gets the balance of this ModifyBalanceEvent.


        :return: The balance of this ModifyBalanceEvent.
        :rtype: float
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """
        Sets the balance of this ModifyBalanceEvent.


        :param balance: The balance of this ModifyBalanceEvent.
        :type: float
        """
        
        self._balance = balance

    @property
    def balance_change(self):
        """
        Gets the balance_change of this ModifyBalanceEvent.


        :return: The balance_change of this ModifyBalanceEvent.
        :rtype: float
        """
        return self._balance_change

    @balance_change.setter
    def balance_change(self, balance_change):
        """
        Sets the balance_change of this ModifyBalanceEvent.


        :param balance_change: The balance_change of this ModifyBalanceEvent.
        :type: float
        """
        
        self._balance_change = balance_change

    @property
    def bonus(self):
        """
        Gets the bonus of this ModifyBalanceEvent.


        :return: The bonus of this ModifyBalanceEvent.
        :rtype: float
        """
        return self._bonus

    @bonus.setter
    def bonus(self, bonus):
        """
        Sets the bonus of this ModifyBalanceEvent.


        :param bonus: The bonus of this ModifyBalanceEvent.
        :type: float
        """
        
        self._bonus = bonus

    @property
    def bonus_change(self):
        """
        Gets the bonus_change of this ModifyBalanceEvent.


        :return: The bonus_change of this ModifyBalanceEvent.
        :rtype: float
        """
        return self._bonus_change

    @bonus_change.setter
    def bonus_change(self, bonus_change):
        """
        Sets the bonus_change of this ModifyBalanceEvent.


        :param bonus_change: The bonus_change of this ModifyBalanceEvent.
        :type: float
        """
        
        self._bonus_change = bonus_change

    @property
    def info(self):
        """
        Gets the info of this ModifyBalanceEvent.


        :return: The info of this ModifyBalanceEvent.
        :rtype: str
        """
        return self._info

    @info.setter
    def info(self, info):
        """
        Sets the info of this ModifyBalanceEvent.


        :param info: The info of this ModifyBalanceEvent.
        :type: str
        """
        
        self._info = info

    @property
    def reason(self):
        """
        Gets the reason of this ModifyBalanceEvent.


        :return: The reason of this ModifyBalanceEvent.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """
        Sets the reason of this ModifyBalanceEvent.


        :param reason: The reason of this ModifyBalanceEvent.
        :type: str
        """
        
        self._reason = reason

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




