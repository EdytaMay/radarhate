
# 🚨 Radar Hate – Demo AI do wykrywania mowy nienawiści

Radar Hate to demo aplikacja AI zbudowana na Streamlit, wykorzystująca model `cardiffnlp/twitter-roberta-base-offensive` do klasyfikacji tekstu jako:
- Neutralny
- Obraźliwy
- Hejt

## 🔧 Jak uruchomić lokalnie?

### 1. Sklonuj repozytorium

```bash
git clone https://github.com/twoja-nazwa-uzytkownika/radar-hate.git
cd radar-hate
```

### 2. Zainstaluj zależności

Upewnij się, że masz zainstalowany Python (>=3.8) i pip.

```bash
pip install -r requirements.txt
```

### 3. Uruchom aplikację

```bash
streamlit run app.py
```

## 🌐 Uruchamianie na Streamlit Cloud

1. Utwórz nowe repozytorium na GitHub i wrzuć tam pliki:
   - `app.py`
   - `requirements.txt`
   - `README.md`

2. Przejdź na [streamlit.io/cloud](https://streamlit.io/cloud) i połącz swoje konto z GitHubem.

3. Wybierz repozytorium i kliknij "Deploy".

Aplikacja uruchomi się automatycznie po zainstalowaniu zależności.

## 🧠 Użyty model

Model: [`cardiffnlp/twitter-roberta-base-offensive`](https://huggingface.co/cardiffnlp/twitter-roberta-base-offensive)

Dzięki Hugging Face możemy w czasie rzeczywistym analizować język i wykrywać mowę nienawiści.

## 📄 Licencja

Projekt demo edukacyjny. © 2025 Radar Hate
