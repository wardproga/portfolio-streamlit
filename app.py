from pathlib import Path
import streamlit as st

# إعداد الصفحة
st.set_page_config(
    page_title="ملف أعمال معاذ النمرات",
    page_icon="💼",
    layout="centered"
)

# ----------- العنوان والترحيب -----------
st.title("مرحباً بكم في ملف أعمالي 💼")

# ----------- من أنا؟ -----------
st.header("من أنا؟")
st.write("""
أنا معاذ محمود النمرات، مطوّر برمجيات ومحلل بيانات بخبرة تزيد عن 14 عامًا في التعليم والتقنية.  
أمتلك شغفًا بمجالات تعلم الآلة، تحليل البيانات، وتصميم الحلول الذكية باستخدام البرمجة.  
أسعى لاستخدام المهارات التقنية في تطوير التعليم وتحسين الأداء المؤسسي.  
""")

# ----------- المهارات -----------
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
st.markdown("\n".join(f"- {skill}" for skill in skills))

# ----------- تحميل السيرة الذاتية -----------
st.header("📄 السيرة الذاتية")
cv_path = Path("CV_Moad_Nimrat.pdf")
if cv_path.is_file():
    with open(cv_path, "rb") as pdf_file:
        PDFbyte = pdf_file.read()
    st.download_button(
        label="📥 تحميل السيرة الذاتية (PDF)",
        data=PDFbyte,
        file_name="CV_Moad_Nimrat.pdf",
        mime="application/octet-stream"
    )
else:
    st.error("⚠️ لم يتم العثور على ملف السيرة الذاتية داخل المشروع.")

# ----------- روابط مهمة -----------
st.header("🌍 روابط مهمة")
st.markdown("[🔗 زيارة حساب GitHub](https://github.com/wardproga)")

# ----------- تواصل معي -----------
st.header("📬 تواصل معي")
contact_form = """
<form action="https://formsubmit.co/wardproga@gmail.com" method="POST">
    <input type="text" name="name" placeholder="اسمك الكامل" required>
    <input type="email" name="email" placeholder="بريدك الإلكتروني" required>
    <textarea name="message" placeholder="اكتب رسالتك هنا..." required></textarea>
    <button type="submit">إرسال</button>
</form>
"""
st.markdown(contact_form, unsafe_allow_html=True)

# ----------- تذييل -----------
st.write("---")
st.write("جميع الحقوق محفوظة © 2025 | تم بناء هذا الموقع باستخدام Streamlit")
