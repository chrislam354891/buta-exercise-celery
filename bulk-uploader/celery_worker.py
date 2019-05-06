#!/usr/bin/env python
import os
from app import celery

# app = create_app(os.getenv('FLASK_CONFIG') or 'default')
# app.app_context().push()

celery.autodiscover_tasks([
        'app.tasks',
    ],
    force=True
)
