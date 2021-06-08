# spacy_nlp_tools
Simple NLP tools using Spacy

## Installation

```
pip install spacy-nlp-tools==0.1
```

## Usage

```
from spacy_nlp_tools import simple_nlp

ip_text = input()
nlp_tool = simple_nlp.SimpleNlp(text=ip_text)

#get entities
entities = nlp_tool.get_entities()

#get summary
summary = nlp_tool.get_summary(lines=5)

```

- Please note: Working on adding some more general pipelines, will be updated as soon as it is done.
