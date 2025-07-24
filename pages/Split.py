import streamlit as st
from PyPDF2 import PdfReader, PdfWriter
import tempfile
import os

st.set_page_config(page_title="Split PDF", page_icon="✂️")

st.title("✂️ Pemisah PDF Berdasarkan Halaman")
st.write("Unggah file PDF dan pilih halaman yang ingin diambil.")

uploaded_file = st.file_uploader("Unggah file PDF", type="pdf")

# Masukkan range halaman (misal 1-3)
page_range = st.text_input("Masukkan range halaman (contoh: 1-3):")

if uploaded_file and page_range and st.button("Split PDF"):
    try:
        start_page, end_page = map(int, page_range.split('-'))
        if start_page < 1 or end_page < start_page:
            st.error("Rentang halaman tidak valid.")
        else:
            with tempfile.TemporaryDirectory() as tmpdir:
                # Simpan PDF yang diunggah
                input_path = os.path.join(tmpdir, "input.pdf")
                with open(input_path, "wb") as f:
                    f.write(uploaded_file.read())

                # Proses split
                reader = PdfReader(input_path)
                writer = PdfWriter()

                total_pages = len(reader.pages)
                if end_page > total_pages:
                    end_page = total_pages

                for i in range(start_page - 1, end_page):
                    writer.add_page(reader.pages[i])

                output_path = os.path.join(tmpdir, "output_split.pdf")
                with open(output_path, "wb") as f:
                    writer.write(f)

                st.success(f"Berhasil mengekstrak halaman {start_page} hingga {end_page}.")
                with open(output_path, "rb") as f:
                    st.download_button(
                        label="📥 Unduh Hasil Split",
                        data=f,
                        file_name=f"halaman_{start_page}_sampai_{end_page}.pdf",
                        mime="application/pdf"
                    )

    except ValueError:
        st.error("Format range halaman salah. Gunakan format seperti: 2-5")
