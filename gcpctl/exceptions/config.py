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
from gcpctl.exceptions import GcpctlException


CONFIG_DOCS_URL = "https://github.com/bregman-arie/gcpctl"
CHECK_DOCS_MSG = f"Check the documentation at {CONFIG_DOCS_URL} \
for more information"


class SchemaError(GcpctlException):
    def __init__(self, error: str):
        super().__init__(
            message=f'Configuration file found to be invalid due to error:\n'
                    f'\t- {error}\n'
                    f'\n'
                    f'{CHECK_DOCS_MSG}'
        )
