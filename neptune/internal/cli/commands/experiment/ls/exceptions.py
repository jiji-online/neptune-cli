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
from neptune.internal.common import NeptuneException


class EntitySourceError(NeptuneException):
    pass


class ConnError(EntitySourceError):
    pass


class StatusCodeError(EntitySourceError):

    def __init__(self, status_code, message=None):
        super(StatusCodeError, self).__init__(message)
        self.status_code = status_code

    def __str__(self):
        return super(StatusCodeError, self).__str__() + u'Status Code: {}.'.format(self.status_code)
