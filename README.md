# celery-research
What is Celery? Celery is a task queue implementation for Python web applications used to asynchronously execute work outside the HTTP request-response cycle.
	Why would this be useful? “You want your WSGI server to respond to incoming requests as quickly as possible because each request ties up a worker process until the response is finished. Moving work off those workers by spinning up asynchronous jobs as tasks in a queue is a straightforward way to improve WSGI server response times.”
	Compared to OpenMP and MPI: Similar to SLURM
	What are the different types of Celery? There are two types of Celery: Celery daemon (Celeryd) and Celerybeat. Celeryd actually executes the tasks while Celerybeat schedules the tasks. A good way to think about the differences is: “Think of Celeryd as a tunnel-vision set of one or more workers that handle whatever tasks you put in front of them. Each worker will perform a task and when the task is completed will pick up the next one. The cycle will repeat continously, only waiting idly when there are no more tasks to put in front of them.
Celerybeat on the other hand is like a boss who keeps track of when tasks should be executed. Your application can tell Celerybeat to execute a task at time intervals, such as every 5 seconds or once a week. Celerybeat can also be instructed to run tasks on a specific date or time, such as 5:03pm every Sunday. When the interval or specific time is hit, Celerybeat will hand the job over to Celeryd to execute on the next available worker.”
	What is a task queue? A task queue is a mechanism that distributes work across multiple threads or machines

Need a Broker: Celery requires a solution to send and receive messages; usually this comes in the form of a separate service called a message broker. Some options are:
•	RabbitMQ
•	Redis
•	AmazonSQS

First we need to install a broker. For this we will be using Redis. To install this, run:
$ pip install redis

How to install Celery:
$ pip install celery
