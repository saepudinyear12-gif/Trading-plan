import streamlit as st
import yfinance as yf
import pandas as pd

st.set_page_config(page_title="Whale Tracker & IDX Screener", layout="centered")

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

st.title("🐋 Whale Tracker & IDX Screener")

# Inisialisasi Session State agar data hasil scan tidak hilang saat klik tombol lain
if "bsjp_df" not in st.session_state:
    st.session_state.bsjp_df = None
if "bpjs_df" not in st.session_state:
    st.session_state.bpjs_df = None
if "haka_df" not in st.session_state:
    st.session_state.haka_df = None
if "scalp_df" not in st.session_state:
    st.session_state.scalp_df = None
if "support_df" not in st.session_state:
    st.session_state.support_df = None
if "sesi2_df" not in st.session_state:
    st.session_state.sesi2_df = None

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
                supply_tp = round(df['High'].iloc[-10:].max(), 2)
                demand_zone = round(df['Low'].iloc[-20:].min(), 2) if len(df) >= 20 else round(df['Low'].min(), 2)
                suggested_sl = round(demand_zone * 0.98, 2)
                
                st.markdown(f"### 📋 Trading Plan (Supply & Demand): {final_ticker.replace('.JK', '')}")
                
                col1, col2 = st.columns(2)
                col1.metric("Harga Acuan", f"Rp {int(last_price)}")
                col2.metric("Area Demand (Support)", f"Rp {int(demand_zone)}")
                
                col3, col4 = st.columns(2)
                col3.metric("Target TP (Supply Zone)", f"Rp {int(supply_tp)}")
                col4.metric("Stop Loss (Bawah Demand)", f"Rp {int(suggested_sl)}")
                
                st.subheader(f"Grafik Harga Penutupan - {final_ticker}")
                st.line_chart(df['Close'])
                
                st.subheader("Data Transaksi Terakhir")
                st.dataframe(df.tail(5))
            else:
                st.warning(f"Data untuk '{ticker_input}' tidak ditemukan.")
        except Exception:
            st.error("Gagal memuat data. Silakan coba lagi.")

st.markdown("---")

WATCHLIST = [
    "PANI.JK", "BSDE.JK", "CTRA.JK", "PWON.JK", "SMRA.JK", "ASRI.JK", "LPKR.JK", 
    "DILD.JK", "BEST.JK", "DUTI.JK", "BKSL.JK", "KIJA.JK", "MMLP.JK", "GWSA.JK",
    "SILO.JK", "HEAL.JK", "MIKA.JK", "KAEF.JK", "INAF.JK", "DVLA.JK", "PEHA.JK", "RSGK.JK",
    "GOTO.JK", "BUKA.JK", "EMTK.JK", "MTDL.JK", "BELI.JK", "SCMA.JK", 
    "EXCL.JK", "ISAT.JK", "WIFI.JK", "AXIO.JK", "BRPT.JK", "TPIA.JK", "TKIM.JK", 
    "INKP.JK", "IMPC.JK", "ESSA.JK", "NCKL.JK", "MBMA.JK", "PSAB.JK", "DKHH.JK", 
    "ANTM.JK", "INCO.JK", "MDKA.JK", "BUMI.JK", "BRMS.JK", "DEWA.JK", "ENRG.JK", 
    "ELSA.JK", "DOID.JK", "RAJA.JK", "PGEO.JK", "ADRO.JK", "PTBA.JK", "ITMG.JK", 
    "HRUM.JK", "ADMR.JK", "MEDC.JK", "INDY.JK", "TOBA.JK", "BSSR.JK", "BIPI.JK", 
    "SGER.JK", "RMKE.JK", "IATA.JK", "COAL.JK", "SHIP.JK", "SOCI.JK", "TPMA.JK",
    "ARGO.JK", "BELL.JK", "TRIS.JK", "POLU.JK", "SSTM.JK", "ERTX.JK", "ESTI.JK", 
    "RICY.JK", "TFCO.JK", "PBRX.JK", "ADMG.JK", "ASSA.JK", "BIRD.JK", "HAIS.JK", 
    "PSSI.JK", "BBRM.JK", "GTSI.JK", "SMDR.JK", "TMAS.JK", "BOAT.JK", "LEAD.JK", 
    "WINS.JK", "HITS.JK", "IPCC.JK", "ACES.JK", "ERAA.JK", "MAPI.JK", "MAPA.JK", 
    "CMRY.JK", "SIDO.JK", "JPFA.JK", "CPIN.JK", "CLEO.JK", "MIDI.JK", "ARTO.JK", 
    "BRIS.JK", "PNLF.JK", "BBYB.JK", "AGRO.JK", "BABP.JK", "CFIN.JK", "ADMF.JK", 
    "WOMF.JK", "BANK.JK", "INPC.JK", "BBHI.JK", "MASB.JK", "BGTG.JK", "TAPG.JK", 
    "DSNG.JK", "SSMS.JK", "LSIP.JK", "AALI.JK", "PALM.JK", "BWPT.JK", "SIMP.JK", 
    "SGRO.JK", "CSRA.JK", "AUTO.JK", "DRMA.JK", "SMSM.JK", "BOLT.JK", "GJTL.JK", 
    "IMAS.JK", "KBLI.JK", "VOKS.JK", "ARNA.JK", "MARK.JK", "TMPO.JK", "FILM.JK", 
    "FORU.JK", "MARI.JK", "MNCN.JK", "BMTR.JK", "VIVA.JK", "ACST.JK", "TOTL.JK", 
    "NRCA.JK", "PPRE.JK", "WEGE.JK", "IDPR.JK", "KBLM.JK", "SSIA.JK", "IPAC.JK", 
    "MPXL.JK", "SAME.JK", "PBID.JK", "IPOL.JK", "FAPA.JK", "SOUL.JK", "TALF.JK", 
    "KMTR.JK", "NPGF.JK", "MAIN.JK", "SIPD.JK", "WMUU.JK", "WMPP.JK", "FAST.JK", 
    "PZZA.JK", "PANR.JK", "BUVA.JK", "ABMM.JK", "ABDA.JK", "ASBI.JK", "AHAP.JK", 
    "TOWR.JK", "TBIG.JK", "CENT.JK", "IBST.JK", "MTEL.JK", "BALI.JK", "NICL.JK", 
    "DKFT.JK", "CITA.JK", "NICK.JK", "DOOH.JK", "HUMI.JK", "STRK.JK", "KEEN.JK", 
    "CUAN.JK", "PACK.JK", "TRUE.JK", "HILL.JK", "NSSS.JK", "MOLI.JK", "JGLE.JK", 
    "MPRO.JK", "AMMN.JK", "SAGE.JK"
]

