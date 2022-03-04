import numpy
import spacy
from spacy.attrs import ENT_IOB, ENT_TYPE
from spacy.tokens import Span

nlp = spacy.load("pt_core_news_lg")
doc = nlp("Aprendi a importância de ser colaborativo e do trabalho em equipe")
ents = [(e.text, e.start_char, e.end_char, e.label_) for e in doc.ents]
print('Before : ', ents)
# The model didn't recognize 'facebook' as an entity

doc2 = nlp("Estamos em um processo colaborativo")
doc3 = nlp("Priorizamos o trabalho em equipe")
doc4 = nlp("Tokio tower é bonita")

# Printing the new entity list
ents = [(e.text, e.start, e.end, e.label_) for e in doc2.ents]
ents2 = [(e.text, e.start, e.end, e.label_) for e in doc3.ents]
print(ents)
print(ents2)

nlp1 = spacy.load(r".\output\model-best") #load the best model
doc5 = nlp1("Estamos em um processo colaborativo") 
print(doc5.ents)