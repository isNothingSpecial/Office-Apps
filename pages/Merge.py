import streamlit as st
import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfMerger

def merge_pdfs():
    files = filedialog.askopenfilenames(title="Pilih file PDF yang ingin digabung", filetypes=[("PDF files", "*.pdf")])
    if not files:
        return

    merger = PdfMerger()

    for pdf in files:
        merger.append(pdf)

    output_path = filedialog.asksaveasfilename(
        defaultextension=".pdf",
        filetypes=[("PDF files", "*.pdf")],
        title="Simpan sebagai"
    )

    if output_path:
        merger.write(output_path)
        merger.close()
        messagebox.showinfo("Sukses", f"PDF berhasil digabung dan disimpan sebagai:\n{output_path}")

# GUI setup
root = tk.Tk()
root.title("Merge PDF - Tanpa Flask/Streamlit")

frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

label = tk.Label(frame, text="Klik tombol di bawah untuk memilih dan menggabungkan PDF:")
label.pack(pady=10)

button = tk.Button(frame, text="Pilih & Gabungkan PDF", command=merge_pdfs)
button.pack(pady=10)

root.mainloop()

