FROM python:3.11.2

ENV PYTHONBUFFERRED=1

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY ./src/ /app/

CMD [ "python", "main.py" ]
