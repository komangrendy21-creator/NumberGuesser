
import random
import streamlit as st

st.set_page_config(
    page_title="Game Tebak Angka",
    page_icon="🎯",
    layout="centered"
)

# Inisialisasi permainan
if "angka_rahasia" not in st.session_state:
    st.session_state.angka_rahasia = random.randint(1, 100)
    st.session_state.kesempatan = 5
    st.session_state.percobaan = 0
    st.session_state.selesai = False
    st.session_state.pesan = ""

# Tampilan aplikasi
st.title("🎯 GAME TEBAK ANGKA")
st.write("Tebak angka dari 1 sampai 100!")
st.info("Kamu punya 5 kali percobaan.")

st.progress(
    st.session_state.percobaan / 5
)

st.write(
    f"Kesempatan tersisa: "
    f"{5 - st.session_state.percobaan}"
)

# Input tebakan
if not st.session_state.selesai:

    tebakan = st.number_input(
        "Masukkan tebakan kamu:",
        min_value=1,
        max_value=100,
        step=1
    )

    if st.button("TEBAK!", use_container_width=True):

        st.session_state.percobaan += 1

        if tebakan == st.session_state.angka_rahasia:
            st.session_state.pesan = "Mantap! Tebakan kamu benar!"
            st.session_state.selesai = True

        elif tebakan < st.session_state.angka_rahasia:
            st.session_state.pesan = "Terlalu rendah!"

        else:
            st.session_state.pesan = "Terlalu tinggi!"

        if st.session_state.percobaan == 5 and not st.session_state.selesai:
            st.session_state.selesai = True

    if st.session_state.pesan:
        st.write(st.session_state.pesan)

# Hasil permainan
if st.session_state.selesai:

    if st.session_state.pesan == "Mantap! Tebakan kamu benar!":
        st.success(st.session_state.pesan)
        st.balloons()
    else:
        st.error("Kesempatan kamu sudah habis!")
        st.write(
            f"Angka yang benar adalah "
            f"{st.session_state.angka_rahasia}."
        )

    if st.button("🔄 MAIN LAGI", use_container_width=True):
        for key in [
            "angka_rahasia",
            "kesempatan",
            "percobaan",
            "selesai",
            "pesan"
        ]:
            del st.session_state[key]

        st.rerun()
