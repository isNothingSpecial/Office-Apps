import streamlit as st

st.set_page_config(page_title="PDF Tools Dashboard", layout="wide")
st.markdown("<h1 style='text-align: center;'>📚 PDF Tools Dashboard</h1>", unsafe_allow_html=True)
st.write("")

# CSS custom agar tombol terlihat kotak dan rata tengah
st.markdown("""
    <style>
    .grid-container {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 30px;
        justify-items: center;
        padding: 30px 10px;
    }

    .grid-item {
        background-color: #f1f1f1;
        border-radius: 16px;
        width: 150px;
        height: 150px;
        display: flex;
        align-items: center;
        justify-content: center;
        text-align: center;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        transition: transform 0.2s ease;
        font-size: 18px;
    }

    .grid-item:hover {
        transform: scale(1.05);
        background-color: #e0e0e0;
    }

    a.card-link {
        text-decoration: none;
        color: black;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# Grid dengan card link ke halaman lain
st.markdown("""
<div class="grid-container">
    <div class="grid-item">
        <a class="card-link" href="/pages/Merge" target="_self">📎<br>Merge PDF</a>
    </div>
    <div class="grid-item">
        <a class="card-link" href="/pages/Split" target="_self">✂️<br>Split PDF</a>
    </div>
    <div class="grid-item">
        <a class="card-link" href="/pages/Delete" target="_self">🗑️<br>Delete Page</a>
    </div>
    <div class="grid-item">
        <a class="card-link" href="/pages/Word" target="_self">📄<br>PDF to Word</a>
    </div>
</div>
""", unsafe_allow_html=True)
