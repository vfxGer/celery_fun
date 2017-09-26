FROM python:3
ADD requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
ADD ./test_celery/ /app/
WORKDIR /app/
ENTRYPOINT celery -A test_celery worker --concurrency=2 --loglevel=info