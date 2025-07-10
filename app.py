#app.py (نسخة محسّنة للجوال والكمبيوتر)

import streamlit as st import plotly.graph_objects as go import datetime import streamlit.components.v1 as components import calendar import pandas as pd import requests import os

تحسين عرض الجوال والكمبيوتر

st.markdown(""" <style> @media screen and (max-width: 768px) { section[data-testid="stSidebar"] { display: none; } } .css-1v0mbdj, .css-qrbaxs, .css-1r6slb0 { font-size: 16px !important; line-height: 2 !important; } .stRadio > div { flex-direction: column; } </style> """, unsafe_allow_html=True)

إعداد الصفحة

st.set_page_config(page_title="ملف أعمال معاذ النمرات", page_icon="💼", layout="wide")

زر عرض القائمة للجوال

if st.button("📋 عرض القائمة"): st.sidebar.markdown("## القائمة الجانبية")

اللغة

lang_toggle = st.sidebar.toggle("🌐 عربي / English", value=True) lang = "العربية" if lang_toggle else "English"

عداد الزيارات

counter_file = "counter.txt" if not os.path.exists(counter_file): with open(counter_file, "w") as f: f.write("0") with open(counter_file, "r") as f: visits = int(f.read()) visits += 1 with open(counter_file, "w") as f: f.write(str(visits))

نصوص متعددة اللغات

texts = { "العربية": { "sections": ["من أنا؟", "🏅 معرض الشهادات", "📁 المشاريع", "📊 تقييم المهارات", "📨 تواصل معي", "📆 حجز موعد"], "welcome": "مرحبًا بك في موقعي الشخصي!", "contact_title": "📨 تواصل معي", "name": "الاسم", "email": "البريد الإلكتروني", "message": "رسالتك", "send": "إرسال", "visits": "عدد زيارات الموقع: ", "booking": "📆 نموذج حجز موعد", "book": "حجز الموعد", "date": "اختر التاريخ", "time": "اختر الوقت" }, "English": { "sections": ["About Me", "🏅 Certificates", "📁 Projects", "📊 Skill Evaluation", "📨 Contact Me", "📆 Book Appointment"], "welcome": "Welcome to my personal website!", "contact_title": "📨 Contact Me", "name": "Name", "email": "Email", "message": "Your Message", "send": "Send", "visits": "Website Visits: ", "booking": "📆 Appointment Booking Form", "book": "Book Appointment", "date": "Select Date", "time": "Select Time" } }

التنقل بين الأقسام

section = st.sidebar.radio("🔎 التنقل بين الأقسام", texts[lang]["sections"]) st.sidebar.markdown(f"{texts[lang]['visits']} {visits}")

إشعار ترحيبي

if "first_visit" not in st.session_state: st.session_state.first_visit = True if st.session_state.first_visit: st.toast("👋 مرحبًا بك في موقعي الشخصي!", icon="💼") st.session_state.first_visit = False

من أنا

if section == texts[lang]['sections'][0]: st.header(texts[lang]['welcome']) start_date = datetime.date(2010, 9, 1) today = datetime.date.today() delta = today - start_date years = delta.days // 365 months = (delta.days % 365) // 30 days = (delta.days % 365) % 30 st.success(f"📅 لديك خبرة {years} سنة و {months} شهر و {days} يوم") st.video("https://www.youtube.com/watch?v=VDoqL9pChrk")

معرض الشهادات

if section == texts[lang]['sections'][1]: cert_dir = "certificates" st.markdown("## 🏅 شهاداتي" if lang == "العربية" else "## 🏅 My Certificates") if os.path.exists(cert_dir): files = os.listdir(cert_dir) image_files = [f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg'))] cols = st.columns(2) for i, file in enumerate(image_files): path = os.path.join(cert_dir, file) with cols[i % 2]: st.image(path, caption=file, use_column_width=True)

تواصل معي

if section == texts[lang]['sections'][4]: st.subheader(texts[lang]['contact_title']) with st.form(key="contact_form"): name = st.text_input(texts[lang]['name']) email = st.text_input(texts[lang]['email']) message = st.text_area(texts[lang]['message']) if st.form_submit_button(texts[lang]['send']): if name and email and message: st.success("✅ تم الإرسال بنجاح!" if lang == "العربية" else "✅ Sent successfully!") else: st.warning("يرجى تعبئة جميع الحقول." if lang == "العربية" else "Please fill out all fields.")

حجز موعد

if section == texts[lang]['sections'][5]: st.subheader(texts[lang]['booking']) with st.form(key='appointment_form'): name = st.text_input(texts[lang]['name']) email = st.text_input(texts[lang]['email']) date = st.date_input(texts[lang]['date']) time = st.time_input(texts[lang]['time']) submitted = st.form_submit_button(texts[lang]['book']) if submitted: if name and email: st.success("✅ تم حجز الموعد بنجاح! سيتم التواصل معك قريبًا." if lang == "العربية" else "✅ Appointment booked successfully!") else: st.warning("يرجى ملء جميع الحقول." if lang == "العربية" else "Please complete all fields.")

تعليقات الزوار

st.markdown("---") st.subheader("💬 تعليقات الزوار") with st.form("comment_form"): user_name = st.text_input("الاسم") user_comment = st.text_area("اترك تعليقك") if st.form_submit_button("إرسال"): if user_name and user_comment: with open("comments.txt", "a", encoding="utf-8") as f: f.write(f"{user_name}: {user_comment}\n") st.success("شكراً لتعليقك!") else: st.warning("يرجى إدخال الاسم والتعليق.")

عرض آخر التعليقات

if os.path.exists("comments.txt"): st.markdown("### آخر التعليقات:") with open("comments.txt", "r", encoding="utf-8") as f: comments = f.readlines()[-10:] for comment in comments[::-1]: st.info(comment.strip())

