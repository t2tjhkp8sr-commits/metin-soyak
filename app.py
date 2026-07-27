import random
import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime

# 1. Sayfa Ayarları
st.set_page_config(
    page_title="Metin Soyak - Üretim Merkezi",
    page_icon="👔",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# 2. Arşiv Hafızası (Session State)
if 'history' not in st.session_state:
    st.session_state['history'] = []

# 3. iOS Özel Tasarım
st.markdown("""
    <style>
    .stApp { background-color: #f2f2f7; }
    .profile-container {
        background-color: #ffffff; border-radius: 16px; padding: 18px;
        border: 1px solid #d1d1d6; box-shadow: 0 4px 12px rgba(0,0,0,0.06);
        text-align: center; margin-bottom: 20px;
    }
    .story-box {
        background-color: #ffffff; border-left: 5px solid #2c3e50;
        padding: 18px; border-radius: 12px; font-size: 15px;
        color: #1c1c1e; line-height: 1.7; box-shadow: 0 2px 8px rgba(0,0,0,0.04);
        margin-bottom: 15px;
    }
    .archive-item {
        background-color: #e5e5ea; padding: 10px; border-radius: 8px;
        margin-bottom: 5px; font-size: 13px; color: #3a3a3c;
    }
    </style>
""", unsafe_allow_html=True)

# Profil Bölümü
st.markdown('<div class="profile-container">', unsafe_allow_html=True)
try:
    st.image("IMG_7535.jpeg", width=130)
except:
    try: st.image("IMG_7535.JPG", width=130)
    except: st.write("👔")
st.markdown("""
    <div style="font-size:20px; font-weight:700;">Metin SOYAK (52)</div>
    <div style="font-size:13px; color:#8e8e93;">Müdiriyet Kıdemli Başyazarı</div>
    </div>
""", unsafe_allow_html=True)

# Hikaye Motoru Şablonları
GIRISLER = ["Saat tam dokuzu çeyrek geçe masamın başındaydım...", "Bizzat kaleme aldığım disiplin raporundaydım ki...", "Etraftakiler 'Çok laf az iş' diyordu ama..."]
GELISMELER = ["Mesele doğrudan {kw} etrafında düğümlendi...", "Kriz büyüdü ve işin içine {kw} dahil oldu...", "Kırmızı kalemimi çıkarıp {kw} hatalarını buldum..."]
SONUCLAR = ["Nihayetinde {kw} konusunu sıfır hatayla çözdüm.", "Kriz ne kadar absürt olsa da {kw} meselesini nizami hale getirdim."]

# Giriş Alanı
raw_input = st.text_input("🔑 Anahtar Kelimeler:", value="mühür, klasör, fotokopi")

if st.button("✍️ HİKAYE ÜRET", use_container_width=True):
    words = [w.strip().lower() for w in raw_input.split(",") if w.strip()]
    if words:
        # Hikaye Oluşturma
        content = f"{random.choice(GIRISLER)} {random.choice(GELISMELER).format(kw=words[0])} {random.choice(SONUCLAR).format(kw=words[-1])}"
        
        # Arşive Ekle
        timestamp = datetime.now().strftime("%H:%M:%S")
        st.session_state['history'].append({"time": timestamp, "text": content})
        
        # Gösterim
        st.markdown(f'<div class="story-box">{content}</div>', unsafe_allow_html=True)
        
        # Seslendirme Butonu
        clean_text = content.replace("'", "\\'").replace('"', '\\"')
        tts_html = f"""
            <button onclick="window.speechSynthesis.speak(new SpeechSynthesisUtterance('{clean_text}'))" 
            style="width:100%; background:#2c3e50; color:white; border:none; padding:12px; border-radius:10px; font-weight:bold;">
            🔊 SESLİ DİNLE
            </button>
        """
        components.html(tts_html, height=60)

# --- ARŞİV VE İNDİRME BÖLÜMÜ ---
if st.session_state['history']:
    st.divider()
    st.subheader("📜 Hikaye Arşivi")
    
    for idx, item in enumerate(reversed(st.session_state['history'])):
        with st.expander(f"🕒 {item['time']} - Kayıt #{len(st.session_state['history'])-idx}"):
            st.write(item['text'])
            st.download_button(
                label="📥 Dosya Olarak İndir (.txt)",
                data=item['text'],
                file_name=f"metin_soyak_hikaye_{item['time']}.txt",
                mime="text/plain",
                key=f"dl_{idx}"
            )
