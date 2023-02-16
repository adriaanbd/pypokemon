## Setup

You need the Python version specified in the Dockerfile. 

Then, install the Python dependencies:

```shell
$ pip install -r requirements.txt
```

After that, use docker to get your development environment running:

```shell
$ docker-compose up -d
````

Verify the api works: http://127.0.0.1:5004/health

Get a shell to the api:

```shell
# get a shell into the api container
$ make api

# get an interactive python shell
$ flask shell

# get the session object
>> from app import DEFAULT_SESSION_FACTORY
>> session = DEFAULT_SESSION_FACTORY()

# run a raw sql
>> session.execute("SELECT * FROM table")
```