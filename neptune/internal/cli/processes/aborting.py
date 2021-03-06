#
# Copyright (c) 2016, deepsense.io
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
from future.builtins import object

import logging

import psutil


class Aborting(object):
    def __init__(self, pid):
        self._pid = pid
        self._logger = logging.getLogger(__name__)

    def abort(self, kill_timeout=5):
        process = None
        try:
            process = psutil.Process(self._pid)
        except psutil.NoSuchProcess:
            self._logger.debug('Received an abort message, but the job is already finished.')

        if process is not None:
            processes = self._get_processes(process)
            for p in processes:
                self._abort(p)
            _, alive = psutil.wait_procs(processes, timeout=kill_timeout)
            for p in alive:
                self._kill(p)

    @staticmethod
    def _get_processes(process):
        try:
            return [process] + process.children(recursive=True)
        except psutil.NoSuchProcess:
            return []

    def _abort(self, process):
        try:
            if process.is_running():
                self._logger.debug("Sending SIGTERM to %s", process.pid)
                process.terminate()
        except psutil.NoSuchProcess:
            self._logger.info("Process %s already finished...", process.pid)

    def _kill(self, process):
        for process in self._get_processes(process):
            try:
                if process.is_running():
                    self._logger.debug("Sending SIGKILL to %s", process.pid)
                    process.kill()
            except psutil.NoSuchProcess:
                self._logger.info("Process %s already finished...", process.pid)
