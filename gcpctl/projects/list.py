# Copyright 2023 Arie Bregman
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
from google.cloud import resourcemanager_v3
import logging
import sys

from gcpctl.projects.manager import ProjectManager

LOG = logging.getLogger(__name__)


class ProjectLister(ProjectManager):

    def __init__(self) -> None:
        super().__init__()

    def list(self, folder_id=None):
        """List projects."""
        LOG.debug(f"Listing projects from folder {folder_id}")
        if folder_id:
            request = resourcemanager_v3.ListProjectsRequest(
                parent=f"folders/{folder_id}")
        else:
            request = resourcemanager_v3.ListProjectsRequest()
        for project in self.client.list_projects(request=request):
            print(project.display_name)
        print()
