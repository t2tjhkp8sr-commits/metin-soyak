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

# Ses Kaydedici Modülü
try:
    from streamlit_mic_recorder import speech_to_text

    MIC_AVAILABLE = True
except ImportError:
    MIC_AVAILABLE = False

# Kalıcı Hafıza
if "story_archive" not in st.session_state:
    st.session_state["story_archive"] = []
if "is_speaking" not in st.session_state:
    st.session_state["is_speaking"] = False
if "auto_play_trigger" not in st.session_state:
    st.session_state["auto_play_trigger"] = False

# Dosya Yolları
STATIC_IMG = "IMG_7535.jpeg"
TALKING_GIF = "hailuo-2_3_A_52-year-old_Turkish_senior_bureaucrat_talking_subtle_lip_movement_and_head_mot-0-ezgif.com-gif-maker.gif"


# Base64 Görsel Yükleyici
def load_image_as_b64(file_path):
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            data = f.read()
            return base64.b64encode(data).decode("utf-8")
    return None


static_b64 = load_image_as_b64(STATIC_IMG)
gif_b64 = load_image_as_b64(TALKING_GIF)

# CSS Tasarımı
st.markdown(
    """
    <style>
    .stApp { background-color: #f2f2f7; }
    .profile-container {
        background-color: #ffffff; border-radius: 16px; padding: 18px;
        border: 1px solid #d1d1d6; box-shadow: 0 4px 12px rgba(0,0,0,0.06);
        text-align: center; margin-bottom: 20px;
    }
    .answer-box {
        background-color: #ffffff; border-left: 5px solid #2c3e50;
        padding: 20px; border-radius: 12px; font-size: 16px;
        color: #1c1c1e; line-height: 1.8; box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        margin-bottom: 15px; font-weight: 500;
    }
    .avatar-frame {
        width: 150px; height: 150px; border-radius: 50%;
        object-fit: cover; border: 3px solid #2c3e50;
        box-shadow: 0 4px 12px rgba(0,0,0,0.18);
    }
    </style>
""",
    unsafe_allow_html=True,
)


# YAPAY ZEKA MOTORU
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


# AVATAR VE PROFİL BÖLÜMÜ
st.markdown('<div class="profile-container">', unsafe_allow_html=True)

# Cevap verilip seslendirme aşamasındaysa OTOMATİK GIF göster
if st.session_state["is_speaking"] and gif_b64:
    img_src = f"data:image/gif;base64,{gif_b64}"
elif static_b64:
    img_src = f"data:image/jpeg;base64,{static_b64}"
else:
    img_src = "https://img.icons8.com/color/96/user-male-circle--v1.png"

