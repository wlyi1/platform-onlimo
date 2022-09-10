import pyodbc
import pandas as pd
from sqlalchemy import create_engine, event
from sqlalchemy.engine import URL
from datetime import date
import numpy as np
from datetime import datetime
from numpy import load

#import pre data
data_24 = load('jam_24.npy', allow_pickle = True)
df_nan = pd.read_csv('df_nan.csv')
index = np.arange(1,25)

conn_str = 'DRIVER={SQL Server};server=DESKTOP-ELAQ9RU\SQLEXPRESS;Database=awlr_mondylia;Trusted_Connection=yes;'
con_url = URL.create('mssql+pyodbc', query={'odbc_connect': conn_str})
engine = create_engine(con_url)

#import data from SQL Server
query = """select pH, DO, Cond, Turb, Temp, NH4,NO3,ORP,COD,BOD,TSS,NH3_N,logDate, datepart(hour, logTime) as logTime 
from periodicdata where Station=12 order by logDate,logTime"""
df = pd.read_sql(query, engine)
df['logDate'] = pd.to_datetime(df['logDate']).dt.date

tanggal = np.unique(df['logDate'].values)

#drop today data
tgl = date.today()
df = df.loc[df['logDate'] != tgl]

arr = []

for i in tanggal:
    df_tgl = df.loc[df['logDate'] == i]
    
    if not np.array_equiv(df_tgl['logTime'].values, data_24):
        df_clean = df_tgl.drop_duplicates(subset='logTime', keep='last')
        df_clean = pd.concat([df_clean, df_nan])
        df_clean = df_clean.sort_values(by=['logTime'])
        df_clean = df_clean.fillna(method='ffill').fillna(method='bfill')
        df_clean = df_clean.drop_duplicates(subset='logTime', keep='last')
        df_clean.drop(columns=df_clean.columns[-1], axis=1, inplace=True)
        arr_clean = df_clean.to_numpy()
        arr.append(arr_clean)
       
    else:
        arr_clean = df_tgl.to_numpy()
        arr.append(arr_clean)
