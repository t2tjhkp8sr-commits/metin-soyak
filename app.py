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

# 2. KALICI HAFIZA (Sayfa Yenilense De Silinmez)
if "story_archive" not in st.session_state:
    st.session_state["story_archive"] = []

# 3. iOS ve Safari Uyumlu Tasarım
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
    "💬 *'Ne sorarsanız sorun; fıkhi, mantıki ve idari gerçeği söyler, sıfır hatayla rapora bağlarım!'*"
)

# --- DİNAMİK VE GERÇEKÇİ CEVAP MOTORU ---

ZAMAN_VE_MEKAN = [
    "Pazartesi sabahı saat tam 08:45'te müdiriyetin çay ocağı önünde evrak sırasındayken",
    "Bizzat başkanlık ettiğim 'Evrak Arşivinde İmla Standartları' toplantısının ortasında",
    "Öğle molasına beş dakika kala, masamdaki 1998 yılına ait karar defterini incelerken",
    "Yıllık izne ayrılacak memurun zimmet teslim tutanağını kontrol ettiğim esnada",
]

TEPKILER = [
    "Odadakiler ne yapacağını bilemeyip paniğe kapılırken, ben 'Sıfır Hata Metin' soğukkanlılığıyla çayımdan bir yudum aldım. İnsanlar böylesine hususlarda hemen telaş yapar ama usule ve hakikate hakim olan adam çizgisini bozmaz.",
    "Genç memurlar sorunun karmaşıklığı karşısında dehşete düşmüştü. Kendilerine dönüp tam 20 dakika boyunca 'Mevzuat ve Mantık Hiyerarşisi' üzerine mini bir konferans verdim. Arkamdan 'Yine lafı uzattı' dediler ama durumun ciddiyetini kavrayan tek kişi bendim.",
]

SONUCLAR = [
    "Netice itibarıyla kararı ve resmi gerekçeyi rapora bağlayıp altına mühürlü kaşemi bastım. Varsın arkamdan 'Çok konuştu' desinler... Günün sonunda hem soru tam cevaplandı hem de evrakta sıfır hata sağlandı! Dosyayı kaldırıp çayımı tazeledim.",
    "Sonuç olarak kriz çözüldü, hakikat ve nizami cevap kayda geçti. Üzerine 'Görüldü, İnceledi ve Onaylandı - Metin SOYAK' yazıp parafımı attım. Mühür basıldı, konu kapandı.",
]


def cevap_ve_hikaye_uret(user_query):
    query_lower = user_query.lower().strip()

    # Akıllı/Gerçekçi Mantık Çıkarımı (Soru Türüne Göre Gerçekçi Yanıt Üretme)
    if "migros" in query_lower or "market" in query_lower:
        cevap = "Yapılan inceleme neticesinde: Alınan gıda veya maddeler helal, tayyib ve hukuka uygun olduğu sürece alışveriş yapmak tamamen CAİZDİR. Ancak alkol, domuz ürünü veya haram maddelerin alımı elbette caiz değildir. Ticaretin yapıldığı mekandan ziyade sepete koyduğunuz ürünün mahiyeti esastır."
    elif "borsa" in query_lower or "hisse" in query_lower:
        cevap = "Mevzuat ve fıkıh tetkiki sonucunda: Faaliyet alanı dinen helal olan, kumar ve spekülasyondan uzak şirketlerin hisselerini alıp satmak CAİZDİR. Ancak faizli, haram işler yapan şirketlerin hisseleri caiz değildir."
    elif "uzay" in query_lower or "uzaylı" in query_lower:
        cevap = "Fiziksel ve idari veriler ışığında: Evrenin büyüklüğü göz önüne alındığında başka yaşam formlarının bulunma ihtimali bilimsel olarak tartışılabilir; ancak mevcut resmi evrak ve kayıtlarda henüz onaylanmış bir temas bulunmamaktadır."
    elif "çay" in query_lower or "kahve" in query_lower:
        cevap = "İdari ve insani standartlar gereği: Mesai saatleri içerisinde çay/kahve molası verimliliği artırmak kaydıyla haktır; ancak işlerin aksamasına sebep olacak derecede uzun molalar usulsüzdür ve kamu zararına girer."
    else:
        # Genel sorular için mantıklı ve resmi cevap kurgusu
        cevap = f"Masama gelen '{user_query}' hususuyla ilgili yaptığım incelemede: Meselenin esası, genel mantık kurallarına, kamu düzenine ve temel ahlak/fıkıh ilkelerine uygun hareket edilmesidir. Usulüne ve mevzuatına uygun atılan her adım meşru ve geçerlidir."

    # Hikayeyi Birleştirme
    zaman = random.choice(ZAMAN_VE_MEKAN)
    tepki = random.choice(TEPKILER)
    sonuc = random.choice(SONUCLAR)

    full_text = f"{zaman} masama doğrudan şu soru geldi: '{user_query}'. {tepki} Resmî incelemem neticesinde varılan net cevap şudur: {cevap} {sonuc}"
    return full_text


