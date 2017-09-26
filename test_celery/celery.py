from __future__ import absolute_import
from celery import Celery
app = Celery('test_celery',broker='amqp://admin:mypass@rabbit',backend='rpc://',include=['test_celery.tasks'])