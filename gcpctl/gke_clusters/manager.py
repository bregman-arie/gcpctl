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

from gcpctl.gke_clusters.cluster import GKECluster

LOG = logging.getLogger(__name__)


class GKEManager():
    """Execute GCP GKE related operations."""

    def __init__(self, project_id) -> None:
        self.client = container_v1.ClusterManagerClient()
        self.project_id = project_id

    def list(self) -> None:
        """List GKE clusters."""
        parent = "projects/%s/locations/-" % self.project_id
        response = self.client.list_clusters(parent=parent)
        clusters = [GKECluster(
            name=cluster.name, project_id=cluster.project_id,
            zone=cluster.zone) for cluster in response.clusters]
        LOG.info("Obtained %d GKE clusters", len(clusters))
        for cluster in clusters:
            print(cluster)

    def create(self) -> None:
        """Creates a new GKE cluster."""
