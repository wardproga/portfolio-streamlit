import streamlit as st
import plotly.graph_objects as go
import datetime
import streamlit.components.v1 as components
import calendar
import pandas as pd
import requests
import os

# إعداد الصفحة
st.set_page_config(page_title="ملف أعمال معاذ النمرات", page_icon="💼", layout="wide")

# عداد الزيارات
counter_file = "counter.txt"
if not os.path.exists(counter_file):
    with open(counter_file, "w") as f:
        f.write("0")

with open(counter_file, "r") as f:
    visits = int(f.read())
visits += 1
with open(counter_file, "w") as f:
    f.write(str(visits))

# إدراج CSS
st.markdown("""
    <style>
    .fade-in {
        animation: fadeIn ease 2s;
    }
    @keyframes fadeIn {
        0% {opacity:0; transform: translateY(20px);}
        100% {opacity:1; transform: translateY(0);}
    }
    .card { background-color: #f9f9f9; border-radius: 10px; padding: 20px; margin: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); }
    .card:hover { box-shadow: 0 8px 16px rgba(0,0,0,0.2); }
    .timeline { border-left: 4px solid indigo; margin-left: 20px; padding-left: 20px; }
    .timeline-event { margin-bottom: 30px; }
    .timeline-event h4 { margin: 0; color: indigo; }
    .timeline-event p { margin: 5px 0 0 0; color: #555; }
    </style>
""", unsafe_allow_html=True)

# اللغة
lang_toggle = st.sidebar.toggle("🌐 عربي / English", value=True)
lang = "العربية" if lang_toggle else "English"

# الوضع الليلي
mode = st.sidebar.radio("اختر المظهر:", ["🌞 الوضع النهاري", "🌙 الوضع الليلي"])
if mode == "🌙 الوضع الليلي":
    st.markdown("""
        <style>
        body { background-color: #111; color: white; }
        .card { background-color: #222; color: white; }
        .timeline-event p { color: #ccc; }
        </style>
    """, unsafe_allow_html=True)

# الترجمة
texts = {
    "العربية": {
        "sections": ["من أنا؟", "المهارات", "الخبرات", "السيرة الذاتية", "معرض المشاريع", "تقييم المهارات", "تقييم تفاعلي", "📦 تحميل مشروع", "📅 تقويم", "🗺️ خريطة العمل", "الخط الزمني", "تواصل معي", "📆 حجز موعد"],
        "welcome": "مرحبًا بك في موقعي الشخصي!",
        "contact_title": "📨 تواصل معي",
        "name": "الاسم",
        "email": "البريد الإلكتروني",
        "message": "رسالتك",
        "send": "إرسال",
        "visits": "عدد زيارات الموقع: ",
        "booking": "📆 نموذج حجز موعد",
        "book": "حجز الموعد",
        "date": "اختر التاريخ",
        "time": "اختر الوقت"
    },
    "English": {
        "sections": ["About Me", "Skills", "Experience", "Resume", "Portfolio", "Skill Evaluation", "Feedback", "📦 Download Project", "📅 Calendar", "🗺️ Work Map", "Timeline", "Contact Me", "📆 Book Appointment"],
        "welcome": "Welcome to my personal website!",
        "contact_title": "📨 Contact Me",
        "name": "Name",
        "email": "Email",
        "message": "Your Message",
        "send": "Send",
        "visits": "Website Visits: ",
        "booking": "📆 Appointment Booking Form",
        "book": "Book Appointment",
        "date": "Select Date",
        "time": "Select Time"
    }
}

section = st.sidebar.radio("🔎 التنقل بين الأقسام", texts[lang]["sections"])

skills = {
    "Python": 95,
    "Pandas / NumPy": 90,
    "Streamlit": 85,
    "Git & GitHub": 80,
    "C++": 70,
    "PHP / Laravel": 75,
    "HTML / CSS / JS": 85
}

st.sidebar.markdown(f"**{texts[lang]['visits']} {visits}**")

# القسم الأول - الترحيب + فيديو
if section == texts[lang]['sections'][0]:
    st.markdown(f"<div class='fade-in'><h2 style='text-align: center;'>{texts[lang]['welcome']}</h2></div>", unsafe_allow_html=True)
    st.video("https://www.youtube.com/watch?v=VDoqL9pChrk")
    st.write("👆 فيديو تعريفي بسيط (يمكن استبداله لاحقًا برابط خاص بك)")

# نموذج حجز موعد بسيط
if section == texts[lang]["sections"][12]:
    st.markdown(f"<div class='fade-in'><h2 style='text-align: center;'>{texts[lang]['booking']}</h2></div>", unsafe_allow_html=True)
    with st.form(key='appointment_form'):
        name = st.text_input(texts[lang]['name'])
        email = st.text_input(texts[lang]['email'])
        date = st.date_input(texts[lang]['date'])
        time = st.time_input(texts[lang]['time'])
        submitted = st.form_submit_button(texts[lang]['book'])
        if submitted:
            if name and email:
                st.success("✅ تم حجز الموعد بنجاح! سيتم التواصل معك قريبًا.")
            else:
                st.warning("يرجى ملء جميع الحقول.")
