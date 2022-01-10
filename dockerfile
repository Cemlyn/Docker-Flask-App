FROM ubuntu:18.04

ENV PYTHONUNBUFFERED=1

# Install dependencies
RUN apt-get update -y
RUN apt-get install -y git curl python python-pip

COPY . /app

WORKDIR /app

# Giving permission to run the serve.sh file
RUN chmod 577 serve.sh

RUN pip install -r ./config/requirements.txt

ENTRYPOINT ["./serve.sh"]