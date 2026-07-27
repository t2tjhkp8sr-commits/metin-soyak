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

# 2. Görsel / GIF Dosyalarını Dinamik Bulma (Kırık Görsel Önleyici)
def get_avatar_path():
    files = os.listdir(".")
    gif_file = next((f for f in files if f.endswith(".gif")), None)
    jpg_file = next((f for f in files if f.endswith((".jpeg", ".jpg", ".png"))), None)
    
    if gif_file:
        return gif_file
    elif jpg_file:
        return jpg_file
    return None

AVATAR_PATH = get_avatar_path()

# 3. Kalıcı Arşiv Hafızası
if "story_archive" not in st.session_state:
    st.session_state["story_archive"] = []

# 4. CSS Tasarım
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
        padding: 20px; border-radius: 12px; font-size: 15px;
        color: #1c1c1e; line-height: 1.8; box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        margin-bottom: 15px;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# Profil Bölümü
st.markdown('<div class="profile-container">', unsafe_allow_html=True)

if AVATAR_PATH:
    st.image(AVATAR_PATH, width=140)
else:
    st.write("👔")

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


# --- YAPAY ZEKA MOTORU ---
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
    3. HAFİF ALAKASIZ BÜROKRATİK TEPKİ: Cevabın bir yerine şu cümleyi veya benzeri komik bir bürokratik detayı ekle: "{chosen_distraction}"
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


# --- MİKROFON İLE SESLİ SORU (KİLİTLENMEYEN SAF MİKROFON) ---
st.markdown("### 🎙️ Sesli Soru Sorun")

st_voice_html = """
    <script>
    function startDictation() {
        if (window.hasOwnProperty('webkitSpeechRecognition') || window.hasOwnProperty('SpeechRecognition')) {
            var SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
            var recognition = new SpeechRecognition();

            recognition.continuous = false;
            recognition.interimResults = false;
            recognition.lang = "tr-TR";
            
            var btn = document.getElementById('mic-btn');
            btn.innerHTML = "🔴 Dinleniyor...";
            btn.style.background = "#e74c3c";

            recognition.start();

            recognition.onresult = function(e) {
                var transcript = e.results[0][0].transcript;
                recognition.stop();
                btn.innerHTML = "🎤 MİKROFONA BASIP SORU SOR";
                btn.style.background = "#2c3e50";

                var doc = window.parent.document;
                var textarea = doc.querySelector('textarea');
                if (textarea) {
                    textarea.value = transcript;
                    textarea.dispatchEvent(new Event('input', { bubbles: true }));
                }
            };

            recognition.onerror = function(e) {
                recognition.stop();
                btn.innerHTML = "🎤 MİKROFONA BASIP SORU SOR";
                btn.style.background = "#2c3e50";
                alert("Ses algılanamadı veya izin verilmedi.");
            };
        } else {
            alert("Tarayıcınız ses tanımayı desteklemiyor.");
        }
    }
    </script>
    <button id="mic-btn" onclick="startDictation()" 
    style="width:100%; background:#2c3e50; color:white; border:none; padding:14px; border-radius:10px; font-weight:bold; cursor:pointer; font-size:15px; margin-bottom:10px;">
    🎤 MİKROFONA BASIP SORU SOR
    </button>
"""
components.html(st_voice_html, height=60)

# GİRDİ ALANI
user_prompt = st.text_area(
    "📝 Metin Soyak'a Bir Soru Sorun (Maksimum 50 kelime):",
    value="",
    placeholder="Mikrofona basıp konuştuğunuzda sesiniz buraya dolacaktır...",
    height=80,
)

words = user_prompt.strip().split()
word_count = len(words) if user_prompt.strip() else 0

# CEVAPLAMA BUTONU
if st.button("✍️ METİN SOYAK'A SOR VE CEVAP AL", use_container_width=True):
    if not user_prompt.strip():
        st.warning("⚠️ Lütfen Metin Bey'e bir soru iletin!")
    elif word_count > 50:
        st.error("⚠️ Lütfen sorunuz 50 kelimeden az olsun!")
    else:
        with st.spinner("Metin Bey mevzuatı ve hakikati inceliyor..."):
            answer_result = metin_soyak_ai_cevap(user_prompt)
            time_stamp = datetime.now().strftime("%H:%M:%S")

            st.session_state["story_archive"].insert(
                0,
                {
                    "time": time_stamp,
                    "prompt": user_prompt.strip(),
                    "answer": answer_result,
                },
            )

# --- CEVAP VE SESLİ OKUMA ---
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

    sync_tts_script = f"""
        <script>
        function speakText() {{
            if ('speechSynthesis' in window) {{
                window.speechSynthesis.cancel();
                var text = "{clean_text}";
                var msg = new SpeechSynthesisUtterance(text);
                msg.lang = 'tr-TR';
                msg.rate = 0.95;
                window.speechSynthesis.speak(msg);
            }}
        }}
        setTimeout(speakText, 300);
        </script>
        <button onclick="speakText()" 
        style="width:100%; background:#2c3e50; color:white; border:none; padding:12px; border-radius:10px; font-weight:bold; cursor:pointer; font-size:15px;">
        🔊 CEVABI TEKRAR SESLİ DİNLE
        </button>
    """
    components.html(sync_tts_script, height=60)

# --- ARŞİV ---
if len(st.session_state["story_archive"]) > 0:
    st.divider()
    st.subheader(
        f"📚 Soru ve Cevap Geçmişi ({len(st.session_state['story_archive'])} Kayıt)"
    )

    for idx, item in enumerate(st.session_state["story_archive"]):
        expander_title = f"🕒 {item['time']} - Soru: \"{item['prompt'][:40]}\""

        with st.expander(expander_title, expanded=(idx == 0)):
            st.write(item["answer"])

            arch_text = (
                item["answer"]
                .replace("'", "\\'")
                .replace('"', '\\"')
                .replace("\n", " ")
            )
            arch_tts = f"""
                <script>
                function speakArch_{idx}() {{
                    if ('speechSynthesis' in window) {{
                        window.speechSynthesis.cancel();
                        var msg = new SpeechSynthesisUtterance("{arch_text}");
                        msg.lang = 'tr-TR';
                        msg.rate = 0.95;
                        window.speechSynthesis.speak(msg);
                    }}
                }}
                </script>
                <button onclick="speakArch_{idx}()" 
                style="width:100%; background:#8e8e93; color:white; border:none; padding:8px; border-radius:8px; font-weight:bold; cursor:pointer; font-size:13px; margin-top:5px;">
                🔊 Bu Cevabı Sesli Dinle
                </button>
            """
            components.html(arch_tts, height=50)

            st.download_button(
                label="📥 Cevabı İndir (.txt)",
                data=item["answer"],
                file_name=f"metin_soyak_cevap_{item['time'].replace(':','-')}.txt",
                mime="text/plain",
                key=f"dl_{idx}_{item['time']}",
            )
