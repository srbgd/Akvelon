# Akvelon

Solution of the tasks from: https://myte.me/tasks/XC9Ll8ZtR59KEnAJVcyd

## Components

**backend** - folder contains a basic restful flask application which manages user-transaction entity relationsship, uses SQLAlchemy for ORM, Marshmallow for json validation and serialization and PostgreSQL DB for entities storing. 

**test** - folder contains rest client for the backend api and a set of basic smoke tests which use the client to ensure that backend works.

**nginx** - folder contains single nginx config file used by docker-compose in order not to expose the flask app on the internet.

**docker-compose.yml** - docker compose file for running the application. (Note: it doesn't build it. Instead it pulls the valid build from `https://hub.docker.com/repository/docker/srbgd/backend`.)

## Usage

There is no need to install anything. Simple clone the repo and run:
```
$ docker-compose up
```

## Test

In order to insure that everything works run tests with following commands:
```
$ cd test
$ pytest .
```

Running tests localy takes a couple of seconds. IT assumes that application is accessible on localhost via tcp port 80.

## Stage
This application is deployed on AWS EC2 free t2.micro (1 CPU, 1 GB of RAM) instance without elastic IP. Current instance ip is 3.87.243.231 but as long as elastic IP is not connected this public ip may be changed. Please, let me know if you want to check out the stage and this ip is not reachable or tcp port 80 is not opened.

In order to insure that the deployed application works run tests with following commands:
```
$ cd test
$ export FLASK_APP_URL="http://3.87.243.231:80";  pytest .
```

Running tests against the stage takes approximatly 50 seconds. 
You may see the logs from the stage in file `example.log`
