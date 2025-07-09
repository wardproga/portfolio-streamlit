import streamlit as st
from PIL import Image

st.set_page_config(page_title="ملف أعمال معاذ النمرات", page_icon="💼", layout="wide")

# --- تنسيق عام ---
st.markdown(
    """
    <style>
        .main {
            background-color: #f8f9fa;
            font-family: 'Cairo', sans-serif;
        }
        h1, h2, h3 {
            color: #003566;
        }
        .stButton>button {
            background-color: #198754;
            color: white;
            border-radius: 8px;
            padding: 10px 20px;
        }
        .stDownloadButton>button {
            background-color: #0d6efd;
            color: white;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# --- العنوان ---
st.title("👋 أهلاً بك في ملف أعمالي")
st.markdown("مرحبًا، أنا **معاذ النمرات** — مطور برمجيات ومحلل بيانات من الأردن، بخبرة أكثر من 14 سنة في التعليم والتقنية.")

st.divider()

import streamlit as st

# إعدادات الصفحة
st.set_page_config(page_title="ملف أعمال معاذ النمرات", page_icon="💼", layout="wide")

# عنوان رئيسي
st.title("مرحباً بكم في ملف أعمالي 💼")

# -------- من أنا ----------
st.header("من أنا؟")
st.write("""
أنا مطور ومحلل بيانات مهتم بمجالات تعلم الآلة وتحليل البيانات.  
أسعى لاستخدام البرمجة لإيجاد حلول ذكية للمشكلات.  
أعمل في مجال التعليم منذ أكثر من 14 سنة، وخريج جامعة آل البيت بتخصص علم الحاسوب.
""")

# -------- المهارات ----------
st.header("المهارات")
skills = [
    "🐍 Python",
    "📊 تحليل البيانات (Pandas, NumPy)",
    "💻 Streamlit",
    "🌐 Git & GitHub",
    "🧠 C++",
    "🕸️ PHP / Laravel",
    "🧠 JavaScript / HTML / CSS"
]
st.write("\n".join(f"- {skill}" for skill in skills))
st.header("📂 مشاريعي")

col1, col2 = st.columns(2)

with col1:
    st.subheader("🧠 نظام الحوسبة التعليمية - OpenEMIS")
    st.write("""
    نظام إلكتروني متكامل لإدارة معلومات التعليم، يساعد المدارس على جمع وتحليل البيانات التعليمية.
    """)
    st.markdown("- **التقنيات**: PHP, Laravel, MySQL")
    st.markdown("[🔗 رابط المشروع](https://openemis.org/)")

with col2:
    st.subheader("🌐 ملف الأعمال - Portfolio Streamlit")
    st.write("""
    تطبيق تفاعلي باستخدام Streamlit لعرض سيرتي الذاتية ومشاريعي بشكل أنيق وسهل الاستخدام.
    """)
    st.markdown("- **التقنيات**: Python, Streamlit, GitHub")
    st.markdown("[🔗 رابط مباشر للموقع](https://portfolio-app-mubu7hqoxrgwdadhnnrbau.streamlit.app)")

st.divider()
# -------- تحميل السيرة الذاتية ----------
st.header("📄 السيرة الذاتية")
with open("CV_Moad_Nimrat.pdf", "rb") as pdf_file:
    PDFbyte = pdf_file.read()

st.download_button(label="📥 تحميل السيرة الذاتية (PDF)",
                   data=PDFbyte,
                   file_name="CV_Moad_Nimrat.pdf",
                   mime="application/octet-stream")

# -------- رابط GitHub ----------
st.header("🌍 روابط مهمة")
st.markdown("[🔗 زيارة حساب GitHub](https://github.com/wardproga)")

# -------- نموذج تواصل ----------
st.header("📬 تواصل معي")
contact_form = """
<form action="https://formsubmit.co/wardproga@gmail.com" method="POST">
     <input type="text" name="الاسم" placeholder="اسمك الكامل" required style="width: 100%; padding: 8px;"><br><br>
     <input type="email" name="البريد" placeholder="بريدك الإلكتروني" required style="width: 100%; padding: 8px;"><br><br>
     <textarea name="الرسالة" placeholder="اكتب رسالتك هنا..." required style="width: 100%; padding: 8px;"></textarea><br><br>
     <button type="submit" style="padding: 10px 20px;">إرسال</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)

# -------- فاصل --------
st.markdown("---")
st.caption("تم بناء هذا الموقع باستخدام Streamlit | جميع الحقوق محفوظة © 2025")
