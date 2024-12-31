import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    return pd.read_csv('./data/data.csv', index_col=0)

st.set_page_config(page_title='Prediksi Biaya Perkalanan Haji', layout='wide', page_icon="📊")

st.sidebar.title('Sidebar Title')

st.title('Prediksi Biaya Perkalanan Haji')
st.table(load_data())

