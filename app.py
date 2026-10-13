import streamlit as st
import pandas as pd
from pathlib import Path


st.set_page_config(page_title="ฐานข้อมูลสายพันธุ์พืช", page_icon="🌱")


@st.cache_data
def load_plant_names() -> pd.DataFrame:
    """โหลดรายชื่อพืชจากไฟล์ CSV"""
    csv_path = Path(__file__).parent / "plant_names_th.csv"
    return pd.read_csv(csv_path)


try:
    plants = load_plant_names()

    st.markdown(
        """
        <style>
        .hero {
            padding: 3rem 2rem;
            border-radius: 24px;
            background: linear-gradient(135deg, #166534 0%, #22c55e 100%);
            color: white;
            margin-bottom: 1.5rem;
        }
        .hero h1 { font-size: 2.6rem; margin-bottom: .7rem; }
        .hero p { font-size: 1.15rem; margin-bottom: 0; }
        .card {
            padding: 1.2rem;
            border: 1px solid #dcfce7;
            border-radius: 16px;
            background: #f0fdf4;
            min-height: 120px;
        }
        .card h3 { color: #166534; margin-bottom: .4rem; }
        </style>
        <section class="hero">
            <h1>ระบบฐานข้อมูลสายพันธุ์พืชทางการเกษตร</h1>
            <p>แหล่งรวมข้อมูลพืชเบื้องต้นสำหรับนักศึกษาเทคโนโลยีการเกษตร สจล.</p>
        </section>
        """,
        unsafe_allow_html=True,
    )

    st.subheader("ค้นหาข้อมูลพืชได้ง่ายในที่เดียว")
    st.write("รวบรวมรายชื่อพืชให้ค้นหาและใช้งานประกอบการเรียนหรือการศึกษาต่อได้สะดวกขึ้น")

    metric_1, metric_2, metric_3 = st.columns(3)
    metric_1.metric("รายการพืช", len(plants))
    metric_2.metric("ภาษา", "ไทย")
    metric_3.metric("สถานะระบบ", "ต้นแบบ")

    card_1, card_2, card_3 = st.columns(3)
    with card_1:
        st.markdown("<div class='card'><h3>ค้นหาเร็ว</h3><p>ค้นหาชื่อพืชจากรายการข้อมูลเบื้องต้น</p></div>", unsafe_allow_html=True)
    with card_2:
        st.markdown("<div class='card'><h3>ใช้งานง่าย</h3><p>ออกแบบให้เหมาะกับนักศึกษาและผู้เริ่มต้น</p></div>", unsafe_allow_html=True)
    with card_3:
        st.markdown("<div class='card'><h3>พัฒนาต่อได้</h3><p>รองรับการเพิ่มรายละเอียดสายพันธุ์ในอนาคต</p></div>", unsafe_allow_html=True)

    st.divider()
    st.subheader("เริ่มค้นหารายชื่อพืช")
    keyword = st.text_input("ค้นหาชื่อพืช", placeholder="เช่น ดอกมะลิ")

    if keyword.strip():
        result = plants[
            plants["name_th"].str.contains(keyword.strip(), case=False, na=False)
        ]
    else:
        result = plants

    st.success(f"พบข้อมูล {len(result)} รายการ")
    st.dataframe(result, use_container_width=True, hide_index=True)
except FileNotFoundError:
    st.error("ไม่พบไฟล์ plant_names_th.csv กรุณาวางไฟล์ไว้ในโฟลเดอร์เดียวกับ app.py")
except Exception as error:
    st.error(f"เกิดข้อผิดพลาดในการโหลดข้อมูล: {error}")
