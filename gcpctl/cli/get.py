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
from gcpctl.folders.manager import FolderManager
from gcpctl.projects.manager import ProjectManager
from gcpctl.gke_clusters.manager import GKEManager

LOG = logging.getLogger(__name__)


def add_get_parser(subparsers):
    """The parser for sub command 'get'."""
    get_parser = subparsers.add_parser("get")
    get_parser.set_defaults(parser=get_parser)
    get_subparsers = get_parser.add_subparsers(dest='get_subparser')

    # GKE Clusters
    get_gke_clusters_parser = get_subparsers.add_parser("gke-clusters")
    get_gke_clusters_parser.set_defaults(
        func=get_gke_clusters_main, parser=get_gke_clusters_parser)
    get_gke_clusters_parser.add_argument('-p', '--project', dest="project_ids",
                                         nargs='+', default=[])
    get_gke_clusters_parser.add_argument('-e', '--env-type', nargs='+',
                                         dest="env_types",
                                         help='Env name from config file')

    # Projects
    get_projects_parser = get_subparsers.add_parser("projects")
    get_projects_parser.set_defaults(func=get_projects_main,
                                     parser=get_projects_parser)
    get_projects_parser.add_argument('-e', '--env-type', nargs='+',
                                     dest="env_types",
                                     help='Env names from config file')
    get_projects_parser.add_argument('-f', '--folder-ids', nargs='+',
                                     default=[],
                                     dest="folder_ids", help='Folder IDs')

    # Folders
    get_folders_parser = get_subparsers.add_parser("folders")
    get_folders_parser.set_defaults(func=get_folders_main,
                                    parser=get_folders_parser)
    get_folders_parser.add_argument('-f', '--folder-ids', nargs='+',
                                    default=[],
                                    dest="folder_ids", help='Folder ID')


def get_gke_clusters_main(args):
    """Get GKE clusters main entry."""
    if args.env_types:
        project_manager = ProjectManager(
            folder_ids=Config.get_folder_ids(args.env_types))
        args.project_ids.extend([project.project_id for project in
                                 project_manager.get_projects()])
    gke_manager = GKEManager(project_ids=args.project_ids)
    gke_manager.list_clusters()


def get_projects_main(args):
    """Get projects main entry."""
    args.folder_ids.extend(Config.get_folder_ids(args.env_types))
    projects_manager = ProjectManager(folder_ids=args.folder_ids)
    projects_manager.list()


def get_folders_main(args):
    """Get folders main entry."""
    folder_manager = FolderManager(folder_ids=args.folder_ids)
    folder_manager.list()
