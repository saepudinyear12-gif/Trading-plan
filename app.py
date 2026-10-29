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

# Inisialisasi Session State agar data hasil scan tidak hilang saat klik tombol lain
if "bsjp_df" not in st.session_state:
    st.session_state.bsjp_df = None
if "bpjs_df" not in st.session_state:
    st.session_state.bpjs_df = None
if "haka_df" not in st.session_state:
    st.session_state.haka_df = None
if "scalp_df" not in st.session_state:
    st.session_state.scalp_df = None

# Menu Input Kode Saham untuk Data Real-Time & Trading Plan
ticker_input = st.text_input("Masukkan Kode Saham IDX (Contoh: TMAS, BBCA, ASII)", value="TMAS")

@st.cache_data(ttl=300)
def load_stock_data(ticker):
    if not ticker.endswith(".JK"):
        clean_ticker = ticker.strip().upper() + ".JK"
    else:
        clean_ticker = ticker.strip().upper()
    
    stock = yf.Ticker(clean_ticker)
    df = stock.history(period="1mo")
    return df, clean_ticker

if st.button("🔍 Tarik Data Real-Time & Trading Plan"):
    with st.spinner(f"Menghitung Trading Plan untuk {ticker_input}..."):
        try:
            df, final_ticker = load_stock_data(ticker_input)
            if not df.empty:
                st.success(f"Berhasil memuat data {final_ticker}!")
                
                last_price = df['Close'].iloc[-1]
                resistance_tp = round(df['High'].iloc[-5:].max(), 2)
                suggested_sl = round(last_price * 0.98, 2)
                
                st.markdown(f"### 📋 Trading Plan: {final_ticker.replace('.JK', '')}")
                col1, col2, col3 = st.columns(3)
                col1.metric("Harga Acuan", f"Rp {int(last_price)}")
                col2.metric("Target TP (Resistance)", f"Rp {int(resistance_tp)}")
                col3.metric("Stop Loss (-2%)", f"Rp {int(suggested_sl)}")
                
                st.subheader(f"Grafik Harga Penutupan - {final_ticker}")
                st.line_chart(df['Close'])
                
                st.subheader("Data Transaksi Terakhir")
                st.dataframe(df.tail(5))
            else:
                st.warning(f"Data untuk '{ticker_input}' tidak ditemukan.")
        except Exception as e:
            st.error("Gagal memuat data. Silakan coba lagi.")

st.markdown("---")

