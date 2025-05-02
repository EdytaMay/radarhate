
# DEMO FRONTEND RADARU ANTYHEJTOWEGO
# Framework: Streamlit (działa lokalnie, nie w środowisku sandbox)
# Uruchamianie lokalnie: `streamlit run app.py`

try:
    import streamlit as st
    import requests
except ModuleNotFoundError as e:
    missing_module = str(e).split("No module named ")[-1].replace("'", "")
    raise ImportError(f"\n[!] Brakuje wymaganej biblioteki: {missing_module}.\n[i] Zainstaluj brakujące moduły komendą: pip install streamlit requests\n")

st.set_page_config(page_title="Radar Hate DEMO", layout="wide")
st.title("Radar Hate 🚨")

st.sidebar.header("Ustawienia skanowania")
keyword = st.sidebar.text_input("Słowo kluczowe", "dziecko")
url = st.sidebar.text_input("Backend URL", "http://127.0.0.1:8000")

if st.sidebar.button("Skanuj teraz"):
    with st.spinner("Skanowanie internetu..."):
        try:
            response = requests.get(f"{url}/scan", params={"q": keyword})
            if response.status_code == 200:
                posts = response.json()
                if posts:
                    st.success(f"Znaleziono {len(posts)} wyników.")
                    for post in posts:
                        st.markdown("---")
                        st.subheader(f"Autor: {post['author']} na {post['platform']}")
                        st.write(post['text'])
                        st.info(f"Klasyfikacja: {post['label']} (Pewność: {int(post['confidence'] * 100)}%)")
                        if st.button(f"Zgłoś post ID {post['id']}"):
                            st.warning("Symulacja zgłoszenia - w pełnej wersji trafia do kancelarii.")
                else:
                    st.info("Brak wyników dla podanego słowa kluczowego.")
            else:
                st.error(f"Błąd komunikacji z backendem! Status: {response.status_code}")
        except Exception as e:
            st.error(f"Wyjątek: {str(e)}")

st.sidebar.markdown("---")
st.sidebar.info("Wersja DEMO | Radar Hate 2025")
