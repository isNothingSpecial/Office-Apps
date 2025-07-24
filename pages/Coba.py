from streamlit_extras.switch_page_button import switch_page
import streamlit as st

st.set_page_config(page_title="PDF Tools", layout="wide")
st.markdown("## 📚 PDF Tools Dashboard")

col1, col2 = st.columns(2)

with col1:
    if st.button("📎 Merge PDF", use_container_width=True):
        switch_page("Merge")

    if st.button("✂️ Split PDF", use_container_width=True):
        switch_page("Split")

with col2:
    if st.button("🗑️ Delete Page", use_container_width=True):
        switch_page("Delete")

    if st.button("📄 PDF to Word", use_container_width=True):
        switch_page("Word")
