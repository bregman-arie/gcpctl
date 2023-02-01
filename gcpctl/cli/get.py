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
import crayons
import logging

LOG = logging.getLogger(__name__)


def add_get_parser(subparsers):
    """The parser for sub command 'list'."""
    get_parser = subparsers.add_parser("get")
    get_subparsers = get_parser.add_subparsers()
    get_clusters_parser = get_subparsers.add_parser("clusters")
    get_clusters_parser.set_defaults(func=get_clusters_main)
    get_clusters_parser.add_argument('-e', '--env-type',
                                     dest="env_type", help='Environment type')


def get_clusters_main(args):
    """Get clusters main entry."""
    LOG.info("Listing clusters...\n")