st.markdown(
    f"""
    <div style="display:flex; justify-content:center; align-items:center;">
        <img src="{img_src}" class="avatar-frame">
    </div>
""",
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div style="font-size:20px; font-weight:700; color:#1c1c1e; margin-top:8px;">Metin SOYAK (52)</div>
    <div style="font-size:13px; color:#8e8e93; font-weight:600;">Müdiriyet Kıdemli Başyazarı & Evrak Uzmanı</div>
    """,
    unsafe_allow_html=True,
)
st.caption(
    "💬 *'Sorunuz ne olursa olsun; doğru ve gerçek yanıtı verir, kendi üslubumla ve sıfır hatayla açıklarım!'*"
)
st.markdown("</div>", unsafe_allow_html=True)


# SORU ALMA BÖLÜMÜ
st.subheader("🎙️ Sorunuzu İletin")

voice_text = ""
if MIC_AVAILABLE:
    voice_text = speech_to_text(
        language="tr",
        start_prompt="🎤 Mikrofona Basıp Konuşun",
        stop_prompt="⏹️ Kaydı Bitir ve Sor",
        just_once=True,
        key="STT",
    )

user_prompt = st.text_area(
    "📝 Veya Sorunuzu Yazın:",
    value=voice_text if voice_text else "",
    placeholder="Mikrofon kaydı bittiğinde veya buraya yazıp butona bastığınızda Metin Bey cevaplayacaktır...",
    height=80,
)

final_query = voice_text if voice_text else user_prompt.strip()

# SORU CEVAPLAMA TETİKLEYİCİSİ
if st.button("✍️ METİN SOYAK'A SOR VE CEVAP AL", use_container_width=True):
    if not final_query:
        st.warning("⚠️ Lütfen Metin Bey'e bir soru iletin!")
    else:
        with st.spinner("Metin Bey mevzuatı ve hakikati inceliyor..."):
            answer_result = metin_soyak_ai_cevap(final_query)
            time_stamp = datetime.now().strftime("%H:%M:%S")

            st.session_state["story_archive"].insert(
                0,
                {
                    "time": time_stamp,
                    "prompt": final_query,
                    "answer": answer_result,
                },
            )
            # Konuşma modunu ve OTOMATİK SES OYNATMA'yı aktif et
            st.session_state["is_speaking"] = True
            st.session_state["auto_play_trigger"] = True
            st.rerun()


# OTOMATİK KONUŞMA VE CEVAP BÖLÜMÜ
if len(st.session_state["story_archive"]) > 0:
    latest = st.session_state["story_archive"][0]

    st.markdown("### 💬 Metin Soyak'ın Cevabı")
    st.markdown(
        f'<div class="answer-box">{latest["answer"]}</div>',
        unsafe_allow_html=True,
    )

    clean_text = (
        latest["answer"]
        .replace("'", "\\'")
        .replace('"', '\\"')
        .replace("\n", " ")
    )

    # Otomatik Seslendirme Scripti (Ekstra Buton Yok!)
    if st.session_state["auto_play_trigger"]:
        autoplay_script = f"""
            <script>
            function autoSpeak() {{
                if ('speechSynthesis' in window) {{
                    window.speechSynthesis.cancel();
                    var text = "{clean_text}";
                    var msg = new SpeechSynthesisUtterance(text);
                    msg.lang = 'tr-TR';
                    msg.rate = 0.92;
                    
                    // Ses bittiğinde avatarı otomatik durağan fotoğrafa döndürmek için
                    msg.onend = function() {{
                        console.log("Ses bitti");
                    }};

                    window.speechSynthesis.speak(msg);
                }}
            }}
            // Sayfa yüklendiği an otomatik çalışır
            setTimeout(autoSpeak, 200);
            </script>
        """
        components.html(autoplay_script, height=0)
        st.session_state["auto_play_trigger"] = False  # Tekrarlamayı önle

    # Manuel Tekrar Dinleme ve Durdurma Seçenekleri
    col1, col2 = st.columns(2)
    with col1:
        repeat_script = f"""
            <script>
            function speakAgain() {{
                if ('speechSynthesis' in window) {{
                    window.speechSynthesis.cancel();
                    var msg = new SpeechSynthesisUtterance("{clean_text}");
                    msg.lang = 'tr-TR';
                    msg.rate = 0.92;
                    window.speechSynthesis.speak(msg);
                }}
            }}
            </script>
            <button onclick="speakAgain()" style="width:100%; background:#2c3e50; color:white; border:none; padding:10px; border-radius:8px; font-weight:bold; cursor:pointer;">
            🔄 Tekrar Dinle
            </button>
        """
        components.html(repeat_script, height=45)

    with col2:
        if st.button("⏹️ Avatarı Durdur", use_container_width=True):
            st.session_state["is_speaking"] = False
            st.rerun()

# GEÇMİŞ ARŞİV
if len(st.session_state["story_archive"]) > 0:
    st.divider()
    st.subheader(
        f"📚 Soru ve Cevap Geçmişi ({len(st.session_state['story_archive'])} Kayıt)"
    )

    for idx, item in enumerate(st.session_state["story_archive"]):
        expander_title = f"🕒 {item['time']} - Soru: \"{item['prompt'][:40]}\""
        with st.expander(expander_title, expanded=(idx == 0)):
            st.write(item["answer"])
