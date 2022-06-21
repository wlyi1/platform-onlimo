import pandas as pd
import datetime
from datetime import datetime as dt
import streamlit as st
import streamlit.components.v1 as components


sheet = list(range(41,45))
filename = []
varname = []
for i in sheet:
    filename.append('OL' + str(i) + '_2022.csv')
    varname.append('OL' + str(i))
    
for df in varname:
    globals()[f'{df}'] = pd.read_csv(f'{df}_2022.csv')    
    globals()[f'{df}']['new_date'] = pd.to_datetime(globals()[f'{df}']['DATE'])
    globals()[f'{df}']['tgl'] = pd.to_datetime(globals()[f'{df}']['DATE'] + ' ' + globals()[f'{df}']['TIME'])
    globals()[f'pH_{df[2:]}'] = [x for x in globals()[f'{df}'][-24:]['pH']]
    globals()[f'ab_pH_{df[2:]}'] = sum(map(lambda x : x<5 and x>9, globals()[f'pH_{df[2:]}']))
    globals()[f'DO_{df[2:]}'] = [x for x in globals()[f'{df}'][-24:]['DO']]
    globals()[f'ab_DO_{df[2:]}'] = sum(map(lambda x : x<1, globals()[f'DO_{df[2:]}']))
    globals()[f'NH4_{df[2:]}'] = [x for x in globals()[f'{df}'][-24:]['NH4']]
    globals()[f'ab_NH4_{df[2:]}'] = sum(map(lambda x : x>100, globals()[f'NH4_{df[2:]}']))
    globals()[f'NO3_{df[2:]}'] = [x for x in globals()[f'{df}'][-24:]['NO3']]
    globals()[f'ab_NO3_{df[2:]}'] = sum(map(lambda x : x>100, globals()[f'NO3_{df[2:]}']))
    globals()[f'tgl_{df[2:]}'] = globals()[f'{df}']['tgl'].max().strftime(("%Y-%m-%d %H:%M"))

st.title('Status Masalah ONLIMO KLHK')

#KLHK 41
st.header('KLHK 41')
header_41_a, header_41_b = st.columns(2)

if OL41['new_date'].max().strftime('%Y-%m-%d') == dt.today().strftime('%Y-%m-%d'): 
    header_41_a.button(tgl_41)
    header_41_b.success('ONLINE')
                       
elif OL41['new_date'].max().strftime('%Y-%m-%d') < dt.today().strftime('%Y-%m-%d'): 
    header_41_a.button(tgl_41)
    header_41_b.warning('OFFLINE')
        
else:
    header_41_a.button(tgl_41)                  
    header_41_b.error('ERROR')   

col1, col2, col3, col4 = st.columns(4)
col1.metric('pH', ab_pH_41, pH_41[-1])
col2.metric('DO', ab_DO_41, DO_41[-1])
col3.metric('NH', ab_NH4_41, NH4_41[-1])
col4.metric('NO', ab_NO3_41, NO3_41[-1])

st.markdown("""<hr style="height:5px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)

#KLHK 42
st.header('KLHK 42')
header_42_a, header_42_b = st.columns(2)

if OL42['new_date'].max().strftime('%Y-%m-%d') == dt.today().strftime('%Y-%m-%d'): 
    header_42_a.button(tgl_42)
    header_42_b.warning('OFFLINE')
                       
elif OL42['new_date'].max().strftime('%Y-%m-%d') < dt.today().strftime('%Y-%m-%d'): 
    header_42_a.button(dt.today().strftime('%Y-%m-%d %H:%M'))
    header_42_b.success('ONLINE')
        
else:
    header_42_a.button(tgl_42)                  
    header_42_b.error('ERROR')   

col1_42, col2_42, col3_42, col4_42 = st.columns(4)
col1_42.metric('pH', ab_pH_42, pH_42[-1])
col2_42.metric('DO', ab_DO_42, DO_42[-1])
col3_42.metric('NH', ab_NH4_42, NH4_42[-1])
col4_42.metric('NO', ab_NO3_42, NO3_42[-1])
st.markdown("""<hr style="height:5px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)

#KLHK 43
st.header('KLHK 43')
header_43_a, header_43_b = st.columns(2)

if OL43['new_date'].max().strftime('%Y-%m-%d') == dt.today().strftime('%Y-%m-%d'): 
    header_43_a.button(tgl_43, key='43_a')
    header_43_b.success('ONLINE')
                       
elif OL43['new_date'].max().strftime('%Y-%m-%d') < dt.today().strftime('%Y-%m-%d'): 
    header_43_a.button(tgl_43, key='43b')
    header_43_b.error('ERROR')
        
else:
    header_43_a.button(tgl_43, key='43c')                  
    header_43_b.warning('OFFLINE')   

col1_43, col2_43, col3_43, col4_43 = st.columns(4)
col1_43.metric('pH', ab_pH_43, pH_43[-1])
col2_43.metric('DO', ab_DO_43, DO_43[-1])
col3_43.metric('NH', ab_NH4_43, NH4_43[-1])
col4_43.metric('NO', ab_NO3_43, NO3_43[-1])
st.markdown("""<hr style="height:5px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)

#KLHK 44
st.header('KLHK 44')
header_44_a, header_44_b = st.columns(2)

if OL44['new_date'].max().strftime('%Y-%m-%d') == dt.today().strftime('%Y-%m-%d'): 
    header_44_a.button(tgl_44, key='44a')
    header_44_a.success('ONLINE')
                       
elif OL44['new_date'].max().strftime('%Y-%m-%d') < dt.today().strftime('%Y-%m-%d'): 
    header_44_a.button(tgl_44, key='44b')
    header_44_b.warning('OFFLINE')
        
else:
    header_44_a.button(tgl_44, key='44c')                  
    header_44_b.error('ERROR')   

col1_44, col2_44, col3_44, col4_44 = st.columns(4)
col1_44.metric('pH', ab_pH_44, pH_44[-1])
col2_44.metric('DO', ab_DO_44, DO_44[-1])
col3_44.metric('NH', ab_NH4_44, NH4_44[-1])
col4_44.metric('NO', ab_NO3_44, NO3_44[-1])