import streamlit as st
import random

st.set_page_config(page_title="Chemist Game", page_icon="🎮")

def set_page(page_name):
    st.session_state.current_page = page_name

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
        background-color: rgba(128, 255, 0, 0.7);
        z-index: 0; /* Letakkan di belakang konten lainnya */
    }}
    </style>
    <div class="background"></div>
    """,
    unsafe_allow_html=True
)

GAMBAR_BG = "https://i.pinimg.com/originals/de/93/00/de9300895efbcd083941bc3ebf1f4e18.jpg"

# CSS untuk mengatur gambar sebagai background

st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url('{GAMBAR_BG}');
        background-size: cover;
        background-position: center;
        height: 100vh;
    }}
    </style>
    """, 
    unsafe_allow_html=True
)

# Initialize session state
if 'page' not in st.session_state:
    st.session_state.page = 'Page 1'
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'total_questions' not in st.session_state:
    st.session_state.total_questions = 0

# Sample data
elements = [
    {'name': 'Hidrogen', 'symbol': 'H', 'group': 'IA'},
    {'name': 'Helium', 'symbol': 'He', 'group': 'VIIIA'},
    {'name': 'Litium', 'symbol': 'Li', 'group': 'IA'},
    {'name': 'Karbon', 'symbol': 'C', 'group': 'IVA'},
    {'name': 'Oksigen', 'symbol': 'O', 'group': 'VIA'},
    {'name': 'Nitrogen', 'symbol': 'N', 'group': 'VA'},
    {'name': 'Fluorin', 'symbol': 'F', 'group': 'VIIA'},
    {'name': 'Neon', 'symbol': 'Ne', 'group': 'VIIIA'},
    {'name': 'Natrium', 'symbol': 'Na', 'group': 'IA'},
    {'name': 'Magnesium', 'symbol': 'Mg', 'group': 'IIA'},
    {'name': 'Aluminium', 'symbol': 'Al', 'group': 'IIIA'},
    {'name': 'Silikon', 'symbol': 'Si', 'group': 'IVA'},
    {'name': 'Fosfor', 'symbol': 'P', 'group': 'VA'},
    {'name': 'Belerang', 'symbol': 'S', 'group': 'VIA'},
    {'name': 'Klor', 'symbol': 'Cl', 'group': 'VIIA'},
    {'name': 'Argon', 'symbol': 'Ar', 'group': 'VIIIA'},
    {'name': 'Kalium', 'symbol': 'K', 'group': 'IA'},
    {'name': 'Kalsium', 'symbol': 'Ca', 'group': 'IIA'},
    {'name': 'Scandium', 'symbol': 'Sc', 'group': 'IIIB'},
    {'name': 'Titanium', 'symbol': 'Ti', 'group': 'IVB'},
    {'name': 'Vanadium', 'symbol': 'V', 'group': 'VB'},
    {'name': 'Kromium', 'symbol': 'Cr', 'group': 'VIB'},
    {'name': 'Mangan', 'symbol': 'Mn', 'group': 'VIIB'},
    {'name': 'Besi', 'symbol': 'Fe', 'group': 'VIII'},
    {'name': 'Kobalt', 'symbol': 'Co', 'group': 'VIIIB'},
    {'name': 'Nikel', 'symbol': 'Ni', 'group': 'VIIIB'},
    {'name': 'Tembaga', 'symbol': 'Cu', 'group': 'IB'},
    {'name': 'Zinc', 'symbol': 'Zn', 'group': 'IIB'},
    {'name': 'Galium', 'symbol': 'Ga', 'group': 'III-A'},
    {'name': 'Germanium', 'symbol': 'Ge', 'group': 'IVA'},
    {'name': 'Arsen', 'symbol': 'As', 'group': 'VA'},
    {'name': 'Selenium', 'symbol': 'Se', 'group': 'VIA'},
    {'name': 'Brom', 'symbol': 'Br', 'group': 'VIIA'},
    {'name': 'Kripton', 'symbol': 'Kr', 'group': 'VIIIA'},
    {'name': 'Rubidium', 'symbol': 'Rb', 'group': 'IA'},
    {'name': 'Stronsium', 'symbol': 'Sr', 'group': 'IIA'},
    {'name': 'Yttrium', 'symbol': 'Y', 'group': 'IIIB'},
    {'name': 'Zirkonium', 'symbol': 'Zr', 'group': 'IVB'},
    {'name': 'Niobium', 'symbol': 'Nb', 'group': 'VB'},
    {'name': 'Molibdenum', 'symbol': 'Mo', 'group': 'VIB'},
    {'name': 'Teknesium', 'symbol': 'Tc', 'group': 'VIIB'},
    {'name': 'Rutenium', 'symbol': 'Ru', 'group': 'VIII'},
    {'name': 'Rhodium', 'symbol': 'Rh', 'group': 'VIII'},
    {'name': 'Palladium', 'symbol': 'Pd', 'group': 'VIII'},
    {'name': 'Perak', 'symbol': 'Ag', 'group': 'IB'},
    {'name': 'Kadmium', 'symbol': 'Cd', 'group': 'IIB'},
    {'name': 'Indium', 'symbol': 'In', 'group': 'III-A'},
    {'name': 'Timah', 'symbol': 'Sn', 'group': 'IVA'},
    {'name': 'Antimon', 'symbol': 'Sb', 'group': 'VA'},
    {'name': 'Telurium', 'symbol': 'Te', 'group': 'VIA'},
    {'name': 'Iodin', 'symbol': 'I', 'group': 'VIIA'},
    {'name': 'Xenon', 'symbol': 'Xe', 'group': 'VIIIA'},
    {'name': 'Sesium', 'symbol': 'Cs', 'group': 'IA'},
    {'name': 'Barium', 'symbol': 'Ba', 'group': 'IIA'},
    {'name': 'Lantanum', 'symbol': 'La', 'group': 'III-B'},
    {'name': 'Selenium', 'symbol': 'Ce', 'group': 'III-B'},
    {'name': 'Praseodimium', 'symbol': 'Pr', 'group': 'III-B'},
    {'name': 'Neodimium', 'symbol': 'Nd', 'group': 'III-B'},
    {'name': 'Prometium', 'symbol': 'Pm', 'group': 'III-B'},
    {'name': 'Samarium', 'symbol': 'Sm', 'group': 'III-B'},
    {'name': 'Europium', 'symbol': 'Eu', 'group': 'III-B'},
    {'name': 'Gadolinum', 'symbol': 'Gd', 'group': 'III-B'},
    {'name': 'Terbium', 'symbol': 'Tb', 'group': 'III-B'},
    {'name': 'Dysprosium', 'symbol': 'Dy', 'group': 'III-B'},
    {'name': 'Holmium', 'symbol': 'Ho', 'group': 'III-B'},
    {'name': 'Erbium', 'symbol': 'Er', 'group': 'III-B'},
    {'name': 'Thulium', 'symbol': 'Tm', 'group': 'III-B'},
    {'name': 'Ytterbium', 'symbol': 'Yb', 'group': 'III-B'},
    {'name': 'Lutetium', 'symbol': 'Lu', 'group': 'III-B'},
    {'name': 'Hafnium', 'symbol': 'Hf', 'group': 'IVB'},
    {'name': 'Tantalum', 'symbol': 'Ta', 'group': 'VB'},
    {'name': 'Wolfram', 'symbol': 'W', 'group': 'VIB'},
    {'name': 'Rhenium', 'symbol': 'Re', 'group': 'VIIB'},
    {'name': 'Osmium', 'symbol': 'Os', 'group': 'VIII'},
    {'name': 'Iridium', 'symbol': 'Ir', 'group': 'VIII'},
    {'name': 'Platina', 'symbol': 'Pt', 'group': 'VIII'},
    {'name': 'Emas', 'symbol': 'Au', 'group': 'IB'},
    {'name': 'Merkuri', 'symbol': 'Hg', 'group': 'IIB'},
    {'name': 'Timbal', 'symbol': 'Pb', 'group': 'IVA'},
    {'name': 'Bismut', 'symbol': 'Bi', 'group': 'VA'},
    {'name': 'Polonium', 'symbol': 'Po', 'group': 'VIA'},
    {'name': 'Astatin', 'symbol': 'At', 'group': 'VIIA'},
    {'name': 'Radon', 'symbol': 'Rn', 'group': 'VIIIA'},
    {'name': 'Francium', 'symbol': 'Fr', 'group': 'IA'},
    {'name': 'Radium', 'symbol': 'Ra', 'group': 'IIA'},
    {'name': 'Actinium', 'symbol': 'Ac', 'group': 'III-B'},
    {'name': 'Thorium', 'symbol': 'Th', 'group': 'IV-B'},
    {'name': 'Protactinium', 'symbol': 'Pa', 'group': 'V-B'},
    {'name': 'Uranium', 'symbol': 'U', 'group': 'VI-B'},
    {'name': 'Neptunium', 'symbol': 'Np', 'group': 'VII-B'},
    {'name': 'Plutonium', 'symbol': 'Pu', 'group': 'VIII'},
    {'name': 'Americium', 'symbol': 'Am', 'group': 'III-B'},
    {'name': 'Curium', 'symbol': 'Cm', 'group': 'III-B'},
    {'name': 'Berkelium', 'symbol': 'Bk', 'group': 'III-B'},
    {'name': 'Californium', 'symbol': 'Cf', 'group': 'III-B'},
    {'name': 'Einsteinium', 'symbol': 'Es', 'group': 'III-B'},
    {'name': 'Fermium', 'symbol': 'Fm', 'group': 'III-B'},
    {'name': 'Mendelevium', 'symbol': 'Md', 'group': 'III-B'},
    {'name': 'Nobelium', 'symbol': 'No', 'group': 'III-B'},
    {'name': 'Lawrencium', 'symbol': 'Lr', 'group': 'III-B'},
    {'name': 'Rutherfordium', 'symbol': 'Rf', 'group': 'IV-B'},
    {'name': 'Dubnium', 'symbol': 'Db', 'group': 'VB'},
    {'name': 'Seaborgium', 'symbol': 'Sg', 'group': 'V-B'},
    {'name': 'Bohrium', 'symbol': 'Bh', 'group': 'VI-B'},
    {'name': 'Hassium', 'symbol': 'Hs', 'group': 'VII-B'},
    {'name': 'Meitnerium', 'symbol': 'Mt', 'group': 'VIII'},
    {'name': 'Darmstadtium', 'symbol': 'Ds', 'group': 'VIII'},
    {'name': 'Roentgenium', 'symbol': 'Rg', 'group': 'VIII'},
    {'name': 'Copernicium', 'symbol': 'Cn', 'group': 'I-B'},
    {'name': 'Nihonium', 'symbol': 'Nh', 'group': 'III-A'},
    {'name': 'Flerovium', 'symbol': 'Fl', 'group': 'IVA'},
    {'name': 'Moscovium', 'symbol': 'Mc', 'group': 'VA'},
    {'name': 'Livermorium', 'symbol': 'Lv', 'group': 'VIA'},
    {'name': 'Tennessine', 'symbol': 'Ts', 'group': 'VIIA'},
    {'name': 'Oganesson', 'symbol': 'Og', 'group': 'VIIIA'}

]

