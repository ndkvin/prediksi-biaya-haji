import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    return pd.read_csv('./data/data.csv', index_col=0)

st.set_page_config(page_title='Prediksi Biaya Perjakanan Haji', layout='wide', page_icon="📊")

df = load_data()

tahun = st.sidebar.selectbox('Tahun', df['Tahun'].unique(), index=len(df['Tahun'].unique())-1)
df = df[df['Tahun'] <= tahun]

st.title('Prediksi Biaya Perjakanan Haji')

st.write('## Perbandingan BIPIH, BPIH, dan Nilai Manfaat')
st.line_chart(data=pd.DataFrame({
            'Tahun': df['Tahun'].astype(str), 
            'Bipih (jt)': df['Bipih (jt)'].astype(float),
            'BPIH (jt)': df['BPIH (jt)'].astype(float),
            'Nilai Manfaat (jt)': df['Nilai Manfaat (jt)'].astype(float)
        }).set_index('Tahun'), use_container_width=True)

col1, col2 = st.columns(2)

with col1:
    st.write('## BPIH (Juta)')
    st.bar_chart(data=pd.DataFrame({
        'Tahun': df['Tahun'].astype(str), 
        'BPIH (jt)': df['BPIH (jt)'].astype(float)
    }).set_index('Tahun'), use_container_width=True)
    
    st.write('## Nilai Manfaat (Juta)')
    st.bar_chart(data=pd.DataFrame({
        'Tahun': df['Tahun'].astype(str), 
        'Nilai Manfaat (jt)': df['Nilai Manfaat (jt)'].astype(float)
    }).set_index('Tahun'), use_container_width=True)

with col2:
    st.write('## BIPIH (Juta)')
    st.bar_chart(data=pd.DataFrame({
        'Tahun': df['Tahun'].astype(str), 
        'Bipih (jt)': df['Bipih (jt)'].astype(float)
    }).set_index('Tahun'), use_container_width=True)



