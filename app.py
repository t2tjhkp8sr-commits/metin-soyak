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
    "💬 *'Sorunuz ne olursa olsun; hem fıkhi/idari esası söylerim hem de sıfır hatalı hikayesini kaleme alırım!'*"
)

# --- ŞABLON MOTORU (Cevap Odaklı) ---

ZAMAN_VE_MEKAN = [
    "Pazartesi sabahı saat tam 08:45'te müdiriyetin çay ocağı önünde evrak sırasındayken",
    "Bizzat başkanlık ettiğim 'Evrak Arşivinde İmla Standartları' toplantısının ortasında",
    "Öğle molasına beş dakika kala, masamdaki 1998 yılına ait karar defterini incelerken",
    "Yıllık izne ayrılacak memurun zimmet teslim tutanağını kontrol ettiğim esnada",
]

OLAY_GIRIS = [
    "beklenmedik bir kriz yaşandı ve masama doğrudan şu soru geldi: {topic}.",
    "odaya giren bir memur nefes nefese kalmış bir halde bana {topic} hususunu sordu.",
    "koridorda büyük bir tartışma başladı; herkes {topic} meselesini konuşuyordu.",
]

TEPKI_VE_DEGERLENDIRME = [
    "Odadakiler ne yapacağını bilemeyip birbirine bakarken, ben 'Sıfır Hata Metin' soğukkanlılığıyla çayımdan bir yudum aldım. İnsanlar böylesine sorularda hemen paniğe kapılır ama usule ve fıkha hakim olan adam çizgisini bozmaz. Hemen kırmızı kalemimi çıkarıp konunun esasını inceledim.",
    "Genç memurlar meselenin içinden çıkamayıp dehşete düşmüştü. Kendilerine dönüp tam 20 dakika boyunca 'Mevzuat ve Fıkıh Hiyerarşisi' üzerine bir konferans verdim. Arkamdan 'Yine lafı uzattı' dediler ama meselenin özünü kavrayan tek kişi bendim.",
]

KARAR_VE_CEVAP = [
    "Yaptığım derin inceleme neticesinde resmi kanaatimi belirledim: Alınan ürünler helal, tayyib ve mevzuata uygun olduğu sürece bu işlem tamamen CAİZDİR ve hukuken geçerlidir! Ancak alkol, domuz ürünü veya gayriahlaki maddelerin alımı elbette caiz değildir. Ticaretin yapıldığı mekandan ziyade, sepete konulan ürünün mahiyeti esastır.",
    "Evrakı inceleyip şerhimi düşüm: Şirketin veya marketin ticari yapısı bir yana, alınan gıda/ürün helal dairesinde olduğu müddetçe alışveriş yapmak dinen de hukuken de CAİZDİR. Haram olan bir madde satın alınmadığı sürece ortada hiçbir sakınca yoktur.",
]

SONUC_CUMLESI = [
    "Netice itibarıyla fetvayı ve resmi kararı rapora bağlayıp altına mühürlü kaşemi bastım. Varsın arkamdan 'Çok konuştu' desinler... Günün sonunda hem soru yanıtlandı hem de evrakta sıfır hata sağlandı! Dosyayı kaldırıp çayımı tazeledim.",
    "Sonuç olarak kriz çözüldü, net cevap verildi. Üzerine 'Görüldü, İnceledi ve Onaylandı - Metin SOYAK' yazıp parafımı attım. Mühür basıldı, konu kapandı.",
]


def hikaye_uret(user_input):
    clean_topic = user_input.strip().rstrip("?.")
    zaman = random.choice(ZAMAN_VE_MEKAN)
    giris = random.choice(OLAY_GIRIS).format(topic=f"'{clean_topic}?'")
    tepki = random.choice(TEPKI_VE_DEGERLENDIRME)
    karar = random.choice(KARAR_VE_CEVAP)
    sonuc = random.choice(SONUC_CUMLESI)

    return f"{zaman} {giris} {tepki} {karar} {sonuc}"


# GİRDİ ALANI
user_prompt = st.text_area(
    "📝 Metin Soyak'a Ne Sormak/Anlattırmak İstersiniz? (Maksimum 50 kelime):",
    value="Migrostan alışveriş caiz mi?",
    placeholder="Örn: Borsa oynamak caiz mi? / Ofiste uzaylı belirdi...",
    height=90,
)

words = user_prompt.strip().split()
word_count = len(words)
st.caption(f"📊 Kelime Sayısı: **{word_count} / 50**")

# HİKAYE ÜRETME BUTONU
if st.button("✍️ HİKAYE ÜRET VE CEVAPLA", use_container_width=True):
    if not user_prompt.strip():
        st.warning("⚠️ Lütfen Metin Bey'e bir soru veya konu iletin!")
    elif word_count > 50:
        st.error("⚠️ Lütfen girdi 50 kelimeden az olsun!")
    else:
        new_story = hikaye_uret(user_prompt)
        time_stamp = datetime.now().strftime("%H:%M:%S")

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

    st.markdown("### 📜 Onaylanan Resmi Raporda Verilen Cevap")
    st.markdown(
        f'<div class="story-box">{latest["story"]}</div>',
        unsafe_allow_html=True,
    )

    clean_text_js = latest["story"].replace("'", "\\'").replace('"', '\\"')
    tts_html = f"""
        <button onclick="window.speechSynthesis.cancel(); var msg = new SpeechSynthesisUtterance('{clean_text_js}'); msg.lang='tr-TR'; msg.rate=0.95; window.speechSynthesis.speak(msg);" 
        style="width:100%; background:#2c3e50; color:white; border:none; padding:12px; border-radius:10px; font-weight:bold; cursor:pointer; font-size:15px;">
        🔊 SESLİ DİNLE
        </button>
    """
    components.html(tts_html, height=55)

# --- GEÇMİŞ HİKAYELER ARŞİVİ ---
if len(st.session_state["story_archive"]) > 0:
    st.divider()
    st.subheader(
        f"📚 Geçmiş Hikayeler / Cevaplar ({len(st.session_state['story_archive'])} Kayıt)"
    )

    for idx, item in enumerate(st.session_state["story_archive"]):
        expander_title = (
            f"🕒 {item['time']} - Soru/Konu: \"{item['prompt'][:35]}...\""
        )

        with st.expander(expander_title):
            st.write(item["story"])

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

            st.download_button(
                label="📥 Metin Dosyası Olarak İndir (.txt)",
                data=item["story"],
                file_name=f"metin_soyak_hikaye_{item['time'].replace(':','-')}.txt",
                mime="text/plain",
                key=f"dl_{idx}_{item['time']}",
            )
