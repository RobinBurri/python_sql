FROM python:3.11.4

WORKDIR /app

RUN pip install --upgrade pip

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "main.py"]