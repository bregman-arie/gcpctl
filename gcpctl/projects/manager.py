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
from google.api_core.exceptions import PermissionDenied

from gcpctl.manager import GCPManager
from gcpctl.utils.colors import BCOLORS
from gcpctl.printer import Printer

LOG = logging.getLogger(__name__)


class ProjectManager(GCPManager):
    """Manages GCP operations related to projects."""

    def __init__(self, folder_ids=None) -> None:
        self.client = resourcemanager_v3.ProjectsClient()
        self.folder_ids = folder_ids
        super().__init__()

    def get_projects(self):
        projects = []
        for folder_id in self.folder_ids:
            request = resourcemanager_v3.ListProjectsRequest(
                parent=f"folders/{folder_id}")
            try:
                projects.extend([project for project in
                                self.client.list_projects(request=request)])
            except PermissionDenied:
                if folder_id:
                    msg = "folder %s" % folder_id
                else:
                    msg = "root project"
                LOG.error("%sNo permissions to access %s%s",
                          BCOLORS['RED'], msg, BCOLORS['ENDC'])
        return projects

    def list(self):
        """List projects."""
        projects = self.get_projects()
        Printer.print_headers(["Project", "Parent", "Project ID"])
        for project in projects:
            print(Printer.get_row_str([project.display_name, project.parent,
                                       project.project_id]))
