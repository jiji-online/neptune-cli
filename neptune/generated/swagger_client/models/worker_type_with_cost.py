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


class WorkerTypeWithCost(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, storage_size=None, name=None, preemptible=None, gpu=None, description=None, gpu_memory=None, pessimistic_provisioning_time=None, featured=None, storage_type=None, deprecated=None, machine_type=None, gpu_type=None, cost_per_second=None, optimistic_provisioning_time=None, cpu=None, is_default=None, memory=None):
        """
        WorkerTypeWithCost - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'storage_size': 'int',
            'name': 'str',
            'preemptible': 'bool',
            'gpu': 'int',
            'description': 'str',
            'gpu_memory': 'int',
            'pessimistic_provisioning_time': 'int',
            'featured': 'bool',
            'storage_type': 'StorageType',
            'deprecated': 'bool',
            'machine_type': 'str',
            'gpu_type': 'str',
            'cost_per_second': 'float',
            'optimistic_provisioning_time': 'int',
            'cpu': 'int',
            'is_default': 'bool',
            'memory': 'int'
        }

        self.attribute_map = {
            'storage_size': 'storageSize',
            'name': 'name',
            'preemptible': 'preemptible',
            'gpu': 'GPU',
            'description': 'description',
            'gpu_memory': 'GPUMemory',
            'pessimistic_provisioning_time': 'pessimisticProvisioningTime',
            'featured': 'featured',
            'storage_type': 'storageType',
            'deprecated': 'deprecated',
            'machine_type': 'machineType',
            'gpu_type': 'GPUType',
            'cost_per_second': 'costPerSecond',
            'optimistic_provisioning_time': 'optimisticProvisioningTime',
            'cpu': 'CPU',
            'is_default': 'isDefault',
            'memory': 'memory'
        }

        self._storage_size = storage_size
        self._name = name
        self._preemptible = preemptible
        self._gpu = gpu
        self._description = description
        self._gpu_memory = gpu_memory
        self._pessimistic_provisioning_time = pessimistic_provisioning_time
        self._featured = featured
        self._storage_type = storage_type
        self._deprecated = deprecated
        self._machine_type = machine_type
        self._gpu_type = gpu_type
        self._cost_per_second = cost_per_second
        self._optimistic_provisioning_time = optimistic_provisioning_time
        self._cpu = cpu
        self._is_default = is_default
        self._memory = memory

    @property
    def storage_size(self):
        """
        Gets the storage_size of this WorkerTypeWithCost.


        :return: The storage_size of this WorkerTypeWithCost.
        :rtype: int
        """
        return self._storage_size

    @storage_size.setter
    def storage_size(self, storage_size):
        """
        Sets the storage_size of this WorkerTypeWithCost.


        :param storage_size: The storage_size of this WorkerTypeWithCost.
        :type: int
        """
        
        self._storage_size = storage_size

    @property
    def name(self):
        """
        Gets the name of this WorkerTypeWithCost.


        :return: The name of this WorkerTypeWithCost.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this WorkerTypeWithCost.


        :param name: The name of this WorkerTypeWithCost.
        :type: str
        """
        
        self._name = name

    @property
    def preemptible(self):
        """
        Gets the preemptible of this WorkerTypeWithCost.


        :return: The preemptible of this WorkerTypeWithCost.
        :rtype: bool
        """
        return self._preemptible

    @preemptible.setter
    def preemptible(self, preemptible):
        """
        Sets the preemptible of this WorkerTypeWithCost.


        :param preemptible: The preemptible of this WorkerTypeWithCost.
        :type: bool
        """
        
        self._preemptible = preemptible

    @property
    def gpu(self):
        """
        Gets the gpu of this WorkerTypeWithCost.


        :return: The gpu of this WorkerTypeWithCost.
        :rtype: int
        """
        return self._gpu

    @gpu.setter
    def gpu(self, gpu):
        """
        Sets the gpu of this WorkerTypeWithCost.


        :param gpu: The gpu of this WorkerTypeWithCost.
        :type: int
        """
        
        self._gpu = gpu

    @property
    def description(self):
        """
        Gets the description of this WorkerTypeWithCost.


        :return: The description of this WorkerTypeWithCost.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this WorkerTypeWithCost.


        :param description: The description of this WorkerTypeWithCost.
        :type: str
        """
        
        self._description = description

    @property
    def gpu_memory(self):
        """
        Gets the gpu_memory of this WorkerTypeWithCost.


        :return: The gpu_memory of this WorkerTypeWithCost.
        :rtype: int
        """
        return self._gpu_memory

    @gpu_memory.setter
    def gpu_memory(self, gpu_memory):
        """
        Sets the gpu_memory of this WorkerTypeWithCost.


        :param gpu_memory: The gpu_memory of this WorkerTypeWithCost.
        :type: int
        """
        
        self._gpu_memory = gpu_memory

    @property
    def pessimistic_provisioning_time(self):
        """
        Gets the pessimistic_provisioning_time of this WorkerTypeWithCost.


        :return: The pessimistic_provisioning_time of this WorkerTypeWithCost.
        :rtype: int
        """
        return self._pessimistic_provisioning_time

    @pessimistic_provisioning_time.setter
    def pessimistic_provisioning_time(self, pessimistic_provisioning_time):
        """
        Sets the pessimistic_provisioning_time of this WorkerTypeWithCost.


        :param pessimistic_provisioning_time: The pessimistic_provisioning_time of this WorkerTypeWithCost.
        :type: int
        """
        
        self._pessimistic_provisioning_time = pessimistic_provisioning_time

    @property
    def featured(self):
        """
        Gets the featured of this WorkerTypeWithCost.


        :return: The featured of this WorkerTypeWithCost.
        :rtype: bool
        """
        return self._featured

    @featured.setter
    def featured(self, featured):
        """
        Sets the featured of this WorkerTypeWithCost.


        :param featured: The featured of this WorkerTypeWithCost.
        :type: bool
        """
        
        self._featured = featured

    @property
    def storage_type(self):
        """
        Gets the storage_type of this WorkerTypeWithCost.


        :return: The storage_type of this WorkerTypeWithCost.
        :rtype: StorageType
        """
        return self._storage_type

    @storage_type.setter
    def storage_type(self, storage_type):
        """
        Sets the storage_type of this WorkerTypeWithCost.


        :param storage_type: The storage_type of this WorkerTypeWithCost.
        :type: StorageType
        """
        
        self._storage_type = storage_type

    @property
    def deprecated(self):
        """
        Gets the deprecated of this WorkerTypeWithCost.


        :return: The deprecated of this WorkerTypeWithCost.
        :rtype: bool
        """
        return self._deprecated

    @deprecated.setter
    def deprecated(self, deprecated):
        """
        Sets the deprecated of this WorkerTypeWithCost.


        :param deprecated: The deprecated of this WorkerTypeWithCost.
        :type: bool
        """
        
        self._deprecated = deprecated

    @property
    def machine_type(self):
        """
        Gets the machine_type of this WorkerTypeWithCost.


        :return: The machine_type of this WorkerTypeWithCost.
        :rtype: str
        """
        return self._machine_type

    @machine_type.setter
    def machine_type(self, machine_type):
        """
        Sets the machine_type of this WorkerTypeWithCost.


        :param machine_type: The machine_type of this WorkerTypeWithCost.
        :type: str
        """
        
        self._machine_type = machine_type

    @property
    def gpu_type(self):
        """
        Gets the gpu_type of this WorkerTypeWithCost.


        :return: The gpu_type of this WorkerTypeWithCost.
        :rtype: str
        """
        return self._gpu_type

    @gpu_type.setter
    def gpu_type(self, gpu_type):
        """
        Sets the gpu_type of this WorkerTypeWithCost.


        :param gpu_type: The gpu_type of this WorkerTypeWithCost.
        :type: str
        """
        
        self._gpu_type = gpu_type

    @property
    def cost_per_second(self):
        """
        Gets the cost_per_second of this WorkerTypeWithCost.


        :return: The cost_per_second of this WorkerTypeWithCost.
        :rtype: float
        """
        return self._cost_per_second

    @cost_per_second.setter
    def cost_per_second(self, cost_per_second):
        """
        Sets the cost_per_second of this WorkerTypeWithCost.


        :param cost_per_second: The cost_per_second of this WorkerTypeWithCost.
        :type: float
        """
        
        self._cost_per_second = cost_per_second

    @property
    def optimistic_provisioning_time(self):
        """
        Gets the optimistic_provisioning_time of this WorkerTypeWithCost.


        :return: The optimistic_provisioning_time of this WorkerTypeWithCost.
        :rtype: int
        """
        return self._optimistic_provisioning_time

    @optimistic_provisioning_time.setter
    def optimistic_provisioning_time(self, optimistic_provisioning_time):
        """
        Sets the optimistic_provisioning_time of this WorkerTypeWithCost.


        :param optimistic_provisioning_time: The optimistic_provisioning_time of this WorkerTypeWithCost.
        :type: int
        """
        
        self._optimistic_provisioning_time = optimistic_provisioning_time

    @property
    def cpu(self):
        """
        Gets the cpu of this WorkerTypeWithCost.


        :return: The cpu of this WorkerTypeWithCost.
        :rtype: int
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        """
        Sets the cpu of this WorkerTypeWithCost.


        :param cpu: The cpu of this WorkerTypeWithCost.
        :type: int
        """
        
        self._cpu = cpu

    @property
    def is_default(self):
        """
        Gets the is_default of this WorkerTypeWithCost.


        :return: The is_default of this WorkerTypeWithCost.
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """
        Sets the is_default of this WorkerTypeWithCost.


        :param is_default: The is_default of this WorkerTypeWithCost.
        :type: bool
        """
        
        self._is_default = is_default

    @property
    def memory(self):
        """
        Gets the memory of this WorkerTypeWithCost.


        :return: The memory of this WorkerTypeWithCost.
        :rtype: int
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        """
        Sets the memory of this WorkerTypeWithCost.


        :param memory: The memory of this WorkerTypeWithCost.
        :type: int
        """
        
        self._memory = memory

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




