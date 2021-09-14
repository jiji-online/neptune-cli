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

from .base_enum_model import BaseEnumModel


class ExperimentStateDTO(BaseEnumModel):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        pass

    allowable_values = [u'creating', u'waiting', u'initializing', u'running', u'cleaning', u'succeeded', u'failed', u'aborted', u'crashed', u'preempted']

    creating = u'creating'
    waiting = u'waiting'
    initializing = u'initializing'
    running = u'running'
    cleaning = u'cleaning'
    succeeded = u'succeeded'
    failed = u'failed'
    aborted = u'aborted'
    crashed = u'crashed'
    preempted = u'preempted'
    

    @staticmethod
    def value_allowed(value):
        return value in ExperimentStateDTO.allowable_values