# --- LOGIKA TOMBOL BSJP ---
if st.button("📈 BSJP — Beli Sore Jual Pagi"):
    with st.spinner("Memindai seluruh sektor untuk kandidat BSJP..."):
        bsjp_results = []
        for s in WATCHLIST:
            try:
                t = yf.Ticker(s)
                hist = t.history(period="1mo")
                if len(hist) >= 10:
                    close_today = hist['Close'].iloc[-1]
                    close_yesterday = hist['Close'].iloc[-2]
                    vol_today = hist['Volume'].iloc[-1]
                    change = ((close_today - close_yesterday) / close_yesterday) * 100
                    turnover = close_today * vol_today
                    supply_zone = hist['High'].max()
                    demand_zone = hist['Low'].min()
                    avg_vol = hist['Volume'].iloc[-6:-1].mean()
                    rvol = vol_today / avg_vol if avg_vol > 0 else 0
                    
                    if close_today <= 3000 and turnover >= 3_000_000_000 and (1.0 <= change <= 8.0) and rvol >= 1.5:
                        bsjp_results.append({
                            "Saham": s.replace(".JK", ""),
                            "Harga Closing": round(close_today, 2),
                            "Demand Zone": round(demand_zone, 2),
                            "Supply TP": round(supply_zone, 2)
                        })
            except:
                continue
        
        if bsjp_results:
            df_res = pd.DataFrame(bsjp_results).sort_values(by="Harga Closing", ascending=False)
            st.session_state.bsjp_df = df_res.head(5)
        else:
            st.session_state.bsjp_df = pd.DataFrame()

if st.session_state.bsjp_df is not None:
    if not st.session_state.bsjp_df.empty:
        st.success(f"Ditemukan {len(st.session_state.bsjp_df)} kandidat BSJP terbaik:")
        st.markdown("### 🎯 Rincian Trading Plan (BSJP)")
        for index, row in st.session_state.bsjp_df.iterrows():
            saham = row.get("Saham", "-")
            harga = row.get("Harga Closing", 0)
            demand = row.get("Demand Zone", 0)
            tp = row.get("Supply TP", 0)
            sl = round(demand * 0.98, 2)
            st.markdown(f"- **{saham}** (Harga: {harga}) ➡️ **Demand:** Rp {demand} | **TP:** Rp {tp} | **SL:** Rp {sl}")
    else:
        st.warning("Belum ada saham yang memenuhi kriteria kenaikan 1%-8% + Volume Spike untuk BSJP.")

