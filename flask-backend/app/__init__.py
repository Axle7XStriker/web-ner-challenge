import re
from unicodedata import name
from flask import Flask, render_template, flash, redirect, url_for, request
from flask_cors import CORS
from flaskext.markdown import Markdown
from config import Config

from app.forms import TextForm

from spacy import displacy
import en_core_web_sm
nlp = en_core_web_sm.load()

app = Flask(__name__)
Markdown(app)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"
app.config.from_object(Config)


@app.route("/", methods=['GET', 'POST'])
def home():
    form = TextForm()
    if form.validate_on_submit():
        doc = ner_spacy(form.text.data)
        html = displacy.render(doc,style="ent")
        return render_template('index.html', form=form, result=html)
    return render_template('index.html', form=form)

''' Locate and Classify named-entities in the given text using spaCy. '''
def ner_spacy(text):
    doc = nlp(text)
    # named_entities = [(X.text, X.label_) for X in doc.ents]
    return doc
