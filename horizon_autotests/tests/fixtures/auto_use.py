"""
Auto use fixtures.

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

import logging
import os
import shutil

import pytest
import xvfbwrapper

from horizon_autotests.third_party import VideoRecorder

from ._config import VIRTUAL_DISPLAY, TEST_REPORTS_DIR
from ._utils import slugify

__all__ = [
    'report_dir',
    'reports_dir',
    'sanitizer',
    'video_capture',
    'virtual_display'
]

LOGGER = logging.getLogger(__name__)


@pytest.fixture(scope='session')
def reports_dir():
    """Fixture to clear reports directory before tests."""
    if os.path.exists(TEST_REPORTS_DIR):
        shutil.rmtree(TEST_REPORTS_DIR)
        os.makedirs(TEST_REPORTS_DIR)
    return TEST_REPORTS_DIR


@pytest.fixture
def report_dir(request, reports_dir):
    """Create report directory to put test logs."""
    _report_dir = os.path.join(reports_dir, slugify(request.node.name))
    if not os.path.isdir(_report_dir):
        os.makedirs(_report_dir)
    return _report_dir


@pytest.fixture(scope="session")
def virtual_display(request):
    """Run test in virtual X server if env var is defined."""
    if not VIRTUAL_DISPLAY:
        return

    _virtual_display = xvfbwrapper.Xvfb(width=1920, height=1080)
    # workaround for memory leak in Xvfb taken from:
    # http://blog.jeffterrace.com/2012/07/xvfb-memory-leak-workaround.html
    # and disables X access control
    args = ["-noreset", "-ac"]

    if hasattr(_virtual_display, 'extra_xvfb_args'):
        _virtual_display.extra_xvfb_args.extend(args)  # xvfbwrapper>=0.2.8
    else:
        _virtual_display.xvfb_cmd.extend(args)

    _virtual_display.start()

    def fin():
        LOGGER.info('Stop xvfb')
        _virtual_display.stop()

    request.addfinalizer(fin)


@pytest.yield_fixture
def video_capture(report_dir, virtual_display):
    """Capture video of test."""
    recorder = VideoRecorder(report_dir)
    recorder.start()

    yield recorder

    LOGGER.info("Stop video recording")
    recorder.stop()


@pytest.fixture(autouse=True)
def sanitizer(video_capture):
    """Fixture to aggregate sanity fixtures."""
