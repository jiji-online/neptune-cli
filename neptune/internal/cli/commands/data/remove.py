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


from __future__ import print_function

from neptune.internal.cli.commands.command_names import CommandNames
from neptune.internal.cli.commands.data.utils.api_wrapper import DataApiWrapper
from neptune.internal.cli.commands.exceptions.data_exceptions import NeptuneCantRemoveWithoutRecursiveException
from neptune.internal.cli.commands.framework import CommandUnsuccessfulError
from neptune.internal.cli.commands.neptune_command import NeptuneCommand
from neptune.internal.common.api.exceptions import NeptuneBadClientRequest
from neptune.internal.common.models.rich_project import ProjectNotFoundError, ProjectResolver


class DataRemove(NeptuneCommand):

    def __init__(self,
                 config,
                 api_service,
                 organization_name,
                 project_name,
                 path,
                 recursive):
        super(DataRemove, self).__init__(CommandNames.RM, config, api_service)
        self.organization_name = organization_name
        self.project_name = project_name
        self.path = path
        self.config = config
        self.recursive = recursive

    def run(self, args):
        try:
            project_id = ProjectResolver.resolve(
                api_service=self.api_service,
                organization_name=self.organization_name,
                project_name=self.project_name).id
        except ProjectNotFoundError as exc:
            raise CommandUnsuccessfulError(str(exc))
        DataApiWrapper.execute(self._rm_data_api_call, project_id=project_id,
                               path_param=self.path, recursive=self.recursive)

    def _rm_data_api_call(self, project_id, path_param, recursive):
        try:
            self.api_service.rm_data(project_id=project_id, path_param=path_param, recursive=recursive)
        except NeptuneBadClientRequest as ex:
            raise NeptuneCantRemoveWithoutRecursiveException(ex.response_message)
