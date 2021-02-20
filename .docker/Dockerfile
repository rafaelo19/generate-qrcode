FROM python:3.9.2-alpine

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]