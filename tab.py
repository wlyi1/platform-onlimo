import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
import streamlit as st
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.metrics import accuracy_score   
from sklearn.model_selection import cross_val_score
import datetime as dt

df = pd.read_csv('df49.csv')
df_test = pd.read_csv('testml.csv')
st.header('Data Normal & Anomali')
j=47

def ml(data_input):
    #training machine learning model
    X = df_test.drop('Status', axis = 1)
    y = df_test['Status']

    test_size = 0.3
    seed = 7
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=seed)
    NN = KNeighborsClassifier(n_neighbors=5)
    NN.fit(X_train, y_train)
    y_pred = NN.predict(X_test)
    status = NN.predict(data_input)
    return status

def data(param):
    arr = df[param].to_numpy()
    arr = arr.reshape(j,4,6)
    

    mean = []
    std_data = []
    std_grad = []
    max_data = []
    min_data = []

    for i in range(j):
        y = arr[i].flatten()
        y_g = np.gradient(arr[i].flatten())
        x_mean = np.mean(y)
        x_std = np.std(y)
        x_g_std = np.std(y_g)
        x_max = np.max(y)
        x_min = np.min(y)
        mean.append(x_mean)
        std_data.append(x_std)
        std_grad.append(x_g_std)
        max_data.append(x_max)
        min_data.append(x_min)
        
    df_ml = pd.DataFrame(list(zip(mean, max_data, min_data, std_data, std_grad)), columns = ['Mean', 'Max', 'Min', 'Std_Data', 'Std_Gradient'])
    arr_ml = df_ml.to_numpy()
        
    df['TGL'] = pd.to_datetime(df['TGL']).dt.date
    df_ml['TGL'] = df['TGL'].unique()
    df_ml['TGL'] = df_ml['TGL'].apply(lambda x: dt.datetime.strftime(x, '%Y-%m-%d'))

    df_ml = df_ml.set_index(pd.DatetimeIndex(df_ml['TGL']))
    df_ml.index = df_ml.index.strftime('%Y-%m-%d')
    
    return arr, df_ml, arr_ml

def data_anom():
    result_DO = [x for x in df[-24:]['DO']]
    result_pH = [x for x in df[-24:]['pH']]
    result_NH = [x for x in df[-24:]['NH4']]
    result_NO = [x for x in df[-24:]['NO3']]
    ab_pH = sum(map(lambda x : x<5 and x>9, result_pH))
    ab_DO = sum(map(lambda x : x<1, result_DO))
    ab_NH4 = sum(map(lambda x : x>100, result_NH))
    ab_NO3 = sum(map(lambda x : x>100, result_NO))
    
    locals_stored = list(locals())
    list_var = dict()
    for i in locals_stored:
        list_var[i] = eval(i)
    return list_var

tab1, tab2, tab3, tab4, tab5 = st.tabs(['pH', 'DO', 'NH4', 'NO3', 'NO3'])
name_param = ['pH', 'DO', 'NH4', 'NO3']
stat_data = data_anom()

l_tab = [tab1, tab2, tab3, tab4]


for i1,j2 in zip(l_tab, name_param):
    with i1:
        st.write(f'Data {j2} Normal')
        st.write(24 - stat_data[f'ab_{j2}'])
        st.write(f'Data {j2} Anomali')
        st.write(stat_data[f'ab_{j2}'])

        
with tab5:
    st.header('Analisis Anomali Nitrat')
    st.text('Analisis menggunakan algoritma machine learning KNN')
    
    df_no = data('NO3')
    status = ml(df_no[2])

    df_no[1]['Status'] = status

    d1 = st.date_input('Pilih Tanggal', dt.date(2022,1,2))  
    d1 = d1.strftime('%Y-%m-%d')    

    stats = df_no[1]['Status'].loc[df_no[1]['TGL'] == str(d1)].values
    #st.write(stats)
    if stats == 'Normal':
        st.success('Data Nitrat Normal')
    else:
        st.error('Data Nitrat Anomali')









    