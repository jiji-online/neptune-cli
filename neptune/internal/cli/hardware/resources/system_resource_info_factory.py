#
# Copyright (c) 2018, deepsense.io
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import psutil

from neptune.internal.cli.hardware.cgroup.cgroup_monitor import CGroupMonitor
from neptune.internal.cli.hardware.gauges.gauge_mode import GaugeMode
from neptune.internal.cli.hardware.resources.gpu_card_indices_provider import GPUCardIndicesProvider
from neptune.internal.cli.hardware.resources.system_resource_info import SystemResourceInfo


class SystemResourceInfoFactory(object):
    def __init__(self, gpu_monitor, os_environ):
        self.__gpu_monitor = gpu_monitor
        self.__gpu_card_indices_provider = GPUCardIndicesProvider(
            cuda_visible_devices=os_environ.get(u'CUDA_VISIBLE_DEVICES'),
            gpu_card_count=self.__gpu_monitor.get_card_count())

    def create(self, gauge_mode):
        if gauge_mode == GaugeMode.SYSTEM:
            return self.__create_whole_system_resource_info()
        elif gauge_mode == GaugeMode.CGROUP:
            return self.__create_cgroup_resource_info()
        else:
            raise ValueError(str(u'Unknown gauge mode: {}'.format(gauge_mode)))

    def __create_whole_system_resource_info(self):
        return SystemResourceInfo(
            cpu_core_count=float(psutil.cpu_count()),
            memory_amount_bytes=psutil.virtual_memory().total,
            gpu_card_indices=self.__gpu_card_indices_provider.get(),
            gpu_memory_amount_bytes=self.__gpu_monitor.get_top_card_memory_in_bytes()
        )

    def __create_cgroup_resource_info(self):
        cgroup_monitor = CGroupMonitor.create()

        return SystemResourceInfo(
            cpu_core_count=cgroup_monitor.get_cpu_usage_limit_in_cores(),
            memory_amount_bytes=cgroup_monitor.get_memory_limit_in_bytes(),
            gpu_card_indices=self.__gpu_card_indices_provider.get(),
            gpu_memory_amount_bytes=self.__gpu_monitor.get_top_card_memory_in_bytes()
        )
