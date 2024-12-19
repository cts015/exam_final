import streamlit as st
import pandas as pd
import pickle
import math

# Load the pre-trained models
with open('best_model1.pkl', 'rb') as model_file1:
    model1 = pickle.load(model_file1)

with open('best_model2.pkl', 'rb') as model_file2:
    model2 = pickle.load(model_file2)

# Title of the app
st.title("Predicting H2 and Char Yield from CLG")

# Sidebar inputs for user preferences
st.sidebar.header("Inputs")

C = st.sidebar.number_input("C (%)")
H = st.sidebar.number_input("H (%)")
N = st.sidebar.number_input("N (%)")
O = st.sidebar.number_input("O (%)")
S = st.sidebar.number_input("S (%)")
VM = st.sidebar.number_input("VM (%)")
Ash = st.sidebar.number_input("Ash (%)")
FC = st.sidebar.number_input("FC (%)")
moisture = st.sidebar.number_input("Moisture (%)")
T = st.sidebar.number_input("T (°C)")
OC = st.sidebar.number_input("OC (%)")
SBR = st.sidebar.number_input("SBR")

# Encoding the inputs
input_data = pd.DataFrame({
    'C (%)': [C],
    'h (%)': [H],
    'N (%)': [N],
    'O (%)': [O],
    'S (%)': [S],
    'VM (%)': [VM],
    'Ash (%)': [Ash],
    'FC (%)': [FC],
    'Moisture (%)': [moisture],
    'T (°C)': [T],
    'OC (%)': [OC],
    'SBR': [SBR]
})


# Make the predictions
prediction1 = model1.predict(input_data)
prediction2 = model2.predict(input_data)

#Transform the output (reverese normalization)
output1 = (prediction1 * (73.289514 - 11.484463)) + 11.484463
output2 = (prediction2 * (68.233942 - 0)) + 0.587804

# Display the prediction
st.subheader(f"Predicted H (%): {output1}")
st.subheader(f"Predicted Char (%): {output2}")
