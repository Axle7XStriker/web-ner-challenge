from collections import defaultdict
from flask import Blueprint, render_template
from app.forms import TextForm

from spacy import displacy
import en_core_web_sm
nlp = en_core_web_sm.load()

DEFAULT_LABEL_COLORS = {
    "ORG": "#7aecec",
    "PRODUCT": "#bfeeb7",
    "GPE": "#feca74",
    "LOC": "#ff9561",
    "PERSON": "#aa9cfc",
    "NORP": "#c887fb",
    "FAC": "#9cc9cc",
    "EVENT": "#ffeb80",
    "LAW": "#ff8197",
    "LANGUAGE": "#ff8197",
    "WORK_OF_ART": "#f0d0ff",
    "DATE": "#bfe1d9",
    "TIME": "#bfe1d9",
    "MONEY": "#e4e7d2",
    "QUANTITY": "#e4e7d2",
    "ORDINAL": "#e4e7d2",
    "CARDINAL": "#e4e7d2",
    "PERCENT": "#e4e7d2",
}

main = Blueprint('main', __name__, template_folder="templates", static_folder='static')

@main.route("/", methods=['GET', 'POST'])
def home():
    form = TextForm()
    if form.validate_on_submit():
        doc = ner_spacy(form.text.data)
        html = displacy.render(doc,style="ent", minify=True)
        entities = defaultdict(set)
        for ent in doc.ents:
            entities[ent.label_].add(ent.text)
        return render_template('index.html', form=form, result={'html': html, 'entities': entities, 'label_config': DEFAULT_LABEL_COLORS})
    return render_template('index.html', form=form)

''' Locate and Classify named-entities in the given text using spaCy. '''
def ner_spacy(text):
    doc = nlp(text)
    return doc