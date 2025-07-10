import streamlit as st

# إعدادات الصفحة
st.set_page_config(page_title="ملف أعمال معاذ النمرات", page_icon="💼", layout="wide")

# تفعيل الوضع الليلي/النهاري
theme = st.radio("اختر المظهر:", ["🌞 الوضع النهاري", "🌙 الوضع الليلي"])
if theme == "🌙 الوضع الليلي":
    st.markdown("""
        <style>
            body, .stApp {
                background-color: #0e1117;
                color: white;
            }
        </style>
    """, unsafe_allow_html=True)

# التنقل الجانبي
section = st.sidebar.radio("🔍 التنقل بين الأقسام", [
    "من أنا؟", 
    "المهارات", 
    "الخبرات", 
    "السيرة الذاتية", 
    "📜 الشهادات", 
    "معرض المشاريع", 
    "تقييم المهارات", 
    "تقييم تفاعلي", 
    "روابط مهمة", 
    "تواصل معي"
])

# القسم: من أنا؟
if section == "من أنا؟":
    st.title("مرحباً بكم في ملف أعمالي 💼")
    st.subheader("من أنا؟")
    st.write("""
    أنا مطور ومحلل بيانات مهتم بمجالات تعلم الآلة وتحليل البيانات.
    أسعى لاستخدام البرمجة لإيجاد حلول ذكية للمشكلات.
    أعمل في مجال التعليم منذ أكثر من 14 سنة، وخريج جامعة آل البيت بتخصص علم الحاسوب.
    """)

# القسم: المهارات
elif section == "المهارات":
    st.header("🧠 المهارات")
    st.markdown("""
    - 🐍 Python  
    - 📊 تحليل البيانات (Pandas, NumPy)  
    - 🖥️ Streamlit  
    - 🌐 Git & GitHub  
    - 💻 C++  
    - ⚙️ PHP / Laravel  
    - 🎨 JavaScript / HTML / CSS  
    """)

# القسم: الخبرات
elif section == "الخبرات":
    st.header("🧩 الخبرات")
    st.write("أكثر من 14 سنة في التعليم، شاركت في تطوير نظام OpenEMIS التعليمي وتحسين بيئة التعلم الرقمي.")

# القسم: السيرة الذاتية
elif section == "السيرة الذاتية":
    st.header("📄 السيرة الذاتية")
    st.download_button("تحميل السيرة الذاتية (PDF)", 
                       data=open("CV_Moad_Nimrat.pdf", "rb").read(), 
                       file_name="CV_Moad_Nimrat.pdf")
    st.download_button("تحميل السيرة الذاتية (Word)", 
                       data=open("CV_Moad_Nimrat.docx", "rb").read(), 
                       file_name="CV_Moad_Nimrat.docx")

# ✅ القسم الجديد: الشهادات
elif section == "📜 الشهادات":
    st.header("📜 شهاداتي")
    st.write("إليك مجموعة من الشهادات التي حصلت عليها:")

    certificate_files = [
        "certificate_final_streamlit.jpg",
        "images.jpeg",
        "images.png",
        "laravel-featured.png"
    ]

    cols = st.columns(2)
    for i, cert in enumerate(certificate_files):
        with cols[i % 2]:
            st.image(f"certificates/{cert}", 
                     caption=cert.replace("_", " ").replace("-", " ").replace(".jpg", "").replace(".png", "").replace(".jpeg", ""),
                     use_column_width=True)

# القسم: معرض المشاريع
elif section == "معرض المشاريع":
    st.header("🗂️ معرض المشاريع")
    st.write("🔗 [مشروع Streamlit الخاص بي](https://moadau.streamlit.app)")

# القسم: تقييم المهارات
elif section == "تقييم المهارات":
    st.header("📊 تقييم المهارات")
    st.write("سيتم عرض تقييم المهارات باستخدام الرسوم البيانية لاحقًا.")

# القسم: تقييم تفاعلي
elif section == "تقييم تفاعلي":
    st.header("✅ تقييم تفاعلي")
    st.write("أضفنا هذه الميزة لاحقًا باستخدام عناصر إدخال وتفاعل.")

# القسم: روابط مهمة
elif section == "روابط مهمة":
    st.header("🌐 روابط مهمة")
    st.markdown('[زيارة حسابي على GitHub](https://github.com/wardproga)')

# القسم: تواصل معي
elif section == "تواصل معي":
    st.header("📬 تواصل معي")
    with st.form("contact_form"):
        name = st.text_input("اسمك الكامل")
        email = st.text_input("بريدك الإلكتروني")
        message = st.text_area("اكتب رسالتك هنا...")
        submitted = st.form_submit_button("إرسال")
        if submitted:
            st.success("تم إرسال رسالتك بنجاح! سأقوم بالتواصل معك قريباً.")
