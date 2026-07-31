import streamlit as st

st.markdown("# :red[🏃แอปพลิเคชั้นคำนวณค่าดัชนีมวลกาย BMI]")
st.write("กรอกข้อมูลน้ำหนักและส่วนสูงของคุณ เพื่อเช็กสุขภาพเบื้องต้น")

weight = st.number_input("กรอกค่าน้ำหนักของคุณ (Kg): ")
height_cm = st.number_input("กรอกข้อมูลส่วนสูงของคุณ (Cm)")

if st.buttom("คำนวณ ค่า BMI 🎯"):
    height_m = height_cm / 100
    bmi = weight / (height_m ** 2)
    st.write("---")
    st.header(f"ค่า BMI ของคุณคือ : **{bmi: .2f}**")

if bmi < 18.5:
    st.warning("⚠️ คุณมีน้ำหนักต่ำกว่าเกณฑ์ (ผอม)") 
elif 18.5 <= bmi < 23.0:
    st.success("🎉 คุณมีน้ำหนักอยู่ในเกณฑ์ปกติ (สุขภาพดี)")
elif 18.5 <= bmi < 23.0:
    st.info(" 💡 คุณเริ่มมีมีน้ำหนักเกินเกณฑ์เกณฑ์ (ท้วม)")
else: 
    st.error("🚨 คุณอยู่ในเกณฑ์อ้วน ควรระวังเรื่องสุขภาพและออกกำลังกาย ")  

st.divider()
st.write("นายวัชรชัย ไทยราช เลขที่ 40 ม.4/6")
