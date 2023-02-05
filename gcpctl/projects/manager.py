"""GCP Projects Manager"""
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
import logging
from google.cloud import resourcemanager_v3

from gcpctl.manager import GCPManager
from gcpctl.utils.colors import BCOLORS

LOG = logging.getLogger(__name__)


class ProjectManager(GCPManager):
    """Manages GCP operations related to projects."""

    def __init__(self, folder_ids=None, env_types=None) -> None:
        self.client = resourcemanager_v3.ProjectsClient()
        self.folder_ids = folder_ids
        self.env_types = env_types
        super().__init__()
        self._load_conf()

    def _list_call_and_print(self, folder_id=None):
        if folder_id:
            LOG.info("%sListing projects from folder %s%s\n",
                     BCOLORS['YELLOW'], folder_id, BCOLORS['ENDC'])
            request = resourcemanager_v3.ListProjectsRequest(
                parent=f"folders/{folder_id}")
        else:
            request = resourcemanager_v3.ListProjectsRequest()
        for project in self.client.list_projects(request=request):
            print(project.display_name)
        print()

    def list(self):
        """List projects."""
        if self.folder_ids:
            for folder_id in self.folder_ids:
                self._list_call_and_print(folder_id)
        if self.env_types:
            for env_type in self.env_types:
                for folder_id in \
                        self.config.data.get('environments').get(env_type):
                    self._list_call_and_print(folder_id)
        if not self.env_types and not self.folder_ids:
            self._list_call_and_print()

    def create(self):
        """Creates a new GCP project."""
