import numpy
import numpy
import spacy
from spacy import displacy
from spacy.tokens import Span
from spacy.attrs import ENT_IOB, ENT_TYPE
from spacy.tokens import Span
from IPython.core.display import display, HTML

nlp = spacy.load("pt_core_news_lg")
doc = nlp("Aprendi a importância de ser colaborativo e do trabalho em equipe")

nlp1 = spacy.load(r"./output/model-best") #load the best model
doc5 = nlp1("fatores críticos de sucesso")
entidades = []
for ent in doc5.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)
    entidades.append(ent)

colors = {"Habilidade": "linear-gradient(90deg, #429cf5, #42ddf5)","Conteúdo": "linear-gradient(90deg, #429cf5, #42ddf5)","Softskill": "linear-gradient(90deg, #429cf5, #42ddf5)"}
options = {"ents": ["Habilidade","Conteúdo","Softskill"], "colors": colors}
spacy.displacy.serve(doc5, style='ent', options=options)