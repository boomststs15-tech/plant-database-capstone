import streamlit as st

st.set_page_config(page_title="ระบบฐานข้อมูลสายพันธุ์พืชทางการเกษตร", page_icon="🌱", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Prompt:wght@400;500;600;700&display=swap');
.stApp { background:#f6fbf7; font-family:'Prompt',sans-serif; }
.block-container { max-width:1150px; padding-top:3rem; }
.hero { padding:5rem 4rem; border-radius:32px; background:linear-gradient(135deg,#104b32,#2c9b68); color:white; text-align:center; box-shadow:0 18px 45px rgba(16,75,50,.18); }
.hero h1 { font-size:3rem; line-height:1.25; margin:0 auto 1rem; max-width:850px; }
.hero p { font-size:1.2rem; opacity:.92; margin:0 auto; max-width:700px; }
.eyebrow { letter-spacing:.12em; text-transform:uppercase; font-size:.85rem; opacity:.8; margin-bottom:1rem; }
.section-title { text-align:center; color:#123c2b; font-weight:700; margin:3rem 0 .7rem; }
.section-subtitle { text-align:center; color:#60786b; margin-bottom:2rem; }
.card { padding:1.6rem; border:1px solid #dcefe2; border-radius:22px; background:white; min-height:150px; box-shadow:0 8px 24px rgba(25,75,45,.06); }
.card h3 { color:#167044; margin:0 0 .6rem; font-size:1.2rem; }
.card p { color:#60786b; margin:0; line-height:1.7; }
.footer { text-align:center; color:#789184; margin-top:3rem; padding:1.5rem; border-top:1px solid #dcefe2; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<section class="hero">
    <div class="eyebrow">AGRICULTURAL PLANT DATABASE</div>
    <h1>ระบบฐานข้อมูลสายพันธุ์พืชทางการเกษตร</h1>
    <p>พื้นที่รวบรวมและนำเสนอข้อมูลพืชเบื้องต้นสำหรับนักศึกษาเทคโนโลยีการเกษตร สจล.</p>
</section>
""", unsafe_allow_html=True)

st.markdown("<h2 class='section-title'>เรียนรู้พืชอย่างเป็นระบบ</h2>", unsafe_allow_html=True)
st.markdown("<p class='section-subtitle'>ช่วยให้การค้นคว้าและทำความเข้าใจข้อมูลพืชเป็นเรื่องง่ายขึ้น</p>", unsafe_allow_html=True)

card_1, card_2, card_3 = st.columns(3)
with card_1:
    st.markdown("<div class='card'><h3>รวมข้อมูลไว้ในที่เดียว</h3><p>จัดระเบียบข้อมูลพืชให้เหมาะกับการเรียนรู้และการทำโครงงาน</p></div>", unsafe_allow_html=True)
with card_2:
    st.markdown("<div class='card'><h3>ออกแบบสำหรับนักศึกษา</h3><p>นำเสนอข้อมูลด้วยภาษาที่เข้าใจง่ายและใช้งานได้สะดวก</p></div>", unsafe_allow_html=True)
with card_3:
    st.markdown("<div class='card'><h3>ต่อยอดได้ในอนาคต</h3><p>รองรับการพัฒนาเป็นระบบข้อมูลพืชที่มีรายละเอียดมากขึ้น</p></div>", unsafe_allow_html=True)

st.markdown("<div class='footer'>โครงงานกลุ่มนักศึกษาเทคโนโลยีการเกษตร สจล.</div>", unsafe_allow_html=True)
