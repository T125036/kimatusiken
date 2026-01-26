import streamlit as st
import pandas as pd

st.title('日本の給与所得者数と')
df = pd.read_csv('FEH_00351000_260121151701.csv')

for col in df.columns:
    if '【' in col:
        df[col] = df[col].astype(str).str.replace(',', '').replace('-', '0').astype(float)

with st.sidebar:
    selected_cats = st.multiselect('年を選択してください（複数選択可）',
                          df['年'].unique())
    selected_media = st.selectbox('業種を選んでください',
                          df['業種（2008年～）'].unique())
    
    st.subheader('色分け')
    selected_values = st.multiselect('集計月を選択してください',
                                     options=['給与所得者数(３月末)【人】','給与所得者数(６月末)【人】','給与所得者数(９月末)【人】','給与所得者数(１２月末)【人】'])
    if selected_values == '給与所得者数(３月末)【人】':
     month = '給与所得者数(３月末)【人】'
    elif selected_values == '給与所得者数(６月末)【人】':
     month = '給与所得者数(６月末)【人】'
    elif selected_values == '給与所得者数(９月末)【人】':
     month = '給与所得者数(９月末)【人】'
    elif selected_values == '給与所得者数(１２月末)【人】':
     month = '給与所得者数(１２月末)【人】'
  
df = df[df['年'].isin(selected_cats)]
df = df[df['業種（2008年～）'] == selected_media]
df = df[df['']]
st.dataframe(df,width=800,height=400)
