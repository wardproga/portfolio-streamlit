import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="ملف أعمال معاذ النمرات", page_icon="💼", layout="wide")

# --- الوضع الليلي / النهاري ---
mode = st.selectbox("اختر المظهر:", ["🌞 الوضع النهاري", "🌙 الوضع الليلي"])

def set_custom_theme(mode):
    if mode == "🌙 الوضع الليلي":
        st.markdown("""
            <style>
            body, .stApp {
                background-color: #0e1117;
                color: #FFFFFF;
            }
            div, p, label, input, textarea {
                color: #FFFFFF !important;
            }
            .stTextInput>div>div>input {
                background-color: #1e1e1e;
                color: white;
            }
            .stDownloadButton>button {
                background-color: #333333;
                color: white;
            }
            </style>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
            <style>
            body, .stApp {
                background-color: #FFFFFF;
                color: #000000;
            }
            </style>
        """, unsafe_allow_html=True)

set_custom_theme(mode)

# --- الشريط الجانبي ---
st.sidebar.title("🔍 التنقل بين الأقسام")
section = st.sidebar.radio("اختر القسم:", [
    "من أنا؟", 
    "المهارات", 
    "الخبرات",
    "السيرة الذاتية", 
    "معرض المشاريع", 
    "تقييم المهارات", 
    "تقييم تفاعلي",
    "روابط مهمة", 
    "تواصل معي"
])

# --- من أنا ---
if section == "من أنا؟":
    st.title("مرحباً بكم في ملف أعمالي 💼")
    st.subheader("من أنا؟")
    st.write("""
    أنا مطور ومحلل بيانات مهتم بمجالات تعلم الآلة وتحليل البيانات.
    أعمل في مجال التعليم منذ أكثر من 14 سنة، وخريج جامعة آل البيت بتخصص علم الحاسوب.
    أسعى لاستخدام البرمجة لإيجاد حلول ذكية للمشكلات.
    """)

# --- المهارات ---
elif section == "المهارات":
    st.header("🧠 المهارات")
    skills = [
        "🐍 Python",
        "📊 تحليل البيانات (Pandas, NumPy)",
        "🧱 Streamlit",
        "🌐 Git & GitHub",
        "🧠 C++",
        "🕸 PHP / Laravel",
        "🧠 JavaScript / HTML / CSS"
    ]
    st.write("\n".join(f"- {skill}" for skill in skills))

# --- الخبرات ---
elif section == "الخبرات":
    st.header("📅 خبرات العمل")

    experiences = [
        {"المؤسسة": "وزارة التربية والتعليم", "الفترة": "2010 - الآن", "الدور": "معلم حاسوب ومشرف نظم"},
        {"المؤسسة": "مشروع Open EMIS", "الفترة": "2021 - الآن", "الدور": "مطوّر نظام حوسبة تعليمية"},
    ]

    st.write("### سجل خبراتي العملية:")

    st.markdown(
        "<style>th, td {padding: 10px; text-align: right;}</style>",
        unsafe_allow_html=True
    )
    table_md = "| المؤسسة | الفترة | الدور |\n|---|---|---|\n"
    for exp in experiences:
        table_md += f"| {exp['المؤسسة']} | {exp['الفترة']} | {exp['الدور']} |\n"

    st.markdown(table_md)

# --- السيرة الذاتية ---
elif section == "السيرة الذاتية":
    st.header("📄 السيرة الذاتية")
    with open("CV_Moad_Nimrat.pdf", "rb") as pdf_file:
        st.download_button("📥 تحميل السيرة الذاتية (PDF)", pdf_file.read(), file_name="CV_Moad_Nimrat.pdf")
    with open("CV_Moad_Nimrat.docx", "rb") as docx_file:
        st.download_button("📄 تحميل السيرة الذاتية (Word)", docx_file.read(), file_name="CV_Moad_Nimrat.docx")

