import numpy
import spacy
from spacy.attrs import ENT_IOB, ENT_TYPE
from spacy.tokens import Span

nlp = spacy.load("pt_core_news_lg")
doc = nlp("Aprendi a importância de ser colaborativo e do trabalho em equipe")
ents = [(e.text, e.start_char, e.end_char, e.label_) for e in doc.ents]
print('Before : ', ents)
# The model didn't recognize 'facebook' as an entity

# Creating a span for the new entity
facebook_ent = [Span(doc, 5,6,label="SOFTSKILL"),Span(doc, 8,11,label="SOFTSKILL")] 

orig_ents = list(doc.ents)
doc.ents = orig_ents + facebook_ent

# Printing the new entity list
ents = [(e.text, e.start, e.end, e.label_) for e in doc.ents]
print('After : ', ents)