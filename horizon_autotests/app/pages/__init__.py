"""
Module with horizon pages.

@author: schipiga@mirantis.com
"""

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from .access import PageAccess
from .base import PageBase
from .containers import PageContainers
from .images import PageImages
from .instances import PageInstances
from .login import PageLogin
from .projects import PageProjects
from .routers import PageRouters
from .settings import PagePassword, PageSettings
from .users import PageUsers
from .volumes import (PageAdminVolumes,
                      PageVolume,
                      PageVolumes,
                      PageVolumeTransfer)

pages = [
    PageAccess,
    PageAdminVolumes,
    PageBase,
    PageContainers,
    PageImages,
    PageInstances,
    PageLogin,
    PagePassword,
    PageProjects,
    PageRouters,
    PageSettings,
    PageUsers,
    PageVolume,
    PageVolumes,
    PageVolumeTransfer
]
