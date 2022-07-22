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

#st.set_page_config(layout="wide")
st.title('Stasiun ONLIMO')
#KLHK 41

def status_onlimo(id_ol):
    st.header(id_ol)
    globals()[f'header_a_{id_ol}'], globals()[f'header_b_{id_ol}'] = st.columns(2)

    if OL41['new_date'].max().strftime('%Y-%m-%d') == dt.today().strftime('%Y-%m-%d'): 
        globals()[f'header_a_{id_ol}'].button(tgl_41, key=f'{id_ol}_a')
        globals()[f'header_b_{id_ol}'].success('ONLINE')

    elif OL41['new_date'].max().strftime('%Y-%m-%d') < dt.today().strftime('%Y-%m-%d'): 
        globals()[f'header_a_{id_ol}'].button(tgl_41, key=f'{id_ol}_b')
        globals()[f'header_b_{id_ol}'].warning('OFFLINE')

    else:
        globals()[f'header_a_{id_ol}'].button(tgl_41, key=f'{id_ol}_b')                  
        globals()[f'header_b_{id_ol}'].error('ERROR')   

    col1, col2, col3, col4 = st.columns(4)
    col1.metric('pH', ab_pH_41, pH_41[-1])
    col2.metric('DO', ab_DO_41, DO_41[-1])
    col3.metric('NH', ab_NH4_41, NH4_41[-1])
    col4.metric('NO', ab_NO3_41, NO3_41[-1])

    st.markdown("""<hr style="height:5px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)

onlimo = ['41', '42', '43', '44']

for id_ol in onlimo:
    status_onlimo(id_ol)