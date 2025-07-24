import streamlit as st
from flask import Flask, request, send_file
from PyPDF2 import PdfMerger
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def merge_pdfs():
    if request.method == 'POST':
        files = request.files.getlist('pdf_files')
        merger = PdfMerger()

        for file in files:
            merger.append(file)

        output_path = "hasil_merge.pdf"
        merger.write(output_path)
        merger.close()

        return send_file(output_path, as_attachment=True)

    return '''
        <h2>Unggah beberapa file PDF untuk digabung</h2>
        <form method="POST" enctype="multipart/form-data">
            <input type="file" name="pdf_files" multiple accept=".pdf" required>
            <input type="submit" value="Gabungkan PDF">
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)
