import streamlit as st
import pandas as pd
import plotly.graph_objects as go

@st.cache_data
def load_data():
    return pd.read_csv('./data/data.csv', index_col=0)

st.set_page_config(page_title='Prediksi Biaya Perjalanan Haji', layout='wide', page_icon="📊")

df = load_data()

col1, col2 = st.sidebar.columns(2)

with col1:
    start_year = st.selectbox('Tahun Awal', df['Tahun'].unique(), index=0)

with col2:
    end_year = st.selectbox('Tahun Akhir', df['Tahun'].unique(), index=len(df['Tahun'].unique())-1)

if end_year < start_year:
    st.sidebar.error('Tahun Akhir tidak boleh kurang dari Tahun Awal')
else:
    df = df[(df['Tahun'] >= start_year) & (df['Tahun'] <= end_year)]

st.title('Prediksi Biaya Perjalanan Haji')

st.write('## Perbandingan BIPIH, BPIH, dan Nilai Manfaat')
fig = go.Figure()

fig.add_trace(go.Bar(
    x=df['Tahun'],
    y=df['BPIH (jt)'],
    name='BPIH (jt)',
    marker_color='#17becf'
))

fig.add_trace(go.Bar(
    x=df['Tahun'],
    y=df['Bipih (jt)'],
    name='BIPIH (jt)',
    marker_color='#ff7f0e'
))

fig.update_layout(
    barmode='overlay',
    xaxis=dict(
        tickmode='linear',
        dtick=1
    ),
    yaxis=dict(
        title='Juta',
    ),
    showlegend=True,
    margin=dict(t=30)
)

st.plotly_chart(fig, use_container_width=True)

st.write('## Nilai BIPIH/BPIH')

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=df['Tahun'], 
    y=df['BIPIH/BPIH'],
    mode='lines+markers',
    name='BIPIH/BPIH',
    marker=dict(size=10) 
))

fig.update_layout(
    title='Perubahan BIPIH/BPIH Per Tahun',
    xaxis_title='Tahun',
    yaxis_title='BIPIH/BPIH',
    template='plotly_white',
    yaxis=dict(range=[0, 1])
)

st.plotly_chart(fig, use_container_width=True)
