import spacy

nlp = spacy.load("en_core_web_sm")

def extract_action_items(text):
    doc = nlp(text)
    action_items = []

    for sent in doc.sents:
        sentence = sent.text.strip()

        # Better filtering
        if any(word in sentence.lower() for word in ["will", "should", "need to", "must", "have to"]):            
            if len(sentence.split()) < 5:
                continue  # skip useless short lines

            person = None
            deadline = None

            for ent in sent.ents:
                if ent.label_ == "PERSON":
                    person = ent.text
                if ent.label_ in ["DATE", "TIME"]:
                    deadline = ent.text

            action_items.append({
                "person": person,
                "task": sentence,
                "deadline": deadline
            })

    return action_items