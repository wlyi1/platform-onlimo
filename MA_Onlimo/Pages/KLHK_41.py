#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import datetime
from datetime import datetime as dt
import streamlit as st
import streamlit.components.v1 as components
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from csv import writer
sns.set()

def chart(ylabel, xlabel, yvalues, xvalues, title=''):
    #create new graph
    
    fig = plt.figure(figsize = (10,7))
    plt.plot(xvalues, yvalues)
    plt.title(title, fontsize = 20, fontweight = 'bold')
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    return fig
    
    
    
df = pd.read_csv('OL41_2022.csv')
df['new_date']=pd.to_datetime(df['DATE'])
df['tgl'] = pd.to_datetime(df['DATE'] + ' ' + df['TIME'])

#nilai list 24 jam
result_DO = [x for x in df[-24:]['DO']]
result_pH = [x for x in df[-24:]['pH']]
result_SUHU = [x for x in df[-24:]['TEMP']]
result_NH = [x for x in df[-24:]['NH4']]
result_NO = [x for x in df[-24:]['NO3']]

#nilai abnormal
ab_pH = sum(map(lambda x : x<5 and x>9, result_pH))
ab_DO = sum(map(lambda x : x<1, result_DO))
ab_NH = sum(map(lambda x : x>100, result_NH))
ab_NO = sum(map(lambda x : x>100, result_NO))

#start streamlit
st.header('KLHK 41')


header_col1, header_col2 = st.columns(2)
tanggal_data = df['tgl'].max().strftime(("%Y-%m-%d %H:%M:%S")) 

if df['new_date'].max().strftime('%Y-%m-%d') == dt.today().strftime('%Y-%m-%d'): 
    header_col1.button(tanggal_data)
    header_col2.success('ONLINE')
                       
elif df['new_date'].max().strftime('%Y-%m-%d') < dt.today().strftime('%Y-%m-%d'): 
    header_col1.button(tanggal_data)
    header_col2.warning('OFFLINE')
        
else:
    header_col1.button(tanggal_data)                  
    header_col2.error('ERROR')                
                       
st.title('Jumlah Nilai Anomali per 24 Jam')        
                       
col1, col2, col3, col4 = st.columns(4)
col1.metric('pH', ab_pH, result_pH[-1])
col2.metric('DO', ab_DO, result_DO[-1])
col3.metric('NH', ab_NH, result_NH[-1])
col4.metric('NO', ab_NO, result_NO[-1])

st.markdown("""<hr style="height:5px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)
st.title('Grafik Parameter')
option = st.selectbox('Parameter untuk dilihat data dan grafiknya', ('pH', 'DO', 'NH4', 'NO3'))


#empty chart
c1, c2 = st.columns(2)
with c1:
    space_initial = st.empty()
with c2:
    space_initial_2 = st.empty()

#chart parameter
pH = chart('pH', 'Date', df[-24:]['pH'], df[-24:]['tgl'], title= 'Grafik pH')
DO = chart('DO', 'Date', df[-24:]['DO'], df[-24:]['tgl'], title= 'Grafik DO')
suhu = chart('Suhu', 'Date', df[-24:]['TEMP'], df[-24:]['tgl'], title= 'Grafik Suhu')
NH = chart('NH', 'Date', df[-24:]['NH4'], df[-24:]['tgl'], title= 'Grafik NH')
NO = chart('NO', 'Date', df[-24:]['NO3'], df[-24:]['tgl'], title= 'Grafik NO')

#dataframe parameter
data_pH = df[-24:][['tgl', 'pH']]
data_DO = df[-24:][['tgl', 'DO']]
data_NH = df[-24:][['tgl', 'NH4']]
data_NO = df[-24:][['tgl', 'NO']]
data_T0 = df[-24:][['tgl', 'TEMP']]

#chart column
    
if option == 'pH':
    space_initial.write(pH)
    space_initial_2.write(data_pH)
elif option == 'DO':
    space_initial.write(DO)
    space_initial_2.write(data_DO)
elif option == 'NH4':
    space_initial.write(NH)
    space_initial_2.write(data_NH)
elif option == 'NO3':
    space_initial.write(NO)
    space_initial_2.write(data_NO)



st.markdown("""<hr style="height:5px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)
st.title('Take Action !')

#input action from PJ
@st.cache(allow_output_mutation=True)
def get_data_input():
    return[]

@st.cache(allow_output_mutation=True)
def get_data_output():
    return[]

emoji = st.markdown(':smiley:')

aksi = st.radio(f'Hallo Iqbal, apa yang sudah dilakukan untuk data anomali ini ?', ('Kalibrasi ulang', 'Mencelupkan sensor ke air bersih','Reset logger', 'Membersihkan sensor'))
tgl_aksi = datetime.datetime.now()

if st.button('add input'):
    get_data_input().append({'Tanggal Aksi': tgl_aksi, 'Aksi':aksi})
    input_41 = pd.DataFrame(get_data_input())
    input_41.tail(1).to_csv('log_41.csv', mode='a', index = False, header = False)

hasil = st.text_input(f'Hallo Iqbal, bagaimana hasilnya?')
tgl_hasil = datetime.datetime.now()

if st.button('add output'):
    get_data_output().append({'Tanggal Hasil': tgl_hasil, 'Hasil':hasil})
    hasil_41 = pd.DataFrame(get_data_output())
    hasil_41.tail(1).to_csv('log_hasil_41.csv', mode='a', index=False, header=False)

    
st.subheader('Datalog Aksi')
st.write(pd.DataFrame(get_data_input()))

st.subheader('Datalog Hasil')
st.write(pd.DataFrame(get_data_output()))
    
              
                 

    