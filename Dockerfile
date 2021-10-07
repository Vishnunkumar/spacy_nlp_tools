FROM python:3.8-slim-buster

WORKDIR ./app

COPY ./spacy_nlp_tools ./app

RUN pip install -r requirements.txt && \
python -m spacy download en_core_web_lg
