import streamlit as st
import pandas as pd
import numpy as np
# from sklearn.model_selection import train_test_split
import joblib
# import plotly.figure_factory as ff
# import matplotlib.pyplot as plt

# Text/Title
st.title("Yoga Recommender")

df = pd.read_csv('Training.csv')

#seperated the independent and dependent values to repective variables 
x = df.drop(['prognosis'],axis =1)
y = df['prognosis']

#divided into testing and training
# x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)

a = list(range(2,134))
i_name  = st.text_input('Enter your name: ')
i_age = st.number_input('Enter your age: ')
for i in range(len(x.columns)):
    st.write(str(i+1) + ":", x.columns[i])

choices = st.text_input('Enter the Serial no.s which in your Symptoms are exist:  ')
b = [int(x) for x in choices.split()]
count = 0
while count < len(b):
    item_to_replace =  b[count]
    replacement_value = 1
    indices_to_replace = [i for i,x in enumerate(a) if x==item_to_replace]
    count += 1
    for i in indices_to_replace:
        a[i] = replacement_value
a = [0 if x !=1 else x for x in a]

dt = joblib.load(open('health_model', 'rb'))
y_diagnosis = dt.predict([a])

asan = {"down_dog": ["Impetigo", "Acne", "(vertigo) Paroymsal  Positional Vertigo", "Psoriasis", "Fungal infection", "Dimorphic hemmorhoids(piles)", "AIDS", "Diabetes", "Hypoglycemia", "Common Cold", "Gastroenteritis", "Peptic ulcer diseae", "Hypertension"],
"tree": ["Migraine"],
"warrior_2": ["Pneumonia", "Bronchial Asthma", "Hypothyroidism"],
"cow_face": ["hepatitis A", "Hepatitis B", "Hepatitis C", "Hepatitis D", "Hepatitis E", "Jaundice", "Typhoid"],
"plank": ["Migraine", "Osteoarthristis", "Cervical spondylosis", "Arthritis"]
}

# def searchKeysByVal(Val):
#     # list_of_keys = [key
#     #             for key, list_of_values in sorted(dict.items())
#     #             if value in list_of_values]
#     result_list = []
#     for d in asan:
#     	result_list.append([v for k,v in d.items()])
#     return result_list

# def GetKey(val):
#    for key, value in asan.items():
#       if val == value:
#          return key
#       return "key doesn't exist"
def searchKeysByVal(val):
	yoga = [key	for key, list_of_values in asan.items() if val in list_of_values]
	return yoga

if choices:
	yoga = searchKeysByVal(y_diagnosis)
	if yoga:
		st.write(f"Recommended yoga: {yoga} ")
	else:
		st.write("You should seek immediate medical help")
st.write(f"Name = {i_name} , Age = {i_age}")