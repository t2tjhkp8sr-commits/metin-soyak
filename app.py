from datetime import datetime
import random
import streamlit as st
import streamlit.components.v1 as components

# 1. Sayfa Ayarları
st.set_page_config(
    page_title="Metin Soyak - Sıfır Hata Yaratım Merkezi",
    page_icon="👔",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# 2. Kalıcı Arşiv Hafızası (Session State)
if "story_archive" not in st.session_state:
    st.session_state["story_archive"] = []

# 3. iOS ve Safari Uyumlu Özel Tasarım
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
        padding: 20px; border-radius: 12px; font-size: 15px;
        color: #1c1c1e; line-height: 1.8; box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        margin-bottom: 15px;
    }
    .archive-card {
        background-color: #ffffff; border-radius: 10px; padding: 12px;
        margin-bottom: 10px; border: 1px solid #e5e5ea;
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
    "💬 *'Ne anlatırsanız anlatın; usulüne uygun, mantık silsilesi kusursuz ve sıfır hatalı bir hikayeye dönüştürürüm!'*"
)

# --- GELİŞMİŞ VE DEĞİŞKEN HİKAYE MOTORU ---

ZAMAN_VE_MEKAN = [
    "Pazartesi sabahı saat tam 08:45'te müdiriyetin çay ocağı önünde evrak sırasındayken",
    "Bizzat başkanlık ettiğim 'Evrak Arşivinde İmla Standartları' toplantısının ortasında",
    "Öğle molasına beş dakika kala, masamdaki 1998 yılına ait karar defterini incelerken",
    "Yıllık izne ayrılacak memurun zimmet teslim tutanağını kontrol ettiğim esnada",
    "Aşağı kattaki evrak kayıt odasından gelen garip gürültüleri tahkik etmek üzere merdivenlerden inerken",
]

OLAY_GIRIS = [
    "beklenmedik bir gelişme yaşandı ve {topic} konusu patlak verdi.",
    "odaya giren bir memur nefes nefese kalmış bir halde bana {topic} hususunu iletti.",
    "koridorda büyük bir panik dalgası yayıldı; herkes {topic} meselesini konuşuyordu.",
    "önüme getirilen acil kodlu resmi yazıda aynen şu ifade geçiyordu: {topic}.",
]

TEPKI_VE_ABSURDLUK = [
    "Odadakiler ne yapacağını bilemeyip sağa sola koştururken, ben 'Sıfır Hata Metin' soğukkanlılığıyla çayımdan bir yudum aldım. İnsanlar böylesine absürt durumlarda hemen paniğe kapılır ama mevzuata hakim olan adam asla çizgisini bozmaz. Hemen kırmızı kalemimi çıkarıp olayın mantık hatalarını tespit ettim.",
    "Genç memurlar krizin büyüklüğü karşısında dehşete düşmüştü. Kendilerine dönüp tam 20 dakika boyunca 'Bürokraside Kriz Yönetimi ve Sabır' konulu mini bir konferans verdim. Arkamdan 'Yine çok laf ediyor' diye fısıldaştılar ama durumun ciddiyetini kavrayan tek kişi bendim.",
    "Bina amiri bile ne yapacağını şaşırmış, gözlerini bana dikmişti. 'Sakin olun evlatlar' dedim, 'Devletin evrakında ve düzeninde rastgeleliğe yer yoktur!' Masanın üzerindeki gözlüğümü takıp meselenin hukuki ve idari altyapısını çözmeye koyuldum.",
]

ABSURT_COZUM = [
    "Hemen 3 nüsha halinde özel bir beyanname kaleme aldım. İki nokta üst üste işaretlerinden virgüllerin dizilimine kadar tek bir imla hatasına izin vermeden süreci resmi sicile işledim. Absürt gibi görünen bu mesele, devlet ciddiyeti karşısında diz çöktü.",
    "Olayı derhal 2026/04 sayılı iç genelgenin ek maddesine bağladım. Sayfa kenar boşluklarını milimetrik cetvelle ölçüp altına kırmızı mühürlü kaşemi bastım. Mesele öyle bir nizama girdi ki kimse tek bir itiraz bile edemedi.",
    "Sonuç olarak, meselenin tüm detaylarını maddeler halinde arşiv dosyasında birleştirdim. Üzerine 'Görüldü ve İnceledi - Metin SOYAK' yazıp parafımı attım.",
]

SONUC_CUMLESI = [
    "Varsın arkamdan 'Çok konuştu, işi uzattı' desinler... Günün sonunda ortada sıfır hata var mı? Var! Dosyayı kapağına kaldırıp çayımı tazeledim.",
    "Netice itibarıyla kriz ne kadar büyük veya saçma olursa olsun, Metin Soyak masadaysa oradan sadece düzen çıkar. Mühür basıldı, konu kapandı.",
]


