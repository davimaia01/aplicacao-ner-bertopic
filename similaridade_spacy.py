import spacy
from spacy.tokens import Span

nlp = spacy.load("pt_core_news_lg")

doc1 = nlp("aprendi")
doc2 = nlp("aprender")

doc = nlp("Aprendi a importância da Colaboração e do trabalho em equipe")

ents = [(e.text, e.start_char, e.end_char, e.label_) for e in doc.ents]
print('Antes', ents)
# The model didn't recognize "fb" as an entity :(

# Create a span for the new entity
fb_ent = Span(doc, 0, 5, label="Softskill")
orig_ents = list(doc.ents)

# Option 1: Modify the provided entity spans, leaving the rest unmodified
doc.set_ents([fb_ent], default="unmodified")

# Option 2: Assign a complete list of ents to doc.ents
doc.ents = orig_ents + [fb_ent]

ents = [(e.text, e.start, e.end, e.label_) for e in doc.ents]
print('After', ents)
# [('fb', 0, 1, 'ORG')] 🎉
