import streamlit as st
import plotly.graph_objects as go
import datetime
import streamlit.components.v1 as components
import calendar
import pandas as pd
import requests
import os
from streamlit_calendar import calendar

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

# CSS مخصص
st.markdown("""
    <style>
    .fade-in {
        animation: fadeIn ease 2s;
    }
    @keyframes fadeIn {
        0% {opacity:0; transform: translateY(20px);}
        100% {opacity:1; transform: translateY(0);}
    }
    .card {
        background-color: #f9f9f9;
        border-radius: 10px;
        padding: 20px;
        margin: 10px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    .card:hover {
        box-shadow: 0 8px 16px rgba(0,0,0,0.2);
    }
    .timeline {
        border-left: 4px solid indigo;
        margin-left: 20px;
        padding-left: 20px;
    }
    .timeline-event {
        margin-bottom: 30px;
    }
    .timeline-event h4 {
        margin: 0;
        color: indigo;
    }
    .timeline-event p {
        margin: 5px 0 0 0;
        color: #555;
    }
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

# من أنا؟
if section == texts[lang]['sections'][0]:
    st.markdown(f"<div class='fade-in'><h2 style='text-align: center;'>{texts[lang]['welcome']}</h2></div>", unsafe_allow_html=True)
    st.video("https://www.youtube.com/watch?v=VDoqL9pChrk")
    st.write("👆 فيديو تعريفي بسيط")

# السيرة الذاتية
elif section == texts[lang]['sections'][3]:
    st.download_button("⬇️ تحميل السيرة الذاتية PDF", "سيرتي الذاتية".encode(), file_name="CV.pdf")
    st.download_button("⬇️ تحميل السيرة الذاتية Word", "سيرتي الذاتية".encode(), file_name="CV.docx")

# معرض المشاريع
elif section == texts[lang]['sections'][4]:
    st.markdown("""
        <div class='fade-in'>
            <h2 style='text-align: center;'>🎯 معرض المشاريع</h2>
            <div style='display: flex; flex-wrap: wrap; gap: 20px; justify-content: center;'>

                <div class='card' style='width: 300px;'>
                    <h4>📘 نظام Open EMIS</h4>
                    <p>نظام حوسبة متكامل لإدارة التعليم المدرسي.</p>
                    <a href='https://moadau.streamlit.app' target='_blank'>🔗 معاينة المشروع</a>
                </div>

                <div class='card' style='width: 300px;'>
                    <h4>📊 تحليل بيانات المبيعات</h4>
                    <p>لوحة بيانات تفاعلية باستخدام Python وPandas.</p>
                    <a href='https://github.com/wardproga/sales' target='_blank'>🔗 زيارة GitHub</a>
                </div>

            </div>
        </div>
    """, unsafe_allow_html=True)

# تقويم
elif section == texts[lang]['sections'][8]:
    st.markdown(f"<div class='fade-in'><h2 style='text-align: center;'>📅 تقويم المهام</h2></div>", unsafe_allow_html=True)
    events = [
        {"title": "تطوير مشروع", "start": "2025-07-15T10:00:00", "end": "2025-07-15T12:00:00"},
        {"title": "ورشة تحليل بيانات", "start": "2025-07-18T14:00:00", "end": "2025-07-18T16:00:00"}
    ]
    calendar_options = {"initialView": "timeGridWeek", "editable": False, "selectable": False}
    calendar(events=events, options=calendar_options)

# خريطة العمل
elif section == texts[lang]['sections'][9]:
    st.markdown(f"<div class='fade-in'><h2 style='text-align: center;'>🗺️ مواقع العمل</h2></div>", unsafe_allow_html=True)
    map_data = pd.DataFrame({
        'lat': [31.9539, 32.3809],
        'lon': [35.9106, 36.2252],
        'place': ['وزارة التربية والتعليم', 'جامعة آل البيت']
    })
    st.map(map_data, zoom=7)
    for i in range(len(map_data)):
        st.markdown(f"- 📍 {map_data.place[i]}")

# الخط الزمني
elif section == texts[lang]['sections'][10]:
    st.markdown("<div class='fade-in'><h2 style='text-align: center;'>📌 الخط الزمني المهني</h2></div>", unsafe_allow_html=True)
    st.markdown("""
    <div class='timeline'>
        <div class='timeline-event'>
            <h4>🎓 2010 - التخرج من جامعة آل البيت</h4>
            <p>بكالوريوس علم الحاسوب</p>
        </div>
        <div class='timeline-event'>
            <h4>🏫 2011–2024 - العمل في التعليم</h4>
            <p>أكثر من 14 سنة خبرة في التعليم المدرسي</p>
        </div>
        <div class='timeline-event'>
            <h4>📊 2023 - التخصص في تحليل البيانات</h4>
        </div>
        <div class='timeline-event'>
            <h4>🖥️ 2024 - تطوير نظام Open EMIS</h4>
        </div>
    </div>
    """, unsafe_allow_html=True)

# نموذج تواصل
elif section == texts[lang]['sections'][11]:
    st.markdown(f"<div class='fade-in'><h2 style='text-align: center;'>{texts[lang]['contact_title']}</h2></div>", unsafe_allow_html=True)
    with st.form(key='contact_form'):
        name = st.text_input(texts[lang]['name'])
        email = st.text_input(texts[lang]['email'])
        message = st.text_area(texts[lang]['message'])
        submit_button = st.form_submit_button(texts[lang]['send'])
        if submit_button:
            if name and email and message:
                st.success("✅ تم إرسال رسالتك بنجاح!")
            else:
                st.warning("⚠️ يرجى ملء جميع الحقول.")

# تقييم تفاعلي
elif section == texts[lang]['sections'][6]:
    st.markdown(f"<div class='fade-in'><h2 style='text-align: center;'>📈 تقييمك يهمني</h2></div>", unsafe_allow_html=True)
    rating = st.slider("🌟 اختر تقييمك (1 إلى 10)", 1, 10, 5)
    if rating <= 3:
        st.warning("😕 نعتذر إذا لم تكن تجربتك جيدة. يسعدنا معرفة رأيك.")
    elif rating <= 7:
        st.info("🙂 شكرًا على تقييمك! سنواصل التحسين.")
    else:
        st.success("🤩 سعيد أن تجربتك كانت ممتازة!")

# حجز موعد
elif section == texts[lang]['sections'][12]:
    st.markdown(f"<div class='fade-in'><h2 style='text-align: center;'>{texts[lang]['booking']}</h2></div>", unsafe_allow_html=True)
    with st.form(key='appointment_form'):
        name = st.text_input(texts[lang]['name'])
        email = st.text_input(texts[lang]['email'])
        date = st.date_input(texts[lang]['date'])
        time = st.time_input(texts[lang]['time'])
        submitted = st.form_submit_button(texts[lang]['book'])
        if submitted and name and email:
            st.success("✅ تم حجز الموعد بنجاح!")
        else:
            st.warning("يرجى ملء جميع الحقول.")
