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

# --- WATCHLIST KOMPREHENSIF SEKTOR ---
WATCHLIST = [
    # --- 1. PROPERTI & REAL ESTATE ---
    "PANI.JK", "BSDE.JK", "CTRA.JK", "PWON.JK", "SMRA.JK", "ASRI.JK", "LPKR.JK", 
    "DILD.JK", "BEST.JK", "DUTI.JK", "BKSL.JK", "KIJA.JK", "MMLP.JK", "GWSA.JK",

    # --- 2. KESEHATAN (Health) ---
    "SILO.JK", "HEAL.JK", "MIKA.JK", "KAEF.JK", "INAF.JK", "DVLA.JK", "PEHA.JK", "RSGK.JK",
    
    # --- 3. TEKNOLOGI, DIGITAL & KABEL ---
    "GOTO.JK", "BUKA.JK", "EMTK.JK", "MTDL.JK", "BELI.JK", "SCMA.JK", 
    "EXCL.JK", "ISAT.JK", "WIFI.JK", "AXIO.JK",
    
    # --- 4. BAHAN BAKU / BASIC MATERIALS ---
    "BRPT.JK", "TPIA.JK", "TKIM.JK", "INKP.JK", "IMPC.JK", "ESSA.JK", "NCKL.JK", 
    "MBMA.JK", "PSAB.JK", "DKHH.JK", "ANTM.JK", "INCO.JK", "MDKA.JK",
    
    # --- 5. ENERGI (Batubara, Migas, EBT & Jasa Energi) ---
    "BUMI.JK", "BRMS.JK", "DEWA.JK", "ENRG.JK", "ELSA.JK", "DOID.JK", "RAJA.JK", "PGEO.JK",
    "ADRO.JK", "PTBA.JK", "ITMG.JK", "HRUM.JK", "ADMR.JK", "MEDC.JK", "INDY.JK", "TOBA.JK", 
    "BSSR.JK", "BIPI.JK", "SGER.JK", "RMKE.JK", "IATA.JK", "COAL.JK", "SHIP.JK", "SOCI.JK", "TPMA.JK",
    
    # --- 6. TEKSTIL & GARMEN ---
    "ARGO.JK", "BELL.JK", "TRIS.JK", "POLU.JK", "SSTM.JK", "ERTX.JK", "ESTI.JK", "RICY.JK", "TFCO.JK", "PBRX.JK", "ADMG.JK",

    # --- 7. TRANSPORTASI, LOGISTIK & MARITIM ---
    "ASSA.JK", "BIRD.JK", "HAIS.JK", "PSSI.JK", "BBRM.JK", "GTSI.JK", "SMDR.JK", "TMAS.JK", "BOAT.JK",
    "LEAD.JK", "WINS.JK", "HITS.JK", "IPCC.JK",

    # --- 8. CONSUMER, RETAIL, KEUANGAN & MULTIFINANCE ---
    "ACES.JK", "ERAA.JK", "MAPI.JK", "MAPA.JK", "CMRY.JK", "SIDO.JK", "JPFA.JK", "CPIN.JK", "CLEO.JK", "MIDI.JK",
    "ARTO.JK", "BRIS.JK", "PNLF.JK", "BBYB.JK", "AGRO.JK", "BABP.JK", "CFIN.JK", "ADMF.JK", "WOMF.JK",
    "BANK.JK", "INPC.JK", "BBHI.JK", "MASB.JK", "BGTG.JK",

    # --- 9. PERKEBUNAN, CPO & PERTANIAN ---
    "TAPG.JK", "DSNG.JK", "SSMS.JK", "LSIP.JK", "AALI.JK", "PALM.JK", "BWPT.JK", "SIMP.JK", "SGRO.JK", "CSRA.JK",

    # --- 10. PERINDUSTRIAN & KOMPONEN OTOMOTIF ---
    "AUTO.JK", "DRMA.JK", "SMSM.JK", "BOLT.JK", "GJTL.JK", "IMAS.JK", "KBLI.JK", "VOKS.JK", "ARNA.JK", "MARK.JK",

    # --- 11. MEDIA & HIBURAN ---
    "TMPO.JK", "FILM.JK", "FORU.JK", "MARI.JK", "MNCN.JK", "BMTR.JK", "VIVA.JK",

    # --- 12. KONSTRUKSI SWASTA, KAWASAN INDUSTRI & INFRASTRUKTUR ---
    "ACST.JK", "TOTL.JK", "NRCA.JK", "PPRE.JK", "WEGE.JK", "IDPR.JK", "KBLM.JK",
    "SSIA.JK", "IPAC.JK", "MPXL.JK", "SAME.JK",

    # --- 13. KEMASAN, PLASTIK & DAUR ULANG ---
    "PBID.JK", "IPOL.JK", "FAPA.JK", "SOUL.JK", "TALF.JK", "KMTR.JK", "NPGF.JK",

    # --- 14. PETERNAKAN & PAKAN TERNAK (POULTRY) ---
    "MAIN.JK", "SIPD.JK", "WMUU.JK", "WMPP.JK",

    # --- 15. HOTEL, RESTORAN & PARIWISATA (HOREKA) ---
    "FAST.JK", "PZZA.JK", "PANR.JK", "BUVA.JK",

    # --- 16. HOLDING INVESTASI & ASURANSI ---
    "ABMM.JK", "ABDA.JK", "ASBI.JK", "AHAP.JK",

    # --- 17. INFRASTRUKTUR, DATA CENTER & MENARA ---
    "TOWR.JK", "TBIG.JK", "CENT.JK", "IBST.JK", "MTEL.JK", "BALI.JK",

    # --- 18. NIKEL, MINERAL KRITIS & EV ---
    "NICL.JK", "DKFT.JK", "CITA.JK", "NICK.JK",

    # --- HIGH VOLATILITY / GORENGAN SUPER AKTIF LAINNYA ---
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
                    change = ((close_today - close_yesterday) / close_yesterday) * 100
                    if change > 0:
                        bsjp_results.append({
                            "Saham": s,
                            "Harga Closing": round(close_today, 2),
                            "Kenaikan (%)": round(change, 2)
                        })
            except:
                continue
        
        if bsjp_results:
            st.success(f"Ditemukan {len(bsjp_results)} kandidat BSJP:")
            st.dataframe(pd.DataFrame(bsjp_results))
        else:
            st.warning("Belum ada saham yang memenuhi kriteria BSJP saat ini.")

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
            st.success(f"Ditemukan {len(bpjs_results)} kandidat BPJS:")
            st.dataframe(pd.DataFrame(bpjs_results))
        else:
            st.warning("Data BPJS belum tersedia.")

st.markdown("---")
st.subheader("⚙️ PENGATURAN API")
api_key = st.text_input("", type="password", value="1234567890abcdef")
high_accuracy = st.toggle("Mode Akurasi Tinggi (50.000 simulasi MC)")
