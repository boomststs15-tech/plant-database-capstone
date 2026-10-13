from pathlib import Path

import streamlit as st

st.set_page_config(page_title="Plant Sense", page_icon="🌿", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@600;700&display=swap');
.stApp { background:#f3f0ec; color:#3d4542; font-family:'DM Sans',sans-serif; }
.block-container { max-width:1220px; padding:1.4rem 3rem 2rem; }
.topbar { display:flex; justify-content:space-between; align-items:center; padding:.4rem 0 3.8rem; }
.brand { font-weight:700; font-size:1.35rem; color:#3d4542; letter-spacing:-.03em; }
.brand span { color:#b366b5; }
.nav { color:#777c78; font-size:.9rem; }
.pill { display:inline-block; padding:.65rem 1rem; border-radius:999px; background:#3d4542; color:white; font-size:.85rem; }
.hero { display:grid; grid-template-columns:1.05fr .95fr; gap:4rem; align-items:center; min-height:430px; }
.eyebrow { color:#b366b5; font-size:.78rem; font-weight:700; letter-spacing:.16em; text-transform:uppercase; margin-bottom:1.25rem; }
.hero h1 { font-family:'Playfair Display',serif; font-size:4.7rem; line-height:1.02; letter-spacing:-.055em; color:#3d4542; margin:0 0 1.5rem; }
.hero h1 em { color:#b366b5; font-style:normal; }
.hero p { color:#777c78; font-size:1.1rem; line-height:1.7; max-width:500px; }
.visual { position:relative; min-height:420px; border-radius:38px; background:#dcd9dc; overflow:hidden; }
.orb { position:absolute; width:310px; height:310px; border-radius:50%; left:50%; top:50%; transform:translate(-50%,-50%); background:radial-gradient(circle at 35% 30%,#ead7e8 0 15%,#c28d6b 36%,#b366b5 68%,#7a557f 100%); box-shadow:0 25px 60px rgba(179,102,181,.26); }
.leaf { position:absolute; width:150px; height:150px; border-radius:100% 0 100% 0; background:#9ab39c; transform:rotate(22deg); right:8%; top:8%; opacity:.8; }
.leaf.two { width:110px; height:110px; left:6%; bottom:12%; transform:rotate(205deg); background:#c28d6b; }
.visual-label { position:absolute; left:1.5rem; bottom:1.5rem; padding:.8rem 1rem; border-radius:14px; background:rgba(255,255,255,.7); backdrop-filter:blur(12px); font-size:.8rem; color:#3d4542; }
.section-title { text-align:center; font-family:'Playfair Display',serif; font-size:2rem; margin:5rem 0 2rem; color:#3d4542; }
.card { background:#fff; border-radius:24px; padding:1.5rem; min-height:150px; border:1px solid #e5e0dc; box-shadow:0 12px 30px rgba(61,69,66,.05); }
.card small { color:#b366b5; font-weight:700; }
.card h3 { margin:.8rem 0 .5rem; color:#3d4542; font-size:1.15rem; }
.card p { color:#777c78; line-height:1.6; margin:0; }
.footer { text-align:center; color:#999a96; margin-top:4rem; padding:1.5rem; font-size:.85rem; }
@media (max-width:800px) { .block-container { padding:1rem 1.2rem; } .hero { grid-template-columns:1fr; gap:2rem; } .hero h1 { font-size:3.3rem; } .visual { min-height:300px; } .nav { display:none; } }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="topbar">
  <div class="brand">plant<span>.</span>sense</div>
  <div class="nav">ค้นพบ · เกี่ยวกับโครงการ · ทีมผู้จัดทำ</div>
  <div class="pill">KMITL · AGTECH</div>
</div>
<section class="hero">
  <div>
    <div class="eyebrow">Agricultural plant collection</div>
    <h1>ค้นพบความงามของ <em>พืช</em> รอบตัวเรา</h1>
    <p>พื้นที่เล็ก ๆ สำหรับรวบรวมและนำเสนอข้อมูลพืชทางการเกษตร ให้การเรียนรู้เป็นเรื่องง่าย สงบ และเป็นระบบ</p>
  </div>
  <div class="visual">
    <div class="orb"></div><div class="leaf"></div><div class="leaf two"></div>
    <div class="visual-label">ระบบฐานข้อมูลสายพันธุ์พืชทางการเกษตร</div>
  </div>
</section>
""", unsafe_allow_html=True)

st.markdown("<h2 class='section-title'>ข้อมูลโครงการ</h2>", unsafe_allow_html=True)
st.markdown("<p class='section-subtitle'>ภาพรวมของข้อมูลที่โครงการกำลังรวบรวมและนำเสนอ</p>", unsafe_allow_html=True)
info_1, info_2 = st.columns([1, 1])
with info_1:
    st.markdown("""
    <div class="card">
      <small>PROJECT SCOPE</small>
      <h3>ไม้ดอกและพืชประดับเบื้องต้น</h3>
      <p>รวบรวมรายชื่อพืช 27 รายการ เช่น ดอกบัว ดอกมะลิ ดอกดาวเรือง กุหลาบ กล้วยไม้ เบญจมาศ ทานตะวัน และดอกรักเร่</p>
    </div>
    """, unsafe_allow_html=True)
with info_2:
    st.markdown("""
    <div class="card">
      <small>DATA SOURCE</small>
      <h3>แหล่งข้อมูลอ้างอิง</h3>
      <p>กรมวิชาการเกษตร — ฐานข้อมูลพรรณพืชและเชื้อพันธุกรรมพืช ใช้เป็นแหล่งตรวจสอบข้อมูลพืชของโครงการ</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<h2 class='section-title'>ดอกไม้สำหรับไหว้และบูชา</h2>", unsafe_allow_html=True)
st.markdown("<p class='section-subtitle'>ข้อมูลความเชื่อ การใช้งาน ลักษณะ และแนวทางดูแลดอกไม้ที่พบในโครงการ</p>", unsafe_allow_html=True)
st.markdown("""
<div class="card">
  <small>REFERENCE GUIDE · 25 TOPICS</small>
  <h3>เรียนรู้ความหมายของดอกไม้แต่ละชนิด</h3>
  <p>เปิดอ่านข้อมูลสรุปตั้งแต่ดอกบัว มะลิ ดาวเรือง กุหลาบ กล้วยไม้ เบญจมาศ ไปจนถึงดอกไม้ที่ใช้ในคติจีนและพิธีเฉพาะพื้นที่</p>
</div>
""", unsafe_allow_html=True)
with st.expander("เปิดอ่านข้อมูลดอกไม้ทั้งหมด", expanded=False):
    guide_path = Path(__file__).with_name("worship_flowers.md")
    if guide_path.exists():
        st.markdown(guide_path.read_text(encoding="utf-8"))
    else:
        st.info("ยังไม่พบไฟล์ข้อมูลดอกไม้")

st.markdown("<h2 class='section-title'>ออกแบบมาเพื่อการเรียนรู้ที่ดีขึ้น</h2>", unsafe_allow_html=True)
card_1, card_2, card_3 = st.columns(3)
with card_1:
    st.markdown("<div class='card'><small>01 / EXPLORE</small><h3>ค้นพบข้อมูล</h3><p>รวบรวมข้อมูลพืชให้มองเห็นภาพรวมและทำความเข้าใจได้ง่าย</p></div>", unsafe_allow_html=True)
with card_2:
    st.markdown("<div class='card'><small>02 / LEARN</small><h3>เรียนรู้อย่างเป็นระบบ</h3><p>นำเสนอเนื้อหาที่เหมาะกับนักศึกษาเทคโนโลยีการเกษตร</p></div>", unsafe_allow_html=True)
with card_3:
    st.markdown("<div class='card'><small>03 / GROW</small><h3>ต่อยอดความรู้</h3><p>เป็นจุดเริ่มต้นสำหรับพัฒนาระบบข้อมูลพืชในอนาคต</p></div>", unsafe_allow_html=True)

st.markdown("<div class='footer'>โครงงานกลุ่มนักศึกษาเทคโนโลยีการเกษตร สจล. · 2026</div>", unsafe_allow_html=True)
