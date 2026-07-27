import base64
import os
import random
from datetime import datetime
from google import genai
import streamlit as st
import streamlit.components.v1 as components

# Sayfa Ayarları
st.set_page_config(
    page_title="Metin Soyak - Yapay Zeka Yanıt Merkezi",
    page_icon="👔",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Ses Kaydedici
try:
    from streamlit_mic_recorder import speech_to_text

    MIC_AVAILABLE = True
except ImportError:
    MIC_AVAILABLE = False

# Oturum Hafızası
if "story_archive" not in st.session_state:
    st.session_state["story_archive"] = []

# Dosyalar
STATIC_IMG = "IMG_7535.jpeg"
TALKING_GIF = "hailuo-2_3_A_52-year-old_Turkish_senior_bureaucrat_talking_subtle_lip_movement_and_head_mot-0-ezgif.com-gif-maker.gif"


def load_b64(path):
    if os.path.exists(path):
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode("utf-8")
    return ""


static_b64 = load_b64(STATIC_IMG)
gif_b64 = load_b64(TALKING_GIF)

# CSS
st.markdown(
    """
    <style>
    .stApp { background-color: #f2f2f7; }
    .answer-box {
        background-color: #ffffff; border-left: 5px solid #2c3e50;
        padding: 18px; border-radius: 12px; font-size: 15px;
        color: #1c1c1e; line-height: 1.7; box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        margin-top: 10px; margin-bottom: 15px;
    }
    </style>
""",
    unsafe_allow_html=True,
)


# AI Yanıt Motoru
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
        for m in client.models.list():
            model_name = m.name.replace("models/", "")
            try:
                res = client.models.generate_content(
                    model=model_name, contents=system_prompt
                )
                if res and res.text:
                    return res.text
            except Exception:
                continue
        return "⚠️ Yanıt üretilemedi. Lütfen tekrar deneyin."
    except Exception as e:
        return f"🚨 HATA: {str(e)}"


# Soru İletme Alanı
st.subheader("🎙️ Sorunuzu İletin")

voice_text = ""
if MIC_AVAILABLE:
    voice_text = speech_to_text(
        language="tr",
        start_prompt="🎤 Mikrofona Basıp Konuşun",
        stop_prompt="⏹️ Kaydı Bitir",
        just_once=True,
        key="STT",
    )

user_prompt = st.text_area(
    "📝 Veya Sorunuzu Yazın:",
    value=voice_text if voice_text else "",
    placeholder="Sorunuzu buraya yazın veya mikrofona konuşun...",
    height=80,
)

final_query = voice_text if voice_text else user_prompt.strip()

if st.button("✍️ METİN SOYAK'A SOR VE CEVAP AL", use_container_width=True):
    if not final_query:
        st.warning("⚠️ Lütfen bir soru yazın veya ses kaydedin!")
    else:
        with st.spinner("Metin Bey mevzuatı inceliyor..."):
            answer = metin_soyak_ai_cevap(final_query)
            t_stamp = datetime.now().strftime("%H:%M:%S")
            st.session_state["story_archive"].insert(
                0, {"time": t_stamp, "prompt": final_query, "answer": answer}
            )
            st.rerun()

# CEVAP VE AVATAR CANLI SESLENDİRME ALANI
if len(st.session_state["story_archive"]) > 0:
    latest = st.session_state["story_archive"][0]
    clean_text = (
        latest["answer"]
        .replace("'", "\\'")
        .replace('"', '\\"')
        .replace("\n", " ")
    )

    st.markdown("---")

    # HTML/JS - AVATAR GIF KONTROLÜ VE SESLENDİRME
    interactive_avatar_html = f"""
    <div style="text-align: center; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
        <div style="display: flex; justify-content: center; margin-bottom: 10px;">
            <img id="metin-avatar" src="data:image/jpeg;base64,{static_b64}" 
                 style="width: 150px; height: 150px; border-radius: 50%; object-fit: cover; border: 3px solid #2c3e50; box-shadow: 0 4px 12px rgba(0,0,0,0.18);">
        </div>
        <div style="font-size:20px; font-weight:700; color:#1c1c1e;">Metin SOYAK (52)</div>
        <div style="font-size:13px; color:#8e8e93; font-weight:600; margin-bottom: 15px;">Müdiriyet Kıdemli Başyazarı & Evrak Uzmanı</div>
        
        <button id="speak-btn" onclick="startSpeaking()" 
                style="width:100%; background:#2c3e50; color:white; border:none; padding:14px; border-radius:10px; font-weight:bold; cursor:pointer; font-size:15px;">
            🗣️ METİN BEY'İ DİNLE (AVATAR KONUŞSUN)
        </button>
    </div>

    <script>
    function startSpeaking() {{
        var img = document.getElementById('metin-avatar');
        var btn = document.getElementById('speak-btn');
        var gifSrc = "data:image/gif;base64,{gif_b64}";
        var staticSrc = "data:image/jpeg;base64,{static_b64}";

        if ('speechSynthesis' in window) {{
            window.speechSynthesis.cancel();
            
            var text = "{clean_text}";
            var msg = new SpeechSynthesisUtterance(text);
            msg.lang = 'tr-TR';
            msg.rate = 0.92;

            // Ses Başladığında GIF Yap
            msg.onstart = function() {{
                if(gifSrc) img.src = gifSrc;
                btn.innerHTML = "🔊 Metin Bey Konuşuyor...";
                btn.style.background = "#e74c3c";
            }};

            // Ses Bittiğinde Durağan Resme Dön
            msg.onend = function() {{
                if(staticSrc) img.src = staticSrc;
                btn.innerHTML = "🗣️ METİN BEY'İ TEKRAR DİNLE";
                btn.style.background = "#2c3e50";
            }};

            msg.onerror = function() {{
                if(staticSrc) img.src = staticSrc;
                btn.innerHTML = "🗣️ METİN BEY'İ TEKRAR DİNLE";
                btn.style.background = "#2c3e50";
            }};

            window.speechSynthesis.speak(msg);
        }} else {{
            alert("Tarayıcınız ses sentezini desteklemiyor.");
        }}
    }}
    
    // Otomatik Başlatma Denemesi
    setTimeout(function() {{
        startSpeaking();
    }}, 400);
    </script>
    """

    components.html(interactive_avatar_html, height=310)

    st.markdown("### 💬 Metin Soyak'ın Cevabı")
    st.markdown(
        f'<div class="answer-box">{latest["answer"]}</div>',
        unsafe_allow_html=True,
    )
