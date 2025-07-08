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
# روابط مهمة
st.markdown("""
### 🌐 روابط خارجية
- [🔗 زيارة حسابي على GitHub](https://github.com/wardproga)
- [📄 عرض السيرة الذاتية (PDF)](https://github.com/wardproga/portfolio-streamlit/raw/main/CV_Moad_Nimrat.pdf)
""")
st.header("المهارات")
st.markdown("""
- Python 🐍  
- تحليل البيانات (Pandas, NumPy) 📊  
- Streamlit 🖥️  
- Git & GitHub 🌐  
- التفكير التحليلي والمنطقي 🧠
""")
import streamlit as st
import base64

# عرض أزرار تحميل السيرة الذاتية
st.subheader("📄 السيرة الذاتية")

def download_button(file_path, file_label):
    with open(file_path, "rb") as f:
        data = f.read()
    b64 = base64.b64encode(data).decode()
    href = f'<a href="data:application/octet-stream;base64,{b64}" download="{file_path}">⬇️ تحميل {file_label}</a>'
    st.markdown(href, unsafe_allow_html=True)

download_button("CV_Moad_Nimrat.pdf", "السيرة الذاتية PDF")
download_button("CV_Moad_Nimrat.docx", "السيرة الذاتية Word")
download_button("CV_Moad_Nimrat.html", "السيرة الذاتية HTML")

# المشاريع
st.header("📂 المشاريع")
st.write("إليك بعض مشاريعي:")
st.markdown("""
- [مشروع تحليل بيانات مبيعات](https://example.com)
- [تطبيق واجهة Streamlit](https://example.com)
""")

# التواصل
st.header("📬  تواصل معي ")
st.write("لأي استفسار، لا تتردد في التواصل معي عبر البريد الإلكتروني:")
st.markdown("**wardproga@gmail.com**")
st.header("📬 تواصل معي")

# زر تحميل السيرة الذاتية
with open("cv.pdf", "rb") as file:
    btn = st.download_button(
        label="📄 تحميل السيرة الذاتية",
        data=file,
        file_name="cv.pdf",
        mime="application/pdf"
    )
    st.header("📬 تواصل معي")
contact_form = """
<form action="https://formsubmit.co/wardproga@gmail.com" method="POST">
    <input type="text" name="name" placeholder="الاسم الكامل" required style="width:100%; padding:8px; margin-bottom:8px">
    <input type="email" name="email" placeholder="البريد الإلكتروني" required style="width:100%; padding:8px; margin-bottom:8px">
    <textarea name="message" placeholder="رسالتك" required style="width:100%; padding:8px; height:100px;"></textarea>
    <button type="submit" style="margin-top:10px; padding:10px 20px; background:#4CAF50; color:white; border:none;">إرسال</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)