# --- LOGIKA TOMBOL BPJS ---
if st.button("📉 BPJS — Beli Pagi Jual Siang/Sore"):
    with st.spinner("Memindai seluruh sektor untuk kandidat BPJS..."):
        bpjs_results = []
        for s in WATCHLIST:
            try:
                t = yf.Ticker(s)
                hist = t.history(period="1mo")
                if len(hist) >= 10:
                    close_price = hist['Close'].iloc[-1]
                    supply_zone = hist['High'].max()
                    demand_zone = hist['Low'].min()
                    avg_vol = hist['Volume'].iloc[-6:-1].mean()
                    vol_today = hist['Volume'].iloc[-1]
                    rvol = vol_today / avg_vol if avg_vol > 0 else 0
                    change = ((close_price - hist['Open'].iloc[-1]) / hist['Open'].iloc[-1]) * 100
                    turnover = close_price * vol_today
                    
                    if close_price <= 3000 and turnover >= 3_000_000_000 and (1.0 <= change <= 8.0) and rvol >= 1.5:
                        bpjs_results.append({
                            "Saham": s.replace(".JK", ""),
                            "Terakhir": round(close_price, 2),
                            "Demand Zone": round(demand_zone, 2),
                            "Supply TP": round(supply_zone, 2)
                        })
            except:
                continue
        
        if bpjs_results:
            df_res = pd.DataFrame(bpjs_results).sort_values(by="Terakhir", ascending=False)
            st.session_state.bpjs_df = df_res.head(5)
        else:
            st.session_state.bpjs_df = pd.DataFrame()

if st.session_state.bpjs_df is not None:
    if not st.session_state.bpjs_df.empty:
        st.success(f"Ditemukan {len(st.session_state.bpjs_df)} kandidat BPJS terbaik:")
        st.markdown("### 🎯 Rincian Trading Plan (BPJS)")
        for index, row in st.session_state.bpjs_df.iterrows():
            saham = row.get("Saham", "-")
            harga = row.get("Terakhir", 0)
            demand = row.get("Demand Zone", 0)
            tp = row.get("Supply TP", 0)
            sl = round(demand * 0.98, 2)
            st.markdown(f"- **{saham}** (Harga: {harga}) ➡️ **Demand:** Rp {demand} | **TP:** Rp {tp} | **SL:** Rp {sl}")
    else:
        st.warning("Belum ada saham yang memenuhi kriteria kenaikan 1%-8% untuk BPJS.")

# --- LOGIKA TOMBOL HAKA / BREAKOUT ---
if st.button("🚀 HAKA — Free Breakout Scanner"):
    with st.spinner("Memindai emiten potensial Breakout / HAKA..."):
        haka_results = []
        for s in WATCHLIST:
            try:
                t = yf.Ticker(s)
                hist = t.history(period="15d")
                if len(hist) >= 10:
                    close_today = hist['Close'].iloc[-1]
                    prev_supply = hist['High'].iloc[-10:-1].max()
                    vol_today = hist['Volume'].iloc[-1]
                    change = ((close_today - hist['Close'].iloc[-2]) / hist['Close'].iloc[-2]) * 100
                    turnover = close_today * vol_today
                    next_supply = round(close_today * 1.06, 2)
                    demand_zone = hist['Low'].min()
                    avg_vol = hist['Volume'].iloc[-10:-1].mean()
                    rvol = vol_today / avg_vol if avg_vol > 0 else 0
                    
                    if close_today <= 3000 and turnover >= 3_000_000_000 and close_today >= prev_supply and (1.0 <= change <= 8.0) and rvol >= 2.0:
                        haka_results.append({
                            "Saham": s.replace(".JK", ""),
                            "Harga Breakout": round(close_today, 2),
                            "Demand Zone": round(demand_zone, 2),
                            "Next Supply TP": next_supply
                        })
            except:
                continue
        
        if haka_results:
            df_res = pd.DataFrame(haka_results).sort_values(by="Harga Breakout", ascending=False)
            st.session_state.haka_df = df_res.head(5)
        else:
            st.session_state.haka_df = pd.DataFrame()

