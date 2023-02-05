"""Main CLI entry"""
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
import argparse
import logging
import sys

import gcpctl.cli.get as get_parser

LOG = logging.getLogger(__name__)


def create_parser():
    """Returns argument parser"""

    # Top level parser
    parser = argparse.ArgumentParser()
    parser.set_defaults(parser=parser)
    subparsers = parser.add_subparsers(dest='main_subparser')

    parser.add_argument('--debug', '-d', action='store_true',
                        dest="debug", help='Turn on debug')

    get_parser.add_get_parser(subparsers)

    return parser


def setup_logging(debug):
    """Sets the logging."""
    logging_format = '%(message)s'
    level = logging.DEBUG if debug else logging.INFO
    logging.basicConfig(level=level, format=logging_format)


def set_logging_level(module, level):
    """Sets logging level (DEBUG, INFO, etc.)"""
    logging.getLogger(module).setLevel(level)


def main():
    """Main Entry."""
    # Parse arguments provided by the user
    parser = create_parser()
    args = parser.parse_args()
    setup_logging(args.debug)

    if hasattr(args, 'func'):
        args.func(args)
    else:
        args.parser.print_help()


if __name__ == '__main__':
    sys.exit(main())
