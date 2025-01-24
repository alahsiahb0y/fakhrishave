import streamlit as st
import random
import base64
import pandas as pd

st.set_page_config(page_title="Sato Keisanki", page_icon="🍇")

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
        background-color: rgba(255, 102, 102, 0.95); /*atur warna pelapis disini*/
        z-index: 0; /* Letakkan di belakang konten lainnya */
    }}
    </style>
    <div class="background"></div>
    """,
    unsafe_allow_html=True
)

#INI PENGATURAN UNTUK SEGALA HIASAN MENU TINGGAL DIPANGGIL
def set_background():
    st.markdown(
        """
        <style>
        html, body, [class*="css"] {
        font-family: 'Creepster', cursive; !important; /* Font monospaced */
        color: #ffff !important; /* Warna teks default */
        
        }

        /* Atur heading jika diperlukan */
        h2, h3, h5, h6 {
        font-family: 'Creepster', cursive; !important;
        color: #ff6666 !important; /* Warna heading */
        }

        h1 {
        font-family: 'Creepster', cursive; !important;
        color: #ffff !important; /* Warna heading */
        }

        /* Mengubah font tombol */
        button {
        font-family: 'Creepster', cursive; !important;
        font-size: 20px ;
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
            background-color: #ffff !important; 
            padding: 10px;              /* Jarak antara teks dan border */
            border-radius: 20px;         /* Sudut border yang melengkung */
            font-size: 25px !important;            /* Ukuran font */
            color: #ff6666;                /* Warna teks */
        }
        
        .typing {
                font-family: 'Creepster', cursive;;
                white-space: normal;  /* Mengizinkan teks untuk membungkus ke baris berikutnya */
                word-wrap: break-word; /* Memastikan kata yang terlalu panjang terpotong dan dibungkus */
                overflow: hidden;

            }

        .bordered-textx {
            
            border: 10px solid #ffff;  /* Warna border (merah-oranye) */
            background-color: #ffff !important; 
            padding: 10px;              /* Jarak antara teks dan border */
            border-radius: 20px;         /* Sudut border yang melengkung */
            font-size: 25px !important;            /* Ukuran font */
            color: #ff6666;                /* Warna teks */
        }
        
        .typingx {
                font-family: 'Creepster', cursive;;
                white-space: normal;  /* Mengizinkan teks untuk membungkus ke baris berikutnya */
                word-wrap: break-word; /* Memastikan kata yang terlalu panjang terpotong dan dibungkus */
                overflow: hidden;

            }

        /* Background gradient */
        .stApp {
            background: linear-gradient(135deg, #f5f7fa, #c3cfe2);
            font-family: 'Creepster', cursive;;
            text-align: center;
            color: #ffff
        }

        /* Button */
        .stButton > button {
            background-color: #FF6666 !important; /* Warna latar belakang default */
            color: #FFFF !important;             /* Warna teks default */
            border: 5px solid #FFFF  !important; /* Warna border default */
            padding: 24px;
            font-weight: bold;
            border-radius: 10px;
            font-size: 50px !important;
            cursor: pointer;
            transition: background-color 0.2s, color 0.2s; /* Efek transisi */
        }

                /* Gaya tombol saat hover */
        button:hover {
            background-color: #ffff !important;  /* Warna latar belakang saat hover */
            color: #ff6666 !important;          /* Warna teks saat hover */
            border: 3px solid #ffff !important; /* Border tetap saat hover */
        }

        /* Image Style */
        .stImage > img {
            border-radius: 10px;
            box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.3);
        }

            .typewriter {
            font-family: 'Creepster', cursive;: inline-block;
            border-right: 2px solid #fff;
            padding-right: 2px;
            white-space: nowrap;
            overflow: hidden;
            animation: typing 2s steps(30) 1s 1 normal both, blink 5s step-end infinite;
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
        <div style="font-family: 'Creepster', cursive; margin-top: -20px; text-align: right;">
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

st.markdown("<br><br>", unsafe_allow_html=True)



#ATUR BACKGROUND
image_url = "https://siva.kemenperin.go.id/public/uploads/news_1687308491.jpg"

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

# Halaman utama
if "page" not in st.session_state:
    st.session_state["page"] = "home"

# Fungsi navigasi
def navigate_to(page):
    st.session_state["page"] = page

# Halaman "home"
if st.session_state["page"] == "home":
    st.markdown('<h2 class="typing bordered-text"> Kira-Kira Berapa Ya Jumlah Gula Buah Yang Kamu Butuhkan Dalam Sehari 🤔🤔🤔</h2>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🍌 Let's Find Out !!! 🥑", key="start_button", use_container_width=True):
        navigate_to("next")

# Halaman "next"
elif st.session_state["page"] == "next":
    st.markdown("<h1 class=' typewriter title'>Want to Find Something ? 🧐🧐🧐</h1>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🍓 Kalkulator Gula Dalam Buah 🥝", use_container_width=True):
            navigate_to("calc")

    with col2:
        if st.button("🍈 Apa Itu Gula Buah ??? 🍋", use_container_width=True):
            navigate_to("explain")
        
    # test_methods = ["ORAC", "TRAP", "LPIC", "FRAP", "TEAC", "DPPH", "CUPRAC", "ABTS"]
    # cols = st.columns(4)
    # for i, method in enumerate(test_methods):
    #     with cols[i % 4]:
    #         if st.button(method, key=method, use_container_width=True):
    #             st.session_state.current_page = f"ATOX.CALC-{method}"
    
    st.markdown("<br><br>", unsafe_allow_html=True)

    if st.button("Back to Menu", use_container_width=True):    
        navigate_to("home")

elif st.session_state["page"] == "calc":
    # Data gula per 100 gram buah (untuk contoh, Anda bisa menambahkan lebih banyak buah)
    buah_data = {
        'Nama Buah': ['Apel', 'Arbei', 'Apricot', 'Anggur', 'Alpukat', 'Bit' , 'Belimbing','Bengkuang','Blueberi','Blewah','Ceri','Ciplukan','Carica','Cermai','Cranberry','Cempedak','Delima','Durian','Duku','Jeruk','Jambu Biji','Jambu Air','Kurma', 'Kedondong','Kelapa','Kecapi','Kelengkeng','Kiwi','Kesemek','Leci','Labu','Lemon','Mangga','Murbei','Matoa','Mengkudu', 'Manggis','Melon','Markisa','Naga','Nangka','Nanas','Pepaya','Pir','Persik','Plum','Pisang','Rambutan','Sirsak','Sukun','Salak','Stroberi','Semangka','Sawo','Tin','Tomat','Tebu','Timun','Zaitun'],
        'Gula (gram)': [10,8,9,16,0.7,8,5,1.8,14,8,8,3,3,3,4,13.5,16,19,20,9,9,4.5,66,6,3,14,65,9,20,21.5,3.5,2.5,13.7,8,21,8,15.6,8,11,13,19.3,10,7.8,10,10,10,12,15,13.5,24.5,21,7.4,6,18,16,2.6,16,5,0],  # Gula per 100 gram
    }
    #untuk input gambar background
    def add_gradient_overlay_background(image_url, overlay_opacity=1):
        """
        Menambahkan background gambar dengan overlay warna hitam dan opacity yang dapat diatur.
        
        Parameters:
        - image_url: URL gambar untuk background.
        - overlay_opacity: Opacity overlay hitam (0.0 - 1.0).
        """
        st.markdown(
            f"""
            <style>
            .stApp {{
                background: 
                    linear-gradient(
                        rgba(0, 0, 0, {overlay_opacity}), /* Overlay warna hitam dengan opacity */
                        rgba(0, 0, 0, {overlay_opacity})
                    ),
                    url("{image_url}");
                background-size: cover;
                background-repeat: no-repeat;
                background-attachment: fixed;
                background-position: center;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )

    # URL gambar Anda (ganti dengan URL gambar yang Anda gunakan)
    image_url = "https://akcdn.detik.net.id/community/media/visual/2022/05/16/buah-buahan-1_169.jpeg?w=700&q=90"

    # Tambahkan background dengan overlay hitam (opacity 0.5)
    add_gradient_overlay_background(image_url, overlay_opacity=0.7)

    # Membuat DataFrame untuk buah
    df_buah = pd.DataFrame(buah_data)

    # Fungsi untuk menghitung kebutuhan gula berdasarkan berat badan dan usia
    def hitung_kebutuhan_gula(usia, berat_badan):
        # Asumsi kebutuhan gula (contoh: 10% dari kalori harian, dengan 1 gram gula = 4 kalori)
        kebutuhan_kalori = berat_badan * 24  # Asumsi 24 kalori per kg berat badan
        kebutuhan_gula = (kebutuhan_kalori * 0.1) / 4  # 10% kalori berasal dari gula
        return kebutuhan_gula

    # Fungsi untuk menghitung gula dalam jumlah buah yang dikonsumsi
    def hitung_gula_buah(fruit, jumlah_gram):
        gula_per_100gram = df_buah[df_buah['Nama Buah'] == fruit]['Gula (gram)'].values[0]
        gula_total = (gula_per_100gram / 100) * jumlah_gram
        return gula_total

    # Tampilan Streamlit
    st.title("Kalkulator Kebutuhan gula manusia dalam buah ")

    # Input Usia dan Berat Badan
    usia = st.number_input("Masukkan Usia (tahun)", min_value=1, max_value=100, value=30)
    berat_badan = st.number_input("Masukkan Berat Badan (kg)", min_value=30, max_value=200, value=70)

    # Hitung kebutuhan gula berdasarkan berat badan dan usia
    kebutuhan_gula = hitung_kebutuhan_gula(usia, berat_badan)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"""
             <h2 class="typing bordered-text">
             Kebutuhan gula harian Anda adalah sekitar {kebutuhan_gula:.2f} gram.
             </h2>
             """, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    # Input Buah dan jumlahnya
    buah_terpilih = st.multiselect("Pilih Buah", df_buah['Nama Buah'].tolist())
    jumlah_buah = st.number_input("Masukkan Jumlah Berat Buah (gram)", min_value=50, max_value=1000, value=100)

    # Menampilkan informasi gula dari buah yang dipilih
    if buah_terpilih:
        for buah in buah_terpilih:
            gula_buah = hitung_gula_buah(buah, jumlah_buah)
        st.markdown(f"""
            <h2 class="typing bordered-text">
            Untuk {jumlah_buah} gram Buah {buah}, Artinya Anda Telah Mengonsumsi Kurang Lebih {gula_buah:.2f} gram Gula.
            </h2>
             """, unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        total_gula = sum([hitung_gula_buah(buah, jumlah_buah) for buah in buah_terpilih])
        st.markdown(f"""
            <h2 class="typing boredered-text">
            Total gula yang dikonsumsi dari buah-buah terpilih: {total_gula:.2f} gram.
            </h2>
            """, unsafe_allow_html=True)
        
    # Fungsi untuk memberikan kesimpulan korelasi
    def kesimpulan(usia, berat_badan, total_gula, kebutuhan_gula):
        if usia < 18:
            usia_kategori = "usia yang relatif masih muda"
        elif 18 <= usia <= 60:
            usia_kategori = "usia yang relatif telah beranjak dewasa"
        else:
            usia_kategori = "usia yang relatif sudah tua"

        if total_gula > kebutuhan_gula:
            rekomendasi = "Anda telah mengonsumsi gula melebihi kebutuhan harian. Kurangi konsumsi buah dengan kadar gula tinggi."
        elif total_gula < kebutuhan_gula * 0.5:
            rekomendasi = "Anda mengonsumsi gula jauh di bawah kebutuhan harian. Anda bisa menambah konsumsi buah."
        else:
            rekomendasi = "Anda mengonsumsi gula dalam kisaran yang sehat. Pertahankan pola konsumsi ini."

        kesimpulan_teks = (
            f"Dengan kategori {usia_kategori} dan berat badan {berat_badan} kg, kebutuhan gula harian Anda adalah sekitar {kebutuhan_gula:.2f} gram.\n"
            f" total gula sebesar {total_gula:.2f} gram dari buah-buahan yang dipilih.\n"
            f"{rekomendasi}"
        )
        return kesimpulan_teks

    # Hitung dan tampilkan kesimpulan
    if buah_terpilih:
        kesimpulan_teks = kesimpulan(usia, berat_badan, total_gula, kebutuhan_gula)
        st.markdown("<h1 class='typing'>Kesimpulan</h1>", unsafe_allow_html=True)
        st.markdown(f"<h2 class='typingx bordered-textx'>{kesimpulan_teks}</h2>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Back to Home"):
        navigate_to("home")

elif st.session_state["page"] == "explain":
    st.markdown("""
                <h2 class="typing bordered-text">
Gula buah adalah nama lain dari fruktosa, yaitu jenis gula alami yang ditemukan terutama dalam buah-buahan, madu, dan beberapa sayuran. Fruktosa termasuk dalam kategori monosakarida, yaitu gula sederhana yang tidak bisa dipecah menjadi unit gula yang lebih kecil.

Karakteristik Gula Buah (Fruktosa)
Rasa Manis:

Fruktosa adalah salah satu jenis gula yang paling manis secara alami, lebih manis dibandingkan glukosa dan sukrosa (gula meja).
Sumber Alami:

Ditemukan dalam buah-buahan seperti apel, anggur, dan mangga.
Terdapat juga dalam madu dan sayuran tertentu seperti wortel dan bit.
Struktur Kimia:

Fruktosa memiliki rumus kimia C₆H₁₂O₆, sama dengan glukosa, tetapi struktur molekulnya berbeda, menjadikannya isomer dari glukosa.
Larut dalam Air:

Fruktosa sangat larut dalam air, sehingga mudah dicerna oleh tubuh dan memberikan rasa manis langsung saat dikonsumsi.
Manfaat dan Peran Gula Buah
Sumber Energi:

Fruktosa menyediakan energi bagi tubuh karena dapat diubah menjadi glukosa dalam hati melalui proses metabolisme.
Pemanfaatan dalam Industri Makanan:

Digunakan sebagai pemanis alami dalam produk makanan dan minuman karena sifatnya yang sangat manis.
Indeks Glikemik Rendah:

Fruktosa memiliki indeks glikemik lebih rendah dibandingkan glukosa, sehingga tidak menyebabkan lonjakan gula darah yang tajam.
Efek Samping Konsumsi Berlebih
Meskipun alami, konsumsi fruktosa dalam jumlah besar (seperti dalam sirup jagung tinggi fruktosa atau makanan olahan) dapat menyebabkan masalah kesehatan, seperti:

Resistensi insulin.
Peningkatan kadar lemak hati (steatosis hati).
Risiko obesitas dan penyakit kardiovaskular.
Untuk konsumsi fruktosa alami dari buah-buahan, biasanya aman karena kandungan serat dalam buah membantu mengatur penyerapan gula.
                """, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Back to Home"):
        navigate_to("home")