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
                hist = t.history(period="3d")
                if len(hist) >= 2:
                    close_today = hist['Close'].iloc[-1]
                    close_yesterday = hist['Close'].iloc[-2]
                    vol_today = hist['Volume'].iloc[-1]
                    
                    change = ((close_today - close_yesterday) / close_yesterday) * 100
                    
                    if change >= 1.5 and vol_today > 50000:
                        bsjp_results.append({
                            "Saham": s,
                            "Harga Closing": round(close_today, 2),
                            "Kenaikan (%)": round(change, 2),
                            "Volume": int(vol_today)
                        })
            except:
                continue
        
        if bsjp_results:
            st.session_state.bsjp_df = pd.DataFrame(bsjp_results).sort_values(by="Kenaikan (%)", ascending=False)
        else:
            st.session_state.bsjp_df = pd.DataFrame()

# Tampilkan hasil BSJP jika ada di memori
if st.session_state.bsjp_df is not None:
    if not st.session_state.bsjp_df.empty:
        st.success(f"Ditemukan {len(st.session_state.bsjp_df)} kandidat BSJP berkualitas:")
        st.dataframe(st.session_state.bsjp_df)
    else:
        st.warning("Belum ada saham yang memenuhi kriteria ketat BSJP saat ini.")

# --- LOGIKA TOMBOL BPJS ---
if st.button("📉 BPJS — Beli Pagi Jual Siang/Sore"):
    with st.spinner("Memindai seluruh sektor untuk kandidat BPJS..."):
        bpjs_results = []
        for s in WATCHLIST:
            try:
                t = yf.Ticker(s)
                hist = t.history(period="2d")
                if not hist.empty:
                    open_price = hist['Open'].iloc[-1]
                    close_price = hist['Close'].iloc[-1]
                    vol_today = hist['Volume'].iloc[-1]
                    
                    change = ((close_price - open_price) / open_price) * 100
                    
                    if change >= 1.0 and vol_today > 50000:
                        bpjs_results.append({
                            "Saham": s,
                            "Open Pagi": round(open_price, 2),
                            "Terakhir": round(close_price, 2),
                            "Est. Intraday (%)": round(change, 2),
                            "Volume": int(vol_today)
                        })
            except:
                continue
        
        if bpjs_results:
            st.session_state.bpjs_df = pd.DataFrame(bpjs_results).sort_values(by="Est. Intraday (%)", ascending=False)
        else:
            st.session_state.bpjs_df = pd.DataFrame()

# Tampilkan hasil BPJS jika ada di memori
if st.session_state.bpjs_df is not None:
    if not st.session_state.bpjs_df.empty:
        st.success(f"Ditemukan {len(st.session_state.bpjs_df)} kandidat BPJS berkualitas:")
        st.dataframe(st.session_state.bpjs_df)
    else:
        st.warning("Belum ada saham yang memenuhi kriteria ketat BPJS saat ini.")

st.markdown("---")
st.subheader("⚙️ PENGATURAN API")
api_key = st.text_input("", type="password", value="1234567890abcdef")
high_accuracy = st.toggle("Mode Akurasi Tinggi (50.000 simulasi MC)")
