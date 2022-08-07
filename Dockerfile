FROM python:3.7.4-alpine3.10
RUN apk add --no-cache --virtual .build-deps g++ python3-dev libffi-dev openssl-dev && \
  apk add --no-cache --update python3 && \
  pip3 install --upgrade pip setuptools
RUN pip3 install pendulum service_identity
WORKDIR /my-website-tracker
COPY app /my-website-tracker/app
COPY requirements.txt app.py /my-website-tracker/
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]