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
import logging
import time

from neptune.internal.common.exceptions.base_exceptions import NeptuneThreadInterruptedException
from neptune.internal.common.threads.neptune_thread import NeptuneThread


class HardwareMetricReportingThread(NeptuneThread):
    def __init__(self, metric_service, metric_sending_interval_seconds):
        super(HardwareMetricReportingThread, self).__init__(is_daemon=True)
        self.__logger = logging.getLogger(__name__)
        self.__metric_service = metric_service
        self.__metric_sending_interval_seconds = metric_sending_interval_seconds

    def run(self):
        try:
            while not self.is_interrupted():
                before = time.time()
                self.__metric_service.report_and_send(timestamp=time.time())
                reporting_duration = time.time() - before

                time.sleep(max(0, self.__metric_sending_interval_seconds - reporting_duration))
        except NeptuneThreadInterruptedException:
            pass
        except Exception as e:
            self.__logger.error(e)
