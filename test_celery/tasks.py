from test_celery.celery import app
import time


@app.task
def longtime_add(i):
    print('long time task begins %d' % i)
    print("Doing something %d" % i)
    time.sleep(60)
    print('long time task finished %d' % i)
    return i


