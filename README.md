# celery-research
What is Celery? 

Celery is a task queue implementation for Python web applications used to asynchronously execute work outside the HTTP request-response cycle.

What is a task queue? A task queue is a mechanism that distributes work across multiple threads or machines

Why would this be useful? Celery is very useful because it allows you to quickly implement task queues for many workers. Celery takes care of the hard part which is  appropriately receiving tasks and assigning them to workers. Say you have a bunch of tasks and some or all of them long running, and we want to queue them up,  forget about them, and then have the ability to add new tasks when needed, you will want to use a task queue. Also, if you need a large amount of computing power or concurrency, then you especially want to use a task queue. 

Celery compared to other parallel systems: Celery is comparable to SLURM. People who use SLURM as their cluster managers look to celery to be their new task manager because of its simplicity and how autonomous it is.

What are the different types of Celery? 
There are two types of Celery: Celery daemon (Celeryd) and Celerybeat. Celeryd actually executes the tasks while Celerybeat schedules the tasks. A good way to think about the differences is best described by Full Stack Python: “Think of Celeryd as a tunnel-vision set of one or more workers that handle whatever tasks you put in front of them. Each worker will perform a task and when the task is completed will pick up the next one. The cycle will repeat continously, only waiting idly when there are no more tasks to put in front of them.
Celerybeat on the other hand is like a boss who keeps track of when tasks should be executed. Your application can tell Celerybeat to execute a task at time intervals, such as every 5 seconds or once a week. Celerybeat can also be instructed to run tasks on a specific date or time, such as 5:03pm every Sunday. When the interval or specific time is hit, Celerybeat will hand the job over to Celeryd to execute on the next available worker.”
Here is a link to the full article: https://www.fullstackpython.com/celery.html

Need a Broker: Celery communicates via messages, and you need broker to communicate between the clients(tasks) and workers(resources. To start a task the client will add a message to the queue, and then the broker will deliver that message to a worker. Some options of brokers to use are:
•	RabbitMQ
•	Redis
•	AmazonSQS

First we need to install a broker. For this we will be using Redis. To install this, run:
$ pip install redis

How to install Celery:
$ pip install celery

If using macOS, you may need to use brew in order to download both the broker and celery. Using brew, use these commands instead:
$ brew install redis
$ brew install celery

To start the broker to actually be able to communicate with celery, run:
$ redis-server
or:
$ brew service start redis

As a sanity check, you can run:
$ redis-cli ping
If redis is working correctly it should give you the feedback: PONG

Now we need to have an application to run on the celery worker server. Please see the celery-hello.py

To start the celery worker server with your hello world file, now run:
$ celery -A celery-hello worker --loglevel=INFO

In order to utilize celery, there is a web development framework called Django that is really powerful, but takes a lot of work to set up. It is really tricky to get everything working correctly and it depends a lot on your OS and other variables. I was not able to impliment a more complex tutorial because there were a lot of new components that I was not able to get working. You need all parts of your computer to be set up perfectly for all the parts to be able to talk to each other. If you are interested in web development and python, I highly recommend trying tutorials that include celery, a broker, and Django in order to create some really cool projects. I will include links to websites that hae great tutorials.


I also was not able to get any output from when I run the command to call the celery worker. I have searched dozens of tutorials and there seems to not be any solid tutorial that takes you from nothing in to having a fully running small program. A lot of them assumes you already know a lot about web development and working knowledge of Django or other frameworks. I followed these tutorials and they would always throw in some other program or framework and expect you to fully understand how to use them. So I hit a dead end in my research.

If you have an understanding of Django and would like to continue to explore celery, I recommend this tutorial because it seems easy to follow and explains a lot:

Django+Redis+Celery tutorial: https://medium.com/swlh/python-developers-celery-is-a-must-learn-technology-heres-how-to-get-started-578f5d63fab3
