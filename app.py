import random
import streamlit as st

# Safari ve Mobil Ekran Ayarları
st.set_page_config(
    page_title="Metin Soyak - Sıfır Hata",
    page_icon="👔",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# iOS Özel Tasarım
st.markdown(
    """
    <style>
    .stApp {
        background-color: #f2f2f7;
    }
    .profile-container {
        background-color: #ffffff;
        border-radius: 16px;
        padding: 18px;
        border: 1px solid #d1d1d6;
        box-shadow: 0 4px 12px rgba(0,0,0,0.06);
        text-align: center;
        margin-bottom: 20px;
    }
    .profile-name {
        font-size: 20px;
        font-weight: 700;
        color: #1c1c1e;
        margin-bottom: 2px;
    }
    .profile-tag {
        font-size: 13px;
        color: #8e8e93;
        font-weight: 600;
        margin-bottom: 8px;
    }
    .badge-container {
        display: flex;
        justify-content: center;
        gap: 6px;
        flex-wrap: wrap;
    }
    .badge {
        background-color: #e5e5ea;
        color: #2c3e50;
        font-size: 11px;
        font-weight: bold;
        padding: 4px 8px;
        border-radius: 6px;
    }
    .story-box {
        background-color: #ffffff;
        border-left: 5px solid #2c3e50;
        padding: 18px;
        border-radius: 12px;
        font-size: 15px;
        color: #1c1c1e;
        line-height: 1.7;
        box-shadow: 0 2px 8px rgba(0,0,0,0.04);
    }
    </style>
""",
    unsafe_allow_html=True,
)

# METİN SOYAK PROFİL DÜZENİ
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
        <div class="profile-name">Metin SOYAK (52)</div>
        <div class="profile-tag">Müdiriyet Kıdemli Başyazarı & Evrak Uzmanı</div>
        <div class="badge-container">
            <span class="badge">🎯 Sıfır Hata Metin</span>
            <span class="badge">🗣️ Çok Laf Az İş</span>
            <span class="badge">✍️ Yazarım Çizerim</span>
        </div>
    </div>
""",
    unsafe_allow_html=True,
)

st.caption(
    "💬 *'Müdürlükte 'Yine çok laf az iş' deseler de, evrakta sıfır hata prensibimden taviz vermem!'*"
)

# ÖZGÜN VE AKICI ŞABLON MOTORU
GIRISLER = [
    "Saat tam dokuzu çeyrek geçe masamın başındaydım. Müdiriyetin son genelgesindeki noktalama hatalarını düzeltirken binada sıra dışı bir hareketlilik başladı.",
    "Bizzat kaleme aldığım kurumsal disiplin raporunun dördüncü sayfasındayken koridorda aniden bir kargaşa patlak verdi.",
    "Etraftakiler yine 'Çok laf az iş' diye kendi aralarında fısıldaşıyordu ama az sonra patlayacak idari felaketten hiçbirinin haberi yoktu.",
]

GELISMELER = [
    "Olay yerine vardığımda, meselenin doğrudan {kw} etrafında düğümlendiğini fark ettim. Normal bir memur bunu sıradan bir durum sanabilirdi fakat mevzuat açısından tam bir usulsüzlüktü. Hemen araya girip işin felsefesini anlatmaya başladım.",
    "Tam durumun ciddiyetini vurgularken kriz büyüdü ve işin içine {kw} dahil oldu. Odadaki herkes panikle sağa sola kaçışırken ben 'Sıfır Hata Metin' soğukkanlılığıyla yerimden bile kalkmadım.",
    "Gözlerimin önünde yaşanan bu absürt tablo karşısında hemen kırmızı kalemimi çıkardım. {kw} sürecinde yapılan mantık hatalarını tespit edip sırasıyla şerh düşmeye başladım.",
]

COZUM_SONUC = [
    "Nihayetinde hiç istifimi bozmadan {kw} konusunu mevzuata uygun biçimde ele aldım. Olay ne kadar garip olursa olsun, evrakta tek bir imla hatası bile bırakmadan resmi prosedürü tamamladım. Varsın arkamdan yine çok konuştu desinler, günü sıfır hatayla kapattık.",
    "Son hamle olarak {kw} meselesini dairenin resmi standartlarına kavuşturdum. Ben işimi yazarım, çizerim, nizami hale getiririm. Kriz ne kadar absürt olursa olsun Metin Soyak masadaysa hata çıkmaz.",
]

# GİRDİ ALANI
raw_input = st.text_input(
    "🔑 Anahtar Kelimeler (Virgülle ayırın):",
    value="uzay mekiği, çay bardağı, döner dürüm",
    placeholder="Örn: evrak, zimmet, teftiş",
)

if st.button("✍️ HİKAYE ÜRET", use_container_width=True):
    words = [w.strip().lower() for w in raw_input.split(",") if w.strip()]

    if not words:
        st.warning(
            "⚠️ Metin Soyak kelime girmeden tek bir paragraf bile kaleme almaz!"
        )
    else:
        story = []

        # 1. Giriş
        story.append(random.choice(GIRISLER))

        # 2. Gelişme bölümlerinde kelimeleri doğal dilde yedir
        for i, word in enumerate(words[:2]):
            gelisme_temp = random.choice(GELISMELER)
            story.append(gelisme_temp.format(kw=word))

        # 3. Çözüm ve Sonuç
        last_kw = words[-1] if len(words) > 2 else words[0]
        cozum_temp = random.choice(COZUM_SONUC)
        story.append(cozum_temp.format(kw=last_kw))

        full_text = " ".join(story)

        # Doğrudan hikaye çıktısı (Alt unvan/imza yok)
        st.markdown(
            f"""
            <div class="story-box">
                {full_text}
            </div>
        """,
            unsafe_allow_html=True,
        )
