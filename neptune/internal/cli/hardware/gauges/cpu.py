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
from neptune.internal.cli.hardware.gauges.gauge import Gauge


class SystemCpuUsageGauge(Gauge):
    def name(self):
        return u'cpu'

    def value(self):
        return psutil.cpu_percent()

    def __eq__(self, other):
        return self.__class__ == other.__class__

    def __repr__(self):
        return str(u'SystemCpuUsageGauge')


class CGroupCpuUsageGauge(Gauge):
    def __init__(self):
        self.__cgroup_monitor = CGroupMonitor.create()

    def name(self):
        return u'cpu'

    def value(self):
        return self.__cgroup_monitor.get_cpu_usage_percentage()

    def __eq__(self, other):
        return self.__class__ == other.__class__

    def __repr__(self):
        return str(u'CGroupCpuUsageGauge')
