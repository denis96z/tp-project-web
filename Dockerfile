FROM python:3.6.5
ENV PYTHONUNBUFFERED 1
RUN mkdir /web
ADD /web/requirements.txt /web/
RUN pip install -r /web/requirements.txt
WORKDIR /web