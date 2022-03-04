
import pandas as pd
import os
from tqdm import tqdm
import spacy
from spacy.tokens import DocBin

TRAIN_DATA = [('Aprendi a importância de ser colaborativo', {'entities': [(29, 41, 'SOFTSKILL')]}),
 ('Aprendi a importância do trabalho em equipe', {'entities': [(25, 43, 'SOFTSKILL')]}),
 ('Aprendi a importância da colaboração', {'entities': [(25, 36, 'SOFTSKILL')]}),
 ('Aprendi a importância do trabalho em grupo', {'entities': [(25, 42, 'SOFTSKILL')]}),
 ('identificar os fatores críticos para o sucesso de um projeto', {'entities': [(15, 31, 'CONTEÚDO')]})
 ('Aprendi a gerenciar o tempo e ter mais organização', {'entities': [(39, 50, 'SOFTSKILL')]}),
 ('pudemos aprender diversos pontos, como Fatores Críticos de Sucesso', {'entities': [(39, 66, 'CONTEÚDO')]}),
 ('onde pudemos aprender diversos pontos, como fatores críticos de sucesso, análise e gerenciamento de stakeholders', {'entities': [(44, 71, 'CONTEÚDO')]}),
 ('onde pudemos aprender diversos pontos, como fatores críticos de sucesso, análise e gerenciamento de stakeholders', {'entities': [(73, 112, 'CONTEÚDO')]}),
 ('pudemos aprender diversos pontos, como matriz RACI', {'entities': [(39, 50, 'CONTEÚDO')]}),
 ('aprendi a importância da colaboração dentro da equipe, além do engajamento dentro da nossa problemática.', {'entities': [(62, 73, 'Atitude')]}),
 ('Houve comunicação', {'entities': [(6, 17, 'SOFTSKILL')]})]
 
#nlp = spacy.blank("en") # load a new spacy model
nlp = spacy.load("pt_core_news_lg") # load other spacy model

db = DocBin() # create a DocBin object

for text, annot in tqdm(TRAIN_DATA): # data in previous format
    doc = nlp.make_doc(text) # create doc object from text
    ents = []
    for start, end, label in annot["entities"]: # add character indexes
        span = doc.char_span(start, end, label=label, alignment_mode="contract")
        if span is None:
            print("Skipping entity")
        else:
            ents.append(span)
    doc.ents = ents # label the text with the ents
    db.add(doc)

db.to_disk("./train.spacy") # save the docbin object