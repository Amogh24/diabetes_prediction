import streamlit as st
from Model import run
from PIL import Image
img = Image.open(r"./db1.jpg")
img2 = Image.open(r"./db2.jpg")
img3 = Image.open(r"./db3.jpg")
img5 = Image.open(r"./db5.jfif")
st.title('Diabetes Prediction')
st.image(img)
st.sidebar.title("Tips to stay disease-free")
st.sidebar.image(img2,caption="Eat healthy")
st.sidebar.write("Lots of fruits and vegetables will keep diseases at bay")
st.sidebar.image(img3,caption="workout regularly")
st.sidebar.write("Exercise regularly to stay fit and maintain your body")
st.sidebar.image(img5,caption="visit the doctor regularly",width=300)
st.sidebar.write("Regular medical checkups help in early diagnosis")

bmi = 0

weight = st.number_input("Enter your weight (in kgs)")
  
# TAKE HEIGHT INPUT
# radio button to choose height format
status = st.radio('Select your height format: ',
                  ('cms', 'meters', 'feet'))
  
# compare status value
if(status == 'cms'):
    # take height input in centimeters
    height = st.number_input('Centimeters')
      
    try:
        bmi = weight / ((height/100)**2)
    except:
        st.text("Enter some value of height")
          
elif(status == 'meters'):
    # take height input in meters
    height = st.number_input('Meters')
      
    try:
        bmi = weight / (height ** 2)
    except:
        st.text("Enter some value of height")
          
else:
    # take height input in feet
    height = st.number_input('Feet')
      
    # 1 meter = 3.28
    try:
        bmi = weight / (((height/3.28))**2)
    except:
        st.text("Enter some value of height")
if(st.button('Calculate BMI')):
      
    # print the BMI INDEX
    st.text("Your BMI  is {}.".format(bmi))
      
    # give the interpretation of BMI index
    if(bmi < 16):
        st.error("You are Extremely Underweight")
    elif(bmi >= 16 and bmi < 18.5):
        st.warning("You are Underweight")
    elif(bmi >= 18.5 and bmi < 25):
        st.success("Healthy")        
    elif(bmi >= 25 and bmi < 30):
        st.warning("Overweight")
    elif(bmi >= 30):
        st.error("Extremely Overweight")
age = st.number_input('AGE')
bp = st.number_input("BLOOD PRESSURE")
glucose = st.number_input("GLUCOSE LEVEL")
insulin = st.number_input("INSULIN")
pregnancies = st.slider("NUMBER OF PREGNANCIES",0,10)
#image = Image.open("C:\Users\amogh\Downloads\db1.jpg")

if st.button('SUBMIT'):
    if glucose==0:glucose=117
    if insulin==0:insulin=30
    params = {
    'insulin':insulin,
    'bmi' :bmi,
    'glucose':glucose,
    'bp':bp,
    'pregnancies':pregnancies,
    'age':age
            }
    tag = run(params)
    if tag == 1:
        st.warning("Your parameters show a possibility of diabetes, consult a doctor immediately")
    else:
        st.success("Your parameters do not show a high chance of diabetes, but keep monitoring yourself")
    st.info("Note: Please do not consider this to be a substitute for medical diagnosis. This is a predictive model designed to help you be aware regarding diabetes and aid early diagnosis")