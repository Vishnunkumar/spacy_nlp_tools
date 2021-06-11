import spacy
from sklearn import metrics
nlp = spacy.load('en_core_web_sm')
stop_words = list(nlp.Defaults.stop_words)

class SimpleNlp:
    
    def __init__(self, text):
        self.text = text
    
    def get_entities(self):
        
        doc = nlp(self.text)
        entities = []
        for ent in doc.ents:
            json_ent = {}
            json_ent['word'] = ent.text
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
    
    def get_keywords(self, no_keywords):
        
        doc = nlp(self.text)
        
        list_text = []
        for t in doc:
            if t.text not in stop_words:
                json_dict = {}
                sim = metrics.pairwise.cosine_similarity(t.vector.reshape(1, -1), doc.vector.reshape(1, -1))
                if len(t.text) > 1:
                    json_dict['word'] = t.text.lower()
                    json_dict['score'] = sim[0][0]
                    list_text.append(json_dict)

        newlist = list(sorted(list_text, key=lambda k: k['score'], reverse=True)) 
        distinct_cur = [dict(y) for y in set(tuple(x.items()) for x in newlist)] 
        result = list({i['word']:i for i in reversed(distinct_cur)}.values())
        
        return result[0:no_keywords]
