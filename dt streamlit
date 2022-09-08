import pyodbc
import pandas as pd
from sqlalchemy import create_engine, event
from sqlalchemy.engine import URL
from datetime import date
import numpy as np
from numpy import load
import streamlit as st

def clean_data(x):
    if all(x['logTime'].values == data_24.all()) == False:
        df_clean = x.drop_duplicates(subset='logTime', keep='last')
        df_clean = pd.concat([df_clean, df_nan])
        df_clean = df_clean.sort_values(by=['logTime'])
        df_clean = df_clean.fillna(method='ffill').fillna(method='bfill')
        df_clean = df_clean.drop_duplicates(subset='logTime', keep='last')
        return df_clean
    return x

tgl = st.date_input('Tanggal Awal')
data_24 = load('jam_24.npy', allow_pickle = True)
df_nan = pd.read_csv('df_nan.csv')
index = np.arange(1,25)

conn_str = 'DRIVER={SQL Server};server=DESKTOP-ELAQ9RU\SQLEXPRESS;Database=awlr_mondylia;Trusted_Connection=yes;'
con_url = URL.create('mssql+pyodbc', query={'odbc_connect': conn_str})
engine = create_engine(con_url)

query = """select pH, DO, Cond, Turb, Temp, NH4,NO3,ORP,COD,BOD,TSS,NH3_N,logDate, datepart(hour, logTime) as logTime 
from periodicdata where Station=12 order by logDate,logTime"""
df = pd.read_sql(query, engine)
st.write(df)
df['logDate'] = pd.to_datetime(df['logDate']).dt.date

df_clean = df.loc[df['logDate']==tgl]
st.write(df_clean)

df_con=clean_data(df_clean)
df_con.set_index(index, inplace=True)

st.write(df_con)



