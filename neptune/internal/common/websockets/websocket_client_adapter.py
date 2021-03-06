# -*- coding: utf-8 -*-
#
# Copyright (c) 2017, deepsense.io
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

from future.utils import PY3
from websocket import ABNF, create_connection

from neptune.internal.common import NeptuneException


class WebsocketClientAdapter(object):
    def __init__(self):
        self._ws_client = None
        self._logger = logging.getLogger(__name__)

    def connect(self, url, token):
        self._ws_client = create_connection(url, header=self._auth_header(token))

    def recv(self):
        if self._ws_client is None:
            raise WebsocketNotConnectedException()

        opcode, data = None, None

        while opcode != ABNF.OPCODE_TEXT:
            opcode, data = self._ws_client.recv_data()
            self._logger.debug(u'Received message (code = %s): %s', str(opcode), str(data))

        return data.decode("utf-8") if PY3 else data

    @property
    def connected(self):
        return self._ws_client and self._ws_client.connected

    def abort(self):
        if self._ws_client:
            return self._ws_client.abort()

    def shutdown(self):
        if self._ws_client:
            return self._ws_client.shutdown()

    @classmethod
    def _auth_header(cls, token):
        return ["Authorization: Bearer " + token.access_token.raw]


class WebsocketNotConnectedException(NeptuneException):
    def __init__(self):
        super(WebsocketNotConnectedException, self).__init__('Websocket client is not connected!')
