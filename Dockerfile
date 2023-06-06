FROM python:3.10

WORKDIR /app

# environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE 1

COPY . /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
