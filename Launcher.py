import streamlit as st

st.set_page_config(page_title="PDF Toolkit Apps", layout="wide")

st.title("📚 Dashboard")
st.markdown("Pilih salah satu fitur yang ingin digunakan :")

# Grid layout
cols = st.columns(2)

with cols[0]:
    st.page_link("pages/Merge.py", label="Merge PDF", icon="📎")

    st.page_link("pages/Split.py", label="Split PDF", icon="✂️")

with cols[1]:
    st.page_link("pages/Delete.py", label="Delete Page", icon="🗑️")

    st.page_link("pages/Word.py", label="PDF to Word", icon="📄")
