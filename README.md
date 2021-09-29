# Akvelon

Solution of the tasks from: https://myte.me/tasks/XC9Ll8ZtR59KEnAJVcyd

## Components

**backend** - folder contains a basic restful flask application which manages user-transaction entity relationsship and uses SQLAlchemy for ORM and Marshmallow for json validation and serialization and PostgreSQL DB for entities storing. 

**test** - folder contains rest client for the backend api and a set of basic smoke tests which use the client to ensure that backend works.

**nginx** - folder contains single nginx config file used be docker-compose in order not to expose the flask app on the internet.

**docker-compose.yml** - docker compose file for running the application. (Note: it doesn't build it. Instead it pulls the valid build from DockerHub.)

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

Running tests localy takes a couple of seconds.

## Stage
This application is deployed on AWS EC2 free t2.micro (1 CPU, 1 GB of RAM) instance without elastic IP. Current instance ip is 3.87.243.231 but as long as elastic IP is not connected this public ip may be changed. Please, let me know if you want to check out stage this ip is not reachable or tcp port 80 is not opened.

In order to insure that the deployed application works run tests with following commands:
```
$ cd test
$ export FLASK_APP_URL="http://3.87.243.231:80";  pytest .
```

Running tests against the stage takes approximatly 50 seconds. 
You may see the logs from the stage in file `example.log`

##gRPC
Added gRPC client and server in folder `grpc_middleware`. Now it's implemented in a very messy way. It should be heavily refactored and the folder should be restructured. Also, it's not a middleware yet because the server communicates only with the client through gRPC and doesn't forward requests to backend with REST. Nevertheless, it works.