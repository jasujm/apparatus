FROM python:3.8 AS builder
RUN mkdir -p /usr/src/apparatus
COPY Pipfile Pipfile.lock /usr/src/apparatus/
RUN cd /usr/src/apparatus && \
    pip install pipenv && \
    pipenv lock --requirements > requirements.txt

FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN apt-get update && apt-get install --yes netcat && \
    useradd uwsgi && \
    mkdir -p /usr/src/apparatus
WORKDIR /usr/src/apparatus
COPY --from=builder /usr/src/apparatus/requirements.txt .
RUN pip install -r requirements.txt
COPY . /usr/src/apparatus/
CMD ["./start.sh"]
