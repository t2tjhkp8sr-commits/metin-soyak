import random
import streamlit as st

# Safari ve Mobil Ekran Ayarları
st.set_page_config(
    page_title="Sıfır Hata Metin",
    page_icon="📝",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# iOS Tarzı Özel Görsel Tasarım
st.markdown(
    """
    <style>
    .stApp {
        background-color: #f2f2f7;
    }
    .profile-card {
        background-color: #ffffff;
        padding: 16px;
        border-radius: 14px;
        border: 1px solid #e5e5ea;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        margin-bottom: 15px;
    }
    .profile-title {
        color: #1c1c1e;
        font-weight: bold;
        font-size: 18px;
        margin-bottom: 6px;
    }
    .profile-subtitle {
        color: #3a3a3c;
        font-size: 13px;
        line-height: 1.5;
    }
    .badge {
        background-color: #e5e5ea;
        color: #1c1c1e;
        padding: 2px 6px;
        border-radius: 4px;
        font-weight: bold;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# Metin Soyak Kalıpları
giris_girizgah = [
    "Müdiriyetin 3.05 tarihli talimatına istinaden söylüyorum; 'Sıfır Hata Metin' derler bana, ben lafa bakmam...",
    "Bizzat kaleme aldığım 48 sayfalık raporda sıfır hata prensibimden milim sapmadım;",
    "Müdürlükte 'Yine çok laf az iş' deseler de ben işin felsefesini yazıyorum kardeşim!",
    "Yazarlık ve çizerlik kariyerimde tek bir imla hatasına bile izin vermemiş bir 'Sıfır Hata Metin' olarak,",
    "Evrak kayıt numarasız müracaatların tam ortasında, sıfır hatayla masaya vurduğum gün,",
]

gecisler = [
    "tam o esnada mevzuata hiç uymayan bir şekilde",
    "müteakiben durum kontrolden çıkıp bürokratik bir krize dönüşünce",
    "tarafımca dakikalarca konuşulup (ki çok laf derler ama işin özüdür) karara bağlandığı üzere",
    "resmi sicile işlenmesine lüzum görülmeksizin",
    "sıfır hata prensibimden taviz vermeden aniden",
    "gerekirse yeniden yazarım çizerim diyerek masaya vurduğumda",
]

sonuclar = [
    "Netice itibarıyla; ben 'Sıfır Hata Metin'. Çok laf eder, az iş yapar gibi görünürüm ama yazarım çizerim, benim işim bu!",
    "Sonuç olarak evrakı imzalayıp arşive kaldırdım. Çok laf ettik ama sıfır hatayla günü kapattık.",
    "Bu olaydan sonra müdürlükte adım tescillendi: 'Sıfır Hata Metin / Çok Laf Az İş Uzmanı'.",
    "Hepsini tek tek rapora döküp kaşeledim. Varsın 'Çok laf az iş' desinler, evrakta sıfır hata var mı? Var. Olay kapanmıştır.",
]

# EKRAN BAŞLIĞI VE PROFİL
st.title("📝 Metin Soyak Üretim Merkezi")

st.markdown(
    """
    <div class="profile-card">
        <div class="profile-title">👨‍💼 Metin SOYAK (52)</div>
        <div class="profile-subtitle">
            <b>Unvan:</b> Başyazar & Uzman Çizer<br>
            <b>Nam-ı Diğer:</b> <span class="badge">Sıfır Hata Metin</span><br>
            <b>Müdürlük Kanaati:</b> <i>"Yine çok laf az iş!"</i><br>
            <b>Slogan:</b> <i>"Sıfır hata metin yazarım, çizerim!"</i>
        </div>
    </div>
""",
    unsafe_allow_html=True,
)

# KELİME GİRİŞ ALANI
raw_input = st.text_input(
    "🔑 Anahtar Kelimeler (Virgülle ayırın):",
    value="evrak, çay molası, klasör, mühür, kaşe, rapor",
)

# HİKAYE ÜRETİM BUTONU
if st.button("✍️ SIFIR HATA METİN'E HİKAYE YAZDIR", use_container_width=True):
    words = [w.strip() for w in raw_input.split(",") if w.strip()]

    if not words:
        st.warning(
            "Metin Soyak kelime girmeden tek bir paragraf bile kaleme almaz!"
        )
    else:
        giris = random.choice(giris_girizgah)
        story_parts = [giris]

        for i, word in enumerate(words):
            gecis = random.choice(gecisler)
            if i == 0:
                cümle = f" Her şey koridorda '{word.upper()}' mevzusunun patlak vermesiyle başladı."
            elif i % 2 == 1:
                cümle = f" Tam '{word}' konusuna sıra gelmişti ki, {gecis} masadaki tüm evraklar birbirine girdi."
            else:
                cümle = f" Etraftakiler 'Yine çok laf az iş' diye fısıldaşırken, ben bizzat olaya müdahale edip '{word}' meselesini sıfır hatayla çözüme kavuşturdum."
            story_parts.append(cümle)

        story_parts.append(f"\n\n{random.choice(sonuclar)}")
        full_story = "".join(story_parts)
        full_story += (
            "\n\n----------------------------------------\n"
            "[ İMZA / KAŞE ]\n"
            "Metin SOYAK\n"
            'Nam-ı Diğer: "Sıfır Hata Metin"\n'
            'Müdürlük Kanaati: "Yine çok laf az iş!"'
        )

        st.subheader("📜 Üretilen Evrak ve Hikaye")
        st.text_area("", value=full_story, height=260)