def hikaye_uret(user_input):
    clean_topic = user_input.strip().rstrip(".")
    zaman = random.choice(ZAMAN_VE_MEKAN)
    giris = random.choice(OLAY_GIRIS).format(topic=f"'{clean_topic}'")
    tepki = random.choice(TEPKI_VE_ABSURDLUK)
    cozum = random.choice(ABSURT_COZUM)
    sonuc = random.choice(SONUC_CUMLESI)

    return f"{zaman} {giris} {tepki} {cozum} {sonuc}"


# GİRDİ ALANI
user_prompt = st.text_area(
    "📝 Metin Soyak'a Ne Anlattırmak İstersiniz? (Maksimum 50 kelime):",
    value="Ofiste uzaylı belirdi ve çay molasını uzatmak istedi.",
    placeholder="Örn: Evrak odasında ejderha çıktı...",
    height=90,
)

words = user_prompt.strip().split()
word_count = len(words)
st.caption(f"📊 Kelime Sayısı: **{word_count} / 50**")

# HİKAYE ÜRETME BUTONU
if st.button("✍️ HİKAYE ÜRET", use_container_width=True):
    if not user_prompt.strip():
        st.warning("⚠️ Lütfen Metin Bey'e bir konu anlatın!")
    elif word_count > 50:
        st.error(
            "⚠️ Lütfen konuyu 50 kelimeden az yazın. Metin Bey gereksiz uzun girdileri sevmez!"
        )
    else:
        # Yeni Hikaye Üret
        new_story = hikaye_uret(user_prompt)
        time_stamp = datetime.now().strftime("%H:%M:%S")

        # Hafızadaki Arşive Ekle (En yeni en üste gelecek şekilde)
        st.session_state["story_archive"].insert(
            0,
            {
                "time": time_stamp,
                "prompt": user_prompt.strip(),
                "story": new_story,
            },
        )

# --- EKRANDA EN SON ÜRETİLEN HİKAYE VE SESLENDİRME ---
if st.session_state["story_archive"]:
    latest = st.session_state["story_archive"][0]

    st.markdown("### 📜 Onaylanan Son Hikaye")
    st.markdown(
        f'<div class="story-box">{latest["story"]}</div>',
        unsafe_allow_html=True,
    )

    # Seslendirme Butonu (Safari Web Speech API)
    clean_text_js = latest["story"].replace("'", "\\'").replace('"', '\\"')
    tts_html = f"""
        <button onclick="window.speechSynthesis.cancel(); var msg = new SpeechSynthesisUtterance('{clean_text_js}'); msg.lang='tr-TR'; msg.rate=0.95; window.speechSynthesis.speak(msg);" 
        style="width:100%; background:#2c3e50; color:white; border:none; padding:12px; border-radius:10px; font-weight:bold; cursor:pointer; font-size:15px;">
        🔊 SESLİ DİNLE
        </button>
    """
    components.html(tts_html, height=55)

# --- GEÇMİŞ HİKAYELER ARŞİVİ (SAYFADA KALAN VE İSTEDİĞİN ZAMAN DİNLENEN) ---
if len(st.session_state["story_archive"]) > 0:
    st.divider()
    st.subheader(
        f"📚 Geçmiş Hikayeler Arşivi ({len(st.session_state['story_archive'])} Kayıt)"
    )
    st.caption("Aşağıdaki listeden eski hikayelerinize tıklayıp okuyabilir veya tekrar dinleyebilirsiniz:")

    for idx, item in enumerate(st.session_state["story_archive"]):
        # Akordiyon Başlığı
        expander_title = (
            f"🕒 {item['time']} - Konu: \"{item['prompt'][:35]}...\""
        )

        with st.expander(expander_title):
            st.write(item["story"])

            # Arşivdeki Hikayeyi Sesli Dinleme Butonu
            arch_text_js = (
                item["story"].replace("'", "\\'").replace('"', '\\"')
            )
            arch_tts = f"""
                <button onclick="window.speechSynthesis.cancel(); var msg = new SpeechSynthesisUtterance('{arch_text_js}'); msg.lang='tr-TR'; msg.rate=0.95; window.speechSynthesis.speak(msg);" 
                style="width:100%; background:#8e8e93; color:white; border:none; padding:8px; border-radius:8px; font-weight:bold; cursor:pointer; font-size:13px; margin-top:5px;">
                🔊 Bu Hikayeyi Sesli Dinle
                </button>
            """
            components.html(arch_tts, height=45)

            # İndirme Butonu
            st.download_button(
                label="📥 Metin Dosyası Olarak İndir (.txt)",
                data=item["story"],
                file_name=f"metin_soyak_hikaye_{item['time'].replace(':','-')}.txt",
                mime="text/plain",
                key=f"dl_{idx}_{item['time']}",
            )
