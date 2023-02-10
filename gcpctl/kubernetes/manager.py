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
from kubernetes import client
import re


class KubernetesManager():

    def __init__(self):
        pass

    def get_pods(self, api_instance, pods_names=None, pods_regex=None):
        """Returns Pod instances based on given criteria."""
        pods_res = []
        v1 = client.CoreV1Api()
        namespaces = v1.list_namespace().items
        for namespace in namespaces:
            pods = v1.list_namespaced_pod(namespace.metadata.name).items
            for pod in pods:
                if (pod.metadata.name in pods) or \
                        (pods_regex and re.match(
                            pods_regex, pod.metadata.name)):
                    pods_res.append(pod)
        return pods

    def get_namespaces(self):
        pass
