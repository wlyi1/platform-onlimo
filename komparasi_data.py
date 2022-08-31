import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import streamlit as st
from matplotlib.widgets import CheckButtons

df49 = pd.read_csv('df49.csv')

def chart(ylabel, xlabel, yvalues, xvalues, title=''):
    fig = px.line(x=xvalues, y=yvalues, labels={'x': xlabel, 'y': ylabel})
    return fig

def charts(y_series, xval, alfa, title=' '):
    
    fig = plt.figure(figsize = (10,7))
      
    plt.plot(xval, y_series[0], 'c', alpha=alfa[0], label='subuh')
    plt.plot(xval, y_series[1], 'y', alpha=alfa[1], label='pagi')
    plt.plot(xval, y_series[2], 'r', alpha=alfa[2], label='siang')
    plt.plot(xval, y_series[3], color='green', alpha=alfa[3], label='malam')
    plt.title(title)
    plt.legend()
    return fig


alfa_val = [0,0,0,0]


col1, col2, col3 = st.columns([1,1,1])

with col1:
    d1 = st.date_input('tanggal awal')
    d2 = st.date_input('tanggal akhir')
    d3=d2-d1
    d3=d3.days
    st.write(d3+1)
    
with col2:
    param = st.radio('parameter:', ('pH', 'DO', 'COD', 'BOD', 'NH4', 'NO3', 'TEMP'))
    arr_t = df49[param].to_numpy()
    arr_t = arr_t.reshape(47,4,6)
    #asumsi tanggal awal : 01-08-2022
    i = d3

    subuh = arr_t[0:i, 0, :].flatten()
    pagi = arr_t[0:i, 1, :].flatten()
    siang = arr_t[0:i, 2, :].flatten()
    malam = arr_t[0:i, 3, :].flatten()

    periode = [subuh,pagi,siang,malam]
    x = [x for x in range(len(subuh))]

with col3:
    st.write('periode waktu')
    #checkbox periode
    st_subuh = st.checkbox('Subuh')
    st_pagi = st.checkbox('Pagi')
    st_siang = st.checkbox('Siang')
    st_malam = st.checkbox('Malam')
    status_periode = [st_subuh, st_pagi, st_siang, st_malam]

    if all(status_periode):
        for i in range(len(alfa_val)):
            alfa_val[i] = 1

    if any(status_periode):
        for i in range(len(alfa_val)):
            if status_periode[i] == 1:
                alfa_val[i] = 1
suhu = charts(periode, x, alfa_val, 'Grafik Suhu Sungai Serang')
st.write(suhu)    

    
    
    
    
    
    
    