# --- WATCHLIST KOMPREHENSIF SEKTOR ---
WATCHLIST = [
    "PANI.JK", "BSDE.JK", "CTRA.JK", "PWON.JK", "SMRA.JK", "ASRI.JK", "LPKR.JK", 
    "DILD.JK", "BEST.JK", "DUTI.JK", "BKSL.JK", "KIJA.JK", "MMLP.JK", "GWSA.JK",
    "SILO.JK", "HEAL.JK", "MIKA.JK", "KAEF.JK", "INAF.JK", "DVLA.JK", "PEHA.JK", "RSGK.JK",
    "GOTO.JK", "BUKA.JK", "EMTK.JK", "MTDL.JK", "BELI.JK", "SCMA.JK", 
    "EXCL.JK", "ISAT.JK", "WIFI.JK", "AXIO.JK",
    "BRPT.JK", "TPIA.JK", "TKIM.JK", "INKP.JK", "IMPC.JK", "ESSA.JK", "NCKL.JK", 
    "MBMA.JK", "PSAB.JK", "DKHH.JK", "ANTM.JK", "INCO.JK", "MDKA.JK",
    "BUMI.JK", "BRMS.JK", "DEWA.JK", "ENRG.JK", "ELSA.JK", "DOID.JK", "RAJA.JK", "PGEO.JK",
    "ADRO.JK", "PTBA.JK", "ITMG.JK", "HRUM.JK", "ADMR.JK", "MEDC.JK", "INDY.JK", "TOBA.JK", 
    "BSSR.JK", "BIPI.JK", "SGER.JK", "RMKE.JK", "IATA.JK", "COAL.JK", "SHIP.JK", "SOCI.JK", "TPMA.JK",
    "ARGO.JK", "BELL.JK", "TRIS.JK", "POLU.JK", "SSTM.JK", "ERTX.JK", "ESTI.JK", "RICY.JK", "TFCO.JK", "PBRX.JK", "ADMG.JK",
    "ASSA.JK", "BIRD.JK", "HAIS.JK", "PSSI.JK", "BBRM.JK", "GTSI.JK", "SMDR.JK", "TMAS.JK", "BOAT.JK",
    "LEAD.JK", "WINS.JK", "HITS.JK", "IPCC.JK",
    "ACES.JK", "ERAA.JK", "MAPI.JK", "MAPA.JK", "CMRY.JK", "SIDO.JK", "JPFA.JK", "CPIN.JK", "CLEO.JK", "MIDI.JK",
    "ARTO.JK", "BRIS.JK", "PNLF.JK", "BBYB.JK", "AGRO.JK", "BABP.JK", "CFIN.JK", "ADMF.JK", "WOMF.JK",
    "BANK.JK", "INPC.JK", "BBHI.JK", "MASB.JK", "BGTG.JK",
    "TAPG.JK", "DSNG.JK", "SSMS.JK", "LSIP.JK", "AALI.JK", "PALM.JK", "BWPT.JK", "SIMP.JK", "SGRO.JK", "CSRA.JK",
    "AUTO.JK", "DRMA.JK", "SMSM.JK", "BOLT.JK", "GJTL.JK", "IMAS.JK", "KBLI.JK", "VOKS.JK", "ARNA.JK", "MARK.JK",
    "TMPO.JK", "FILM.JK", "FORU.JK", "MARI.JK", "MNCN.JK", "BMTR.JK", "VIVA.JK",
    "ACST.JK", "TOTL.JK", "NRCA.JK", "PPRE.JK", "WEGE.JK", "IDPR.JK", "KBLM.JK",
    "SSIA.JK", "IPAC.JK", "MPXL.JK", "SAME.JK",
    "PBID.JK", "IPOL.JK", "FAPA.JK", "SOUL.JK", "TALF.JK", "KMTR.JK", "NPGF.JK",
    "MAIN.JK", "SIPD.JK", "WMUU.JK", "WMPP.JK",
    "FAST.JK", "PZZA.JK", "PANR.JK", "BUVA.JK",
    "ABMM.JK", "ABDA.JK", "ASBI.JK", "AHAP.JK",
    "TOWR.JK", "TBIG.JK", "CENT.JK", "IBST.JK", "MTEL.JK", "BALI.JK",
    "NICL.JK", "DKFT.JK", "CITA.JK", "NICK.JK",
    "DOOH.JK", "HUMI.JK", "STRK.JK", "KEEN.JK", "CUAN.JK", "PACK.JK", 
    "TRUE.JK", "HILL.JK", "NSSS.JK", "MOLI.JK", "JGLE.JK", "MPRO.JK", "AMMN.JK", "SAGE.JK"
]

# --- LOGIKA TOMBOL BSJP ---
if st.button("📈 BSJP — Beli Sore Jual Pagi"):
    with st.spinner("Memindai seluruh sektor untuk kandidat BSJP..."):
        bsjp_results = []
        for s in WATCHLIST:
            try:
                t = yf.Ticker(s)
                hist = t.history(period="5d")
                if len(hist) >= 2:
                    close_today = hist['Close'].iloc[-1]
                    close_yesterday = hist['Close'].iloc[-2]
                    vol_today = hist['Volume'].iloc[-1]
                    
                    change = ((close_today - close_yesterday) / close_yesterday) * 100
                    turnover = close_today * vol_today
                    
                    if close_today <= 3000 and turnover >= 3_000_000_000 and change >= 1.5:
                        bsjp_results.append({
                            "Saham": s.replace(".JK", ""),
                            "Harga Closing": round(close_today, 2),
                            "Kenaikan (%)": round(change, 2),
                            "Volume": int(vol_today),
                            "Resistance": round(hist['High'].max(), 2)
                        })
            except:
                continue
        
        if bsjp_results:
            df_res = pd.DataFrame(bsjp_results).sort_values(by="Kenaikan (%)", ascending=False)
            st.session_state.bsjp_df = df_res.head(5) # Dibatasi Top 5
        else:
            st.session_state.bsjp_df = pd.DataFrame()

