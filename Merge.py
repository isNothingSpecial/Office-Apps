import streamlit as st
from PyPDF2 import PdfMerger
import tempfile
import os

st.set_page_config(page_title="Gabung PDF", page_icon="📎")

st.title("📎 Penggabung PDF")
st.write("Unggah beberapa file PDF, lalu gabungkan menjadi satu file.")

# Upload multiple PDF files
uploaded_files = st.file_uploader("Unggah file PDF (bisa lebih dari satu)", type="pdf", accept_multiple_files=True)

if uploaded_files:
    if st.button("Gabungkan PDF"):
        merger = PdfMerger()
        with tempfile.TemporaryDirectory() as tmpdir:
            for uploaded_file in uploaded_files:
                temp_path = os.path.join(tmpdir, uploaded_file.name)
                with open(temp_path, "wb") as f:
                    f.write(uploaded_file.read())
                merger.append(temp_path)

            # Simpan hasil gabungan ke file sementara
            output_path = os.path.join(tmpdir, "hasil_merge.pdf")
            merger.write(output_path)
            merger.close()

            # Buka file untuk diunduh
            with open(output_path, "rb") as f:
                st.download_button(
                    label="📥 Unduh PDF Gabungan",
                    data=f,
                    file_name="hasil_merge.pdf",
                    mime="application/pdf"
                )
