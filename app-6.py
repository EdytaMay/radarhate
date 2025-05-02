
import streamlit as st
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

st.set_page_config(page_title="Radar Hate Demo", layout="centered")

st.title("🚨 Radar Hate – Wykrywanie mowy nienawiści")
st.write("To demo wykorzystuje model AI do klasyfikacji tekstów jako neutralne, obraźliwe lub pełne nienawiści.")

# Ładowanie modelu i tokenizatora
@st.cache_resource
def load_model():
    tokenizer = AutoTokenizer.from_pretrained("cardiffnlp/twitter-roberta-base-offensive")
    model = AutoModelForSequenceClassification.from_pretrained("cardiffnlp/twitter-roberta-base-offensive")
    return tokenizer, model

tokenizer, model = load_model()

# Interfejs użytkownika
user_input = st.text_area("Wpisz tekst do analizy:", height=150)

if st.button("Analizuj"):
    if not user_input.strip():
        st.warning("Proszę wpisać tekst.")
    else:
        inputs = tokenizer(user_input, return_tensors="pt", truncation=True)
        with torch.no_grad():
            outputs = model(**inputs)
            scores = torch.nn.functional.softmax(outputs.logits, dim=1)[0]
            labels = ['neutral', 'offensive', 'hateful']
            results = {label: float(score) for label, score in zip(labels, scores)}

        st.subheader("📊 Wyniki analizy:")
        for label, score in results.items():
            st.write(f"**{label.capitalize()}**: {score:.2%}")
