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


class ExecutionInfo(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, backup=None, command=None, traceback=None, inputs=None, worker_type=None, source_info=None, environment=None, components_versions=None, config_path=None, output=None, exec_args_template=None):
        """
        ExecutionInfo - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'backup': 'Backup',
            'command': 'str',
            'traceback': 'str',
            'inputs': 'list[InputMetadata]',
            'worker_type': 'WorkerTypeWithCost',
            'source_info': 'SourceInfo',
            'environment': 'Environment',
            'components_versions': 'list[ComponentVersion]',
            'config_path': 'str',
            'output': 'StorageLocation',
            'exec_args_template': 'str'
        }

        self.attribute_map = {
            'backup': 'backup',
            'command': 'command',
            'traceback': 'traceback',
            'inputs': 'inputs',
            'worker_type': 'workerType',
            'source_info': 'sourceInfo',
            'environment': 'environment',
            'components_versions': 'componentsVersions',
            'config_path': 'configPath',
            'output': 'output',
            'exec_args_template': 'execArgsTemplate'
        }

        self._backup = backup
        self._command = command
        self._traceback = traceback
        self._inputs = inputs
        self._worker_type = worker_type
        self._source_info = source_info
        self._environment = environment
        self._components_versions = components_versions
        self._config_path = config_path
        self._output = output
        self._exec_args_template = exec_args_template

    @property
    def backup(self):
        """
        Gets the backup of this ExecutionInfo.


        :return: The backup of this ExecutionInfo.
        :rtype: Backup
        """
        return self._backup

    @backup.setter
    def backup(self, backup):
        """
        Sets the backup of this ExecutionInfo.


        :param backup: The backup of this ExecutionInfo.
        :type: Backup
        """
        
        self._backup = backup

    @property
    def command(self):
        """
        Gets the command of this ExecutionInfo.


        :return: The command of this ExecutionInfo.
        :rtype: str
        """
        return self._command

    @command.setter
    def command(self, command):
        """
        Sets the command of this ExecutionInfo.


        :param command: The command of this ExecutionInfo.
        :type: str
        """
        
        self._command = command

    @property
    def traceback(self):
        """
        Gets the traceback of this ExecutionInfo.


        :return: The traceback of this ExecutionInfo.
        :rtype: str
        """
        return self._traceback

    @traceback.setter
    def traceback(self, traceback):
        """
        Sets the traceback of this ExecutionInfo.


        :param traceback: The traceback of this ExecutionInfo.
        :type: str
        """
        
        self._traceback = traceback

    @property
    def inputs(self):
        """
        Gets the inputs of this ExecutionInfo.


        :return: The inputs of this ExecutionInfo.
        :rtype: list[InputMetadata]
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        """
        Sets the inputs of this ExecutionInfo.


        :param inputs: The inputs of this ExecutionInfo.
        :type: list[InputMetadata]
        """
        
        self._inputs = inputs

    @property
    def worker_type(self):
        """
        Gets the worker_type of this ExecutionInfo.


        :return: The worker_type of this ExecutionInfo.
        :rtype: WorkerTypeWithCost
        """
        return self._worker_type

    @worker_type.setter
    def worker_type(self, worker_type):
        """
        Sets the worker_type of this ExecutionInfo.


        :param worker_type: The worker_type of this ExecutionInfo.
        :type: WorkerTypeWithCost
        """
        
        self._worker_type = worker_type

    @property
    def source_info(self):
        """
        Gets the source_info of this ExecutionInfo.


        :return: The source_info of this ExecutionInfo.
        :rtype: SourceInfo
        """
        return self._source_info

    @source_info.setter
    def source_info(self, source_info):
        """
        Sets the source_info of this ExecutionInfo.


        :param source_info: The source_info of this ExecutionInfo.
        :type: SourceInfo
        """
        
        self._source_info = source_info

    @property
    def environment(self):
        """
        Gets the environment of this ExecutionInfo.


        :return: The environment of this ExecutionInfo.
        :rtype: Environment
        """
        return self._environment

    @environment.setter
    def environment(self, environment):
        """
        Sets the environment of this ExecutionInfo.


        :param environment: The environment of this ExecutionInfo.
        :type: Environment
        """
        
        self._environment = environment

    @property
    def components_versions(self):
        """
        Gets the components_versions of this ExecutionInfo.


        :return: The components_versions of this ExecutionInfo.
        :rtype: list[ComponentVersion]
        """
        return self._components_versions

    @components_versions.setter
    def components_versions(self, components_versions):
        """
        Sets the components_versions of this ExecutionInfo.


        :param components_versions: The components_versions of this ExecutionInfo.
        :type: list[ComponentVersion]
        """
        
        self._components_versions = components_versions

    @property
    def config_path(self):
        """
        Gets the config_path of this ExecutionInfo.


        :return: The config_path of this ExecutionInfo.
        :rtype: str
        """
        return self._config_path

    @config_path.setter
    def config_path(self, config_path):
        """
        Sets the config_path of this ExecutionInfo.


        :param config_path: The config_path of this ExecutionInfo.
        :type: str
        """
        
        self._config_path = config_path

    @property
    def output(self):
        """
        Gets the output of this ExecutionInfo.


        :return: The output of this ExecutionInfo.
        :rtype: StorageLocation
        """
        return self._output

    @output.setter
    def output(self, output):
        """
        Sets the output of this ExecutionInfo.


        :param output: The output of this ExecutionInfo.
        :type: StorageLocation
        """
        
        self._output = output

    @property
    def exec_args_template(self):
        """
        Gets the exec_args_template of this ExecutionInfo.


        :return: The exec_args_template of this ExecutionInfo.
        :rtype: str
        """
        return self._exec_args_template

    @exec_args_template.setter
    def exec_args_template(self, exec_args_template):
        """
        Sets the exec_args_template of this ExecutionInfo.


        :param exec_args_template: The exec_args_template of this ExecutionInfo.
        :type: str
        """
        
        self._exec_args_template = exec_args_template

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




