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
ticker_input = st.text_input("Masukkan Kode Saham IDX (Contoh: BBCA, BBRI, ASII)", value="BBCA")

@st.cache_data(ttl=300)
def load_stock_data(ticker):
    if not ticker.endswith(".JK"):
        clean_ticker = ticker.strip().upper() + ".JK"
    else:
        clean_ticker = ticker.strip().upper()
    
    stock = yf.Ticker(clean_ticker)
    df = stock.history(period="1mo")
    return df, clean_ticker

if st.button("🔍 Tarik Data Real-Time"):
    with st.spinner(f"Mengambil data live untuk {ticker_input}..."):
        try:
            df, final_ticker = load_stock_data(ticker_input)
            if not df.empty:
                st.success(f"Berhasil memuat data {final_ticker}!")
                st.subheader(f"Grafik Harga Penutupan - {final_ticker}")
                st.line_chart(df['Close'])
                
                st.subheader("Data Transaksi Terakhir")
                st.dataframe(df.tail(5))
            else:
                st.warning(f"Data untuk '{ticker_input}' tidak ditemukan.")
        except Exception as e:
            st.error("Gagal memuat data. Silakan coba lagi.")

st.markdown("---")
if st.button("🏆 Top 10 Saham · IDX Technical Scan"):
    st.info("Memindai saham pilihan...")
    sample_stocks = ["ADRO.JK", "PTBA.JK", "ANTM.JK", "INCO.JK", "MEDC.JK"]
    data_list = []
    for s in sample_stocks:
        try:
            t = yf.Ticker(s)
            hist = t.history(period="5d")
            if not hist.empty:
                last_close = hist['Close'].iloc[-1]
                prev_close = hist['Close'].iloc[-2]
                change = ((last_close - prev_close) / prev_close) * 100
                data_list.append({"Saham": s, "Harga Terakhir": round(last_close, 2), "Perubahan (%)": round(change, 2)})
        except:
            continue
    
    if data_list:
        df_scan = pd.DataFrame(data_list)
        st.dataframe(df_scan)

# --- LOGIKA TOMBOL BSJP ---
if st.button("📈 BSJP — Beli Sore Jual Pagi"):
    with st.spinner("Menjalankan screening BSJP (Kandidat akumulasi penutupan)..."):
        bsjp_watchlist = ["ASII.JK", "BBCA.JK", "BBRI.JK", "ADRO.JK", "PTBA.JK", "ANTM.JK"]
        bsjp_results = []
        for s in bsjp_watchlist:
            try:
                t = yf.Ticker(s)
                hist = t.history(period="3d")
                if len(hist) >= 2:
                    close_today = hist['Close'].iloc[-1]
                    close_yesterday = hist['Close'].iloc[-2]
                    change = ((close_today - close_yesterday) / close_yesterday) * 100
                    # Filter sederhana: momentum positif di sesi sore
                    if change > 0:
                        bsjp_results.append({
                            "Saham": s,
                            "Harga Closing": round(close_today, 2),
                            "Kenaikan (%)": round(change, 2)
                        })
            except:
                continue
        
        if bsjp_results:
            st.success("Hasil Screening Kandidat BSJP:")
            st.dataframe(pd.DataFrame(bsjp_results))
        else:
            st.warning("Belum ada saham yang memenuhi kriteria BSJP saat ini.")

# --- LOGIKA TOMBOL BPJS ---
if st.button("📉 BPJS — Beli Pagi Jual Siang/Sore"):
    with st.spinner("Menjalankan screening BPJS (Kandidat pantauan pagi)..."):
        bpjs_watchlist = ["GOTO.JK", "BUMI.JK", "DEWA.JK", "ANTM.JK", "BRMS.JK"]
        bpjs_results = []
        for s in bpjs_watchlist:
            try:
                t = yf.Ticker(s)
                hist = t.history(period="2d")
                if not hist.empty:
                    open_price = hist['Open'].iloc[-1]
                    close_price = hist['Close'].iloc[-1]
                    change = ((close_price - open_price) / open_price) * 100
                    bpjs_results.append({
                    "Saham": s,
                    "Open Pagi": round(open_price, 2),
                    "Terakhir": round(close_price, 2),
                    "Est. Intraday (%)": round(change, 2)
                })
            except:
                continue
        
        if bpjs_results:
            st.success("Hasil Screening Kandidat BPJS:")
            st.dataframe(pd.DataFrame(bpjs_results))
        else:
            st.warning("Data BPJS belum tersedia.")

st.markdown("---")
st.subheader("⚙️ PENGATURAN API")
api_key = st.text_input("", type="password", value="1234567890abcdef")
high_accuracy = st.toggle("Mode Akurasi Tinggi (50.000 simulasi MC)")
