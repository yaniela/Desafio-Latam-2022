FROM python:3.9-slim

WORKDIR /code

COPY requirement.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . /code/

CMD ["python","main.py"]

