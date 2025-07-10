import streamlit as st
import os
import datetime
from streamlit_option_menu import option_menu

# إعداد الصفحة
st.set_page_config(page_title="ملف أعمال معاذ النمرات", page_icon="💼", layout="wide")

# إعداد ملف عداد الزيارات
counter_file = "counter.txt"
if not os.path.exists(counter_file):
    with open(counter_file, "w") as f:
        f.write("0")
with open(counter_file, "r") as f:
    visits = int(f.read())
visits += 1
with open(counter_file, "w") as f:
    f.write(str(visits))

# دعم اللغة
lang_toggle = st.sidebar.toggle("🌐 عربي / English", value=True)
lang = "العربية" if lang_toggle else "English"

texts = {
    "العربية": {
        "sections": ["من أنا؟", "🏅 الشهادات", "📁 المشاريع", "📊 المهارات", "📨 تواصل", "📆 حجز موعد"],
        "welcome": "مرحبًا بك في موقعي الشخصي!",
        "name": "الاسم",
        "email": "البريد الإلكتروني",
        "message": "رسالتك",
        "send": "إرسال",
        "booking": "نموذج حجز موعد",
        "book": "حجز",
        "date": "اختر التاريخ",
        "time": "اختر الوقت",
        "visits": "عدد زيارات الموقع: ",
        "comments": "💬 تعليقات الزوار",
        "comment_button": "إرسال",
        "success_comment": "✅ شكراً لتعليقك!"
    },
    "English": {
        "sections": ["About", "🏅 Certificates", "📁 Projects", "📊 Skills", "📨 Contact", "📆 Book"],
        "welcome": "Welcome to my personal website!",
        "name": "Name",
        "email": "Email",
        "message": "Message",
        "send": "Send",
        "booking": "Appointment Form",
        "book": "Book",
        "date": "Select date",
        "time": "Select time",
        "visits": "Site visits: ",
        "comments": "💬 Visitor Comments",
        "comment_button": "Send",
        "success_comment": "✅ Thanks for your comment!"
    }
}

# شريط جانبي باستخدام Option Menu
with st.sidebar:
    choice = option_menu(
        menu_title="القائمة" if lang == "العربية" else "Menu",
        options=texts[lang]["sections"],
        icons=["person", "award", "folder", "bar-chart", "envelope", "calendar"],
        menu_icon="cast",
        default_index=0,
        orientation="vertical"
    )
    st.markdown(f"**{texts[lang]['visits']} {visits}**")

# من أنا؟
if choice == texts[lang]["sections"][0]:
    st.title(texts[lang]["welcome"])
    st.video("https://www.youtube.com/watch?v=VDoqL9pChrk")
    start_date = datetime.date(2010, 9, 1)
    delta = datetime.date.today() - start_date
    years, rem = divmod(delta.days, 365)
    months, days = divmod(rem, 30)
    st.success(f"📅 لديك خبرة {years} سنة و {months} شهر و {days} يوم" if lang == "العربية" else f"📅 You have {years} years, {months} months, and {days} days of experience.")

# الشهادات
if choice == texts[lang]["sections"][1]:
    st.header("📜 الشهادات" if lang == "العربية" else "📜 Certificates")
    cert_dir = "certificates"
    if os.path.exists(cert_dir):
        images = [img for img in os.listdir(cert_dir) if img.lower().endswith((".png", ".jpg", ".jpeg"))]
        cols = st.columns(2)
        for i, img in enumerate(images):
            with cols[i % 2]:
                st.image(os.path.join(cert_dir, img), caption=img, use_column_width=True)
    else:
        st.warning("📂 مجلد الشهادات غير موجود." if lang == "العربية" else "📂 Certificates folder not found.")

# المشاريع
if choice == texts[lang]["sections"][2]:
    st.header("📁 المشاريع" if lang == "العربية" else "📁 Projects")
    st.markdown("- ✅ [نظام الحوسبة التعليمية Open EMIS](https://example.com)")

# المهارات
if choice == texts[lang]["sections"][3]:
    st.header("📊 المهارات" if lang == "العربية" else "📊 Skills")
    skills = {
        "Python": 95,
        "Pandas / NumPy": 90,
        "Streamlit": 90,
        "C++": 80,
        "PHP / Laravel": 75,
        "HTML / CSS / JS": 85,
        "Git & GitHub": 80,
    }
    for skill, level in skills.items():
        st.progress(level / 100)
        st.write(f"{skill}: {level}%")

# تواصل
if choice == texts[lang]["sections"][4]:
    st.subheader(texts[lang]["send"])
    with st.form("contact"):
        name = st.text_input(texts[lang]["name"])
        email = st.text_input(texts[lang]["email"])
        msg = st.text_area(texts[lang]["message"])
        if st.form_submit_button(texts[lang]["send"]):
            if name and email and msg:
                st.success("✅ تم الإرسال!" if lang == "العربية" else "✅ Message sent!")
            else:
                st.warning("❗ يرجى تعبئة الحقول." if lang == "العربية" else "❗ Please fill out all fields.")

# حجز موعد
if choice == texts[lang]["sections"][5]:
    st.subheader(texts[lang]["booking"])
    with st.form("booking"):
        name = st.text_input(texts[lang]["name"])
        email = st.text_input(texts[lang]["email"])
        date = st.date_input(texts[lang]["date"])
        time = st.time_input(texts[lang]["time"])
        if st.form_submit_button(texts[lang]["book"]):
            if name and email:
                st.success("📆 تم حجز الموعد بنجاح!" if lang == "العربية" else "📆 Appointment booked!")
            else:
                st.warning("❗ يرجى تعبئة الحقول." if lang == "العربية" else "❗ Please complete all fields.")

# تعليقات الزوار
st.markdown("### 💬 " + texts[lang]["comments"])
with st.form("comments"):
    commenter = st.text_input(texts[lang]["name"])
    comment = st.text_area(texts[lang]["message"])
    if st.form_submit_button(texts[lang]["comment_button"]):
        if commenter and comment:
            with open("comments.txt", "a", encoding="utf-8") as f:
                f.write(f"{commenter}: {comment}\n")
            st.success(texts[lang]["success_comment"])
        else:
            st.warning("❗" + (" يرجى تعبئة الحقول." if lang == "العربية" else " Please fill all fields."))

if os.path.exists("comments.txt"):
    st.markdown("#### 📝 آخر التعليقات:")
    with open("comments.txt", "r", encoding="utf-8") as f:
        for line in f.readlines()[-5:][::-1]:
            st.info(line.strip())
