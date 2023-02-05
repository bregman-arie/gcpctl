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

from gcpctl.folders.list import FolderLister
from gcpctl.projects.list import ProjectLister
from gcpctl.utils.colors import bcolors

LOG = logging.getLogger(__name__)


def add_get_parser(subparsers):
    """The parser for sub command 'list'."""
    get_parser = subparsers.add_parser("get")
    get_parser.set_defaults(parser=get_parser)
    get_subparsers = get_parser.add_subparsers(dest='get_subparser')

    # Clusters
    get_clusters_parser = get_subparsers.add_parser("clusters")
    get_clusters_parser.set_defaults(func=get_clusters_main,
                                     parser=get_clusters_parser)
    get_clusters_parser.add_argument('-e', '--env-type',
                                     dest="env_type", help='Environment type')

    # Projects
    get_projects_parser = get_subparsers.add_parser("projects")
    get_projects_parser.set_defaults(func=get_projects_main,
                                     parser=get_projects_parser)
    get_projects_parser.add_argument('-e', '--env-type', nargs='+',
                                     dest="env_type",
                                     help='Env name from config file')
    get_projects_parser.add_argument('-f', '--folder-id',
                                     dest="folder_id", help='Folder ID')

    # Folders
    get_folders_parser = get_subparsers.add_parser("folders")
    get_folders_parser.set_defaults(func=get_folders_main,
                                    parser=get_folders_parser)
    get_folders_parser.add_argument('-f', '--folder-id',
                                    dest="folder_id", help='Folder ID',
                                    required=True)


def get_clusters_main(args, config):
    """Get clusters main entry."""
    LOG.info("Listing clusters...\n")


def get_projects_main(args, config):
    """Get projects main entry."""
    projects_lister = ProjectLister()
    if args.env_type:
        for env_type in args.env_type:
            for folder in config['environments'][env_type]:
                LOG.info(f"{bcolors.YELLOW}Listing projects from \
{env_type} environment{bcolors.ENDC}\n")
                projects_lister.list(folder_id=folder)
    if args.folder_id:
        LOG.info(f"{bcolors.YELLOW}Listing projects from \
{args.folder_id} folder{bcolors.ENDC}\n")
        projects_lister.list(folder_id=args.folder_id)
    if not args.folder_id and not args.env_type:
        projects_lister.list()


def get_folders_main(args, config):
    """Get folders main entry."""
    folder_lister = FolderLister(folder_id=args.folder_id)
    folder_lister.list()
