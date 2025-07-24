import streamlit as st
from PyPDF2 import PdfReader, PdfWriter
import tempfile, os, re

st.set_page_config(page_title="Hapus Halaman PDF", page_icon="🗑️")
st.title("🗑️ Hapus Halaman dari PDF")
st.write("Unggah PDF dan masukkan nomor halaman yang ingin dihapus. Contoh input: `2,4-5,7`")

uploaded_file = st.file_uploader("Unggah file PDF", type="pdf")
pages_to_delete_input = st.text_input("Halaman yang dihapus (gunakan koma dan/atau range):", placeholder="misal: 2,4-5")

def parse_pages(text):
    pages = set()
    pattern = r'^\s*\d+(\s*-\s*\d+)?\s*(,\s*\d+(\s*-\s*\d+)?\s*)*$'
    if not re.match(pattern, text.replace(' ', '')):
        return None
    parts = [p.strip() for p in text.split(',') if p.strip()]
    for part in parts:
        if '-' in part:
            a, b = part.split('-')
            start, end = int(a), int(b)
            if start > end: start, end = end, start
            pages.update(range(start, end + 1))
        else:
            pages.add(int(part))
    return sorted(pages)

if uploaded_file and pages_to_delete_input:
    pages_to_delete = parse_pages(pages_to_delete_input)
    if pages_to_delete is None:
        st.error("Format salah. Contoh valid: 2,4-5,7")
    else:
        if st.button("Hapus Halaman"):
            with tempfile.TemporaryDirectory() as tmpdir:
                input_path = os.path.join(tmpdir, "input.pdf")
                with open(input_path, "wb") as f:
                    f.write(uploaded_file.read())

                reader = PdfReader(input_path)
                total_pages = len(reader.pages)

                # Validasi halaman
                valid_pages = [p for p in pages_to_delete if 1 <= p <= total_pages]
                if not valid_pages:
                    st.error("Tidak ada nomor halaman yang valid.")
                else:
                    to_delete_index = {p - 1 for p in valid_pages}
                    writer = PdfWriter()
                    for i in range(total_pages):
                        if i not in to_delete_index:
                            writer.add_page(reader.pages[i])

                    output_path = os.path.join(tmpdir, "hasil.pdf")
                    with open(output_path, "wb") as f:
                        writer.write(f)

                    st.success(f"Berhasil menghapus halaman: {', '.join(map(str, valid_pages))}")
                    with open(output_path, "rb") as f:
                        st.download_button(
                            "📥 Unduh PDF Hasil",
                            data=f,
                            file_name="pdf_setelah_dihapus.pdf",
                            mime="application/pdf"
                        )
