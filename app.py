# app.py

import streamlit as st
import os
import datetime

# إعداد الصفحة
st.set_page_config(page_title="ملف أعمال معاذ", page_icon="💼", layout="wide")

# تحسينات CSS لتصميم الشريط الجانبي بشكل عصري ومتجاوب
st.markdown("""
    <style>
    /* الشريط الجانبي */
    [data-testid="stSidebar"] {
        background-color: #042331;
        width: 220px;
        transition: width 0.3s ease-in-out;
        overflow-x: hidden;
    }

    /* عند تصغير الشاشة */
    @media only screen and (max-width: 768px) {
        [data-testid="stSidebar"] {
            width: 65px !important;
        }
        [data-testid="stSidebar"] .css-1d391kg, 
        [data-testid="stSidebar"] .css-1v3fvcr {
            display: none !important;
        }
    }

    /* عناصر القائمة */
    .sidebar-item {
        color: white;
        padding: 10px 16px;
        font-size: 18px;
        display: flex;
        align-items: center;
        gap: 10px;
        border-bottom: 1px solid #03374e;
        transition: background 0.2s;
    }

    .sidebar-item:hover {
        background-color: #0e94d4;
        cursor: pointer;
    }

    .sidebar-item i {
        color: #0e94d4;
    }

    .active-item {
        background-color: #0e94d4;
        color: white !important;
    }

    </style>
""", unsafe_allow_html=True)

# اللغة
is_arabic = st.sidebar.toggle("🌐 عربي / English", value=True)
lang = "ar" if is_arabic else "en"

# أقسام الموقع
sections = {
    "ar": ["من أنا؟", "🏅 الشهادات", "📁 المشاريع", "📊 المهارات", "📨 تواصل", "📅 حجز موعد"],
    "en": ["About Me", "🏅 Certificates", "📁 Projects", "📊 Skills", "📨 Contact", "📅 Book Appointment"]
}

section = st.sidebar.radio("📋 القائمة", sections[lang], index=0)

# عداد زيارات الموقع
counter_file = "counter.txt"
if not os.path.exists(counter_file):
    with open(counter_file, "w") as f:
        f.write("0")
with open(counter_file, "r") as f:
    visits = int(f.read())
visits += 1
with open(counter_file, "w") as f:
    f.write(str(visits))

st.sidebar.markdown(f"<br><b>{'عدد زيارات الموقع:' if lang == 'ar' else 'Visits:'} {visits}</b>", unsafe_allow_html=True)

# محتوى "من أنا؟"
if section == sections[lang][0]:
    st.title("👋 مرحبًا بك!" if lang == "ar" else "👋 Welcome!")
    st.markdown("""
        <p style='font-size:18px'>
        أنا معاذ النمرات، مطور برمجيات ومحلل بيانات بخبرة تتجاوز 14 عامًا في التعليم والتقنية.
        </p>
    """, unsafe_allow_html=True)

# محتوى "الشهادات"
elif section == sections[lang][1]:
    st.header("🏅 شهاداتي" if lang == "ar" else "🏅 My Certificates")
    cert_dir = "certificates"
    if os.path.exists(cert_dir):
        files = os.listdir(cert_dir)
        image_files = [f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
        cols = st.columns(2)
        for i, file in enumerate(image_files):
            with cols[i % 2]:
                st.image(os.path.join(cert_dir, file), caption=file, use_column_width=True)
    else:
        st.info("لم يتم العثور على شهادات." if lang == "ar" else "No certificates found.")

# محتوى "تواصل"
elif section == sections[lang][4]:
    st.header("📨 تواصل معي" if lang == "ar" else "📨 Contact Me")
    with st.form("contact_form"):
        name = st.text_input("الاسم" if lang == "ar" else "Name")
        email = st.text_input("البريد الإلكتروني" if lang == "ar" else "Email")
        msg = st.text_area("رسالتك" if lang == "ar" else "Your Message")
        if st.form_submit_button("إرسال" if lang == "ar" else "Send"):
            if name and email and msg:
                st.success("✅ تم إرسال الرسالة!" if lang == "ar" else "✅ Message Sent!")
            else:
                st.warning("يرجى تعبئة جميع الحقول." if lang == "ar" else "Please fill all fields.")

# محتوى "حجز موعد"
elif section == sections[lang][5]:
    st.header("📅 حجز موعد" if lang == "ar" else "📅 Book Appointment")
    with st.form("appointment_form"):
        name = st.text_input("الاسم" if lang == "ar" else "Name")
        email = st.text_input("البريد الإلكتروني" if lang == "ar" else "Email")
        date = st.date_input("اختر التاريخ" if lang == "ar" else "Select Date")
        time = st.time_input("اختر الوقت" if lang == "ar" else "Select Time")
        if st.form_submit_button("حجز" if lang == "ar" else "Book"):
            if name and email:
                st.success("✅ تم الحجز بنجاح!" if lang == "ar" else "✅ Appointment booked!")
            else:
                st.warning("يرجى تعبئة جميع الحقول." if lang == "ar" else "Please complete all fields.")

# الأقسام الأخرى
else:
    st.info("🚧 هذا القسم قيد التطوير..." if lang == "ar" else "🚧 This section is under construction...")
