import streamlit as st
import datetime
import os
from streamlit_option_menu import option_menu

# إعداد الصفحة
st.set_page_config(page_title="ملف أعمال معاذ النمرات", page_icon="💼", layout="wide")

# 💡 تحسين عرض الجوال: CSS مخصص للشاشات الصغيرة
st.markdown("""
    <style>
    /* تقليل عرض الشريط الجانبي في الجوال */
    @media (max-width: 768px) {
        section[data-testid="stSidebar"] {
            width: 200px !important;
            min-width: 200px !important;
        }
    }
    /* تحسين شكل الروابط في الشريط */
    .css-1d391kg, .css-1v0mbdj, .css-znku1x {
        font-size: 16px !important;
        padding: 0.5rem 1rem;
    }
    /* تحسين المسافات */
    .main .block-container {
        padding-top: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# 🔁 اللغة
lang_toggle = st.sidebar.toggle("🌐 عربي / English", value=True)
lang = "ar" if lang_toggle else "en"

# 🔢 عداد الزيارات
counter_file = "counter.txt"
if not os.path.exists(counter_file):
    with open(counter_file, "w") as f:
        f.write("0")
with open(counter_file, "r") as f:
    visits = int(f.read())
visits += 1
with open(counter_file, "w") as f:
    f.write(str(visits))

# 📑 النصوص حسب اللغة
texts = {
    "ar": {
        "menu": "القائمة",
        "sections": ["من أنا؟", "🏅 الشهادات", "📁 المشاريع", "📊 المهارات", "📨 تواصل", "📆 حجز موعد"],
        "welcome": "مرحبًا بك في موقعي الشخصي!",
        "contact_title": "📨 تواصل معي",
        "name": "الاسم",
        "email": "البريد الإلكتروني",
        "message": "رسالتك",
        "send": "إرسال",
        "visits": "عدد زيارات الموقع:",
        "booking": "📆 نموذج حجز موعد",
        "book": "حجز الموعد",
        "date": "اختر التاريخ",
        "time": "اختر الوقت",
        "comment": "💬 تعليقات الزوار",
        "last_comments": "آخر التعليقات:"
    },
    "en": {
        "menu": "Menu",
        "sections": ["About Me", "🏅 Certificates", "📁 Projects", "📊 Skills", "📨 Contact", "📆 Book Appointment"],
        "welcome": "Welcome to my personal website!",
        "contact_title": "📨 Contact Me",
        "name": "Name",
        "email": "Email",
        "message": "Your Message",
        "send": "Send",
        "visits": "Website Visits:",
        "booking": "📆 Appointment Booking Form",
        "book": "Book",
        "date": "Select Date",
        "time": "Select Time",
        "comment": "💬 Visitor Comments",
        "last_comments": "Latest Comments:"
    }
}

T = texts[lang]

# 📌 القائمة الجانبية
with st.sidebar:
    selected = option_menu(
        T["menu"],
        options=T["sections"],
        icons=["person", "award", "folder", "bar-chart", "envelope", "calendar"],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {"padding": "5px", "background-color": "#f8f9fa"},
            "icon": {"color": "#6c757d", "font-size": "20px"},
            "nav-link": {"font-size": "16px", "text-align": "right", "margin": "0px"},
            "nav-link-selected": {"background-color": "#FF4B4B", "color": "white"},
        }
    )
    st.markdown(f"**{T['visits']} {visits}**")

# 🎉 إشعار ترحيبي
if "first_visit" not in st.session_state:
    st.session_state.first_visit = True
if st.session_state.first_visit:
    st.toast("👋 " + T["welcome"], icon="💼")
    st.session_state.first_visit = False

# 🧑‍💻 من أنا؟
if selected == T["sections"][0]:
    st.header(T["welcome"])
    start_date = datetime.date(2010, 9, 1)
    today = datetime.date.today()
    delta = today - start_date
    years = delta.days // 365
    months = (delta.days % 365) // 30
    days = (delta.days % 365) % 30
    st.success(f"📅 لديك خبرة {years} سنة و {months} شهر و {days} يوم" if lang == "ar"
               else f"📅 You have {years} years, {months} months, and {days} days of experience.")
    st.video("https://www.youtube.com/watch?v=VDoqL9pChrk")

# 🏅 الشهادات
elif selected == T["sections"][1]:
    st.subheader(T["sections"][1])
    cert_dir = "certificates"
    if os.path.exists(cert_dir):
        files = os.listdir(cert_dir)
        image_files = [f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
        cols = st.columns(2)
        for i, file in enumerate(image_files):
            path = os.path.join(cert_dir, file)
            with cols[i % 2]:
                st.image(path, caption=file, use_column_width=True)

# 📁 المشاريع
elif selected == T["sections"][2]:
    st.subheader(T["sections"][2])
    st.info("📦 قريبًا ستُضاف المشاريع هنا..." if lang == "ar" else "📦 Projects will be added soon...")

# 📊 المهارات
elif selected == T["sections"][3]:
    st.subheader(T["sections"][3])
    skills = {"Python": 90, "Streamlit": 85, "Pandas": 80, "Git": 70, "HTML/CSS": 75}
    for skill, level in skills.items():
        st.markdown(f"**{skill}**")
        st.progress(level)

# 📨 تواصل معي
elif selected == T["sections"][4]:
    st.subheader(T["contact_title"])
    with st.form(key="contact_form"):
        name = st.text_input(T["name"])
        email = st.text_input(T["email"])
        message = st.text_area(T["message"])
        if st.form_submit_button(T["send"]):
            if name and email and message:
                st.success("✅ تم الإرسال بنجاح!" if lang == "ar" else "✅ Sent successfully!")
            else:
                st.warning("يرجى تعبئة جميع الحقول." if lang == "ar" else "Please fill out all fields.")

# 📆 حجز موعد
elif selected == T["sections"][5]:
    st.subheader(T["booking"])
    with st.form(key="appointment_form"):
        name = st.text_input(T["name"])
        email = st.text_input(T["email"])
        date = st.date_input(T["date"])
        time = st.time_input(T["time"])
        submitted = st.form_submit_button(T["book"])
        if submitted:
            if name and email:
                st.success("✅ تم حجز الموعد بنجاح!" if lang == "ar" else "✅ Appointment booked successfully!")
            else:
                st.warning("يرجى ملء جميع الحقول." if lang == "ar" else "Please complete all fields.")

# 💬 تعليقات الزوار
st.markdown("---")
st.subheader(T["comment"])
with st.form("comment_form"):
    user_name = st.text_input(T["name"])
    user_comment = st.text_area(T["message"])
    if st.form_submit_button(T["send"]):
        if user_name and user_comment:
            with open("comments.txt", "a", encoding="utf-8") as f:
                f.write(f"{user_name}: {user_comment}\n")
            st.success("شكراً لتعليقك!" if lang == "ar" else "Thanks for your comment!")
        else:
            st.warning("يرجى إدخال الاسم والتعليق." if lang == "ar" else "Please enter name and comment.")

# عرض آخر التعليقات
if os.path.exists("comments.txt"):
    st.markdown(f"### {T['last_comments']}")
    with open("comments.txt", "r", encoding="utf-8") as f:
        comments = f.readlines()[-10:]
    for comment in comments[::-1]:
        st.info(comment.strip())
