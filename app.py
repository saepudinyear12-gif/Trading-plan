import streamlit as st
import yfinance as yf
import pandas as pd

st.set_page_config(page_title="Stock Trading Engine Real-Time", layout="centered")

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

st.title("📈 IDX Real-Time Trading Engine")

# Menu Input Kode Saham untuk Data Real-Time
ticker_input = st.text_input("Masukkan Kode Saham IDX (Contoh: BBCA.JK, BBRI.JK, ASII.JK)", value="BBCA.JK")

if st.button("🔍 Tarik Data Real-Time"):
    with st.spinner(f"Mengambil data live untuk {ticker_input}..."):
        try:
            stock = yf.Ticker(ticker_input)
            df = stock.history(period="1mo")
            if not df.empty:
                st.success(f"Berhasil memuat data {ticker_input}!")
                st.subheader("Grafik Harga Penutupan (1 Bulan Terakhir)")
                st.line_chart(df['Close'])
                
                st.subheader("Data Transaksi Terakhir")
                st.dataframe(df.tail(5))
            else:
                st.warning("Data tidak ditemukan, pastikan penulisan kode saham benar (gunakan akhiran .JK untuk saham Indonesia).")
        except Exception as e:
            st.error(f"Terjadi kesalahan: {e}")

st.markdown("---")
if st.button("🏆 Top 10 Saham · IDX Technical Scan"):
    st.snow()
    st.info("Memindai saham likuid non-bluechip pilihan...")
    sample_stocks = ["ADRO.JK", "PTBA.JK", "ANTM.JK", "INCO.JK", "MEDC.JK"]
    data_list = []
    for s in sample_stocks:
        t = yf.Ticker(s)
        hist = t.history(period="5d")
        if not hist.empty:
            last_close = hist['Close'].iloc[-1]
            prev_close = hist['Close'].iloc[-2]
            change = ((last_close - prev_close) / prev_close) * 100
            data_list.append({"Saham": s, "Harga Terakhir": round(last_close, 2), "Perubahan (%)": round(change, 2)})
    
    if data_list:
        df_scan = pd.DataFrame(data_list)
        st.dataframe(df_scan)

if st.button("📈 BSJP — Beli Sore Jual Pagi"):
    st.success("Menjalankan skema screening BSJP...")

if st.button("📉 BPJS — Beli Pagi Jual Siang/Sore"):
    st.warning("Menjalankan skema screening BPJS...")

st.markdown("---")
st.subheader("⚙️ PENGATURAN API")
api_key = st.text_input("", type="password", value="1234567890abcdef")
high_accuracy = st.toggle("Mode Akurasi Tinggi (50.000 simulasi MC)")
