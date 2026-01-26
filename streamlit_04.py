import streamlit as st
import pandas as pd
import numpy as np

st.title('Streamlitのレイアウト')

st.header('1. カラム')
st.subheader('カラムとは')
col = st.columns(3)
col[0].write('カラム1')
col[1].write('カラム2')
col[2].write('カラム3')


col2 = st.columns([1,2])
st.subheader('検索条件をカラムに分ける')
col = st.columns(2)

st.sidebar('サイドバー')

with st.sidebar:
  branch = col[0].multiselect('支店を選択して下さい',
                            {'支店A','支店B','支店C','支店D','支店E'},
                            key='m1')
  year = col2[1].number_input('年を入力してください',
                           min_value=2020,
                           max_value=2026,
                           value=2020,
                           step=1,
                           key='n1')

df = pd.DataFrame(data=np.random.randint(0,100,(3,6)),
             index=['支店A','支店B','支店C'],
             columns=['1月','2月','3月','4月','5月','6月'])
st.dataframe(df,width=600,height=200)