if st.session_state.haka_df is not None:
    if not st.session_state.haka_df.empty:
        st.success(f"Ditemukan {len(st.session_state.haka_df)} kandidat HAKA Breakout terbaik:")
        st.markdown("### 🎯 Rincian Trading Plan (HAKA Breakout)")
        for index, row in st.session_state.haka_df.iterrows():
            saham = row.get("Saham", "-")
            harga = row.get("Harga Breakout", 0)
            demand = row.get("Demand Zone", 0)
            tp = row.get("Next Supply TP", 0)
            sl = round(demand * 0.975, 2)
            st.markdown(f"- **{saham}** (Breakout: {harga}) ➡️ **Demand:** Rp {demand} | **TP:** Rp {tp} | **SL:** Rp {sl}")
    else:
        st.warning("Belum ada saham breakout dengan kenaikan 1%-8% saat ini.")

# --- LOGIKA TOMBOL SCALPING FAST TRADE ---
if st.button("⚡ SCALPING — Fast Trade Momentum Scanner"):
    with st.spinner("Memindai emiten scalping dengan volatilitas tinggi..."):
        scalp_results = []
        for s in WATCHLIST:
            try:
                t = yf.Ticker(s)
                hist = t.history(period="6d")
                if len(hist) >= 6:
                    close_today = hist['Close'].iloc[-1]
                    high_today = hist['High'].iloc[-1]
                    low_today = hist['Low'].iloc[-1]
                    vol_today = hist['Volume'].iloc[-1]
                    daily_range = ((high_today - low_today) / low_today) * 100
                    turnover = close_today * vol_today
                    demand_zone = hist['Low'].min()
                    avg_vol = hist['Volume'].iloc[-6:-1].mean()
                    rvol = vol_today / avg_vol if avg_vol > 0 else 0
                    
                    if close_today <= 3000 and turnover >= 3_000_000_000 and (3.0 <= daily_range <= 8.0) and rvol >= 1.8:
                        scalp_results.append({
                            "Saham": s.replace(".JK", ""),
                            "Harga Terakhir": round(close_today, 2),
                            "Demand Zone": round(demand_zone, 2),
                            "Supply TP": round(high_today, 2)
                        })
            except:
                continue
        
        if scalp_results:
            df_res = pd.DataFrame(scalp_results).sort_values(by="Harga Terakhir", ascending=False)
            st.session_state.scalp_df = df_res.head(5)
        else:
            st.session_state.scalp_df = pd.DataFrame()

if st.session_state.scalp_df is not None:
    if not st.session_state.scalp_df.empty:
        st.success(f"Ditemukan {len(st.session_state.scalp_df)} kandidat Scalping Fast Trade Pilihan:")
        st.markdown("### 🎯 Rincian Trading Plan (Scalping)")
        for index, row in st.session_state.scalp_df.iterrows():
            saham = row.get("Saham", "-")
            harga = row.get("Harga Terakhir", 0)
            demand = row.get("Demand Zone", 0)
            tp = row.get("Supply TP", 0)
            sl = round(demand * 0.985, 2)
            st.markdown(f"- **{saham}** (Harga: {harga}) ➡️ **Demand:** Rp {demand} | **TP:** Rp {tp} | **SL:** Rp {sl}")
    else:
        st.warning("Belum ada saham scalping dengan range 3%-8% saat ini.")

# --- LOGIKA TOMBOL SESI 2 SPIKE MOMENTUM ---
if st.button("🚀 SESI 2 — Spike & Momentum (Tiba-Tiba Naik)"):
    with st.spinner("Memindai emiten yang mengalami lonjakan mendadak di Sesi 2..."):
        sesi2_results = []
        for s in WATCHLIST:
            try:
                t = yf.Ticker(s)
                hist = t.history(period="4d")
                if len(hist) >= 4:
                    close_today = hist['Close'].iloc[-1]
                    open_today = hist['Open'].iloc[-1]
                    high_today = hist['High'].iloc[-1]
                    vol_today = hist['Volume'].iloc[-1]
                    intraday_spike = ((close_today - open_today) / open_today) * 100
                    turnover = close_today * vol_today
                    demand_zone = hist['Low'].min()
                    avg_vol = hist['Volume'].iloc[-4:-1].mean()
                    rvol = vol_today / avg_vol if avg_vol > 0 else 0
                    
                    if close_today <= 3000 and turnover >= 3_000_000_000 and (2.0 <= intraday_spike <= 8.0) and rvol >= 1.5:
                        sesi2_results.append({
                            "Saham": s.replace(".JK", ""),
                            "Harga Terakhir": round(close_today, 2),
                            "Demand Zone": round(demand_zone, 2),
                            "Supply TP": round(high_today * 1.03, 2)
                        })
            except:
                continue
        
        if sesi2_results:
            df_res = pd.DataFrame(sesi2_results).sort_values(by="Harga Terakhir", ascending=False)
            st.session_state.sesi2_df = df_res.head(5)
        else:
            st.session_state.sesi2_df = pd.DataFrame()

