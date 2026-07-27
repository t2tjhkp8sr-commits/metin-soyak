from datetime import datetime
import random
import streamlit as st
import streamlit.components.v1 as components

# 1. Sayfa Ayarları
st.set_page_config(
    page_title="Metin Soyak - Sıfır Hata Yanıt Merkezi",
    page_icon="👔",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# 2. Kalıcı Arşiv Hafızası (Soru & Cevaplar Sayfada Kalır)
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
    "💬 *'Aklınıza takılanı sorun; fıkhi, idari veya genel hakikati en doğru ve eksiksiz şekilde açıklayayım!'*"
)

# --- FARKLI MEKAN / MOD VE ÜSLUP ŞABLONLARI ---

DURUM_VE_ORTAMLAR = [
    "Dün akşam mahalle kıraathanesinde arkadaşlarla otururken bu konu açıldı. Ben de cebimden kalemimi çıkarıp olayın özünü şöyle izah ettim:",
    "Gerek 30 yıllık hayat tecrübem gerekse incelediğim yüzlerce mevzuat doğrultusunda bu meseleye son noktayı koyuyorum:",
    "Bana bu soruyu geçen gün berber koltuğundayken de sordular. Şöyle arkama yaslandım ve aynen şunları söyledim:",
    "Meseleyi ne çok karmaşıklaştıracaksınız ne de yüzeysel geçeceksiniz. Hakikat ve doğru usul gayet nettir:",
    "Pazar günü evde haberleri izlerken tam da bu husus tartışılıyordu. Hanıma 'Bak yine işin aslını bilmeden konuşuyorlar' deyip doğrusunu aktardım:",
]


def gercekci_absurt_cevap(user_query):
    query_lower = user_query.lower().strip()

    # Sorunun konusunu tespit edip mantıklı + hafif absürt-detaycı cevabı hazırlama
    if "migros" in query_lower or "market" in query_lower:
        ozet_cevap = "Sorunuzun net cevabı: Alınan gıda veya ürün helal ve meşru olduğu sürece Migros veya başka bir marketten alışveriş yapmak tamamen CAİZDİR. İster süpermarket olsun ister mahalle bakkalı; önemli olan satılan ürünün mahiyetidir. Alkol veya haram gıda almadığınız müddetçe ticarette hiçbir sakınca yoktur."
    elif "borsa" in query_lower or "hisse" in query_lower:
        ozet_cevap = "İşin doğrusu şudur: Faaliyet alanı dinen helal olan, faize ve kumara bulaşmayan şirketlerin hissesini alıp satmak CAİZDİR. Ancak faizle iş yapan veya haram sektörlerde bulunan şirketlerin hissesi caiz değildir. Borsa bir kumar yeri değil, ortaklık mekanizmasıdır."
    elif "uzay" in query_lower or "uzaylı" in query_lower:
        ozet_cevap = "Bu konudaki bilimsel ve mantıki gerçek: Evrenin büyüklüğü göz önüne alındığında başka yaşam ihtimalleri teorik olarak mümkündür; fakat elimizde veya resmi belgelerde onaylanmış tek bir somut uzaylı kanıtı yoktur. İspatlanmamış varsayımlarla hareket edilmez."
    elif "çay" in query_lower or "kahve" in query_lower:
        ozet_cevap = "İşin aslı ve mantığı: Gün içinde çay veya kahve içmek insani bir ihtiyaçtır ve verimliliği artırır. Fakat abartıp işi gücü aksatacak boyuta getirmek hakkınız olmayan zamanı harcamak olur. Dengeli tüketildiği sürece helal ve haktır."
    else:
        ozet_cevap = f"'{user_query}' hususundaki hakikat şudur: Mantığa, ahlaka, genel hukuk ilkelerine ve usule uygun olan her adım geçerlidir. Doğru bilgiye dayanarak hareket ettiğiniz sürece hiçbir problem yaşamazsınız."

    # Rastgele Farklı Bir Durum / Giriş Seçimi
    durum = random.choice(DURUM_VE_ORTAMLAR)

    # Bitiş Cümleleri
    bitis = random.choice([
        "Varsın arkamdan 'Yine lafı uzattı' desinler, ben bilginin ve usulün doğrusunu söylerim. Konu kapanmıştır!",
        "İşin hem mantığı hem gerçeği budur. Sıfır hata prensibiyle cevabı verdik, artık gönül rahatlığıyla hareket edebilirsiniz.",
        "Noktası virgülüne kadar doğru cevap budur. Kim ne derse desin işin aslı değişmez!",
    ])

    full_response = f"{durum}\n\n👉 {ozet_cevap}\n\n{bitis}"
    return full_response


# GİRDİ ALANI
user_prompt = st.text_area(
    "📝 Metin Soyak'a Bir Soru Sorun (Maksimum 50 kelime):",
    value="Migrostan alışveriş caiz mi?",
    placeholder="Örn: Borsa oynamak caiz mi? / Kripto para yatırımı mantıklı mı?",
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
        # Cevabı Oluştur
        answer_result = gercekci_absurt_cevap(user_prompt)
        time_stamp = datetime.now().strftime("%H:%M:%S")

        # KALICI ARŞİVE EKLE (En yeni yanıt en üste gelir)
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

    clean_text_js = latest["answer"].replace("'", "\\'").replace('"', '\\"').replace("\n", " ")
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
        expander_title = (
            f"🕒 {item['time']} - Soru: \"{item['prompt'][:40]}\""
        )

        with st.expander(expander_title):
            st.write(item["answer"])

            arch_text_js = (
                item["answer"].replace("'", "\\'").replace('"', '\\"').replace("\n", " ")
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
