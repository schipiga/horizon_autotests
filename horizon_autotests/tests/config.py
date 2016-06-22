import os

from .utils import generate_ids

DASHBOARD_URL = os.environ['DASHBOARD_URL']

ADMIN_NAME, ADMIN_PASSWD, ADMIN_PROJECT = ['admin'] * 3
DEMO_NAME, DEMO_PASSWD, DEMO_PROJECT = list(generate_ids('demo', count=3))
