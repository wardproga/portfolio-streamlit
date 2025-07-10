# ✅ ملف app.py النهائي لموقع معاذ النمرات

import streamlit as st import plotly.graph_objects as go import datetime import folium from streamlit_folium import st_folium import base64

st.set_page_config(page_title="ملف أعمال معاذ", layout="wide")

اللغة

language = st.sidebar.selectbox("🌐 اختر اللغة", ["العربية", "English"])

الترجمة

text = { "العربية": { "welcome": "👋 مرحباً بك في ملف أعمال معاذ النمرات!", "about": "من أنا", "skills": "المهارات", "experience": "الخبرات", "cv": "السيرة الذاتية", "certificates": "الشهادات", "projects": "المشاريع", "rating": "تقييم المهارات", "project_zip": "تحميل مشروع", "calendar": "تحديد موعد", "map": "خريطة العمل", "contact": "تواصل معي" }, "English": { "welcome": "👋 Welcome to Moad Al-Nimrat's Portfolio!", "about": "About Me", "skills": "Skills", "experience": "Experience", "cv": "CV", "certificates": "Certificates", "projects": "Projects", "rating": "Skill Rating", "project_zip": "Download Project", "calendar": "Book Appointment", "map": "Work Map", "contact": "Contact Me" } }

إشعار ترحيبي

if "welcome_shown" not in st.session_state: st.session_state["welcome_shown"] = True st.success(text[language]["welcome"])

القائمة الجانبية

section = st.sidebar.radio("🔍", [ text[language]["about"], text[language]["skills"], text[language]["experience"], text[language]["cv"], text[language]["certificates"], text[language]["projects"], text[language]["rating"], text[language]["project_zip"], text[language]["calendar"], text[language]["map"], text[language]["contact"] ])

الأقسام

if section == text[language]["about"]: st.header("👤 " + text[language]["about"]) st.markdown(""" الاسم: معاذ محمود مصطفى النمرات
الوظيفة: مطور برمجيات ومحلل بيانات
الخبرة: 14 سنة في التعليم المدرسي
المؤهل: بكالوريوس علم الحاسوب – جامعة آل البيت
المهارات: Python, Pandas, Streamlit, Git, C++, PHP, Laravel, Web Development, JavaScript """)

elif section == text[language]["skills"]: st.header("💡 " + text[language]["skills"]) st.markdown(""" - Python - Pandas / NumPy - Streamlit - Git & GitHub - C++, PHP, Laravel - Web Development - JavaScript """)

elif section == text[language]["experience"]: st.header("🕓 " + text[language]["experience"]) timeline_html = """ <link rel='stylesheet' href='https://cdn.jsdelivr.net/npm/timeline-css@1.0.4/timeline.min.css' /> <div class='timeline'> <div class='timeline-item'><div class='timeline-content'><h3>2009 - 2012</h3><p>مدرس حاسوب - المرحلة الثانوية</p></div></div> <div class='timeline-item'><div class='timeline-content'><h3>2013 - 2016</h3><p>مطور نظم مدرسية - OpenEMIS</p></div></div> <div class='timeline-item'><div class='timeline-content'><h3>2017 - 2020</h3><p>محلل بيانات تعليمية</p></div></div> <div class='timeline-item'><div class='timeline-content'><h3>2021 - الآن</h3><p>مطور مستقل - Python & Streamlit</p></div></div> </div> <style>.timeline { direction: rtl; }</style> """ st.components.v1.html(timeline_html, height=600)

elif section == text[language]["cv"]: st.header("📄 " + text[language]["cv"]) st.download_button("📥 تحميل السيرة الذاتية PDF", open("downloads/cv.pdf", "rb"), file_name="cv.pdf") st.download_button("📥 تحميل السيرة الذاتية Word", open("downloads/cv.docx", "rb"), file_name="cv.docx")

elif section == text[language]["certificates"]: st.header("📜 " + text[language]["certificates"]) col1, col2 = st.columns(2) with col1: st.image("assets/certificate1.png", caption="شهادة Python", use_column_width=True) with col2: st.image("assets/certificate2.png", caption="شهادة تحليل البيانات", use_column_width=True)

elif section == text[language]["projects"]: st.header("🚀 " + text[language]["projects"]) st.markdown(""" ### مشروع نظام الحوسبة التعليمية - OpenEMIS 🔗 رابط المشروع - تم تطويره باستخدام Streamlit وPython - يتيح تتبع أداء الطلاب والمعلمين وإعداد التقارير """)

elif section == text[language]["rating"]: st.header("📊 " + text[language]["rating"]) skills = ["Python", "Pandas", "NumPy", "Streamlit", "Git", "C++", "Laravel"] levels = [95, 90, 85, 90, 80, 75, 80] chart_type = st.radio("اختر نوع الرسم البياني:", ["📊 عمودي", "🟢 دائري"]) if chart_type == "📊 عمودي": fig = go.Figure([go.Bar(x=skills, y=levels, marker_color='seagreen')]) st.plotly_chart(fig, use_container_width=True) else: fig = go.Figure([go.Pie(labels=skills, values=levels, hole=0.3)]) st.plotly_chart(fig, use_container_width=True)

elif section == text[language]["project_zip"]: st.header("🗃️ " + text[language]["project_zip"]) with open("downloads/streamlit_project.zip", "rb") as zip_file: st.download_button("📦 تحميل المشروع (ZIP)", zip_file, file_name="streamlit_project.zip")

elif section == text[language]["calendar"]: st.header("📅 " + text[language]["calendar"]) date = st.date_input("📆 اختر التاريخ") time = st.time_input("⏰ اختر الوقت") name = st.text_input("اسمك") method = st.selectbox("طريقة التواصل", ["واتساب", "بريد إلكتروني", "مكالمة"]) info = st.text_input("أدخل وسيلة التواصل") if st.button("✅ تأكيد الحجز"): st.success(f"تم تسجيل موعدك بنجاح في {date} الساعة {time} عبر {method}.")

elif section == text[language]["map"]: st.header("📍 " + text[language]["map"]) work_map = folium.Map(location=[32.3, 36.3], zoom_start=7) folium.Marker([32.5522, 36.0082], tooltip="2009 - 2012", popup="مدرسة الزرقاء").add_to(work_map) folium.Marker([32.5, 35.9], tooltip="2012", popup="جامعة آل البيت").add_to(work_map) folium.Marker([31.95, 35.9], tooltip="2014 - الآن", popup="مطور نظم - عمان").add_to(work_map) st_folium(work_map, width=700, height=500)

elif section == text[language]["contact"]: st.header("📨 " + text[language]["contact"]) st.markdown(""" 📧 البريد الإلكتروني: wardproga@gmail.com
📱 واتساب: 00962775254934 """)

