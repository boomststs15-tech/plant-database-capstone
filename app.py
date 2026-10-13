import streamlit as st
import pandas as pd
from pathlib import Path


st.set_page_config(page_title="ฐานข้อมูลสายพันธุ์พืช", page_icon="🌱")


@st.cache_data
def load_plant_names() -> pd.DataFrame:
    """โหลดรายชื่อพืชจากไฟล์ CSV"""
    csv_path = Path(__file__).parent / "plant_names_th.csv"
    return pd.read_csv(csv_path)


st.title("ระบบฐานข้อมูลสายพันธุ์พืชทางการเกษตร")
st.write("ต้นแบบสำหรับค้นหารายชื่อพืชเบื้องต้น")

try:
    plants = load_plant_names()
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
