from datetime import datetime
import random
import streamlit as st
import streamlit.components.v1 as components

# 1. Sayfa Ayarları
st.set_page_config(
    page_title="Metin Soyak - Bürokrasi Motoru",
    page_icon="👔",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# 2. Arşiv Hafızası (Session State)
if "history" not in st.session_state:
    st.session_state["history"] = []

# 3. iOS Özel Tasarım
st.markdown(
    """
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
    <div style="font-size:20px; font-weight:700;">Metin SOYAK (52)</div>
    <div style="font-size:13px; color:#8e8e93;">Müdiriyet Kıdemli Başyazarı</div>
    </div>
""",
    unsafe_allow_html=True,
)

st.caption(
    "💬 *'Siz mevzuyu anlatın, ben resmi usul ve sıfır hata prensibiyle hikayesini kaleme alayım!'*"
)

# Hikaye Motoru Kalıpları
GIRISLER = [
    "Saat tam 09:15'te masama oturduğumda, önüme gelen notta yazanlar aynen şöyleydi: '{user_topic}'. Odadakiler şaşkındı ama ben soğukkanlılığımı korudum.",
    "Bizzat kaleme aldığım 48 sayfalık disiplin raporunu incelerken gündeme gelen konu şuydu: '{user_topic}'. Bürokrasiye aykırı bir durum olup olmadığını hemen incelemeye başladım.",
    "Etraftakiler 'Yine çok laf az iş yapacak' diye fısıldaşıyordu ama mevzu '{user_topic}' olunca ipleri elime almam şart oldu.",
]

GELISMELER = [
    "Hemen kırmızı kalemimi çıkarıp konunun detaylarını masaya yatırdım. Normal bir insan bunu sıradan sanabilirdi fakat mevzuat açısından tam bir usulsüzlük riski taşıyordu. Kendilerine 'Sakin olun, usule bakmadan adım atılmaz' diyerek uzun bir idari söylev verdim.",
    "Kriz biraz daha büyüyünce odadaki memurlar panikle sağa sola kaçışmaya başladı. Oysa 'Sıfır Hata Metin' olarak ben yerimden bile kalkmadan olayın mantıksal ve hukuki altyapısını kuruyordum.",
]

SONUCLAR = [
    "Nihayetinde hiç istifimi bozmadan konuyu resmi prosedüre uygun biçimde ele aldım. Evrakta tek bir imla hatası bile bırakmadan çözümü sağladım. Varsın arkamdan yine çok konuştu desinler, günü sıfır hatayla kapattık.",
    "Son hamle olarak meseleyi dairenin resmi standartlarına kavuşturdum. Ben işimi yazarım, çizerim, nizami hale getiririm. Kriz ne kadar absürt olursa olsun Metin Soyak masadaysa hata çıkmaz.",
]

# GİRDİ ALANI (50 Kelime Sınırlı Serbest Metin)
user_prompt = st.text_area(
    "📝 Metin Soyak'a Ne Anlattırmak İstersin? (Maksimum 50 kelime):",
    value="Ofiste uzaylı belirdi ve çay molasını uzatmak istedi.",
    placeholder="Örn: Geç kalan memurlar için ejderha kiralama fikri ortaya atıldı...",
    height=100,
)

# Kelime Sayısı Kontrolü
words = user_prompt.strip().split()
word_count = len(words)

st.caption(f"📊 Kelime Sayısı: **{word_count} / 50**")

if st.button("✍️ HİKAYE ÜRET", use_container_width=True):
    if not user_prompt.strip():
        st.warning(
            "⚠️ Metin Soyak'a bir konu anlatmadan tek bir paragraf bile kaleme almaz!"
        )
    elif word_count > 50:
        st.error(
            "⚠️ Lütfen konuyu en fazla 50 kelimeyle özetleyin! Metin Bey fazla uzun girdilerden hoşlanmaz."
        )
    else:
        # Hikaye Oluşturma
        clean_input = user_prompt.strip()
        story_part1 = random.choice(GIRISLER).format(user_topic=clean_input)
        story_part2 = random.choice(GELISMELER)
        story_part3 = random.choice(SONUCLAR)

        content = f"{story_part1} {story_part2} {story_part3}"

        # Arşive Ekle
        timestamp = datetime.now().strftime("%H:%M:%S")
        st.session_state["history"].append({"time": timestamp, "text": content})

        # Hikaye Ekranı
        st.markdown(
            f'<div class="story-box">{content}</div>', unsafe_allow_html=True
        )

        # Seslendirme Butonu (Safari Web Speech API)
        clean_text = content.replace("'", "\\'").replace('"', '\\"')
        tts_html = f"""
            <button onclick="window.speechSynthesis.speak(new SpeechSynthesisUtterance('{clean_text}'))" 
            style="width:100%; background:#2c3e50; color:white; border:none; padding:12px; border-radius:10px; font-weight:bold; cursor:pointer;">
            🔊 SESLİ DİNLE
            </button>
        """
        components.html(tts_html, height=60)

# --- ARŞİV VE İNDİRME BÖLÜMÜ ---
if st.session_state["history"]:
    st.divider()
    st.subheader("📜 Hikaye Arşivi")

    for idx, item in enumerate(reversed(st.session_state["history"])):
        with st.expander(
            f"🕒 {item['time']} - Kayıt #{len(st.session_state['history'])-idx}"
        ):
            st.write(item["text"])
            st.download_button(
                label="📥 Dosya Olarak İndir (.txt)",
                data=item["text"],
                file_name=f"metin_soyak_hikaye_{item['time']}.txt",
                mime="text/plain",
                key=f"dl_{idx}",
            )