# --- معرض المشاريع ---
elif section == "معرض المشاريع":
    st.header("📂 معرض المشاريع")
    projects = [
        {
            "title": "Open EMIS",
            "description": "نظام حوسبة تعليمية.",
            "link": "https://example.com/open-emis",
            "image": "https://cdn-icons-png.flaticon.com/512/3135/3135715.png"
        },
        {
            "title": "ملف الأعمال باستخدام Streamlit",
            "description": "موقع تفاعلي يعرض السيرة الذاتية والمهارات.",
            "link": "https://moadau.streamlit.app",
            "image": "https://cdn-icons-png.flaticon.com/512/2721/2721293.png"
        },
    ]
    cols = st.columns(2)
    for i, p in enumerate(projects):
        with cols[i % 2]:
            st.image(p["image"], width=80)
            st.subheader(p["title"])
            st.write(p["description"])
            st.markdown(f"[🔗 زيارة المشروع]({p['link']})")

# --- تقييم المهارات ---
elif section == "تقييم المهارات":
    st.header("📈 تقييم المهارات")
    ratings = {
        "Python": 9,
        "Pandas / NumPy": 8,
        "Streamlit": 9,
        "Git / GitHub": 8,
        "C++": 6,
        "PHP / Laravel": 7,
        "JavaScript / HTML / CSS": 7,
    }
    fig = go.Figure(data=[go.Bar(x=list(ratings.keys()), y=list(ratings.values()), marker_color='indigo')])
    fig.update_layout(title="تقييمي الشخصي لمهاراتي", xaxis_title="المهارة", yaxis_title="التقييم (من 10)")
    st.plotly_chart(fig)

# --- تقييم المهارات التفاعلي ---
elif section == "تقييم تفاعلي":
    st.header("🧪 قيّم مهاراتي بنفسك")

    python_rating = st.slider("Python", 1, 10, 8)
    pandas_rating = st.slider("Pandas / NumPy", 1, 10, 8)
    streamlit_rating = st.slider("Streamlit", 1, 10, 9)
    git_rating = st.slider("Git / GitHub", 1, 10, 8)
    cpp_rating = st.slider("C++", 1, 10, 6)
    php_rating = st.slider("PHP / Laravel", 1, 10, 7)
    js_rating = st.slider("JavaScript / HTML / CSS", 1, 10, 7)

    if st.button("📊 عرض النتائج"):
        st.success("هذه التقييمات التي اخترتها:")
        st.write(f"🐍 Python: {python_rating}/10")
        st.write(f"📊 Pandas / NumPy: {pandas_rating}/10")
        st.write(f"🧱 Streamlit: {streamlit_rating}/10")
        st.write(f"🌐 Git / GitHub: {git_rating}/10")
        st.write(f"🧠 C++: {cpp_rating}/10")
        st.write(f"🕸 PHP / Laravel: {php_rating}/10")
        st.write(f"🧠 JavaScript / HTML / CSS: {js_rating}/10")

# --- روابط مهمة ---
elif section == "روابط مهمة":
    st.header("🌍 روابط مهمة")
    st.markdown("[🔗 GitHub](https://github.com/wardproga)")

# --- تواصل معي ---
elif section == "تواصل معي":
    st.header("📫 تواصل معي")
    st.markdown("""
    <form action="https://formsubmit.co/wardproga@gmail.com" method="POST">
        <input type="text" name="name" placeholder="الاسم" required><br>
        <input type="email" name="email" placeholder="البريد" required><br>
        <textarea name="message" placeholder="اكتب رسالتك هنا..." required></textarea><br>
        <button type="submit">إرسال</button>
    </form>
    """, unsafe_allow_html=True)

# --- تحسين عرض الجوال ---
st.markdown("""
    <style>
    textarea, input, button {
        direction: rtl;
        font-family: 'Cairo', sans-serif;
        font-size: 16px;
        width: 100%;
        padding: 10px;
        margin-bottom: 10px;
    }
    @media only screen and (max-width: 768px) {
        .block-container {
            padding: 1rem;
        }
        img {
            max-width: 100% !important;
            height: auto !important;
        }
        .stButton>button, .stDownloadButton>button {
            width: 100%;
        }
    }
    </style>
""", unsafe_allow_html=True)
