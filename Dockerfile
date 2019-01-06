FROM python:3.6
RUN mkdir -p /usr/src/app
ADD requirements.txt /usr/src/app/requirements.txt
ADD servant /usr/src/app/servant
WORKDIR /usr/src/app
RUN pip install -r requirements.txt
