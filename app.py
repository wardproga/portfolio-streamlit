import streamlit as st
# إضافة اختيار الوضع الليلي أو النهاري
mode = st.selectbox("اختر المظهر:", ["🌞 الوضع النهاري", "🌙 الوضع الليلي"])

# CSS لتغيير الألوان بناءً على الوضع المختار
if mode == "🌞 الوضع النهاري":
    st.markdown(
        """
        <style>
        body {
            background-color: #ffffff;
            color: #000000;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
else:
    st.markdown(
        """
        <style>
        body {
            background-color: #0e1117;
            color: #ffffff;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
# -------- إعداد الصفحة --------
st.set_page_config(page_title="ملف أعمال معاذ", layout="centered")

# -------- من أنا --------
st.title("مرحباً بكم في ملف أعمالي 💼")
st.subheader("من أنا؟")
st.write("""
أنا مطور ومحلل بيانات مهتم بمجالات تعلم الآلة وتحليل البيانات.  
أسعى لاستخدام البرمجة لإيجاد حلول ذكية للمشكلات.  
أعمل في مجال التعليم منذ أكثر من 14 سنة، وخريج جامعة آل البيت بتخصص علم الحاسوب.
""")

# -------- المهارات --------
st.header("🧠 المهارات")
skills = [
    "🐍 Python",
    "📊 تحليل البيانات (Pandas, NumPy)",
    "💻 Streamlit",
    "🌐 Git & GitHub",
    "🧠 C++",
    "🕸 PHP / Laravel",
    "🧠 JavaScript / HTML / CSS"
]
for skill in skills:
    st.write(f"- {skill}")

# -------- السيرة الذاتية --------
st.header("📄 السيرة الذاتية")

# تحميل PDF
with open("CV_Moad_Nimrat.pdf", "rb") as pdf_file:
    pdf_bytes = pdf_file.read()
st.download_button(
    label="📄 تحميل السيرة الذاتية (PDF)",
    data=pdf_bytes,
    file_name="CV_Moad_Nimrat.pdf",
    mime="application/pdf"
)

# تحميل Word
with open("CV_Moad_Nimrat.docx", "rb") as docx_file:
    docx_bytes = docx_file.read()
st.download_button(
    label="📄 تحميل السيرة الذاتية (Word)",
    data=docx_bytes,
    file_name="CV_Moad_Nimrat.docx",
    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
)

# -------- روابط مهمة --------
st.header("🌍 روابط مهمة")
st.markdown("[🔗 زيارة حسابي على GitHub](https://github.com/wardproga)")

# -------- نموذج تواصل --------
st.header("📬 تواصل معي")
contact_form = """
<form action="https://formsubmit.co/wardproga@gmail.com" method="POST">
    <input type="text" name="name" placeholder="اسمك الكامل" required><br><br>
    <input type="email" name="email" placeholder="بريدك الإلكتروني" required><br><br>
    <textarea name="message" placeholder="اكتب رسالتك هنا..." rows="5" required></textarea><br><br>
    <button type="submit">إرسال</button>
</form>
"""
st.markdown(contact_form, unsafe_allow_html=True)

# -------- تذييل --------
st.markdown("---")
st.write("© 2025 جميع الحقوق محفوظة | تم بناء هذا الموقع باستخدام Streamlit")
