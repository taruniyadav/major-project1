import spacy

nlp = spacy.load("en_core_web_sm")

def extract_keywords(text):

    doc = nlp(text)

    keywords = []

    for token in doc:
        if token.pos_ in ["NOUN", "PROPN"]:
            word = token.text.lower()

            if word.isalpha() and len(word) > 2:
                keywords.append(word)

    keywords = list(dict.fromkeys(keywords))

    return keywords[:5]
