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

from gcpctl.gke_clusters.manager import GKEManager

LOG = logging.getLogger(__name__)


def add_cluster_exec_parser(subparsers):
    """The parser for sub command 'cluster-exec'."""
    cluster_exec_parser = subparsers.add_parser("cluster-exec")
    cluster_exec_parser.set_defaults(parser=cluster_exec_parser,
                                     func=cluster_exec_main)
    cluster_exec_parser.add_argument('-cl', '--cluster', '--clusters',
                                     dest="clusters", nargs='+')
    cluster_exec_parser.add_argument('-c', '--commands', '--command',
                                     dest="commands", nargs='+')


def cluster_exec_main(args):
    """Main entry for sub-command cluster-exec."""
    gke_manager = GKEManager(project_ids=args.project_ids,
                             env_types=args.env_types)
    gke_manager.cluster_exec(commands=args.commands)
