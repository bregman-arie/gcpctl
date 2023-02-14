"""
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
"""
import subprocess
from kubernetes import config


# TODO(bregman-arie): If possible, replace this with actual Python library
#                     equivalent.
def load_config(cluster):
    try:
        context = f"gke_{cluster.project_id}_{cluster.zone}_{cluster.name}"
        print(f"Loading context: {context}")
        config.load_kube_config(context=context)
    except config.config_exception.ConfigException:
        print(f"Couldn't load the config of {cluster.name}. \
Running gcloud get-credentials")
        subprocess.run(["gcloud", "container", "clusters", "get-credentials",
                        cluster.name, f"--project={cluster.project_id}",
                        f"--zone={cluster.zone}"],
                       capture_output=True, text=True, check=True)
    return context
