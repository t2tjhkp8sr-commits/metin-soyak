from datetime import datetime
import traceback
import google.generativeai as genai
import streamlit as st
import streamlit.components.v1 as components

# 1. Sayfa Ayarları
st.set_page_config(
    page_title="Metin Soyak - Yapay Zeka Yanıt Merkezi",
    page_icon="👔",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# 2. Kalıcı Arşiv Hafızası
if "story_archive" not in st.session_state:
    st.session_state["story_archive"] = []

# 3. Tasarım
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
try:
    st.image("IMG_7535.jpeg", width=130)
except Exception:
    try:
        st.image("IMG_7535.JPG", width=130)
    except Exception:
        st.write("👔")

st.markdown(
    """
    <div style="font-size:20px; font-weight:700; color:#1c1c1e;">Metin SOYAK (52)</div>
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

    system_prompt = f"""
    Sen Metin SOYAK'sın. 52 yaşında, 30 yıllık kıdemli bir memur, evrak uzmanı ve başyazarsın.
    
    Karakter Kuralları:
    - Kendine aşırı güvenirsin, "Sıfır Hata" takıntın vardır.
    - Çok konuşursun, hafif bürokratik ve resmi bir dil kullanırsın ama günlük hayatın içindesin.
    - Kullanıcı sana ne sorarsa sorsun, ÖNCE sorunun GERÇEK VE DOĞRU CEVABINI (fıkhi, bilimsel, hukuki veya mantıki) net olarak tespit et ve açıkla.
    - Kesinlikle hikaye uydurup "çay sırasındaydım, masamdaydım" gibi hep aynı basma kalıp olaylara girme. Doğrudan soruya ve cevaba odaklan.
    - Doğru cevabı verdikten sonra Metin Soyak olarak kendine has üslubunla ("Varsın lafı uzattı desinler, doğru bilgi budur", "Noktası virgülüne sıfır hatayla açıkladım" gibi) resmiyetle konuyu bağla.
    - Toplamda 2-3 paragrafı geçme.
    
    Kullanıcının Sorduğu Soru: "{user_query}"
    """

    genai.configure(api_key=api_key)

    # Güncel ve geçerli model isimleri
    models_to_try = ["gemini-2.5-flash", "gemini-2.0-flash", "gemini-1.5-flash-8b"]

    for model_name in models_to_try:
        try:
            model = genai.GenerativeModel(model_name)
            response = model.generate_content(system_prompt)
            if response and response.text:
                return response.text
        except Exception:
            continue

    return "🚨 TEKNİK HATA: Tanımlanan tüm Gemini modelleri 404 döndü. Lütfen API key yetkilerinizi veya Google AI Studio hesabınızı kontrol edin."


# GİRDİ ALANI
user_prompt = st.text_area(
    "📝 Metin Soyak'a Bir Soru Sorun (Maksimum 50 kelime):",
    value="Migrostan alışveriş caiz mi?",
    placeholder="Örn: Borsa oynamak caiz mi? / Temettü yatırımı nasıl yapılır?",
    height=90,
)

words = user_prompt.strip().split()
word_count = len(words)
st.caption(f"📊 Kelime Sayısı: **{word_count} / 50**")

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

# --- EKRANDA EN SON VERİLEN CEVAP VE SESLENDİRME ---
if len(st.session_state["story_archive"]) > 0:
    latest = st.session_state["story_archive"][0]

    st.markdown("### 💬 Metin Soyak'ın Cevabı")
    st.markdown(
        f'<div class="answer-box">{latest["answer"]}</div>',
        unsafe_allow_html=True,
    )

    clean_text_js = (
        latest["answer"]
        .replace("'", "\\'")
        .replace('"', '\\"')
        .replace("\n", " ")
    )
    tts_html = f"""
        <button onclick="window.speechSynthesis.cancel(); var msg = new SpeechSynthesisUtterance('{clean_text_js}'); msg.lang='tr-TR'; msg.rate=0.95; window.speechSynthesis.speak(msg);" 
        style="width:100%; background:#2c3e50; color:white; border:none; padding:12px; border-radius:10px; font-weight:bold; cursor:pointer; font-size:15px;">
        🔊 CEVABI SESLİ DİNLE
        </button>
    """
    components.html(tts_html, height=55)

# --- TÜM GEÇMİŞ SORULAR VE CEVAPLAR ARŞİVİ ---
if len(st.session_state["story_archive"]) > 0:
    st.divider()
    st.subheader(
        f"📚 Soru ve Cevap Geçmişi ({len(st.session_state['story_archive'])} Kayıt)"
    )

    for idx, item in enumerate(st.session_state["story_archive"]):
        expander_title = f"🕒 {item['time']} - Soru: \"{item['prompt'][:40]}\""

        with st.expander(expander_title):
            st.write(item["answer"])

            arch_text_js = (
                item["answer"]
                .replace("'", "\\'")
                .replace('"', '\\"')
                .replace("\n", " ")
            )
            arch_tts = f"""
                <button onclick="window.speechSynthesis.cancel(); var msg = new SpeechSynthesisUtterance('{arch_text_js}'); msg.lang='tr-TR'; msg.rate=0.95; window.speechSynthesis.speak(msg);" 
                style="width:100%; background:#8e8e93; color:white; border:none; padding:8px; border-radius:8px; font-weight:bold; cursor:pointer; font-size:13px; margin-top:5px;">
                🔊 Bu Cevabı Sesli Dinle
                </button>
            """
            components.html(arch_tts, height=45)

            st.download_button(
                label="📥 Cevabı İndir (.txt)",
                data=item["answer"],
                file_name=f"metin_soyak_cevap_{item['time'].replace(':','-')}.txt",
                mime="text/plain",
                key=f"dl_{idx}_{item['time']}",
            )
