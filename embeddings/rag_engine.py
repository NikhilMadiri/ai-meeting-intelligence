from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import nltk
import re
from nltk.tokenize import sent_tokenize
from transformers import pipeline
from typer import prompt
from models.groq_client import generate_response


nltk.download('punkt')

model = SentenceTransformer("all-MiniLM-L6-v2")
qa_model = pipeline("text2text-generation", model="google/flan-t5-base")


def clean_text(text):
    # Remove extra spaces and fix broken text
    text = re.sub(r'\s+', ' ', text)
    text = text.replace("\n", " ")
    return text.strip()

def create_index(text):
    text = clean_text(text)

    sentences = sent_tokenize(text)

    # Filter bad sentences
    sentences = [
        s.strip() for s in sentences
        if len(s.split()) > 8
        and not any(x in s.lower() for x in [
            "thank you",
            "subscribe",
            "bye",
            "okay",
            "let me end"
        ])
    ]


    embeddings = model.encode(sentences)

    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(np.array(embeddings))

    return index, sentences


def query_index(index, sentences, question, k=5):
    question_embedding = model.encode([question])
    distances, indices = index.search(np.array(question_embedding), k)

    # Better context selection
    results = [sentences[i] for i in indices[0]]
    results = sorted(results, key=len, reverse=True)[:3]

    context = " ".join(results)

    prompt = f"""
    You are an intelligent assistant.

    Answer the question clearly based on the context.

    Context:
    {context}

    Question:
    {question}

    Answer in a clear and complete sentence:
    """

    return generate_response(prompt)