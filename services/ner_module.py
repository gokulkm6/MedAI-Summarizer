import spacy

try:
    nlp = spacy.load("en_ner_bc5cdr_md") 
except Exception as e:
    raise RuntimeError("Error loading scispaCy model. Make sure it's installed.") from e

def extract_medical_entities(text):

    doc = nlp(text)
    entities = []

    for ent in doc.ents:
        entities.append({
            "Symptoms": ent.text
        })

    return entities
