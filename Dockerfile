FROM python:3.9
ENV PYTHONUNBUFFERED 1
RUN apt-get update && apt-get install --yes netcat && \
    useradd uwsgi && \
    mkdir -p /usr/src/apparatus
WORKDIR /usr/src/apparatus
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY src /usr/src/apparatus/
CMD ["./start.sh"]
