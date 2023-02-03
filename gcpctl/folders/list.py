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
from google.cloud import resourcemanager_v3

from gcpctl.folders.manager import FolderManager


class FolderLister(FolderManager):

    def __init__(self, folder_id) -> None:
        super().__init__()
        self.folder_id = folder_id

    def list(self):
        """List folders."""
        request = resourcemanager_v3.ListFoldersRequest(
            parent=f"folders/{self.folder_id}")
        for folder in self.client.list_folders(request=request):
            print(folder.display_name)
