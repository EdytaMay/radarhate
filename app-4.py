
import streamlit as st
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import numpy as np

# Funkcja do załadowania modelu
@st.cache_resource
def load_model():
    model_name = "cardiffnlp/twitter-roberta-base-offensive"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name)
    return tokenizer, model

tokenizer, model = load_model()

# Interfejs użytkownika
st.set_page_config(page_title="Radar Hate", page_icon="🚨")
st.title("🚨 Radar Hate – AI do wykrywania mowy nienawiści")
st.markdown("Wklej tekst, a system wykryje, czy zawiera **hejt**, **treści obraźliwe**, czy jest **neutralny**.")

# Pole tekstowe
text = st.text_area("✏️ Wprowadź tekst do analizy:", height=200)

# Po naciśnięciu przycisku analizuj
if st.button("🔍 Analizuj"):
    if not text.strip():
        st.warning("⚠️ Najpierw wprowadź tekst.")
    else:
        inputs = tokenizer(text, return_tensors="pt", truncation=True)
        with torch.no_grad():
            outputs = model(**inputs)
            scores = torch.nn.functional.softmax(outputs.logits, dim=1).detach().numpy()[0]

        labels = ["Neutral", "Obraźliwy", "Hejt"]
        result = list(zip(labels, scores))
        result.sort(key=lambda x: x[1], reverse=True)

        st.subheader("📊 Wyniki analizy:")
        for label, score in result:
            st.write(f"**{label}**: {score*100:.2f}%")

        st.success(f"🏁 Najbardziej prawdopodobna klasyfikacja: **{result[0][0]}**")

st.markdown("---")
st.caption("Radar Hate © 2025 – demo AI do ochrony wizerunku online")
