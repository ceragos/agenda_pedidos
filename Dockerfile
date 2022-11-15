FROM python:3

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y  libmariadb-dev-compat libmariadb-dev \
    build-essential libssl-dev libffi-dev \
    libxml2-dev libxslt1-dev zlib1g-dev nano cron

RUN mkdir /code
WORKDIR /code

ADD requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ADD . /code/
RUN touch /code/agenda_pedidos/logs/debug.log

CMD ['python', 'python manage.py collectstatic && manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000 && python manage.py test && pip freeze && pip install -r requirements.txt && python manage.py registros_base && python manage.py ubicar_conductores']
