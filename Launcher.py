import streamlit as st
from PyPDF2 import PdfMerger
import os

# Judul Aplikasi
st.title("Aplikasi Penggabung PDF")

# Upload File PDF
uploaded_files = st.file_uploader("Unggah file PDF yang ingin digabungkan", type="pdf", accept_multiple_files=True)

# Tombol untuk menggabungkan PDF
if st.button("Gabungkan PDF"):
    if uploaded_files:
        merger = PdfMerger()
        
        for pdf in uploaded_files:
            merger.append(pdf)

        output_filename = "Hasil_Merge.pdf"
        merger.write(output_filename)
        merger.close()

        # Menyediakan link untuk mengunduh file hasil gabungan
        with open(output_filename, "rb") as f:
            st.download_button("Unduh Hasil PDF", f, file_name=output_filename, mime="application/pdf")

        # Hapus file setelah diunduh (opsional)
        os.remove(output_filename)
    else:
        st.warning("Silakan unggah minimal dua file PDF terlebih dahulu.")
