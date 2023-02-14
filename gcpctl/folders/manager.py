"""GCP Folders Manager."""
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

from google.cloud import resourcemanager_v3
from google.api_core.exceptions import PermissionDenied

from gcpctl.utils.colors import BCOLORS
from gcpctl.printer import Printer


LOG = logging.getLogger(__name__)


class FolderManager():
    """Manages operations related to GCP folders."""

    def __init__(self, folder_ids=None) -> None:
        self.client = resourcemanager_v3.FoldersClient()
        self.folder_ids = folder_ids

    def list(self):
        """List folders."""
        folders = []
        if self.folder_ids:
            for folder_id in self.folder_ids:
                request = resourcemanager_v3.ListFoldersRequest(
                    parent=f"folders/{folder_id}")
                folders = self.client.list_folders(request=request)
                Printer.print_headers(["Folder", "Parent"])
                for folder in folders:
                    print(Printer.get_row_str([folder.display_name,
                                               folder.parent]))
        else:
            request = resourcemanager_v3.ListFoldersRequest()
            try:
                for folder in self.client.list_folders(request=request):
                    print(folder.display_name)
            except PermissionDenied:
                LOG.error("%sNo permissions to access the root of the \
organization.\nConsider accessing a specific folder with -f FOLDER.%s",
                          BCOLORS['RED'], BCOLORS['ENDC'])

    def create(self):
        """Creates new folder."""
