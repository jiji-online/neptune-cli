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

from neptune.internal.cli.hardware.metrics.reports.metric_report import MetricReport, MetricValue


class MetricReporter(object):
    def __init__(self, metrics, reference_timestamp):
        self.__metrics = metrics
        self.__reference_timestamp = reference_timestamp

    def report(self, timestamp):
        """
        :param timestamp: Time of measurement (float, seconds since Epoch).
        :return: list[MetricReport]
        """
        return [
            MetricReport(
                metric=metric,
                values=[self.__metric_value_for_gauge(gauge, timestamp) for gauge in metric.gauges]
            )
            for metric in self.__metrics
        ]

    def __metric_value_for_gauge(self, gauge, timestamp):
        return MetricValue(
            timestamp=timestamp - self.__reference_timestamp,
            gauge_name=gauge.name(),
            value=gauge.value()
        )
