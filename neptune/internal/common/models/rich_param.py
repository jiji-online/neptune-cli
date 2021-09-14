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
from future.utils import iteritems

from neptune.generated.swagger_client.models.parameter import \
    Parameter as SwaggerGeneratedParameter


class RichParam(SwaggerGeneratedParameter):

    """ Wrapper for Parameter class generated by Swagger with value. """

    def __init__(self, param):
        super(RichParam, self).__init__()

        for k, v in iteritems(vars(param)):
            setattr(self, k, v)

    def as_cmd_line_argument(self):
        return [u"--" + self.name, self.value]
