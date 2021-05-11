from celery import Celery

app = Celery('hello', broker='amqp://quest@localhost//')

@app.task
def hello():
  return 'hello world'
