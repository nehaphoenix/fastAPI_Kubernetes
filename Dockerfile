FROM python:3.9-slim
COPY . /app
COPY requirements.txt /app

WORKDIR /app

RUN pip3 install -r requirements.txt

CMD ["uvicorn", "main:app", "--reload"]