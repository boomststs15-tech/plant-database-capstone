import streamlit as st

from database import initialize_database, search_plants

st.set_page_config(page_title="ฐานข้อมูลสายพันธุ์พืช", page_icon="🌱")

@st.cache_resource
def setup_database() -> bool:
    initialize_database()
    return True

try:
    setup_database()
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Prompt:wght@400;500;600;700&display=swap');
    .stApp { background:#f7faf7; font-family:'Prompt',sans-serif; }
    [data-testid='stSidebar'] { background:#103b2a; }
    [data-testid='stSidebar'] * { color:#eefcf3 !important; }
    .hero { padding:3.5rem 3rem; border-radius:28px; background:linear-gradient(135deg,#0f5132,#35a66f); color:white; box-shadow:0 15px 35px rgba(15,81,50,.18); }
    .hero h1 { font-size:2.7rem; line-height:1.2; margin:0 0 .8rem; }
    .hero p { font-size:1.15rem; opacity:.92; margin:0; }
    .section-title { color:#123c2b; font-weight:700; margin-top:1.8rem; }
    .card { padding:1.35rem; border:1px solid #dcefe2; border-radius:20px; background:white; min-height:125px; box-shadow:0 8px 22px rgba(25,75,45,.06); }
    .card h3 { color:#167044; margin:0 0 .5rem; font-size:1.15rem; }
    .card p { color:#527061; margin:0; line-height:1.6; }
    div[data-testid='stMetric'] { background:white; border:1px solid #dcefe2; padding:1rem; border-radius:16px; box-shadow:0 6px 18px rgba(25,75,45,.05); }
    div[data-testid='stMetricLabel'] { color:#527061; }
    div[data-testid='stDataFrame'] { border:1px solid #dcefe2; border-radius:16px; overflow:hidden; }
    </style>
    """, unsafe_allow_html=True)
    page = st.sidebar.radio("เมนูหลัก", ["หน้าแรก", "ฐานข้อมูลพืช"])

    if page == "หน้าแรก":
        st.markdown("""
        <section class="hero">
          <h1>ระบบฐานข้อมูลสายพันธุ์พืชทางการเกษตร</h1>
          <p>แหล่งรวมข้อมูลพืชเบื้องต้นสำหรับนักศึกษาเทคโนโลยีการเกษตร สจล.</p>
        </section>
        """, unsafe_allow_html=True)
        st.markdown("<h2 class='section-title'>ค้นหาข้อมูลพืชได้ง่ายในที่เดียว</h2>", unsafe_allow_html=True)
        st.write("รวบรวมข้อมูลพืชเพื่อใช้ประกอบการเรียนและการศึกษาต่อ")
        plants = search_plants()
        a, b, c = st.columns(3)
        a.metric("รายการพืช", len(plants))
        b.metric("ภาษา", "ไทย")
        c.metric("สถานะระบบ", "ต้นแบบ")
        x, y, z = st.columns(3)
        with x: st.markdown("<div class='card'><h3>ข้อมูลเป็นหมวดหมู่</h3><p>จัดเก็บรายชื่อพืชในรูปแบบฐานข้อมูล</p></div>", unsafe_allow_html=True)
        with y: st.markdown("<div class='card'><h3>ค้นหาได้สะดวก</h3><p>มีเมนูฐานข้อมูลสำหรับค้นหารายชื่อพืช</p></div>", unsafe_allow_html=True)
        with z: st.markdown("<div class='card'><h3>พัฒนาต่อได้</h3><p>รองรับการเพิ่มรายละเอียดสายพันธุ์ในอนาคต</p></div>", unsafe_allow_html=True)
        st.info("เลือกเมนู ‘ฐานข้อมูลพืช’ ทางซ้ายเพื่อเริ่มค้นหา")
    else:
        st.markdown("<h1 class='section-title'>ฐานข้อมูลพืช</h1>", unsafe_allow_html=True)
        st.write("ค้นหารายชื่อพืชจาก SQLite Database")
        keyword = st.text_input("ค้นหาชื่อพืช", placeholder="เช่น ดอกมะลิ")
        result = search_plants(keyword)
        st.success(f"พบข้อมูล {len(result)} รายการ")
        st.dataframe(result, use_container_width=True, hide_index=True)
except Exception as error:
    st.error(f"เกิดข้อผิดพลาดในการโหลดข้อมูล: {error}")
