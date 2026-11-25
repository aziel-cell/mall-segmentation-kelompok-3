from pathlib import Path
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering
from sklearn.preprocessing import StandardScaler

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(
    page_title="Mall Customer Segmentation App",
    page_icon="🛍️",
    layout="wide"
)

BASE_DIR = Path(__file__).resolve().parent

# --- 2. SIDEBAR NAVIGASI ---
st.sidebar.title("📌 Navigasi Menu")
menu = st.sidebar.selectbox(
    "Pilih Halaman",
    [
        "Halaman Utama",
        "Eksplorasi Data (EDA)",
        "Analisis Gender & K-Means",
        "Perbandingan Algoritma Klustering",
        "Form Simulasi Segmen",
        "Tentang Kami"
    ]
)

# --- 3. FUNGSI MEMUAT DATASET ---
@st.cache_data
def load_data():
    csv_path = BASE_DIR / "Mall_Customers.csv"
    return pd.read_csv(csv_path)

# Memanggil fungsi load data
try:
    df_mall = load_data()
except Exception as e:
    st.error(f"Gagal memuat dataset: {e}")
    df_mall = None