if st.session_state.sesi2_df is not None:
    if not st.session_state.sesi2_df.empty:
        st.success(f"Ditemukan {len(st.session_state.sesi2_df)} kandidat Sesi 2 Spike & Momentum:")
        st.markdown("### 🎯 Rincian Trading Plan (Sesi 2 Spike)")
        for index, row in st.session_state.sesi2_df.iterrows():
            saham = row.get("Saham", "-")
            harga = row.get("Harga Terakhir", 0)
            demand = row.get("Demand Zone", 0)
            tp = row.get("Supply TP", 0)
            sl = round(demand * 0.98, 2)
            st.markdown(f"- **{saham}** (Harga: {harga}) ➡️ **Demand:** Rp {demand} | **TP:** Rp {tp} | **SL:** Rp {sl}")
    else:
        st.warning("Belum ada emiten dengan lonjakan spike 2%-8% di Sesi 2 saat ini.")

# --- LOGIKA TOMBOL SUPPORT HUNTING (DENGAN DETEKSI AKUMULASI WHALE) ---
if st.button("🛡️ SUPPORT HUNTING — Deteksi Akumulasi Whale"):
    with st.spinner("Memindai emiten di area Demand Zone yang diakumulasi Whale..."):
        support_results = []
        for s in WATCHLIST:
            try:
                t = yf.Ticker(s)
                hist = t.history(period="1mo")
                if len(hist) >= 20:
                    close_today = hist['Close'].iloc[-1]
                    vol_today = hist['Volume'].iloc[-1]
                    turnover = close_today * vol_today
                    
                    demand_zone = hist['Low'].iloc[-20:].min()
                    supply_zone = hist['High'].iloc[-20:].max()
                    distance_to_demand = ((close_today - demand_zone) / demand_zone) * 100
                    
                    avg_vol_20 = hist['Volume'].iloc[-20:].mean()
                    avg_vol_5 = hist['Volume'].iloc[-5:-1].mean()
                    is_whale_accumulating = avg_vol_5 >= (avg_vol_20 * 1.2) and vol_today >= (avg_vol_20 * 0.9)
                    
                    if close_today <= 3000 and turnover >= 3_000_000_000 and (0 <= distance_to_demand <= 3.0) and is_whale_accumulating:
                        support_results.append({
                            "Saham": s.replace(".JK", ""),
                            "Harga Terakhir": round(close_today, 2),
                            "Demand Zone": round(demand_zone, 2),
                            "Supply TP": round(supply_zone, 2)
                        })
            except:
                continue
        
        if support_results:
            df_res = pd.DataFrame(support_results).sort_values(by="Harga Terakhir", ascending=True)
            st.session_state.support_df = df_res.head(5)
        else:
            st.session_state.support_df = pd.DataFrame()

if st.session_state.support_df is not None:
    if not st.session_state.support_df.empty:
        st.success(f"Ditemukan {len(st.session_state.support_df)} kandidat Saham dengan Indikasi Akumulasi Whale di Support:")
        st.markdown("### 🎯 Rincian Trading Plan (Support Akumulasi)")
        for index, row in st.session_state.support_df.iterrows():
            saham = row.get("Saham", "-")
            harga = row.get("Harga Terakhir", 0)
            demand = row.get("Demand Zone", 0)
            tp = row.get("Supply TP", 0)
            sl = round(demand * 0.975, 2)
            st.markdown(f"- **{saham}** (Harga: {harga}) ➡️ **Demand:** Rp {demand} | **TP:** Rp {tp} | **SL:** Rp {sl}")
    else:
        st.warning("Belum ada emiten yang menunjukkan pola akumulasi whale di area support saat ini.")

st.markdown("---")
st.markdown("### ⚙️ PENGATURAN API")
api_key = st.text_input("API Key", type="password", value="1234567890abcdef")
high_accuracy = st.toggle("Mode Akurasi Tinggi (50.000 simulasi MC)")
