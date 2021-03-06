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

from neptune.internal.common.websockets.reconnecting_websocket import ReconnectingWebsocket


class ReconnectingWebsocketFactory(object):
    def __init__(self, base_address, experiment_id, offline_token_storage_service, keycloak_api_service, local_storage):
        self._base_address = base_address
        self._experiment_id = experiment_id
        self._offline_token_storage_service = offline_token_storage_service
        self._keycloak_api_service = keycloak_api_service
        self._local_storage = local_storage

    def create(self, shutdown_condition):
        url = self._experiment_url(self._base_address, self._experiment_id)
        return ReconnectingWebsocket(url=url, offline_token_storage_service=self._offline_token_storage_service,
                                     keycloak_api_service=self._keycloak_api_service, shutdown_event=shutdown_condition,
                                     local_storage=self._local_storage)

    @staticmethod
    def _experiment_url(base_address, experiment_id):
        return base_address + '/experiments/' + experiment_id + '/operations'
