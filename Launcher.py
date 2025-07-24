import streamlit as st

st.set_page_config(page_title="PDF Tools Dashboard", layout="wide")

st.title("📚 PDF Tools Dashboard")
st.markdown("Pilih salah satu fitur di bawah ini:")

# Grid layout
cols = st.columns(2)

with cols[0]:
    st.page_link("Merge_PDF.py", label="📎 Merge PDF", icon="📎")

    st.page_link("Split_PDF.py", label="✂️ Split PDF", icon="✂️")

with cols[1]:
    st.page_link("Delete_Page.py", label="🗑️ Delete Page", icon="🗑️")

    st.page_link("PDF_to_Word.py", label="📄 PDF to Word", icon="📄")
