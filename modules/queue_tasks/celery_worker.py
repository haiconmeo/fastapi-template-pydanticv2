from celery import Celery

app = Celery('my_celery_project', include=[
             'modules.queue_tasks.celery_worker'])
app.config_from_object('modules.queue_tasks.celeryconfig')

if __name__ == '__main__':
    app.start()
