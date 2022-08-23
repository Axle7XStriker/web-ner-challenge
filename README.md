# Web-based Named Entity Recognition

### Background

[Named entity recognition](https://en.wikipedia.org/wiki/Named-entity_recognition) (NER) is a very important and long-standing goal of the NLP community. In it, we attempt to identify and categorize "entities" from text so that we can use them for downstream processing such as argument attachment or [event extraction](http://ceur-ws.org/Vol-779/derive2011_submission_1.pdf).

### Install & Run:

1. Compile using `make install`
2. Run using `make start`

### Features:

-   An intuitive UI.
-   Text can be of any length.
-   Recognizable Named Entities include: **ORG** (Organization), **PRODUCT**, **GPE** (Geo-Political Entity), **LOC** (Location), **PERSON**, **NORP** (Normal, Ordinary, Responsible Person), **FAC**, **EVENT**, **LAW**, **LANGUAGE**, **WORK_OF_ART**, **DATE**, **TIME**, **MONEY**, **QUANTITY**, **ORDINAL**, **CARDINAL**, **PERCENT**.
-   If no named entities are found, return a "No entities found" message.
-   Multiple ways for visualizing named-entities.
