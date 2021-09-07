FROM python:3.7-slim-buster


WORKDIR /backend

# install requirements
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt


# copy source code
COPY . .

# run flask application
ENV  FLASK_APP=./app.py
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]