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
from gcpctl.utils.colors import BCOLORS


class Printer():

    @staticmethod
    def print_headers(headers, fill=30, sub_header="=====",
                      color=BCOLORS['GREEN']):
        if not headers or not all(isinstance(s, str) for s in headers):
            raise ValueError("A list of headers is required")
        fill_args = [fill for _ in headers]
        format_str = color + " ".join("{: <" + str(f) + "}" for f in fill_args) + BCOLORS['ENDC']
        print(format_str.format(*headers))
        print(format_str.format(*[sub_header for _ in headers]))

    @staticmethod
    def get_row_str(items, fill=30):
        fill_args = [fill for _ in items]
        format_str = " ".join("{: <" + str(f) + "}" for f in fill_args)
        return format_str.format(*items)
