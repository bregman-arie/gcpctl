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

from gcpctl.config import get_folder_ids
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
    pod_exec_parser.add_argument('-p', '--pods', dest="pods")
    pod_exec_parser.add_argument('-pr', '--pods-regex', dest="pods_regex")


def pod_exec_main(args):
    """Main entry for sub-command pod-exec."""
    folder_ids = get_folder_ids(args.env_types)
    gke_manager = GKEManager(folder_ids=folder_ids,
                             env_types=args.env_types, clusters=args.clusters)
    gke_manager.pod_exec(commands=args.commands, pods=args.pods,
                         pods_regex=args.pods_regex)