ions = [
    {"name": "Natrium", "formula": "Na⁺"},
    {"name": "Kalium", "formula": "K⁺"},
    {"name": "Magnesium", "formula": "Mg²⁺"},
    {"name": "Kalsium", "formula": "Ca²⁺"},
    {"name": "Aluminium", "formula": "Al³⁺"},
    {"name": "Seng", "formula": "Zn²⁺"},
    {"name": "Besi (II)", "formula": "Fe²⁺"},
    {"name": "Besi (III)", "formula": "Fe³⁺"},
    {"name": "Tembaga (I)", "formula": "Cu⁺"},
    {"name": "Tembaga (II)", "formula": "Cu²⁺"},
    {"name": "Amonium", "formula": "NH4⁺"},
    {"name": "Timah (II)", "formula": "Sn²⁺"},
    {"name": "Timah (IV)", "formula": "Sn⁴⁺"},
    {"name": "Kobalt (II)", "formula": "Co²⁺"},
    {"name": "Raksa (I)", "formula": "Hg⁺"},
    {"name": "Raksa (II)", "formula": "Hg²⁺"},
    {"name": "Timbal (II)", "formula": "Pb²⁺"},
    {"name": "Timbal (IV)", "formula": "Pb⁴⁺"},
    {"name": "Mangan (II)", "formula": "Mn²⁺"},
    {"name": "Kromium (III)", "formula": "Cr³⁺"},
    {"name": "Litium", "formula": "Li⁺"},
    {"name": "Barium", "formula": "Ba²⁺"},
    {"name": "Stronsium", "formula": "Sr²⁺"},
    {"name": "Perak", "formula": "Ag⁺"},
    {"name": "Nikel (II)", "formula": "Ni²⁺"},
    {"name": "Nikel (III)", "formula": "Ni³⁺"},
    {"name": "Emas (I)", "formula": "Au⁺"},
    {"name": "Emas (III)", "formula": "Au³⁺"},
    {"name": "Platina (II)", "formula": "Pt²⁺"},
    {"name": "Platina (IV)", "formula": "Pt⁴⁺"},
    {"name": "Kadmium", "formula": "Cd²⁺"},
    {"name": "Skandium", "formula": "Sc³⁺"},
    {"name": "Ytrium", "formula": "Y³⁺"},
    {"name": "Titanium (III)", "formula": "Ti³⁺"},
    {"name": "Titanium (IV)", "formula": "Ti⁴⁺"},
    {"name": "Vanadium (III)", "formula": "V³⁺"},
    {"name": "Vanadium (V)", "formula": "V⁵⁺"},
    {"name": "Cerium (III)", "formula": "Ce³⁺"},
    {"name": "Cerium (IV)", "formula": "Ce⁴⁺"},
    {"name": "Hidroksida", "formula": "OH⁻"},
    {"name": "Klorida", "formula": "Cl⁻"},
    {"name": "Bromida", "formula": "Br⁻"},
    {"name": "Iodida", "formula": "I⁻"},
    {"name": "Nitrat", "formula": "NO3⁻"},
    {"name": "Nitrit", "formula": "NO2⁻"},
    {"name": "Sulfat", "formula": "SO4²⁻"},
    {"name": "Sulfit", "formula": "SO3²⁻"},
    {"name": "Karbonat", "formula": "CO3²⁻"},
    {"name": "Bikarbonat", "formula": "HCO3⁻"},
    {"name": "Fosfat", "formula": "PO4³⁻"},
    {"name": "Dihidrogenfosfat", "formula": "H2PO4⁻"},
    {"name": "Hidrogenfosfat", "formula": "HPO4²⁻"},
    {"name": "Asetat", "formula": "CH3COO⁻"},
    {"name": "Hipoklorit", "formula": "ClO⁻"},
    {"name": "Klorit", "formula": "ClO2⁻"},
    {"name": "Klorat", "formula": "ClO3⁻"},
    {"name": "Perklorat", "formula": "ClO4⁻"},
    {"name": "Bromat", "formula": "BrO3⁻"},
    {"name": "Permanganat", "formula": "MnO4⁻"},
    {"name": "Kromat", "formula": "CrO4²⁻"},
    {"name": "Dikromat", "formula": "Cr2O7²⁻"},
    {"name": "Oksalat", "formula": "C2O4²⁻"},
    {"name": "Tiosulfat", "formula": "S2O3²⁻"},
    {"name": "Sianida", "formula": "CN⁻"},
    {"name": "Tiocianat", "formula": "SCN⁻"},
    {"name": "Fluorida", "formula": "F⁻"},
    {"name": "Borida", "formula": "BO3³⁻"},
    {"name": "Silikat", "formula": "SiO3²⁻"},
    {"name": "Amida", "formula": "NH2⁻"}
]

