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
from requests_oauthlib import OAuth2Session

from neptune.internal.common.api.tokens import CompositeToken


class NeptuneOAuth2Session(OAuth2Session):
    def __init__(self, *args, **kwargs):
        super(NeptuneOAuth2Session, self).__init__(*args, **kwargs)

    def refresh_token(self, token_url, refresh_token=None, body='', auth=None,
                      timeout=None, headers=None, verify=True, proxies=None, **kwargs):
        # Skipping **kwargs in order to avoid Issue 3 from https://github.com/requests/requests-oauthlib/issues/264
        fresh_token_from_api = super(NeptuneOAuth2Session, self).refresh_token(
            token_url=token_url, refresh_token=refresh_token, body=body, auth=auth,
            timeout=timeout, headers=headers, verify=verify, proxies=proxies
        )
        self.token = CompositeToken.from_json(fresh_token_from_api).raw_with_expires_at
        return self.token
