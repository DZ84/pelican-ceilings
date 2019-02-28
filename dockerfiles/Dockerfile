FROM python:3.6-slim
ENV PYTHONUNBUFFERED 1

RUN mkdir /site_ceilings/

# vim can be handy for debugging:
RUN apt-get update && apt-get install -y vim  

RUN pip install --upgrade pip==18.1
RUN pip install markdown==3.0.1 pelican==4.0.1

RUN useradd ceilings
USER ceilings

