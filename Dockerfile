FROM python:3.9

RUN apt-get update
RUN pip install --upgrade pip

RUN mkdir django_weather
WORKDIR django_weather
COPY . /django_weather/

RUN pip install -r requirements.txt

CMD python django_weather/manage.py runserver 0.0.0.0:8000