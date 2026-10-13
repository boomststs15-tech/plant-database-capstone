import streamlit as st

from database import initialize_database, search_plants

st.set_page_config(page_title="ฐานข้อมูลสายพันธุ์พืช", page_icon="🌱")

@st.cache_resource
def setup_database():
    initialize_database()
    return True

try:
    setup_database()
    page = st.sidebar.radio("เมนูหลัก", ["หน้าแรก", "ฐานข้อมูลพืช"])

    if page == "หน้าแรก":
        st.markdown("""
        <style>
        .hero { padding: 3rem 2rem; border-radius: 24px; background: linear-gradient(135deg,#166534,#22c55e); color:white; margin-bottom:1.5rem; }
        .hero h1 { font-size:2.6rem; margin-bottom:.7rem; }
        .hero p { font-size:1.15rem; margin-bottom:0; }
        .card { padding:1.2rem; border:1px solid #dcfce7; border-radius:16px; background:#f0fdf4; min-height:120px; }
        .card h3 { color:#166534; margin-bottom:.4rem; }
        </style>
        <section class="hero">
          <h1>ระบบฐานข้อมูลสายพันธุ์พืชทางการเกษตร</h1>
          <p>แหล่งรวมข้อมูลพืชเบื้องต้นสำหรับนักศึกษาเทคโนโลยีการเกษตร สจล.</p>
        </section>
        """, unsafe_allow_html=True)
        st.subheader("ค้นหาข้อมูลพืชได้ง่ายในที่เดียว")
        st.write("รวบรวมข้อมูลพืชเพื่อใช้ประกอบการเรียนและการศึกษาต่อ")
        plants = search_plants()
        a, b, c = st.columns(3)
        a.metric("รายการพืช", len(plants))
        b.metric("ภาษา", "ไทย")
        c.metric("สถานะระบบ", "ต้นแบบ")
        x, y, z = st.columns(3)
        with x: st.markdown("<div class='card'><h3>ข้อมูลเป็นหมวดหมู่</h3><p>จัดเก็บในรูปแบบฐานข้อมูล</p></div>", unsafe_allow_html=True)
        with y: st.markdown("<div class='card'><h3>ค้นหาได้สะดวก</h3><p>ค้นหารายชื่อพืชได้จากเมนูฐานข้อมูล</p></div>", unsafe_allow_html=True)
        with z: st.markdown("<div class='card'><h3>พัฒนาต่อได้</h3><p>รองรับการเพิ่มรายละเอียดในอนาคต</p></div>", unsafe_allow_html=True)
        st.info("เลือกเมนู ‘ฐานข้อมูลพืช’ ทางซ้ายเพื่อเริ่มค้นหา")
    else:
        st.title("ฐานข้อมูลพืช")
        st.write("ค้นหารายชื่อพืชจาก SQLite Database")
        keyword = st.text_input("ค้นหาชื่อพืช", placeholder="เช่น ดอกมะลิ")
        result = search_plants(keyword)
        st.success(f"พบข้อมูล {len(result)} รายการ")
        st.dataframe(result, use_container_width=True, hide_index=True)
except Exception as error:
    st.error(f"เกิดข้อผิดพลาด: {error}")
