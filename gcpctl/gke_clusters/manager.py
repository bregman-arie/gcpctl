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
import sys

from google.cloud import container_v1

from gcpctl.utils.colors import BCOLORS
from gcpctl.gke_clusters.cluster import GKECluster
from gcpctl.kubernetes.config import load_config
from gcpctl.kubernetes.manager import KubernetesManager
from gcpctl.utils.process import local_exec
from gcpctl.printer import Printer

LOG = logging.getLogger(__name__)


class GKEManager():
    """Execute GCP GKE related operations."""

    def __init__(self, project_ids=None, clusters=None) -> None:
        self.client = container_v1.ClusterManagerClient()
        self.project_ids = project_ids
        self.clusters = clusters or []
        super().__init__()

    def _validate_and_get_projects(self):
        """Validate there is at least one project to
        obtain GKE clusters from."""
        project_ids = []
        if not self.project_ids:
            LOG.error("%sProvide a project ID%s",
                      BCOLORS['RED'], BCOLORS['ENDC'])
            sys.exit(2)
        if self.project_ids:
            project_ids.extend(self.project_ids)
        return project_ids

    def list_clusters(self) -> None:
        """List GKE clusters."""
        clusters = []
        for project_id in self._validate_and_get_projects():
            parent = "projects/%s/locations/-" % project_id
            response = self.client.list_clusters(parent=parent)
            clusters.extend([GKECluster(
                name=cluster.name, project_id=project_id,
                zone=cluster.zone) for cluster in response.clusters])
        LOG.info("Obtained %d GKE clusters", len(clusters))
        Printer.print_headers(["Cluster", "Project", "Zone"])
        for cluster in clusters:
            print(cluster)

    def load_clusters(self, project, clusters=None) -> None:
        """Sets self.clusters to actual Cluster instances."""
        parent = f"projects/{project}/locations/-"
        response = self.client.list_clusters(parent=parent)
        for cluster in response.clusters:
            if not clusters or cluster.name in clusters:
                self.clusters.append(GKECluster(cluster.name, project,
                                                cluster.zone))

    def pod_exec(self, commands, pods=None, pods_regex=None) -> None:
        """Executes command on one or more of the clusters Pods
        in the GKE cluster"""
        if not self.clusters:
            LOG.error("%sNo clusters specified...%s\nSpecify \
projects with clusters", BCOLORS['RED'], BCOLORS['ENDC'])
            sys.exit(2)
        k8s_manager = KubernetesManager()
        for cluster in self.clusters:
            context = load_config(cluster)
            namespaces = k8s_manager.get_namespaces()
            for namespace in namespaces:
                pods_instances = k8s_manager.get_pods(
                    pods=pods, pods_regex=pods_regex, namespace=namespace)
                for pod in pods_instances:
                    local_exec(f"kubectl config use-context {context}; \
kubectl exec {pod.metadata.name} -n {namespace.metadata.name} -- {commands}")