if st.session_state.bsjp_df is not None:
    if not st.session_state.bsjp_df.empty:
        st.success(f"Ditemukan {len(st.session_state.bsjp_df)} kandidat BSJP terbaik:")
        st.dataframe(st.session_state.bsjp_df[['Saham', 'Harga Closing', 'Kenaikan (%)', 'Volume']])
        
        st.markdown("### 🎯 Rincian Trading Plan (TP Berdasarkan Resistance Terdekat)")
        for index, row in st.session_state.bsjp_df.iterrows():
            saham = row["Saham"]
            harga = row["Harga Closing"]
            tp = row["Resistance"]
            sl = round(harga * 0.98, 2)
            st.markdown(f"- **{saham}** (Harga: {harga}) ➡️ **Target TP (Resistance):** Rp {tp} | **Stop Loss:** Rp {sl} (-2%)")
    else:
        st.warning("Belum ada saham yang memenuhi kriteria ketat BSJP saat ini.")

# --- LOGIKA TOMBOL BPJS ---
if st.button("📉 BPJS — Beli Pagi Jual Siang/Sore"):
    with st.spinner("Memindai seluruh sektor untuk kandidat BPJS..."):
        bpjs_results = []
        for s in WATCHLIST:
            try:
                t = yf.Ticker(s)
                hist = t.history(period="5d")
                if len(hist) >= 2:
                    open_price = hist['Open'].iloc[-1]
                    close_price = hist['Close'].iloc[-1]
                    vol_today = hist['Volume'].iloc[-1]
                    
                    change = ((close_price - open_price) / open_price) * 100
                    turnover = close_price * vol_today
                    
                    if close_price <= 3000 and turnover >= 3_000_000_000 and change >= 1.0:
                        bpjs_results.append({
                            "Saham": s.replace(".JK", ""),
                            "Open Pagi": round(open_price, 2),
                            "Terakhir": round(close_price, 2),
                            "Est. Intraday (%)": round(change, 2),
                            "Volume": int(vol_today),
                            "Resistance": round(hist['High'].max(), 2)
                        })
            except:
                continue
        
        if bpjs_results:
            df_res = pd.DataFrame(bpjs_results).sort_values(by="Est. Intraday (%)", ascending=False)
            st.session_state.bpjs_df = df_res.head(5) # Dibatasi Top 5
        else:
            st.session_state.bpjs_df = pd.DataFrame()

if st.session_state.bpjs_df is not None:
    if not st.session_state.bpjs_df.empty:
        st.success(f"Ditemukan {len(st.session_state.bpjs_df)} kandidat BPJS terbaik:")
        st.dataframe(st.session_state.bpjs_df[['Saham', 'Open Pagi', 'Terakhir', 'Est. Intraday (%)', 'Volume']])
        
        st.markdown("### 🎯 Rincian Trading Plan (TP Berdasarkan Resistance Terdekat)")
        for index, row in st.session_state.bpjs_df.iterrows():
            saham = row["Saham"]
            harga = row["Terakhir"]
            tp = row["Resistance"]
            sl = round(harga * 0.98, 2)
            st.markdown(f"- **{saham}** (Harga: {harga}) ➡️ **Target TP (Resistance):** Rp {tp} | **Stop Loss:** Rp {sl} (-2%)")
    else:
        st.warning("Belum ada saham yang memenuhi kriteria ketat BPJS saat ini.")

# --- LOGIKA TOMBOL HAKA / BREAKOUT ---
if st.button("🚀 HAKA — Free Breakout Scanner"):
    with st.spinner("Memindai emiten potensial Breakout / HAKA..."):
        haka_results = []
        for s in WATCHLIST:
            try:
                t = yf.Ticker(s)
                hist = t.history(period="10d")
                if len(hist) >= 5:
                    close_today = hist['Close'].iloc[-1]
                    prev_resistance = hist['High'].iloc[-6:-1].max() if len(hist) >= 6 else hist['High'].iloc[:-1].max()
                    vol_today = hist['Volume'].iloc[-1]
                    
                    change = ((close_today - hist['Close'].iloc[-2]) / hist['Close'].iloc[-2]) * 100
                    turnover = close_today * vol_today
                    
                    if close_today <= 3000 and turnover >= 3_000_000_000 and close_today >= prev_resistance and change >= 1.0:
                        haka_results.append({
                            "Saham": s.replace(".JK", ""),
                            "Harga Breakout": round(close_today, 2),
                            "Kenaikan (%)": round(change, 2),
                            "Volume": int(vol_today),
                            "Next Resistance": round(close_today * 1.05, 2)
                        })
            except:
                continue
        
        if haka_results:
            df_res = pd.DataFrame(haka_results).sort_values(by="Kenaikan (%)", ascending=False)
            st.session_state.haka_df = df_res.head(5) # Dibatasi Top 5
        else:
            st.session_state.haka_df = pd.DataFrame()

