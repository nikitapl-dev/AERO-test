FROM python:3.8
WORKDIR /code
COPY requirements.txt .

RUN apt-get update && apt-get install -y cron
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY crontab /etc/cron.d/crontab
RUN crontab /etc/cron.d/crontab
COPY AERO.py .
CMD ["cron", "-f"]
