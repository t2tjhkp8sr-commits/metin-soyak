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

# ABSÜRT AMACLI BÜROKRATİK HİKAYE ŞABLONLARI
GIRIS_KALIPLARI = [
    "Saat tam 09:15’te müdiriyetin 3.05 tarihli genelgesini inceleyip imla hatalarını düzeltirken, daireye sızan inanılmaz bir kriz haberini aldım.",
    "Bizzat kaleme aldığım 48 sayfalık 'Daire İçi Düzen ve Disiplin Raporu'nun tam ortasındaydım ki koridorda büyük bir kargaşa patlak verdi.",
    "Müdürlüktekiler 'Yine çok laf az iş yapacak' diye fısıldaşıyordu ama az sonra patlayacak idari felaketten hiçbirinin haberi yoktu.",
]

GELISME_1 = [
    "Olay yerine intikal ettiğimde, meselenin tamamen **{kw}** ile ilgili olduğunu gördüm. Normal bir insan buna sıradan bir olay derdi fakat mevzuata göre bu, katıksız bir usulsüzlüktü.",
    "Hemen araya girip, **{kw}** hususunda yapılan bu vahim hatanın kurumsal haysiyetimize yakışmadığını belirterek tam 45 dakika boyunca 'Mevzuatın Felsefesi' üzerine konuştum.",
]

GELISME_2 = [
    "Ben tam durumun ciddiyetini anlatırken, masanın üzerindeki **{kw}** aniden kontrolden çıkarak durumu tam bir absürdlük komedisine çevirdi.",
    "Bununla da kalmayıp, krizin içine doğrudan **{kw}** dahil olunca odadaki tüm memurlar panikle sağa sola kaçışmaya başladı.",
]

KRIS = [
    "Müteakiben, **{kw}** mevzusu öyle bir noktaya geldi ki, bina amiri dahi ne yapacağını bilemeyip gözlerini bana çevirdi. 'Sıfır Hata Metin' olarak soğukkanlılığımı korumam gerekiyordu.",
    "Gözlerimin önünde yaşanan bu absürt tablo karşısında hemen kırmızı kalemimi çıkardım ve **{kw}** sürecindeki tüm mantık hatalarını tek tek tespit ettim.",
]

COZUM = [
    "Hiç istifimi bozmadan, **{kw}** konusunu resmi prosedüre uygun şekilde, 3 nüsha halinde ve kırmızı kaşeyle mühürleyerek anında çözüme kavuşturdum.",
    "Bunu yaparken tek bir noktayı, tek bir virgülü bile atlamadım. **{kw}** meselesi bizzat 'Sıfır Hata Metin' imzasıyla resmi sicile işlenmiş oldu.",
]

SONUC = [
    "Netice itibarıyla; olayın absürdlüğüne rağmen evrakta sıfır hatayla günü kapattık. Varsın arkamdan 'Yine çok konuştu' desinler, çayımı koyup evrakı arşive kaldırdım.",
    "Sonuç olarak bir kriz daha ciddiyetimden taviz verilmeden bertaraf edildi. İşi ben yazarım, ben çizerim; kaşeyi basar olayı bitiririm!",
]

# GİRDİ ALANI
raw_input = st.text_input(
    "🔑 Anahtar Kelimeler (Virgülle ayırın):",
    value="uzay mekiği, çay bardağı, fotokopi makinesi, döner dürüm",
    placeholder="Örn: uzay mekiği, zürafa, kaşe",
)

if st.button("✍️ ABSÜRT SIFIR HATA HİKAYESİ ÜRET", use_container_width=True):
    words = [w.strip() for w in raw_input.split(",") if w.strip()]

    if not words:
        st.warning(
            "⚠️ Metin Soyak kelime girmeden tek bir paragraf bile kaleme almaz!"
        )
    else:
        story = []

        # 1. Giriş
        story.append(random.choice(GIRIS_KALIPLARI))

        # 2. Gelişme 1
        w1 = words[0].upper()
        story.append(random.choice(GELISME_1).format(kw=w1))

        # 3. Gelişme 2 (2 veya daha fazla kelime varsa)
        if len(words) >= 2:
            w2 = words[1].upper()
            story.append(random.choice(GELISME_2).format(kw=w2))

        # 4. Kriz (3 veya daha fazla kelime varsa)
        if len(words) >= 3:
            w3 = words[2].upper()
            story.append(random.choice(KRIS).format(kw=w3))
        else:
            story.append(random.choice(KRIS).format(kw=w1))

        # 5. Çözüm (4 veya daha fazla kelime varsa ya da kalanlar)
        if len(words) >= 4:
            remaining_kws = ", ".join([w.upper() for w in words[3:]])
            story.append(random.choice(COZUM).format(kw=remaining_kws))
        else:
            story.append(random.choice(COZUM).format(kw=words[-1].upper()))

        # 6. Sonuç
        story.append(random.choice(SONUC))

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
