from flask import Flask,url_for,render_template,request
import numpy
import spacy
from spacy import displacy
from spacy.attrs import ENT_IOB, ENT_TYPE
from spacy.tokens import Span
from IPython.core.display import display, HTML
from flaskext.markdown import Markdown



nlp = spacy.load("pt_core_news_lg")
doc = nlp("Aprendi a importância de ser colaborativo e do trabalho em equipe")

nlp1 = spacy.load(r"./output/model-best") #load the best model
doc5 = nlp1("O uso correto de artefatos como Matriz RACI, GAP Analysis, Análise de Stakeholders, Gestão de Fatores Críticos de Sucesso, dentre outros.")
entidades = []
for ent in doc5.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)
    entidades.append(ent)

colors = {"Habilidade": "linear-gradient(90deg, #429cf5, #42ddf5)","Conteúdo": "linear-gradient(90deg, #429cf5, #42ddf5)","Softskill": "linear-gradient(90deg, #429cf5, #42ddf5)"}
options = {"ents": ["Habilidade","Conteúdo","Softskill"], "colors": colors}
#spacy.displacy.serve(doc5, style='ent', options=options)
print(entidades)


app = Flask(__name__)
Markdown(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/ner", methods=["GET","POST"])
def press():
    colors = {"Habilidade": "linear-gradient(90deg, #429cf5, #42ddf5)","Conteúdo": "linear-gradient(90deg, #429cf5, #42ddf5)","Softskill": "linear-gradient(90deg, #429cf5, #42ddf5)"}
    options = {"ents": ["Habilidade","Conteúdo","Softskill"], "colors": colors}
    texto = doc5
    html = displacy.render(doc5, style='ent', options=options)
    result = html
    return render_template('ner.html',texto=texto, result=result)

if __name__ == "__main__":
    app.run()