# GİRDİ ALANI
user_prompt = st.text_area(
    "📝 Metin Soyak'a Soru Sorun veya Konu Anlatın (Maksimum 50 kelime):",
    value="Migrostan alışveriş caiz mi?",
    placeholder="Örn: Borsa oynamak caiz mi? / Ofiste uzaylı belirse ne yaparsın?",
    height=90,
)

words = user_prompt.strip().split()
word_count = len(words)
st.caption(f"📊 Kelime Sayısı: **{word_count} / 50**")

# HİKAYE VE CEVAP ÜRETME BUTONU
if st.button("✍️ CEVAPLA VE HİKAYELEŞTİR", use_container_width=True):
    if not user_prompt.strip():
        st.warning("⚠️ Lütfen Metin Bey'e bir soru veya konu iletin!")
    elif word_count > 50:
        st.error("⚠️ Lütfen soru 50 kelimeden az olsun!")
    else:
        # Yanıtı ve Hikayeyi Üret
        story_result = cevap_ve_hikaye_uret(user_prompt)
        time_stamp = datetime.now().strftime("%H:%M:%S")

        # KALICI ARŞİVE EKLE (En yeni en üste)
        st.session_state["story_archive"].insert(
            0,
            {
                "time": time_stamp,
                "prompt": user_prompt.strip(),
                "story": story_result,
            },
        )

# --- EKRANDA EN SON ÜRETİLEN CEVAP VE HİKAYE ---
if len(st.session_state["story_archive"]) > 0:
    latest = st.session_state["story_archive"][0]

    st.markdown("### 📜 Onaylanan Son Rapordaki Cevap")
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

# --- TÜM GEÇMİŞ CEVAPLAR / HİKAYELER ARŞİVİ (SAYFADA KALAN LİSTE) ---
if len(st.session_state["story_archive"]) > 0:
    st.divider()
    st.subheader(
        f"📚 Tüm Sorular ve Cevaplar Arşivi ({len(st.session_state['story_archive'])} Kayıt)"
    )
    st.caption(
        "Aşağıdaki listeden daha önce sorduğunuz tüm soruları görebilir, tıklayıp okuyabilir veya tekrar dinleyebilirsiniz:"
    )

    for idx, item in enumerate(st.session_state["story_archive"]):
        expander_title = (
            f"🕒 {item['time']} - Soru: \"{item['prompt'][:40]}\""
        )

        with st.expander(expander_title):
            st.write(item["story"])

            arch_text_js = (
                item["story"].replace("'", "\\'").replace('"', '\\"')
            )
            arch_tts = f"""
                <button onclick="window.speechSynthesis.cancel(); var msg = new SpeechSynthesisUtterance('{arch_text_js}'); msg.lang='tr-TR'; msg.rate=0.95; window.speechSynthesis.speak(msg);" 
                style="width:100%; background:#8e8e93; color:white; border:none; padding:8px; border-radius:8px; font-weight:bold; cursor:pointer; font-size:13px; margin-top:5px;">
                🔊 Bu Cevabı Sesli Dinle
                </button>
            """
            components.html(arch_tts, height=45)

            st.download_button(
                label="📥 Metin Dosyası Olarak İndir (.txt)",
                data=item["story"],
                file_name=f"metin_soyak_cevap_{item['time'].replace(':','-')}.txt",
                mime="text/plain",
                key=f"dl_{idx}_{item['time']}",
            )
