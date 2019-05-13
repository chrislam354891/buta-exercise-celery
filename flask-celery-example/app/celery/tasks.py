from celery import task

@task(bind=True)
def hello(self):
    # How to call me:
    # At project folder: 
    # $ celery -A app.run_celery.celery call app.celery.tasks.hello
    # app.run_celery.celery is the celery (actually is FlaskCelery) instance
    # (from app.extensions.celery) but with configuration set.

    # self here is the instance of FlaskCelery class

    if self.app is not None:
        return self.app.conf.TITLE
    else:
        return 'No App found, Hello'
