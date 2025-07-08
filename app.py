import streamlit as st
import base64

# --- العنوان الرئيسي ---
st.title("👋 مرحباً بكم في ملف أعمالي")

# --- من أنا ---
st.header("من أنا؟")
st.write("""
أنا مطور ومحلل بيانات مهتم بمجالات تعلم الآلة وتحليل البيانات.
أسعى لاستخدام البرمجة لإيجاد حلول ذكية للمشكلات.
أعمل في مجال التعليم منذ أكثر من 14 سنة، وخريج جامعة آل البيت بتخصص علم الحاسوب.
""")

# --- المهارات ---
st.header("المهارات")
st.markdown("""
- Python 🐍  
- تحليل البيانات (Pandas, NumPy) 📊  
- Streamlit 💻  
- Git & GitHub 🌐  
- C++  
- PHP  
- Laravel  
- JavaScript  
- تطوير الويب (HTML, CSS, JS)  
- التفكير التحليلي والمنطقي 🧠
""")

# --- السيرة الذاتية ---
st.subheader("📄 السيرة الذاتية")

# زر تحميل الملفات
def download_button(file_path, file_label):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        href = f'<a href="data:application/octet-stream;base64,{b64}" download="{file_path}">📥 تحميل {file_label}</a>'
        st.markdown(href, unsafe_allow_html=True)

download_button("CV_Moad_Nimrat.pdf", "السيرة الذاتية PDF")
download_button("CV_Moad_Nimrat.docx", "السيرة الذاتية Word")
download_button("CV_Moad_Nimrat.html", "السيرة الذاتية HTML")

# --- المشاريع ---
st.header("📁 المشاريع")
st.write("إليك بعض مشاريعي:")

st.markdown("""
- 🔗 [ملف الأعمال باستخدام Streamlit](https://moadau.streamlit.app)
- 🧩 مشروع نظام الحوسبة التعليمية Open EMIS
""")

# --- معلومات التواصل ---
st.header("📬 تواصل معي")
st.markdown("""
- 📧 البريد الإلكتروني: wardproga@gmail.com  
- 📱 واتساب: +962775254934  
- 💼 GitHub: [wardproga](https://github.com/wardproga)
""")
