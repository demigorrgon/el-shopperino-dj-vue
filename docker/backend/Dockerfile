FROM python:3.10

COPY . /app
WORKDIR /app

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PORT=8000

RUN apt-get update && apt-get install -y --no-install-recommends \
    tzdata \
    python3-setuptools \
    python3-pip \
    python3-dev \
    python3-venv \
    git \
    && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
RUN pip3 install --upgrade pip 
RUN pip3 install -r requirements.txt
RUN pip3 install gunicorn
# CMD ["gunicorn", "server.wsgi", "--bind", "0.0.0.0:8000", "--workers 4", "--threads 4"]
