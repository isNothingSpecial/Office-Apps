import streamlit as st
from PyPDF2 import PdfReader, PdfWriter
import tempfile
import os
import io

# Konfigurasi halaman Streamlit
st.set_page_config(page_title="Split PDF", page_icon="✂️", layout="centered")

st.markdown(
    """
    <style>
    .reportview-container {
        background: #f0f2f6;
    }
    .main {
        padding-top: 2rem;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-weight: bold;
        padding: 10px 20px;
        border-radius: 8px;
        transition: all 0.3s;
    }
    .stButton>button:hover {
        background-color: #45a049;
        transform: scale(1.02);
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("✂️ Pemisah PDF Berdasarkan Halaman")
st.markdown("Unggah file PDF dan tentukan rentang halaman yang ingin diekstrak. Halaman dihitung mulai dari 1.")

uploaded_file = st.file_uploader("Unggah file PDF", type="pdf")

# Masukkan range halaman (misal 1-3)
page_range = st.text_input("Masukkan rentang halaman (contoh: 1-3).", key="page_range_input")

if uploaded_file and page_range and st.button("Split PDF"):
    # Penggunaan try-except untuk menangani error format input (misal "1,3" bukan "1-3")
    try:
        # 1. Parsing input range
        if '-' not in page_range:
            st.error("Format range halaman salah. Gunakan tanda hubung '-', contoh: 2-5.")
            st.stop()
            
        start_page, end_page = map(int, page_range.split('-'))
        
        # 2. Inisialisasi PDF Reader
        pdf_reader = PdfReader(uploaded_file)
        total_pages = len(pdf_reader.pages)

        # 3. Validasi rentang halaman (PERBAIKAN UTAMA DI SINI)
        # Kondisi 'start_page < 1' memastikan halaman awal harus 1 atau lebih.
        # Kondisi 'end_page < start_page' memastikan rentang tidak terbalik.
        if start_page < 1 or end_page < start_page:
            st.error("Rentang halaman tidak valid. Halaman awal harus 1 atau lebih, dan halaman akhir harus sama atau lebih besar dari halaman awal.")
        
        # 4. Validasi batas atas
        elif start_page > total_pages:
            st.error(f"Halaman awal ({start_page}) melebihi jumlah total halaman ({total_pages}).")
            
        # 5. Proses Split
        else:
            pdf_writer = PdfWriter()
            
            # Sesuaikan halaman akhir jika melebihi total halaman
            actual_end_page = min(end_page, total_pages)
            
            # PyPDF2 menggunakan indexing 0, jadi halaman 1 adalah indeks 0.
            # Range di Python bersifat eksklusif di akhir, jadi kita menggunakan actual_end_page.
            # start_page - 1 adalah indeks awal.
            for i in range(start_page - 1, actual_end_page):
                pdf_writer.add_page(pdf_reader.pages[i])

            # Simpan hasil ke buffer
            output_pdf_buffer = io.BytesIO()
            pdf_writer.write(output_pdf_buffer)
            output_pdf_buffer.seek(0) # Kembali ke awal buffer

            # 6. Tampilkan dan Unduh
            st.success(f"Berhasil mengekstrak halaman {start_page} hingga {actual_end_page} dari total {total_pages} halaman.")
            
            file_name = f"split_halaman_{start_page}_sampai_{actual_end_page}.pdf"
            
            st.download_button(
                label="📥 Unduh Hasil Split",
                data=output_pdf_buffer,
                file_name=file_name,
                mime="application/pdf"
            )

    except ValueError:
        st.error("Terjadi kesalahan parsing. Pastikan format range halaman sudah benar (contoh: 2-5) dan hanya menggunakan angka.")
    except Exception as e:
        st.error(f"Terjadi kesalahan tak terduga: {e}")