def reset_game():
    st.session_state.score = 0
    st.session_state.total_questions = 0

def render_page_1():
    st.markdown("""<style>.title {color: pink; text-align: center; font-size: 40px;} .custom-button {background-color: #32CD32; color: white; border: 1px solid white; border-radius: 10px; padding: 10px 20px; cursor: pointer; display: inline-block;} .custom-button:hover {background-color: #28a745;} .center-content {text-align: center;}</style>""", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align:center; color: pink;'>Checo Games</h1>", unsafe_allow_html=True)
    
    if st.button("Start Game", key="start_game", use_container_width=True, help="Mulai Permainan"):
        st.session_state.page = "Page 2"
    

def render_page_2():
    st.markdown("<h2 style='text-align:center;'>Main Menu</h2>", unsafe_allow_html=True)
    if st.button("Guess the Element", key="guess_element", use_container_width=True):
        st.session_state.page = 'Guess the Element'
    if st.button("Guess the Ion", key="guess_ion", use_container_width=True):
        st.session_state.page = 'Guess the Ion'
    st.markdown("<br><br>", unsafe_allow_html=True)
    if st.button("Back To Menu", use_container_width=True):
        st.session_state.page = 'Page 1'

def render_guess_element():
    st.markdown("<h2 style='text-align:center;'>Guess the Element</h2>", unsafe_allow_html=True)
    if 'current_question' not in st.session_state:
        question_types = [
            {'type': 'name', 'question': "Yang manakah unsur {element_name}?"},
            {'type': 'group', 'question': "Yang manakah unsur golongan {element_group}?"},
            {'type': 'symbol', 'question': "Apa nama unsur dari simbol {element_symbol}?"}
        ]
        question_data = random.choice(question_types)
        correct_element = random.choice(elements)
        options = random.sample([e for e in elements if e != correct_element], 4) + [correct_element]
        random.shuffle(options)

        st.session_state.current_question = {
            'question_data': question_data,
            'correct_element': correct_element,
            'options': options,
            'answered': False
        }

    question_data = st.session_state.current_question['question_data']
    correct_element = st.session_state.current_question['correct_element']
    options = st.session_state.current_question['options']

    if question_data['type'] == 'name':
        question = question_data['question'].format(element_name=correct_element['name'])
    elif question_data['type'] == 'group':
        question = question_data['question'].format(element_group=correct_element['group'])
    else:
        question = question_data['question'].format(element_symbol=correct_element['symbol'])

    st.write(f"<div style='text-align:center; margin-bottom:20px;'>{question}</div>", unsafe_allow_html=True)

    for i, option in enumerate(options):
        display_text = option['symbol'] if question_data['type'] == 'name' else option['name']
        if st.button(display_text, key=f"element_{i}", disabled=st.session_state.current_question['answered'], use_container_width=True):
            if not st.session_state.current_question['answered']:
                st.session_state.current_question['answered'] = True
                if option == correct_element:
                    st.success("Benar! Anda mendapat 10 poin.")
                    st.session_state.score += 10
                else:
                    st.error(f"Salah! Jawaban yang benar adalah {correct_element['name']} ({correct_element['symbol']}).")
                st.session_state.total_questions += 1

    if st.session_state.current_question['answered']:
        if st.button("Next", key="next_question", help="Lanjut ke soal berikutnya", use_container_width=True):
            del st.session_state.current_question

    st.markdown("<div style='text-align:center;'>", unsafe_allow_html=True)
    if st.button("Give Up", key="give_up_element", use_container_width=True):
        st.session_state.page = 'Page Result'
    st.markdown("</div>", unsafe_allow_html=True)

def render_guess_ion():
    st.markdown("<h2 style='text-align:center;'>Guess the Ion</h2>", unsafe_allow_html=True)
    if 'current_question_ion' not in st.session_state:
        question_types = [
            {'type': 'name', 'question': "Yang manakah ion {ion_name}?"},
            {'type': 'formula', 'question': "Apa nama ion dari simbol {ion_formula}?"}
        ]
        question_data = random.choice(question_types)
        correct_ion = random.choice(ions)
        options = random.sample([i for i in ions if i != correct_ion], 4) + [correct_ion]
        random.shuffle(options)

        st.session_state.current_question_ion = {
            'question_data': question_data,
            'correct_ion': correct_ion,
            'options': options,
            'answered': False
        }

    question_data = st.session_state.current_question_ion['question_data']
    correct_ion = st.session_state.current_question_ion['correct_ion']
    options = st.session_state.current_question_ion['options']

    if question_data['type'] == 'name':
        question = question_data['question'].format(ion_name=correct_ion['name'])
    else:
        question = question_data['question'].format(ion_formula=correct_ion['formula'])

    st.write(f"<div style='text-align:center; margin-bottom:20px;'>{question}</div>", unsafe_allow_html=True)

    for i, option in enumerate(options):
        display_text = option['formula'] if question_data['type'] == 'name' else option['name']
        if st.button(display_text, key=f"ion_{i}", disabled=st.session_state.current_question_ion['answered'], use_container_width=True):
            if not st.session_state.current_question_ion['answered']:
                st.session_state.current_question_ion['answered'] = True
                if option == correct_ion:
                    st.success("Benar! Anda mendapat 10 poin.")
                    st.session_state.score += 10
                else:
                    st.error(f"Salah! Jawaban yang benar adalah {correct_ion['name']} ({correct_ion['formula']}).")
                st.session_state.total_questions += 1

    if st.session_state.current_question_ion['answered']:
        if st.button("Next", key="next_ion", help="Lanjut ke soal berikutnya", use_container_width=True):
            del st.session_state.current_question_ion

    st.markdown("<div style='text-align:center;'>", unsafe_allow_html=True)
    if st.button("Give Up", key="give_up_ion", use_container_width=True):
        st.session_state.page = 'Page Result'
    st.markdown("</div>", unsafe_allow_html=True)

def render_page_result():
    st.markdown("<h2 style='text-align:center;'>Result</h2>", unsafe_allow_html=True)
    if st.session_state.total_questions > 0:
        percentage = (st.session_state.score / (st.session_state.total_questions * 10)) * 100
    else:
        percentage = 0
    st.write(f"<div style='text-align:center;'>Hasil Akhir: {percentage:.2f}%</div>", unsafe_allow_html=True)
    st.write(f"<div style='text-align:center;'>Benar: {st.session_state.score // 10}</div>", unsafe_allow_html=True)
    st.write(f"<div style='text-align:center;'>Total Soal: {st.session_state.total_questions}</div>", unsafe_allow_html=True)
    if st.button("Menu", use_container_width=True):
        st.session_state.page = 'Page 1'
        reset_game()

if st.session_state.page == 'Page 1':
    render_page_1()
elif st.session_state.page == 'Page 2':
    render_page_2()
elif st.session_state.page == 'Guess the Element':
    render_guess_element()
elif st.session_state.page == 'Guess the Ion':
    render_guess_ion()
elif st.session_state.page == 'Page Result':
    render_page_result()
