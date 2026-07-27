import base64
import os
import random
from datetime import datetime
from google import genai
import streamlit as st
import streamlit.components.v1 as components

# 1. Sayfa Ayarları
st.set_page_config(
    page_title="Metin Soyak - Yapay Zeka Yanıt Merkezi",
    page_icon="👔",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Ses Kaydedici Bileşeni
try:
    from streamlit_mic_recorder import speech_to_text
    MIC_AVAILABLE = True
except ImportError:
    MIC_AVAILABLE = False

# 2. Kalıcı Durum Hafızası
if "story_archive" not in st.session_state:
    st.session_state["story_archive"] = []
if "is_speaking" not in st.session_state:
    st.session_state["is_speaking"] = False
if "last_processed_voice" not in st.session_state:
    st.session_state["last_processed_voice"] = ""

# Dosya Adları
STATIC_IMG = "IMG_7535.jpeg"
TALKING_GIF = "hailuo-2_3_A_52-year-old_Turkish_senior_bureaucrat_talking_subtle_lip_movement_and_head_mot-0-ezgif.com-gif-maker.gif"

# Base64 Görsel Dönüştürücü
def get_image_b64(file_path):
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            return base64.b64encode(f.read()).decode("utf-8")
    return None

static_b64 = get_image_b64(STATIC_IMG)
gif_b64 = get_image_b64(TALKING_GIF)

# 3. Temiz ve Şık Arayüz Tasarımı (KORUNDU)
st.markdown(
    """
    <style>
    .stApp { background-color: #f4f5f7; }
    .profile-card {
        background-color: #ffffff;
        border-radius: 16px;
        padding: 20px;
        text-align: center;
        border: 1px solid #e1e4e8;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }
    .avatar-img {
        width: 140px;
        height: 140px;
        border-radius: 50%;
        object-fit: cover;
        border: 4px solid #2c3e50;
        box-shadow: 0 4px 10px rgba(0,0,0,0.15);
        margin-bottom: 10px;
    }
    .answer-card {
        background-color: #ffffff;
        border-left: 6px solid #2c3e50;
        padding: 18px 22px;
        border-radius: 12px;
        font-size: 16px;
        color: #1a1a1a;
        line-height: 1.7;
        box-shadow: 0 4px 12px rgba(0,0,0,0.06);
        margin-top: 15px;
        margin-bottom: 15px;
    }
    </style>
""",
    unsafe_allow_html=True,
)


# 4. Yapay Zeka Motoru
def metin_soyak_ai_cevap(user_query):
    if "GEMINI_API_KEY" not in st.secrets or not st.secrets["GEMINI_API_KEY"]:
        return "⚠️ HATA: Streamlit Secrets alanında 'GEMINI_API_KEY' bulunamadı!"

    api_key = st.secrets["GEMINI_API_KEY"].strip()

    random_distractions = [
        "Lafın arasına girmesin ama az önce masama hatalı bir evrak geldi, yine imza eksik...",
        "Tam buna cevap verirken çaycı Hüseyin Efendi taze çay getirdi, bir yudum alıp devam edeyim.",
        "Şu an koridorda bir gürültü var ama ben Sıfır Hata prensibimden taviz vermem.",
        "Gözlüğümün camı silinmemiş, ama mevzuatı ezbere bildiğim için sorun yok.",
        "Geçen gün dairede de tam bu konu açılmıştı, millet bilip bilmeden konuşuyordu...",
    ]
    chosen_distraction = random.choice(random_distractions)

    system_prompt = f"""
    Sen Metin SOYAK'sın. 52 yaşında, 30 yıllık kıdemli memur, evrak uzmanı ve başyazarsın.
    
    ÇOK ÖNEMLİ KISITLAMALAR:
    1. KISA VE ÖZ OL: Cevabın TOPLAMDA MAXIMUM 2 VEYA 3 KISA CÜMLE olsun. Asla uzun paragraflar yazma!
    2. DOĞRU CEVAP: Soruya doğru ve net cevabı ver.
    3. HAFİF ALAKASIZ BÜROKRATİK TEPKİ: Cevabın bir yerine şu cümleyi ekle: "{chosen_distraction}"
    4. TON: Aşırı kendinden emin, "Sıfır Hata" diyen, resmi ama renkli bir üslup.

    Kullanıcının Sorduğu Soru: "{user_query}"
    """

    try:
        client = genai.Client(api_key=api_key)
        available_models = [m.name for m in client.models.list()]

        for model_info in available_models:
            model_name = model_info.replace("models/", "")
            try:
                response = client.models.generate_content(
                    model=model_name, contents=system_prompt
                )
                if response and response.text:
                    return response.text
            except Exception:
                continue

        return "⚠️ Yanıt üretilemedi. Lütfen tekrar deneyin."

    except Exception as e:
        return f"🚨 HATA: {str(e)}"


# --- ÜST PROFİL KARTI ---
if st.session_state["is_speaking"] and gif_b64:
    img_src = f"data:image/gif;base64,{gif_b64}"
elif static_b64:
    img_src = f"data:image/jpeg;base64,{static_b64}"
else:
    img_src = "https://img.icons8.com/color/96/user-male-circle--v1.png"

st.markdown(
    f"""
    <div class="profile-card">
        <img src="{img_src}" class="avatar-img"><br>
        <div style="font-size:22px; font-weight:700; color:#2c3e50;">Metin SOYAK (52)</div>
        <div style="font-size:13px; color:#7f8c8d; font-weight:600; margin-bottom:8px;">Müdiriyet Kıdemli Başyazarı & Evrak Uzmanı</div>
        <div style="font-size:12px; color:#555; font-style:italic;">"Sorunuz ne olursa olsun; doğru ve gerçek yanıtı verir, kendi üslubumla ve sıfır hatayla açıklarım!"</div>
    </div>
""",
    unsafe_allow_html=True,
)


# --- SORU ALMA ALANI ---
st.subheader("🎙️ Sorunuzu İletin")

voice_input = ""
if MIC_AVAILABLE:
    voice_input = speech_to_text(
        language="tr",
        start_prompt="🎤 Mikrofona Basıp Konuşun",
        stop_prompt="⏹️ Kaydı Bitir",
        just_once=True,
        key="STT_MIC",
    )

text_input = st.text_area(
    "📝 Sorunuz:",
    value=voice_input if voice_input else "",
    placeholder="Mikrofona basıp konuşun veya sorunuzu buraya yazın...",
    height=80,
)

# Sesli soru geldiğinde otomatik çalıştırma mantığı
should_process = False
query_to_send = ""

if voice_input and voice_input != st.session_state["last_processed_voice"]:
    should_process = True
    query_to_send = voice_input
    st.session_state["last_processed_voice"] = voice_input

button_clicked = st.button("✍️ METİN SOYAK'A SOR VE CEVAP AL", use_container_width=True)

if button_clicked and text_input.strip():
    should_process = True
    query_to_send = text_input.strip()

# YANIT ÜRETME AKIŞI
if should_process:
    with st.spinner("Metin Bey mevzuatı ve cevabı inceliyor..."):
        answer_text = metin_soyak_ai_cevap(query_to_send)
        time_str = datetime.now().strftime("%H:%M:%S")

        st.session_state["story_archive"].insert(
            0,
            {
                "time": time_str,
                "prompt": query_to_send,
                "answer": answer_text,
            },
        )
        st.session_state["is_speaking"] = True
        st.rerun()


# --- CEVAP VE OTOMATİK SESLENDİRME ---
if len(st.session_state["story_archive"]) > 0:
    latest = st.session_state["story_archive"][0]

    st.markdown("### 💬 Metin Soyak'ın Cevabı")
    st.markdown(
        f'<div class="answer-card">{latest["answer"]}</div>',
        unsafe_allow_html=True,
    )

    clean_answer = (
        latest["answer"]
        .replace("'", "\\'")
        .replace('"', '\\"')
        .replace("\n", " ")
    )

    # Otomatik Seslendirme Scripti
    auto_speak_script = f"""
        <script>
        function speakNow() {{
            if ('speechSynthesis' in window) {{
                window.speechSynthesis.cancel();
                var msg = new SpeechSynthesisUtterance("{clean_answer}");
                msg.lang = 'tr-TR';
                msg.rate = 0.93;
                window.speechSynthesis.speak(msg);
            }}
        }}
        setTimeout(speakNow, 200);
        </script>
    """
    components.html(auto_speak_script, height=0)

    # Avatar Görsel Sıfırlama Butonu
    if st.session_state["is_speaking"]:
        if st.button("⏹️ Durağan Fotoğrafa Dön", use_container_width=True):
            st.session_state["is_speaking"] = False
            st.rerun()

# --- GEÇMİŞ ARŞİV ---
if len(st.session_state["story_archive"]) > 1:
    st.divider()
    st.subheader(f"📚 Önceki Sorular ({len(st.session_state['story_archive']) - 1})")

    for idx, item in enumerate(st.session_state["story_archive"][1:], start=1):
        with st.expander(f"🕒 {item['time']} - \"{item['prompt'][:35]}...\""):
            st.write(item["answer"])