if st.session_state.haka_df is not None:
    if not st.session_state.haka_df.empty:
        st.success(f"Ditemukan {len(st.session_state.haka_df)} kandidat HAKA Breakout terbaik:")
        st.dataframe(st.session_state.haka_df[['Saham', 'Harga Breakout', 'Kenaikan (%)', 'Volume']])
        
        st.markdown("### 🎯 Rincian Trading Plan (HAKA Breakout)")
        for index, row in st.session_state.haka_df.iterrows():
            saham = row["Saham"]
            harga = row["Harga Breakout"]
            tp = row["Next Resistance"]
            sl = round(harga * 0.975, 2)
            st.markdown(f"- **{saham}** (Harga Breakout: {harga}) ➡️ **Target TP:** Rp {tp} | **Stop Loss:** Rp {sl} (-2.5%)")
    else:
        st.warning("Belum ada saham yang menembus level breakout HAKA saat ini.")

# --- LOGIKA TOMBOL SCALPING FAST TRADE ---
if st.button("⚡ SCALPING — Fast Trade Momentum Scanner"):
    with st.spinner("Memindai emiten scalping dengan volatilitas tinggi..."):
        scalp_results = []
        for s in WATCHLIST:
            try:
                t = yf.Ticker(s)
                hist = t.history(period="5d")
                if len(hist) >= 2:
                    close_today = hist['Close'].iloc[-1]
                    open_today = hist['Open'].iloc[-1]
                    high_today = hist['High'].iloc[-1]
                    low_today = hist['Low'].iloc[-1]
                    vol_today = hist['Volume'].iloc[-1]
                    
                    daily_range = ((high_today - low_today) / low_today) * 100
                    turnover = close_today * vol_today
                    
                    if close_today <= 3000 and turnover >= 3_000_000_000 and daily_range >= 3.0:
                        scalp_results.append({
                            "Saham": s.replace(".JK", ""),
                            "Harga Terakhir": round(close_today, 2),
                            "Range Harian (%)": round(daily_range, 2),
                            "Turnover (Miliar)": round(turnover / 1_000_000_000, 2),
                            "Volume": int(vol_today),
                            "Resistance TP": round(high_today, 2)
                        })
            except:
                continue
        
        if scalp_results:
            df_res = pd.DataFrame(scalp_results).sort_values(by="Range Harian (%)", ascending=False)
            st.session_state.scalp_df = df_res.head(5) # Dibatasi Top 5
        else:
            st.session_state.scalp_df = pd.DataFrame()

if st.session_state.scalp_df is not None:
    if not st.session_state.scalp_df.empty:
        st.success(f"Ditemukan {len(st.session_state.scalp_df)} kandidat Scalping Fast Trade Pilihan:")
        st.dataframe(st.session_state.scalp_df[['Saham', 'Harga Terakhir', 'Range Harian (%)', 'Turnover (Miliar)', 'Volume']])
        
        st.markdown("### 🎯 Rincian Trading Plan (Scalping Fast Trade)")
        for index, row in st.session_state.scalp_df.iterrows():
            saham = row["Saham"]
            harga = row["Harga Terakhir"]
            tp = row["Resistance TP"]
            sl = round(harga * 0.985, 2)
            st.markdown(f"- **{saham}** (Harga: {harga}) ➡️ **Target TP (High Harian):** Rp {tp} | **Stop Loss Ketat:** Rp {sl} (-1.5%)")
    else:
        st.warning("Belum ada saham yang memenuhi kriteria ketat scalping volatil saat ini.")

st.markdown("---")
st.subheader("⚙️ PENGATURAN API")
api_key = st.text_input("", type="password", value="1234567890abcdef")
high_accuracy = st.toggle("Mode Akurasi Tinggi (50.000 simulasi MC)")
