import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random

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
        background-color: rgba(255, 128, 0, 0.7);
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
        html, body, [class*="css"] {
        font-family: 'Consolas', 'Courier New', monospace !important; /* Font monospaced */
        color: #ffff !important; /* Warna teks default */
        font-size: 16px !important; /* Ukuran font default */
        }

        /* Atur heading jika diperlukan */
        h1, h2, h3, h4, h5, h6 {
        font-family: 'Consolas', 'Courier New', monospace !important;
        color: #ffff !important; /* Warna heading */
        }

        /* Mengubah font tombol */
        button {
        font-family: 'Consolas', 'Courier New', monospace !important;
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
            font-size: 20px;            /* Ukuran font */
            color: #ffff;                /* Warna teks */
        }
        
        .typing {
                font-family: 'Consolas', 'Courier New', monospace;
                white-space: normal;  /* Mengizinkan teks untuk membungkus ke baris berikutnya */
                word-wrap: break-word; /* Memastikan kata yang terlalu panjang terpotong dan dibungkus */
                overflow: hidden;

            }

        /* Background gradient */
        .stApp {
            background: linear-gradient(135deg, #f5f7fa, #c3cfe2);
            font-family: 'Consolas', 'Courier New', monospace;
            text-align: center;
            color: #ffff
        }

        /* Sidebar */
        [data-testid="stSidebar"] {
            background-color: rgba(255, 153, 51, 0.5) !important; /* Warna oranye dengan transparansi 80% */
    }

        /* Button */
        .stButton > button {
            background-color: #ffff !important; /* Warna latar belakang default */
            color: #ff9933 !important;             /* Warna teks default */
            border: 3px solid #ff9933 !important; /* Warna border default */
            padding: 10px 24px;
            font-weight: bold;
            border-radius: 10px;
            font-size: 16px;
            cursor: pointer;
            transition: background-color 0.2s, color 0.2s; /* Efek transisi */
        }

        /* Gaya tombol saat hover */
        button:hover {
            background-color: #ff9933 !important;  /* Warna latar belakang saat hover */
            color: #ffff !important;          /* Warna teks saat hover */
            border: 3px solid #ffff !important; /* Border tetap saat hover */
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
        </style>
        """,
        unsafe_allow_html=True
    )

# --- Terapkan Background ---
set_background()

# Membuat header dengan logo di kanan atas dan teks di kiri
with st.container():
    col1, col2 = st.columns([14, 1])  # Membagi halaman menjadi dua kolom (5:1)

    with col1:
        # Teks di kiri
        st.write("""
        <div style="font-family: 'Consolas', 'Courier New', monospace; margin-top: -50px; text-align: right;">
            <h1 style="font-weight: bold; margin: 0px; font-size: 24px; line-height: 1;">Politeknik AKA Bogor</h1>
            <p style="margin: 0px; font-size: 18px; line-height: 1; margin-top: -10px; color: #ffff; ">D-IV Nanoteknologi Pangan</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        # Logo di kanan atas tanpa ikon rantai
        st.write("""
        <div style="text-align: right; margin-top: -25px;">
            <img src="https://1.bp.blogspot.com/-I8f-TbrhPeQ/WFd0_c1VaJI/AAAAAAAAAgE/_aPhNqeAR0QV1yphTw69HC4rC4KxUKLFwCLcB/s1600/logo%2BAKA%2BBogor.jpg" 
                 alt="Logo Politeknik AKA Bogor" style="width: 90px;">
        </div>
        """, unsafe_allow_html=True)

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
    st.session_state.current_page = "Home"

def set_page(page_name):
    st.session_state.current_page = page_name

# Sidebar Navigation
if st.sidebar.button("🏠 Home", use_container_width=True):
    st.session_state.current_page = "Home"
elif st.sidebar.button("🧮 About Us", use_container_width=True):
    st.session_state.current_page = "About Us"
elif st.sidebar.button("🔍 Contact", use_container_width=True):
    st.session_state.current_page = "Contact"



def home():
    st.markdown("""<style>.title {color: pink; text-align: center; font-size: 40px;} .custom-button {background-color: #32CD32; color: white; border: 1px solid white; border-radius: 10px; padding: 10px 20px; cursor: pointer; display: inline-block;} .custom-button:hover {background-color: #ffff;} .center-content {text-align: center;}</style>""", unsafe_allow_html=True)
    st.markdown("<h1 class='typing'>🌿 Antioxidant Calc 🌿</h1>", unsafe_allow_html=True)

    if st.button("Start to Calculate", key="start_button", use_container_width=True):
        st.session_state.current_page = "Page 2"

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
    st.markdown("""<style>.title {color: pink; text-align: center; font-size: 40px;} .custom-button {background-color: #32CD32; color: white; border: 1px solid white; border-radius: 10px; padding: 10px 20px; cursor: pointer; display: inline-block;} .custom-button:hover {background-color: #28a745;} .center-content {text-align: center;}</style>""", unsafe_allow_html=True)
    st.markdown("<h1 class='title'>Select a Test Method</h1>", unsafe_allow_html=True)

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
        st.markdown("<h1 style='color: #330066; text-align: center;'>DPPH</h1>", unsafe_allow_html=True)
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
                st.markdown(f"**Persamaan Regresi:** {regression_eq}")

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
                    st.markdown(f"**IC50 Value:** {ic50:.6f} ppm")
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
                st.markdown(f"**Persamaan Regresi:** {regression_eq}")

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
                    st.markdown(f"**EC50 Value:** {ec50:.6f} ppm")
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
    <span><strong>Muhammad Fakhri Al-Fathi</strong> +62 857-7032-0514</span>
</div>
"""
contact_2 = """
<div style="display: flex; align-items: center;">
    <img src="https://portal-uang.com/wp-content/uploads/2021/06/Logo-WhatsApp-Transparan-810x540.png" width="55" height="40" style="margin-right: 10px;">
    <span><strong>Nabila Azizi Rohmah</strong> +62 898-7065-411</span>
</div>
"""
contact_3 = """
<div style="display: flex; align-items: center;">
    <img src="https://portal-uang.com/wp-content/uploads/2021/06/Logo-WhatsApp-Transparan-810x540.png" width="55" height="40" style="margin-right: 10px;">
    <span><strong>Pinkan Regina Ayu Maharani</strong> +62 856-9235-6848</span>
</div>
"""
contact_4 = """
<div style="display: flex; align-items: center;">
    <img src="https://portal-uang.com/wp-content/uploads/2021/06/Logo-WhatsApp-Transparan-810x540.png" width="55" height="40" style="margin-right: 10px;">
    <span><strong>Syifa Ahista Maharani</strong> +62 878-8730-4171</span>
</div>
"""
contact_5 = """
<div style="display: flex; align-items: center;">
    <img src="https://portal-uang.com/wp-content/uploads/2021/06/Logo-WhatsApp-Transparan-810x540.png" width="55" height="40" style="margin-right: 10px;">
    <span><strong>Anargya Cinta Ismoyo</strong> +62 896-8490-0503</span>
</div>
"""

# Main App Logic

if st.session_state.get("current_page") == "Home":
    home()
elif st.session_state.get("current_page") == "About Us":
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
        st.image("fakhri.jpg", width=150)
        st.write("Anargya Cinta Ismoyo - 2350073")

    # Menampilkan gambar dan teks di kolom kedua
    with col2:
        st.image("fakhri.jpg", width=150)
        st.write("Muhammad Fakhri Al-Fathi - 2350108")

    # Menampilkan gambar dan teks di kolom ketiga
    with col3:
        st.image("fakhri.jpg", width=150)
        st.write("Nabila Azizi Rohmah (2350116)")

    # Menampilkan gambar dan teks di kolom keempat
    with col4:
        st.image("fakhri.jpg", width=150)
        st.write("Pinkan Regina Ayu Maharani - 2350126")

    # Menampilkan gambar dan teks di kolom kelima
    with col5:
        st.image("fakhri.jpg", width=150)
        st.write("Syifa Ahista Maharani - 2350136")

elif st.session_state.get("current_page") == "Contact":
    st.title("Contact")    
    # Menampilkan daftar kontak di aplikasi
    st.markdown(contact_1, unsafe_allow_html=True)
    st.markdown(contact_2, unsafe_allow_html=True)
    st.markdown(contact_3, unsafe_allow_html=True)
    st.markdown(contact_4, unsafe_allow_html=True)
    st.markdown(contact_5, unsafe_allow_html=True)
elif "ATOX.CALC-" in st.session_state.current_page:
    method = st.session_state.current_page.split("-")[1]
    atox_calc_page(method)
else:
    page_2()

# if st.session_state.current_page == "Home":
#     home()
# elif st.session_state.current_page == "About Us":
#     st.title("About Us")

# elif st.session_state.current_page == "Contact":
#     st.title("Contact")
#     st.write("This is the Contact page.")

# else:
#     page_2()


