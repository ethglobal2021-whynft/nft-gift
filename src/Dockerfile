FROM python:3.9.5-slim

WORKDIR /opt

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
     && apt-get -y install gcc libpq-dev python3-dev netcat

RUN pip install --upgrade pip
COPY requirements.txt /opt/.
RUN pip install -r /opt/requirements.txt

COPY ./entrypoint.sh /opt/.

COPY ./ /opt/

ENTRYPOINT ["/opt/entrypoint.sh"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
