
import streamlit as st
import base64

# إعداد الصفحة
st.set_page_config(page_title="ملف أعمال معاذ النمرات", page_icon="💼", layout="wide")

# تصميم الهيدر
st.markdown("<h1 style='text-align: center;'>👋 مرحباً بكم في ملف أعمالي</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>معاذ محمود مصطفى النمرات</h3>", unsafe_allow_html=True)
st.markdown("---")

# من أنا
col1, col2 = st.columns([1, 3])
with col1:
    st.image("https://avatars.githubusercontent.com/u/00000000", width=120)  # صورة رمزية عامة (يمكنك تغييرها)
with col2:
    st.subheader("من أنا؟")
    st.write("""
    أنا مطور ومحلل بيانات مهتم بمجالات تعلم الآلة وتحليل البيانات.
    أسعى لاستخدام البرمجة لإيجاد حلول ذكية للمشكلات.
    لدي خبرة 14 سنة في التعليم، وخريج جامعة آل البيت – علم الحاسوب.
    """)

# المهارات
st.markdown("## 🧠 المهارات")
st.markdown("""
- Python 🐍
- تحليل البيانات (Pandas, NumPy) 📊
- Streamlit 💻
- Git & GitHub 🌐
- التفكير التحليلي والمنطقي 🧠
- PHP, Laravel, JavaScript, C++, Web Development 🌍
""")

# روابط مهمة
st.markdown("## 🌐 روابط خارجية")
st.markdown("""
- [🔗 زيارة حسابي على GitHub](https://github.com/wardproga)
- [📄 عرض السيرة الذاتية (PDF)](https://github.com/wardproga/portfolio-streamlit/raw/main/CV_Moad_Nimrat.pdf)
""")

# أزرار تحميل السيرة الذاتية
st.subheader("📁 تحميل السيرة الذاتية")
def download_button(file_path, file_label):
    with open(file_path, "rb") as f:
        data = f.read()
    b64 = base64.b64encode(data).decode()
    href = f'<a href="data:application/octet-stream;base64,{b64}" download="{file_path}">📎 تحميل {file_label}</a>'
    st.markdown(href, unsafe_allow_html=True)

download_button("CV_Moad_Nimrat.pdf", "السيرة الذاتية PDF")
download_button("CV_Moad_Nimrat.docx", "السيرة الذاتية Word")
download_button("CV_Moad_Nimrat.html", "السيرة الذاتية HTML")

# المشاريع
st.markdown("## 📁 المشاريع")
st.markdown("""
- [📊 مشروع ملف الأعمال باستخدام Streamlit](https://moadau.streamlit.app)
""")

# نموذج تواصل
st.markdown("## 📬 تواصل معي")
contact_form = """
<form action="https://formsubmit.co/wardproga@gmail.com" method="POST">
    <input type="text" name="name" placeholder="الاسم الكامل" required style="width:100%; padding:8px; margin-bottom:8px">
    <input type="email" name="email" placeholder="البريد الإلكتروني" required style="width:100%; padding:8px; margin-bottom:8px">
    <textarea name="message" placeholder="رسالتك" required style="width:100%; padding:8px; height:100px;"></textarea>
    <button type="submit" style="margin-top:10px; padding:10px 20px; background:#4CAF50; color:white; border:none;">إرسال</button>
</form>
"""
st.markdown(contact_form, unsafe_allow_html=True)
