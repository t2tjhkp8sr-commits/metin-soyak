import random
import streamlit as st

# Safari ve Mobil Ekran Ayarları
st.set_page_config(
    page_title="Metin Soyak - Sıfır Hata",
    page_icon="👔",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# iOS Özel Tasarım (Beyaz & Antrasit / Kurumsal Bürokrasi)
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
        padding: 16px;
        border-radius: 8px;
        font-family: 'Courier New', Courier, monospace;
        font-size: 14px;
        color: #2c3e50;
        line-height: 1.6;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# METİN SOYAK PROFİL DÜZENİ
st.markdown('<div class="profile-container">', unsafe_allow_html=True)

# Yüklediğin IMG_7535.jpeg dosyası doğrudan çağrılıyor
try:
    st.image("IMG_7535.jpeg", width=130)
except Exception:
    # Dosya adı büyük/küçük harf duyarlı olabileceği için alternatif kontrol
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

# HİKAYE MOTORU KALIPLARI
GIRIS_KALIPLARI = [
    "Saat tam 09:15'te masama oturduğumda, müdiriyetin 3.05 tarihli genelgesini inceliyordum.",
    "Müdürlük koridorunda adeta bir kriz havası esiyordu fakat 'Sıfır Hata Metin' olarak soğukkanlılığımı korudum.",
    "Bizzat kaleme aldığım 48 sayfalık usul raporunun tam ortasındaydım ki aniden kapı çalındı.",
]

GELISME_KALIPLARI = [
    "Gelen memur panikle masama yaklaştı ve doğrudan **'{kw}'** mevzusunu gündeme getirdi. Kendisine 'Sakin ol evlat, mevzuata bakmadan adım atılmaz' diyerek 20 dakika boyunca bürokrasi felsefesi anlattım.",
    "Konu dönüp dolaşıp **'{kw}'** meselesine dayanınca, odadakiler 'Yine çok laf az iş' diye fısıldaşmaya başladı. Oysa ben meseleyi kökten çözecek altyapıyı zihnimde kuruyordum.",
    "Evrak kayıt numarasız önüme getirilen **'{kw}'** dosyasını görünce kaşlarımı çattım. Noktası virgülü hatalı bir işe asla imza atmam!",
]

KRİZ_KALIPLARI = [
    "Tam bu aşamada **'{kw}'** durumunun mevzuata tamamen aykırı yürütüldüğünü fark ettim. Hemen kırmızı kalemimi çıkarıp hataların altını tek tek çizdim.",
    "Müteakiben, **'{kw}'** süreci kontrolden çıkıp küçük bir idari krize dönüşünce masaya vurup 'Bu dairede sıfır hata esastır!' diye gürledim.",
]

COZUM_KALIPLARI = [
    "Nihayetinde, **'{kw}'** konusunu bizzat ele alıp baştan sona yeniden yazdım, çizdim ve nizami hale getirdim.",
    "Son hamle olarak **'{kw}'** detayını da 3 nüsha halinde düzenleyip resmi sicile işledim.",
]

SONUC_KALIPLARI = [
    "Netice itibarıyla; varsın arkamdan 'Çok laf eder, az iş yapar' desinler. Günün sonunda evrakta sıfır hata var mı? Var! Mühürü bastım, dosyayı kapattım.",
    "Sonuç olarak bir kriz daha 'Sıfır Hata Metin' dokunuşuyla çözüldü. Evrakı kaşelip arşive kaldırdım, çayımı yudumlamaya devam edebilirim.",
]

# GİRDİ ALANI
raw_input = st.text_input(
    "🔑 Anahtar Kelimeler (Virgülle ayırın):",
    value="mühür, çay molası, klasör, genelge",
    placeholder="Örn: evrak, zimmet, teftiş",
)

if st.button("✍️ METİN SOYAK'A EVRAK DÜZENLET", use_container_width=True):
    words = [w.strip() for w in raw_input.split(",") if w.strip()]

    if not words:
        st.warning(
            "⚠️ Metin Soyak kelime girmeden tek bir paragraf bile kaleme almaz!"
        )
    else:
        story = []
        story.append(random.choice(GIRIS_KALIPLARI))

        if len(words) >= 1:
            story.append(
                random.choice(GELISME_KALIPLARI).format(kw=words[0].upper())
            )

        if len(words) >= 2:
            story.append(
                random.choice(KRİZ_KALIPLARI).format(kw=words[1].upper())
            )

        if len(words) >= 3:
            remaining_kws = ", ".join([w.upper() for w in words[2:]])
            story.append(
                random.choice(COZUM_KALIPLARI).format(kw=remaining_kws)
            )

        story.append(random.choice(SONUC_KALIPLARI))
        full_text = " ".join(story)

        st.markdown("### 📜 Onaylanan Resmi Metin")
        st.markdown(
            f"""
            <div class="story-box">
                {full_text}
                <br><br>
                <b>----------------------------------------</b><br>
                <b>[ MÜHÜRLÜ VE ONAYLI EVRAK ]</b><br>
                <b>Metin SOYAK</b> - Müdiriyet Kıdemli Başyazarı<br>
                <i>Kanaat: "Sıfır Hata / Çok Laf Az İş"</i>
            </div>
        """,
            unsafe_allow_html=True,
        )
