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

LOG = logging.getLogger(__name__)


class ProjectManager():
    """Manages GCP operations related to projects."""

    def __init__(self, folder_id=None) -> None:
        self.client = resourcemanager_v3.ProjectsClient()
        self.folder_id = folder_id

    def list(self, folder_id=None):
        """List projects."""
        LOG.debug("Listing projects from folder %s", folder_id)
        if folder_id:
            request = resourcemanager_v3.ListProjectsRequest(
                parent=f"folders/{folder_id}")
        else:
            request = resourcemanager_v3.ListProjectsRequest()
        for project in self.client.list_projects(request=request):
            print(project.display_name)
        print()

    def create(self):
        """Creates a new GCP project."""
