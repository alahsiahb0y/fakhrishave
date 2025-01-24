import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random
import time
import pyperclip
import base64
import clipboard

# Configure the page layout
st.set_page_config(page_title="Antioxidant Calc", page_icon="🌿")

def random_color():
    return f"rgba({random.randint(0, 255)}, {random.randint(0, 255)}, {random.randint(0, 255)}, 1)"  # 0.5 untuk opacity
# Warna acak untuk background
background_color = random_color()

# CSS untuk lapisan background
st.markdown(
    f"""
    <style>
    .background {{
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(255, 128, 0, 0.95);
        z-index: 0; /* Letakkan di belakang konten lainnya */
    }}
    </style>
    <div class="background"></div>
    """,
    unsafe_allow_html=True
)

def set_background():
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&display=swap');

        html, body, [class*="css"] {
        font-family: 'Minion Pro', monospaces; /* Font monospaced */
        color: #ffff !important; /* Warna teks default */
        font-size: 16px !important; /* Ukuran font default */
        }

        /* Atur heading jika diperlukan */
        h1, h2, h3, h5, h6 {
        font-family: 'Minion Pro', monospaces !important;
        color: #ffff !important; /* Warna heading */
        }

        /* Mengubah font tombol */
        button {
        font-family: 'Minion Pro', monospaces !important;
        font-size: 14px !important;
        }


        div.stNumberInput > div > input {
        background-color: #f0f8ff !important; /* Warna latar belakang */
        color: #000080 !important;          /* Warna teks */
        border: 2px solid #000080 !important; /* Warna border */
        border-radius: 5px !important;      /* Radius border */
        padding: 5px !important;            /* Padding */
        font-size: 16px !important;         /* Ukuran font */
        }

        .bordered-text {
            border: 10px solid #ffff;  /* Warna border (merah-oranye) */
            padding: 10px;              /* Jarak antara teks dan border */
            border-radius: 20px;         /* Sudut border yang melengkung */
            font-size: 5;            /* Ukuran font */
            color: #ffff;                /* Warna teks */
        }
        
        .typing {
                font-family: 'Minion Pro', monospaces monospace;
                white-space: normal;  /* Mengizinkan teks untuk membungkus ke baris berikutnya */
                word-wrap: break-word; /* Memastikan kata yang terlalu panjang terpotong dan dibungkus */
                overflow: hidden;

            }

        /* Background gradient */
        .stApp {
            background: linear-gradient(135deg, #f5f7fa, #c3cfe2);
            font-family: 'Minion Pro', monospaces monospace;
            text-align: center;
            color: #ffff
        }

        

        /* Sidebar */
        [data-testid="stSidebar"] {
            background-color: rgba(255, 153, 51, 1) !important; /* Warna oranye dengan transparansi % */
    }

        /* Button */
        .stButton > button {
            background-color: #ff9933 !important; /* Warna latar belakang default */
            color: #ffff !important;             /* Warna teks default */
            border: 3px solid #ffff !important; /* Warna border default */
            padding: 10px 24px;
            font-weight: bold;
            border-radius: 10px;
            font-size: 16px;
            cursor: pointer;
            transition: background-color 0.2s, color 0.2s; /* Efek transisi */
        }

                /* Gaya tombol saat hover */
        button:hover {
            background-color: #ffff !important;  /* Warna latar belakang saat hover */
            color: #ff9933 !important;          /* Warna teks saat hover */
            border: 3px solid #ff9933 !important; /* Border tetap saat hover */
        }

        /* Card Box */
        .info-box {
            background-color: #edf2f4;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);
            margin-bottom: 20px;
        }

        /* Image Style */
        .stImage > img {
            border-radius: 10px;
            box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.3);
        }

        }
        </style>
        """,
        unsafe_allow_html=True
    )

# --- Terapkan Background ---
set_background()

# Membuat header dengan logo di kanan atas dan teks di kiri
with st.container():
    col1, col2 = st.columns([14, 2])  # Membagi halaman menjadi dua kolom (5:1)

    with col1:
        # Teks di kiri
        st.write("""
        <div style="font-family: 'Minion Pro', monospaces monospace; margin-top: -20px; text-align: right;">
            <p style="font-weight: bold; margin: 0px; font-size: 24px; line-height: 1;">Politeknik AKA Bogor</p>
            <p style="margin: 0px; font-size: 22px; line-height: 1; margin-top: 10px; color: #ffff; ">D-IV Nanoteknologi Pangan</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        # Fungsi untuk mengonversi gambar menjadi base64
        def image_to_base64(image_path):
            with open(image_path, "rb") as image_file:
                return base64.b64encode(image_file.read()).decode("utf-8")

        # Konversi gambar lokal
        image_base64 = image_to_base64("aka1.png")

        # Gunakan base64 di dalam HTML
        st.markdown(
            f"""
            <div style="text-align: right; margin-top: -35px;">
                <img src="data:image/png;base64,{image_base64}" 
                    alt="Logo Politeknik AKA Bogor" style="width: 500px !important; height: auto">
            </div>
            """,
            unsafe_allow_html=True,
        )

