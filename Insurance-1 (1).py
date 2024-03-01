import streamlit as st
import pandas as pd
import pickle

st.write("""
# expenses Prediction App

This app predicts the **insurance expenses** type!
""")

st.sidebar.header('User Input Parameters')

def user_input_features():
    age = st.sidebar.slider('age',  [1,  0, 10, 15, 14, 13, 28, 19, 42,  7, 44,  5, 38,  9, 34, 12, 16, 41, 45, 37,  4,  8, 17,  6, 23, 20, 18,  3, 30, 22, 40, 35, 25, 46, 2, 43, 26, 39, 11, 27, 36, 31, 29, 33, 24, 32, 21])
    bmi = st.sidebar.slider('bmi', [102, 161, 153,  50, 112,  80, 157, 100, 121,  81,  85,  86, 167,
       220, 239,  69, 131,  61, 224, 176, 183, 147, 164, 142, 103,  54,
       151,   4, 186, 179, 109, 106, 187,  28,  32, 190, 221,  89, 189,
        41, 194, 196, 209, 171,  68, 175, 159, 110, 193, 141, 140,  52,
        97, 160,  70,  82,  47, 213, 185,  63,  71, 108, 104, 143, 163,
       119, 178,  92, 206, 199, 232, 135,  95,  93, 217, 136,  24,  19,
       139,  78, 124, 122,  98, 107, 132, 174, 120, 180, 145, 271,  57,
       113, 137, 162, 111, 197,   7, 170,  88,  43, 182,  79,  75, 148,
        76, 210, 128, 200,  64,  67, 101, 192, 218, 105, 155,  15, 235,
       126,   0, 156, 115,  87, 130, 238, 144, 129,  10, 215, 184,  46,
        90,  55, 204,  45, 207, 114,  44,  91, 123,  33,   3, 165,  77,
       223,  66, 241,  22, 125, 117,  99,  30,  39, 227, 270, 191, 259,
        53,  49, 198, 203, 172, 154, 230, 188, 168, 146, 116, 181, 251,
        40,  42,  73, 127,  35, 152,  72, 138,   9, 248,  23, 133, 205,
       267,  59,   5,  26,   2,  62, 214,  96,   1, 265, 118, 150, 158,
       246, 208, 263,  74, 149, 233, 166, 134,  38, 249,  83, 253,  84,
       216, 226, 211, 266, 177, 264, 262,  37, 255, 247,  58, 258,  60,
        31,  21, 201,  16,  36, 242, 212, 219, 173, 243, 229,  27,  12,
       236, 254, 228,  94, 202,  51, 169,  20, 231,  48, 237, 240, 234,
       245,  34,  65,   6, 272, 268, 250, 252,  25, 195, 261,  11, 222,
        29,  56,  18, 257,  14, 273, 269,  17, 244,  13, 260, 256, 225,
         8, 274])
    children = st.sidebar.slider('children', [0, 1, 3, 2, 5, 4])
    sex = st.sidebar.selectbox('female', 'male')
    smoker = st.sidebar.selectbox('no','yes')
    region = st.sidebar.selectbox('northeast', 'northwest', 'southeast', 'southwest')
    expenses = st.sidebar.slider ('1005,   57,  306, ...,   32,   91, 1171')
    data = {'age': age,
            'bmi': bmi,
            'children': children,
            'sex': sex,
            'smoker': smoker,
            'region': region,
            'expenses': expenses}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

    

st.subheader('User Input parameters')
st.write(df)

loaded_model = pickle.load(open("insurance().h5", "rb"))

prediction = loaded_model.predict(df)

st.subheader('Prediction')
st.write(prediction)
