FROM python:3.6-alpine

# upgrade setuptools first
RUN apk update && apk add libffi-dev build-base\
    postgresql-dev gcc python3-dev musl-dev bash\
    g++ libgcc libstdc++ linux-headers autoconf automake make nasm --no-cache

# set working directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# add requirements to leverage Docker cache
ADD ./requirements.txt /usr/src/app/requirements.txt

# install requirements
RUN pip3 install -r requirements.txt

# add app
ADD . /usr/src/app

# run server
CMD python manage.py runserver -h 0.0.0.0

