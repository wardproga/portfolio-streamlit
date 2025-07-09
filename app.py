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
