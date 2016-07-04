import os

from .utils import generate_ids

DASHBOARD_URL = os.environ['DASHBOARD_URL']
VIRTUAL_DISPLAY = os.environ.get('VIRTUAL_DISPLAY')

ADMIN_NAME, ADMIN_PASSWD, ADMIN_PROJECT = ['admin'] * 3
DEMO_NAME, DEMO_PASSWD, DEMO_PROJECT = list(generate_ids('demo', count=3))

TESTS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                         '..', 'test_reports'))
