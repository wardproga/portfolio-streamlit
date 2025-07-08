import streamlit as st

st.set_page_config(page_title="ملف أعمالي", layout="wide")

# العنوان الرئيسي
st.title("👋 مرحباً بكم في ملف أعمالي")

# نبذة عنك
st.header("من أنا؟")
st.write("""
أنا مطور ومحلل بيانات مهتم بمجالات تعلم الآلة وتحليل البيانات.  
أسعى لاستخدام البرمجة لإيجاد حلول ذكية للمشكلات.
""")

# المهارات
st.header("المهارات")
st.markdown("""
- Python 🐍  
- تحليل البيانات (Pandas, NumPy) 📊  
- Streamlit 🖥️  
- Git & GitHub 🌐  
- التفكير التحليلي والمنطقي 🧠
""")

# المشاريع
st.header("📂 المشاريع")
st.write("إليك بعض مشاريعي:")
st.markdown("""
- [مشروع تحليل بيانات مبيعات](https://example.com)
- [تطبيق واجهة Streamlit](https://example.com)
""")

# التواصل
st.header("📬 تواصل معي")
st.write("لأي استفسار، لا تتردد في التواصل معي عبر البريد الإلكتروني:")
st.markdown("**email@example.com**")

# زر تحميل السيرة الذاتية
with open("cv.pdf", "rb") as file:
    btn = st.download_button(
        label="📄 تحميل السيرة الذاتية",
        data=file,
        file_name="cv.pdf",
        mime="application/pdf"
    )