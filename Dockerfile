FROM python:3.9

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

COPY ./requirements.txt /usr/src/app/requirements.txt

RUN pip install -r requirements.txt

ADD . /usr/src/app

CMD python manager.py runserver -h 0.0.0.0