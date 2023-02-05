"""Config-related exceptions."""
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
from typing import Tuple, Union

from gcpctl.exceptions import GcpctlException


CONFIG_DOCS_URL = "https://github.com/bregman-arie/gcpctl"
CHECK_DOCS_MSG = f"Check the documentation at {CONFIG_DOCS_URL} \
for more information"


class ConfigurationNotFound(GcpctlException):
    """Configuration file not found exception"""

    def __init__(self, paths: Union[Tuple[str], str]):
        if paths:
            paths = f" at: '{paths}'"
        else:
            paths = ""
        self.message = f"""Could not find configuration file{paths}.
{CHECK_DOCS_MSG}"""

        super().__init__(self.message)


class EmptyConfiguration(GcpctlException):
    """Configuration file is empty exception."""

    def __init__(self, file: str):
        self.message = f"""Configuration file {file} is empty.
{CHECK_DOCS_MSG}"""

        super().__init__(self.message)
