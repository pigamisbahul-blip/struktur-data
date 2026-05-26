from gtts import gTTS
import streamlit as st
import queue
# membuat visualisasi queue kasus antrian klinik
st.title("Antrian Klinik")
st.write("Simulasi Antrian Klinik Menggunakan Queue")
# inisiasi state
if 'antrian' not in st.session_state:
    st.session_state.antrian = queue.Queue()

#membuat tombol input antrian
input_antrian = st.text_input("Masukkan Nama Pasien")
if st.button("tambah antrian"):
    st.session_state.antrian.put(input_antrian)
    st.write("Antrian telah ditambahkan")

# menampilkan seluruh antrian
st.write("Antrian saat ini:")
nomor = 1
for i in st.session_state.antrian.queue:
    st.write(f"{nomor}. {i}")
    nomor += 1

# membuat tombol panggil antrian
if st.button("panggil antrian"):
    if not st.session_state.antrian.empty():
        passien = st.session_state.antrian.get()
        st.write(f"memanggil passien: {passien}")
        tts = gTTS(f"memanggil passien: {passien}", lang="id")
        tts.save("passien.mp3")
        st.audio("passien.mp3", autoplay=True)
    else:
        tts = gTTS("antrian kosong", lang="id")
        tts.save("kosong.mp3")
        st.audio("kosong.mp3", autoplay=True)
        
