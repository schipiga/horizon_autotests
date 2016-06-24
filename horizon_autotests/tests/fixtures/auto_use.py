import logging

import pytest
import xvfbwrapper

from horizon_autotests.third_party import VideoRecorder

from .config import VIRTUAL_DISPLAY

__all__ = [
    'sanitizer',
    'video_capture',
    'virtual_display'
]

LOGGER = logging.getLogger(__name__)


@pytest.fixture(scope="session")
def virtual_display(request):
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
def video_capture(virtual_display):
    recorder = VideoRecorder()
    recorder.start()

    yield recorder

    LOGGER.info("Stop video recording")
    recorder.stop()


@pytest.fixture(autouse=True)
def sanitizer(virtual_display,
              video_capture):
    pass
