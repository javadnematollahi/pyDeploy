import streamlit as st
import datetime

st.title("Body Mass Index")

# with st.sidebar:
#     agree = st.checkbox("agree")
#     appointment = st.slider("select a range of number:", 0.0, 100.0, (25.0,75.0))
#     d = st.date_input("when is your birthday:", datetime.date(2019, 7 , 6))



col1, col2, col3 = st.columns(3)

with col1:
    weight = st.number_input("Enter Your Weight (Kg)")
    height = st.number_input("Enter Your Height (cm)")

    calculator = st.button("Calculate BMI")
    if calculator: 
        if height != 0:
            bmi = weight / (height/100)**2
            st.info(bmi)
            if bmi <= 18.5:
                st.write("لاغر")
            elif 18.5<= bmi < 25:
                st.write("مناسب")
            elif 25 <= bmi < 30 : 
                st.write("اضافه وزن")
            elif 30 <= bmi < 40 : 
                st.write("چاق")
            elif 40 <= bmi: 
                st.write("خیلی چاق")


with col3:
    if calculator: 
        if height != 0:
            if bmi <= 18.5:
                st.image("assets/18.jpg")
            elif 18.5<= bmi < 25:
                st.image("assets/18_24.jpg")
            elif 25 <= bmi < 30 : 
                st.image("assets/25_29.jpg")
            elif 30 <= bmi < 40 : 
                st.image("assets/30_39.jpg")
            elif 40 <= bmi: 
                st.image("assets/40.jpg")



if calculator: 
    if height == 0:
        st.warning("Height can't be zero")
