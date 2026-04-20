"""
ASGI config for f1hub_backend project.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "f1hub_backend.settings")

application = get_asgi_application()

