#!/usr/bin/env python
import os
from app import celery, create_app

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
app.app_context().push()

@app.route('/task-list/<string:userid>')
def get_task_list(name):
    return json.dumps(filestore.get_user_task_list(user_id))

