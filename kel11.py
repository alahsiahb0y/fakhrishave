import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random
import time
import pyperclip
import base64

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

            .typewriter {
            font-family: 'Minion ': inline-block;
            border-right: 2px solid #fff;
            padding-right: 2px;
            white-space: nowrap;
            overflow: hidden;
            animation: typing 2s steps(35) 1s 1 normal both, blink 5s step-end infinite;
        }

        @keyframes typing {
            from {
                width: 0;
            }
            to {
                width: 100%;
            }
        }

        @keyframes blink {
            1% {
                border-color: transparent;
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
    st.markdown("<h1 class='typewriter typing'>🌿 Antioxidant Calc 🌿</h1>", unsafe_allow_html=True)

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
    st.markdown("<h1 class=' typewriter title'>Select a Test Method</h1>", unsafe_allow_html=True)

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

with st.sidebar:
    # Sidebar Navigation
    if st.button("🏠 Home", use_container_width=True):
        set_page("Home")
    elif st.button("👤👤 About Us", use_container_width=True):
        set_page("About Us")
    elif st.button("☎ Contact", use_container_width=True):
        set_page("Contact")
    elif st.button("✈ Share Me", use_container_width=True):
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
    # Memberikan jarak antar elemen dengan menggunakan st.markdown() dan CSS
    st.markdown("<br>", unsafe_allow_html=True)  # Menambahkan jarak antar elemen

    # Fungsi untuk menyalin link ke clipboard
    def copy_to_clipboard():
        link = "https://fakhrishave-brhm5hpskxnzeapaxkrgwx.streamlit.app/"
        try:
            pyperclip.copy(link)  # Menyalin link ke clipboard
            st.session_state["copy_status"] = "Link berhasil disalin!"  # Menyimpan status
        except pyperclip.PyperclipException as e:
            st.session_state["copy_status"] = f"Terjadi kesalahan: {e}"  # Menyimpan pesan kesalahan

    # Inisialisasi status salinan jika belum ada
    if "copy_status" not in st.session_state:
        st.session_state["copy_status"] = ""

    st.title("Share Via Link")
    # Membuat layout dengan satu kolom
    with st.container():
        col1, col2 = st.columns([4, 1])  # Mengatur tata letak: teks link dan tombol
        with col1:
            # Menampilkan link
            st.markdown(
                '<div style="border: 2px solid #ff9933; padding: 10px; border-radius: 5px; background-color: #ff9933;">'
                '<a href="https://fakhrishave-brhm5hpskxnzeapaxkrgwx.streamlit.app/" '
                'target="_blank" style="font-size: 16px; color: #ffff; text-decoration: none;">'
                'https://fakhrishave-brhm5hpskxnzeapaxkrgwx.streamlit.app/</a>'
                '</div>', unsafe_allow_html=True,
            )
        with col2:
            # Menambahkan tombol "Salin Link"
            if st.button("Salin Link", key="copy_button", on_click=copy_to_clipboard):
                pass


    # Link aplikasi
    app_link = "https://fakhrishave-brhm5hpskxnzeapaxkrgwx.streamlit.app/"

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
    st.image("./barcode.jpg")

elif "ATOX.CALC-" in st.session_state.current_page:
    method = st.session_state.current_page.split("-")[1]
    atox_calc_page(method)

else:
    page_2()
