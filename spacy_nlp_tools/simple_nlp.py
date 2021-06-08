import spacy
from sklearn import metrics
nlp = spacy.load('en_core_web_sm')

class SimpleNlp:
    
    """
    Module for tools that are widely used for NLP 
    
    Arguements:
     text: input text
    """
    
    def __init__(self, text):
        self.text = text
    
    def get_entities(self):
        
        doc = nlp(self.text)
        entities = []
        for ent in doc.ents:
            json_ent = {}
            json_ent['text'] = ent.text
            json_ent['label'] = ent.label_

            entities.append(json_ent)
        
        return entities
    
    def get_summary(self, lines):
        
        doc = nlp(self.text)
        dc = []
        
        for sent in doc.sents:
            dc.append(nlp(str(sent)))
        
        list_sent = []
        for d in dc:
            json_dict = {}
            sim = metrics.pairwise.cosine_similarity(d.vector.reshape(1, -1), doc.vector.reshape(1, -1))
            json_dict['sentence'] = d.text
            json_dict['score'] = sim
            list_sent.append(json_dict)
            
        newlist = sorted(list_sent, key=lambda k: k['score'], reverse=True) 
        summary = newlist[0:lines]
        summary = [t['sentence'] for t in summary]
        summary = ('.').join(summary)
        
        return summary
