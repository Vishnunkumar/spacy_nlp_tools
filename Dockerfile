FROM python:3.8-slim-buster

WORKDIR /APP

COPY /app /APP

RUN pip install -r requirements.txt && \
python -m spacy download en_core_web_lg