image_url = "https://indonesiacollege.co.id/blog/wp-content/uploads/2022/10/jurusan-politeknik-aka-bogor.jpg"

# CSS untuk mengatur gambar sebagai background
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url('{image_url}');
        background-size: cover;
        background-position: center;
        height: 100vh;
    }}
    </style>
    """, 
    unsafe_allow_html=True
)

# Initialize session state if not already done
if "current_page" not in st.session_state:
    st.session_state.current_page = "home"

def set_page(page_name):
    st.session_state.current_page = page_name

def home():
    st.markdown("<h1 class=' typing'>🌿 Antioxidant Calc 🌿</h1>", unsafe_allow_html=True)

    if st.button("Start to Calculate", key="start_button", use_container_width=True):
        st.session_state.current_page = "page 2"

    st.write("""
<div class="typing bordered-text">
        Antioksidan adalah suatu zat yang dapat melindungi senyawa kimia dalam tubuh dari oksidasi yang dapat merusak dengan cara bereaksi dengan radikal bebas dan spesi oksigen reaktif, sehingga dapat menghambat oksidasi. Antioksidan juga disebut sebagai scavenger (zat/peredam) radikal bebas dan dapat menetralkan radikal bebas. Antioksidan sebagai senyawa yang dapat menonaktifkan radikal bebas dengan 
        menggunakan dua mekanisme utama yaitu Hidrogen Atom Transfer (HAT) dan 
        Single Electron Transfer (SET). Kedua mekanisme tersebut menjadi dasar metode
        pengujian antioksidan.
        Metode HAT mengukur kemampuan antioksidan untuk meredam radikal bebas dengan 
        sumbangan hidrogen (donor proton), Metode SET mengukur kemampuan antioksidan 
        untuk mereduksi radikal bebas melalui transfer elektron tunggal. Sedangkan pada
        mekanisme SET, antioksidan mendonasikan satu elektron ke radikal bebas sehingga
        radikal bebas menjadi netral dan stabil. Proses ini mencegah radikal bebas 
        merusak molekul biologis seperti lipid, protein, dan DNA.
    </div>
    """, unsafe_allow_html=True)

def page_2():
    st.markdown("""<style>.title {color: pink; text-align: center; font-size: 40px;} .custom-button {background-color: #32CD32; color: white; border: 1px solid white; border-radius: 10px; padding: 10px 20px; cursor: pointer; display: inline-block;} .custom-button:hover {background-color: #ffff;} .center-content {text-align: center;}</style>""", unsafe_allow_html=True)
    st.markdown("<h1 class='  title'>Select a Test Method</h1>", unsafe_allow_html=True)

    test_methods = ["ORAC", "TRAP", "LPIC", "FRAP", "TEAC", "DPPH", "CUPRAC", "ABTS"]
    cols = st.columns(4)
    for i, method in enumerate(test_methods):
        with cols[i % 4]:
            if st.button(method, key=method, use_container_width=True):
                st.session_state.current_page = f"ATOX.CALC-{method}"
    st.markdown("<br><br>", unsafe_allow_html=True)
    if st.button("Back to Menu", use_container_width=True):
        set_page("Home")

def atox_calc_page(method):
    if method == "DPPH":
            
        blank = st.number_input("Input blanko", format="%.6f")
        num_samples = st.number_input("Berapa banyak sampel ingin diuji", min_value=2, step=1)

        if num_samples > 0:
            st.write("Masukkan konsentrasi (ppm) dan absorbansi untuk setiap sampel")
            cols = st.columns(2)
            concentrations = []
            absorbances = []
            for i in range(num_samples):
                with cols[0]:
                    concentrations.append(st.number_input(f"Input konsentrasi (ppm) sampel {i+1}", format="%.2f"))
                with cols[1]:
                    absorbances.append(st.number_input(f"Input absorbansi sampel {i+1}", format="%.6f"))

            # Calculate % inhibition and other results
            if st.button("Calculate"):
                results = pd.DataFrame({
                    "Konsentrasi (ppm)": concentrations,
                    "% Inhibisi": [(1 - a/blank)*100 if blank != 0 else 0 for a in absorbances]
                })
                st.table(results)
               
                # Linear regression
                coefficients = np.polyfit(concentrations, results["% Inhibisi"], 1)
                slope, intercept = coefficients
                regression_eq = f"y = {slope:.6f}x {'+' if intercept >= 0 else '-'} {abs(intercept):.6f}"

                # Calculate predicted values
                predicted1 = slope * np.array(concentrations) + intercept

                # Calculate R²
                ss_res = np.sum((results["% Inhibisi"] - predicted1) ** 2)
                ss_tot = np.sum((results["% Inhibisi"] - np.mean(results["% Inhibisi"])) ** 2)
                r_squared = 1 - (ss_res / ss_tot)

                # Linear regression
                coefficients = np.polyfit(concentrations, results["% Inhibisi"], 1)
                slope, intercept = coefficients
                regression_eq = f"y = {slope:.6f}x {'+' if intercept >= 0 else '-'} {abs(intercept):.6f}"
                st.markdown(f"""<h2 class='typing bordered-text'>
                            {regression_eq}
                            <br>
                            R^2 = {r_squared:.4f}
                            </h2>""", unsafe_allow_html=True)
                st.markdown("<br>", unsafe_allow_html=True)

                # Graph
                fig, ax = plt.subplots()
                ax.plot(concentrations, results["% Inhibisi"], 'o-', label="Data Points")
                ax.plot(concentrations, slope * np.array(concentrations) + intercept, '-', label="Regresi")
                ax.set_xlabel("Konsentrasi (ppm)")
                ax.set_ylabel("% Inhibisi")
                ax.legend()
                st.pyplot(fig)

                # Display IC50 value
                ic50 = (50 -intercept) / slope if slope != 0 else None
                if ic50:
                    st.markdown(f"<h2 class='typing bordered-text'>IC50 Value: {ic50:.6f} ppm</h2>", unsafe_allow_html=True)
                else:
                    st.markdown("**IC50 Value:** Tidak dapat dihitung.")
        st.markdown("<br><br>", unsafe_allow_html=True)
        if st.button("Back to Menu", use_container_width=True):
            set_page("Home")

    elif method == "FRAP":
        st.markdown("<h1 style='color: #FF3333; text-align: center;'>FRAP</h1>", unsafe_allow_html=True)
        blank = st.number_input("Input blanko", format="%.6f")
        num_samples = st.number_input("Berapa banyak sampel ingin diuji", min_value=2, step=1)

        if num_samples > 0:
            st.write("Masukkan konsentrasi (ppm) dan absorbansi untuk setiap sampel")
            cols = st.columns(2)
            concentrations = []
            absorbances = []
            for i in range(num_samples):
                with cols[0]:
                    concentrations.append(st.number_input(f"Input konsentrasi (ppm) sampel {i+1}", format="%.6f"))
                with cols[1]:
                    absorbances.append(st.number_input(f"Input absorbansi sampel {i+1}", format="%.6f"))

            # Calculate % reducing power and other results
            if st.button("Calculate"):
                results = pd.DataFrame({
                    "Konsentrasi (ppm)": concentrations,
                    "% Reducing Power": [(1 - (blank / a)) * 100 if blank != 0 else 0 for a in absorbances]
                })
                st.table(results)

                # Linear regression
                coefficients = np.polyfit(concentrations, results["% Reducing Power"], 1)
                slope, intercept = coefficients
                regression_eq = f"y = {slope:.6f}x {'+' if intercept >= 0 else '-'} {abs(intercept):.6f}"

                # Calculate predicted values
                predicted = slope * np.array(concentrations) + intercept

                # Calculate R²
                ss_res = np.sum((results["% Reducing Power"] - predicted) ** 2)
                ss_tot = np.sum((results["% Reducing Power"] - np.mean(results["% Reducing Power"])) ** 2)
                r_squared = 1 - (ss_res / ss_tot)

                # Linear regression
                coefficients = np.polyfit(concentrations, results["% Reducing Power"], 1)
                slope, intercept = coefficients
                regression_eq = f"y = {slope:.6f}x {'+' if intercept >= 0 else '-'} {abs(intercept):.6f}"
                st.markdown(f"""<h2 class='typing bordered-text'>
                            {regression_eq}
                            <br>
                            R^2 = {r_squared:.4f}
                            </h2>""", unsafe_allow_html=True)

                # Graph
                fig, ax = plt.subplots()
                ax.plot(concentrations, results["% Reducing Power"], 'o-', label="Data Points")
                ax.plot(concentrations, slope * np.array(concentrations) + intercept, '-', label="Regresi")
                ax.set_xlabel("Konsentrasi (ppm)")
                ax.set_ylabel("% Reducing Power")
                ax.legend()
                st.pyplot(fig)

                # Display EC50 value
                ec50 = (50 - intercept) / slope if slope != 0 else None
                if ec50:
                    st.markdown(f"<h2 class='typing bordered-text'>EC50 Value: {ec50:.6f} ppm </h2>", unsafe_allow_html=True)
                else:
                    st.markdown("**EC50 Value:** Tidak dapat dihitung.")
        st.markdown("<br><br>", unsafe_allow_html=True)
        if st.button("Back to Menu", use_container_width=True):
            set_page("Home")

    elif method == "ORAC":
        st.markdown(
            """<div style="text-align: center;">
                <p>Kalkulator Hadir Pada 30/Januari/2025.</p>
                <span style="font-size: 50px;">😓</span>
            </div>""",
            unsafe_allow_html=True,
        )

        # Link ke Google Calendar
        google_calendar_link = (
            "https://calendar.google.com/calendar/render?action=TEMPLATE"
            "&text=Pengingat+Kalkulator+ORAC"  # Judul acara
            "&details=Jangan+lupa+gunakan+kalkulator+ORAC+pada+tanggal+30+Januari+2025!"  # Detail acara
            "&dates=20250130T000000Z/20250130T235900Z"  # Tanggal mulai dan selesai (UTC)
        )

        # Tombol untuk langsung membuka Google Calendar
        st.markdown(
            f"""
            <a href="{google_calendar_link}" target="_blank">
                <button style="padding: 10px 20px; font-size: 16px; color: white; background-color: #ff9933; border: solid #ffff; border-radius: 10px; cursor: pointer;">
                    Set Pengingat di Google Calendar
                </button>
            </a>
            """,
            unsafe_allow_html=True,
        )
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Back to Menu"):
            set_page("Home")

    elif method == "TRAP":
        st.markdown(
            """<div style="text-align: center;">
                <p>Kalkulator Hadir Pada 15/Februari/2025.</p>
                <span style="font-size: 50px;">😓</span>
            </div>""",
            unsafe_allow_html=True,
        )

        # Link ke Google Calendar
        google_calendar_link = (
            "https://calendar.google.com/calendar/render?action=TEMPLATE"
            "&text=Pengingat+Kalkulator+TRAP"  # Judul acara
            "&details=Jangan+lupa+gunakan+kalkulator+TRAP+pada+tanggal+15+Februari+2025!"  # Detail acara
            "&dates=20250215T000000Z/20250215T235900Z"  # Tanggal mulai dan selesai (UTC)
        )

        # Tombol untuk langsung membuka Google Calendar
        st.markdown(
            f"""
            <a href="{google_calendar_link}" target="_blank">
                <button style="padding: 10px 20px; font-size: 16px; color: white; background-color: #ff9933; border: solid #ffff; border-radius: 10px; cursor: pointer;">
                    Set Pengingat di Google Calendar
                </button>
            </a>
            """,
            unsafe_allow_html=True,
        )
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Back to Menu"):
            set_page("Home")

    elif method == "LPIC":
        st.markdown(
            """<div style="text-align: center;">
                <p>Kalkulator Hadir Pada 28/Februari/2025.</p>
                <span style="font-size: 50px;">😓</span>
            </div>""",
            unsafe_allow_html=True,
        )

        # Link ke Google Calendar
        google_calendar_link = (
            "https://calendar.google.com/calendar/render?action=TEMPLATE"
            "&text=Pengingat+Kalkulator+LPIC"  # Judul acara
            "&details=Jangan+lupa+gunakan+kalkulator+LPIC+pada+tanggal+28+Februari+2025!"  # Detail acara
            "&dates=20250228T000000Z/20250228T235900Z"  # Tanggal mulai dan selesai (UTC)
        )

        # Tombol untuk langsung membuka Google Calendar
        st.markdown(
            f"""
            <a href="{google_calendar_link}" target="_blank">
                <button style="padding: 10px 20px; font-size: 16px; color: white; background-color: #ff9933; border: solid #ffff; border-radius: 10px; cursor: pointer;">
                    Set Pengingat di Google Calendar
                </button>
            </a>
            """,
            unsafe_allow_html=True,
        )
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Back to Menu"):
            set_page("Home")

    elif method == "TEAC":
        st.markdown(
            """<div style="text-align: center;">
                <p>Kalkulator Hadir Pada 15/Maret/2025.</p>
                <span style="font-size: 50px;">😓</span>
            </div>""",
            unsafe_allow_html=True,
        )

        # Link ke Google Calendar
        google_calendar_link = (
            "https://calendar.google.com/calendar/render?action=TEMPLATE"
            "&text=Pengingat+Kalkulator+TEAC"  # Judul acara
            "&details=Jangan+lupa+gunakan+kalkulator+TEAC+pada+tanggal+15+Maret+2025!"  # Detail acara
            "&dates=20250315T000000Z/20250315T235900Z"  # Tanggal mulai dan selesai (UTC)
        )

        # Tombol untuk langsung membuka Google Calendar
        st.markdown(
            f"""
            <a href="{google_calendar_link}" target="_blank">
                <button style="padding: 10px 20px; font-size: 16px; color: white; background-color: #ff9933; border: solid #ffff; border-radius: 10px; cursor: pointer;">
                    Set Pengingat di Google Calendar
                </button>
            </a>
            """,
            unsafe_allow_html=True,
        )
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Back to Menu"):
            set_page("Home")

    elif method == "CUPRAC":
        st.markdown(
            """<div style="text-align: center;">
                <p>Kalkulator Hadir Pada 30/Maret/2025.</p>
                <span style="font-size: 50px;">😓</span>
            </div>""",
            unsafe_allow_html=True,
        )

        # Link ke Google Calendar
        google_calendar_link = (
            "https://calendar.google.com/calendar/render?action=TEMPLATE"
            "&text=Pengingat+Kalkulator+CUPRAC"  # Judul acara
            "&details=Jangan+lupa+gunakan+kalkulator+CUPRAC+pada+tanggal+30+Maret+2025!"  # Detail acara
            "&dates=20250330T000000Z/20250330T235900Z"  # Tanggal mulai dan selesai (UTC)
        )

        # Tombol untuk langsung membuka Google Calendar
        st.markdown(
            f"""
            <a href="{google_calendar_link}" target="_blank">
                <button style="padding: 10px 20px; font-size: 16px; color: white; background-color: #ff9933; border: solid #ffff; border-radius: 10px; cursor: pointer;">
                    Set Pengingat di Google Calendar
                </button>
            </a>
            """,
            unsafe_allow_html=True,
        )
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Back to Menu"):
            set_page("Home")

    elif method == "ABTS":
        st.markdown(
            """<div style="text-align: center;">
                <p>Kalkulator Hadir Pada 15/April/2025.</p>
                <span style="font-size: 50px;">😓</span>
            </div>""",
            unsafe_allow_html=True,
        )

        # Link ke Google Calendar
        google_calendar_link = (
            "https://calendar.google.com/calendar/render?action=TEMPLATE"
            "&text=Pengingat+Kalkulator+ABTS"  # Judul acara
            "&details=Jangan+lupa+gunakan+kalkulator+ABTS+pada+tanggal+15+April+2025!"  # Detail acara
            "&dates=20250415T000000Z/20250415T235900Z"  # Tanggal mulai dan selesai (UTC)
        )

        # Tombol untuk langsung membuka Google Calendar
        st.markdown(
            f"""
            <a href="{google_calendar_link}" target="_blank">
                <button style="padding: 10px 20px; font-size: 16px; color: white; background-color: #ff9933; border: solid #ffff; border-radius: 10px; cursor: pointer;">
                    Set Pengingat di Google Calendar
                </button>
            </a>
            """,
            unsafe_allow_html=True,
        )
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Back to Menu"):
            set_page("Home")



    else:
        st.markdown("""<div style="text-align: center;">
                        <p>Kalkulator sedang dalam pengembangan.</p>
                        <span style="font-size: 50px;">😓</span>
                      </div>""", unsafe_allow_html=True)
        if st.button("Back to Menu"):
            set_page("Home")


contact_1 = """
<div style="display: flex; align-items: center;">
    <img src="https://portal-uang.com/wp-content/uploads/2021/06/Logo-WhatsApp-Transparan-810x540.png" width="55" height="40" style="margin-right: 10px;">
    <span><strong>Anargya Cinta Ismoyo</strong> +62 896-8490-0503</span>
</div>
"""
contact_2 = """
<div style="display: flex; align-items: center;">
    <img src="https://portal-uang.com/wp-content/uploads/2021/06/Logo-WhatsApp-Transparan-810x540.png" width="55" height="40" style="margin-right: 10px;">
    <span><strong>Muhammad Fakhri Al-Fathi</strong> +62 857-7032-0514</span>
</div>
"""
contact_3 = """
<div style="display: flex; align-items: center;">
    <img src="https://portal-uang.com/wp-content/uploads/2021/06/Logo-WhatsApp-Transparan-810x540.png" width="55" height="40" style="margin-right: 10px;">
    <span><strong>Nabila Azizi Rohmah</strong> +62 898-7065-411</span>
</div>
"""
contact_4 = """
<div style="display: flex; align-items: center;">
    <img src="https://portal-uang.com/wp-content/uploads/2021/06/Logo-WhatsApp-Transparan-810x540.png" width="55" height="40" style="margin-right: 10px;">
    <span><strong>Pinkan Regina Ayu Maharani</strong> +62 856-9235-6848</span>
</div>
"""
contact_5 = """
<div style="display: flex; align-items: center;">
    <img src="https://portal-uang.com/wp-content/uploads/2021/06/Logo-WhatsApp-Transparan-810x540.png" width="55" height="40" style="margin-right: 10px;">
    <span><strong>Syifa Ahista Maharani</strong> +62 878-8730-4171</span>
</div>
"""

# Main App Logic

def set_page(page):
    st.session_state["current_page"] = page

# Inisialisasi state jika belum ada
if "current_page" not in st.session_state:
    st.session_state["current_page"] = "Home"  # Halaman default

# Sidebar dengan navigasi
with st.sidebar:
    
    if st.button("🏠 Home", use_container_width=True):
        set_page("Home")
    if st.button("👤👤 About Us", use_container_width=True):
        set_page("About Us")
    if st.button("☎ Contact", use_container_width=True):
        set_page("Contact")
    if st.button("✈ Share Me", use_container_width=True):
        set_page("Share Me")

if st.session_state.current_page == "Home":
    home()

elif st.session_state.current_page == "About Us":
    st.title("About Us")
    html_code = """
            <style>
                .profile-pic {
                    border: 5px solid white;
                    border-radius: 15px;
                    width: 150px;
                    height: 150px;
                    object-fit: cover;
                }
            </style>
        """
    
        # Menampilkan HTML dan CSS
    st.markdown(html_code, unsafe_allow_html=True)

    # Daftar nama dan foto
    col1, col2, col3, col4, col5 = st.columns(5)

    # Menampilkan gambar dan teks di kolom pertama
    with col1:
        st.image("cinta1.jpg", width=150)
        st.write("Anargya Cinta Ismoyo <br>As A <br><b style='font-weight:900'>QA Engineer & Algorithm Engineer</b>", unsafe_allow_html=True)

    # Menampilkan gambar dan teks di kolom kedua
    with col2:
        st.image("fakhri1.jpg", width=150)
        st.write("Muhammad Fakhri Al-Fathi <br>As A <br><b style='font-weight:900'>Full-stack Developer, DevOps Engineer, & Machine Learning Engineer</b>", unsafe_allow_html=True)

    # Menampilkan gambar dan teks di kolom ketiga
    with col3:
        st.image("bilzi1.jpg", width=150)
        st.write("Nabila Azizi Rohmah <br>As A <br><b style='font-weight:900'>Fronted Developer & QA Engineer</b>", unsafe_allow_html=True)

    # Menampilkan gambar dan teks di kolom keempat
    with col4:
        st.image("pinkan1.jpg", width=150)
        st.write("Pinkan Regina Ayu Maharani <br>As A <br><b style='font-weight:900'>Fronted Developer, Beckend Developer, & DevOps Engineer</b>", unsafe_allow_html=True)

    # Menampilkan gambar dan teks di kolom kelima
    with col5:
        st.image("tata1.jpg", width=150)
        st.write("Syifa Ahista Maharani <br>As A <br><b style='font-weight:900'>Mobile Developer & Software Architect</b>", unsafe_allow_html=True)     

elif st.session_state.current_page == "Contact":
    st.title("Contact")    
    # Menampilkan daftar kontak di aplikasi
    st.markdown(contact_1, unsafe_allow_html=True)
    st.markdown(contact_2, unsafe_allow_html=True)
    st.markdown(contact_3, unsafe_allow_html=True)
    st.markdown(contact_4, unsafe_allow_html=True)
    st.markdown(contact_5, unsafe_allow_html=True)

elif st.session_state.current_page == "Share Me":
    # Contoh penggunaan
    link = "https://fakhrishave-hlqgha2kkfbevzxwxtm3fq.streamlit.app/"
    st.title("Share Via Link:")
    
    # Tampilkan link sebagai kode (agar pengguna bisa menyalin manual)
    st.code(link)
    
    # Sediakan tombol untuk mengunduh link sebagai file teks
    st.download_button(
        label="Unduh Link",
        data=link,
        file_name="fallback_link.txt",
        mime="text/plain"
    )

    # Tombol untuk membagikan link
    st.title("Share Via WhatsApp")

    # Link aplikasi dan pesan
    app_link = "https://fakhrishave-brhm5hpskxnzeapaxkrgwx.streamlit.app/"
    wa_message = f"Check out this Antioxidant Calculator: {app_link}"
    wa_url = f"https://wa.me/?text={wa_message}"  # WhatsApp API URL

    # Tombol langsung membuka WhatsApp
    if st.button("Bagikan Link ke WhatsApp"):
        # Script untuk langsung membuka WhatsApp
        js_code = f"""
        <script>
            window.open('{wa_url}', '_blank');
        </script>
        """
        st.components.v1.html(js_code, height=0)



    st.title("Share Via Barcode")
    st.image("./brcd.jpg")

elif "ATOX.CALC-" in st.session_state.current_page:
    method = st.session_state.current_page.split("-")[1]
    atox_calc_page(method)

else:
    page_2()
