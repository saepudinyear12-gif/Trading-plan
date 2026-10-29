import streamlit as st

st.set_page_config(page_title="Stock Trading Engine", layout="centered")

st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        font-weight: bold;
        padding: 0.6rem;
    }
    </style>
    """, unsafe_allow_html=True)

avg_sell = st.text_input("", placeholder="Avg Sell Price (opsional)")
col_hapus, _ = st.columns([1, 2])
with col_hapus:
    if st.button("× Hapus"):
        st.toast("Input dibersihkan!")

if st.button("+ Tambah Broker"):
    st.info("Fitur tambah broker diklik.")

col1, col2 = st.columns(2)
with col1:
    if st.button("📊 Kamus Indikator"):
        st.write("Membuka Kamus Indikator...")
with col2:
    if st.button("📈 Riwayat Prediksi"):
        st.write("Membuka Riwayat Prediksi...")

if st.button("🔄 Reset Memory"):
    st.success("Memory berhasil di-reset!")

if st.button("🏆 Top 10 Saham Besok · IDX Technical Scan"):
    st.snow()
    st.write("Menjalankan pemindaian IDX Technical Scan...")

if st.button("📈 BSJP — Beli Sore Jual Pagi"):
    st.success("Menjalankan skema screening BSJP...")

if st.button("📉 BPJS — Beli Pagi Jual Siang/Sore"):
    st.warning("Menjalankan skema screening BPJS...")

st.markdown("---")
st.subheader("⚙️ PENGATURAN API")

api_key = st.text_input("", type="password", value="1234567890abcdef")

col_tampil, col_simpan = st.columns(2)
with col_tampil:
    show_key = st.button("👁️ Tampilkan")
with col_simpan:
    save_key = st.button("💾 Simpan Key")

high_accuracy = st.toggle("Mode Akurasi Tinggi (50.000 simulasi MC, lebih presisi tapi lebih lambat)")

st.markdown("""
    <style>
    div.stButton > button:first-child {
        background-color: #f0a500;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

if st.button("▶ Run Hyper-Hybrid Macro Engine V21"):
    with st.spinner("Menjalankan kalkulasi Macro Engine V21..."):
        st.success("Analisis Macro Engine V21 Selesai!")
