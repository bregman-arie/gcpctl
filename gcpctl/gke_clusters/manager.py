"""GCP GKE Manager class"""
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
from google.cloud import container_v1
import sys

from gcpctl.utils.colors import BCOLORS
from gcpctl.gke_clusters.cluster import GKECluster
from gcpctl.manager import GCPManager
from gcpctl.projects.manager import ProjectManager

LOG = logging.getLogger(__name__)


class GKEManager(GCPManager):
    """Execute GCP GKE related operations."""

    def __init__(self, project_ids=None, env_types=None) -> None:
        self.client = container_v1.ClusterManagerClient()
        self.project_ids = project_ids
        self.env_types = env_types
        super().__init__()
        self._load_conf()

    def _validate_and_get_projects(self):
        """Validate there is at least one project to
        obtain GKE clusters from."""
        project_ids = []
        if not self.env_types and not self.project_ids:
            LOG.error("%sProvide either a project ID or environment name%s",
                      BCOLORS['RED'], BCOLORS['ENDC'])
            sys.exit(2)
        if self.env_types:
            project_manager = ProjectManager(env_types=self.env_types)
            for env_type in self.env_types:
                folder_ids = self.config.data.get('environments').get(env_type)
                for folder_id in folder_ids:
                    project_ids.extend(project_manager.get_projects(folder_id))
        if self.project_ids:
            projects_ids.extend(self.project_ids)
        return project_ids

    def list(self) -> None:
        """List GKE clusters."""
        clusters = []
        for project_id in self._validate_and_get_projects():
            parent = "projects/%s/locations/-" % project_id
            response = self.client.list_clusters(parent=parent)
            clusters.extend([GKECluster(
                name=cluster.name, project_id=project_id,
                zone=cluster.zone) for cluster in response.clusters])
        LOG.info("Obtained %d GKE clusters", len(clusters))
        for cluster in clusters:
            print(cluster)

    def create(self) -> None:
        """Creates a new GKE cluster."""
