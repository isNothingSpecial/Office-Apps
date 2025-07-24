import streamlit as st
from pdf2docx import Converter
import os

st.set_page_config(page_title="Konversi PDF ke Word", page_icon="📄")

st.title("📄 Konversi PDF ke Word (.docx)")

uploaded_file = st.file_uploader("Unggah file PDF", type=["pdf"])

if uploaded_file is not None:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    if st.button("Konversi ke Word"):
        with st.spinner("Sedang mengonversi..."):
            output_path = "hasil.docx"
            cv = Converter("temp.pdf")
            cv.convert(output_path, start=0, end=None)
            cv.close()

        st.success("Konversi selesai!")
        with open(output_path, "rb") as f:
            st.download_button(
                label="📥 Unduh File Word",
                data=f,
                file_name="hasil_konversi.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )

        # Hapus file sementara (opsional)
        os.remove("temp.pdf")
        os.remove("hasil.docx")
