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

from gcpctl.config import AppConfig
import gcpctl.cli.parser as app_parser

LOG = logging.getLogger(__name__)


def setup_logging(debug):
    """Sets the logging."""
    format = '%(message)s'
    level = logging.DEBUG if debug else logging.INFO
    logging.basicConfig(level=level, format=format)


def set_logging_level(module, level):
    logging.getLogger(module).setLevel(level)


def main():
    """Main Entry."""
    # Parse arguments provided by the user
    parser = app_parser.create_parser()
    args = parser.parse_args()
    setup_logging(args.debug)

    config = AppConfig()

    if hasattr(args, 'func'):
        args.func(args, **config)


if __name__ == '__main__':
    sys.exit(main())
