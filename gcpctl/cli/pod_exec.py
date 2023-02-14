"""app get sub-command parser and entry points"""
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

from gcpctl.config import Config
from gcpctl.projects.manager import ProjectManager
from gcpctl.gke_clusters.manager import GKEManager

LOG = logging.getLogger(__name__)


def add_pod_exec_parser(subparsers):
    """The parser for sub command 'pod-exec'."""
    pod_exec_parser = subparsers.add_parser("pod-exec")
    pod_exec_parser.set_defaults(parser=pod_exec_parser,
                                 func=pod_exec_main)
    pod_exec_parser.add_argument('-cl', '--clusters', '--cluster',
                                 dest="clusters", nargs='+')
    pod_exec_parser.add_argument('-c', '--commands', '--command',
                                 dest="commands", nargs='+')
    pod_exec_parser.add_argument('-po', '--pods', dest="pods")
    pod_exec_parser.add_argument('-pr', '--pods-regex', dest="pods_regex")
    pod_exec_parser.add_argument('-p', '--project', '--projects',
                                 dest="project_ids", nargs='+', default=[])
    pod_exec_parser.add_argument('-e', '--env-type', nargs='+',
                                 dest="env_types",
                                 help='Env names from config file')


def pod_exec_main(args):
    """Main entry for sub-command pod-exec."""
    if args.env_types:
        project_manager = ProjectManager(
            folder_ids=Config.get_folder_ids(args.env_types))
        args.project_ids.extend([project.project_id for project in
                                 project_manager.get_projects()])
    gke_manager = GKEManager()
    for project_id in args.project_ids:
        gke_manager.load_clusters(clusters=args.clusters,
                                  project=project_id)
    gke_manager.pod_exec(commands=args.commands, pods=args.pods,
                         pods_regex=args.pods_regex)
