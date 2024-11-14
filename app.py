import pandas as pd
import numpy as np
import streamlit as st
from functions.plotfunctions import *
from functions.calcfunctions import *

df = pd.read_csv('dataset/AirQualityUCI.csv')
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
df = df.loc[df['Date'].notna()]
cpdf = df.copy()
columns = ["CO(GT)","PT08.S1(CO)","C6H6(GT)","NOx(GT)","NO2(GT)","Temperature","Relative Humidity","Absolute Humidity"]
all_columns = columns + ["NMHC(GT)","PT08.S2(NMHC)","PT08.S3(NOx)","PT08.S4(NO2)","PT08.S5(O3)"]
pollutants = ["CO(GT)","PT08.S1(CO)","C6H6(GT)","NOx(GT)","NO2(GT)","NMHC(GT)","PT08.S2(NMHC)","PT08.S3(NOx)","PT08.S4(NO2)","PT08.S5(O3)"]
df[columns] = df[columns].replace(-200, np.nan)
df['DateTime'] = pd.to_datetime(df['Date'] + ' ' + df['Time'], format='%m/%d/%Y %H:%M:%S')
df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y')
df['Time'] = pd.to_datetime(df['Time'], format='%H:%M:%S')
df['CO(GT)'] = df['CO(GT)']*1000
df.set_index('DateTime', inplace=True)

st.set_page_config(layout="wide")
st.markdown('# Air Quality Analysis')
st.divider()

st.markdown('### Dataset Overview')
st.write("This project utilizes the Air Quality dataset from the UCI Machine Learning Repository. An insight into the dataset is provided below:")
st.write(cpdf.head())
st.write("The dataset can be downloaded from the UCI Machine Learning Repository [here](https://archive.ics.uci.edu/ml/datasets/Air+Quality).")
st.divider()

st.markdown('### Time Series Plot for pollutants:')
selectedpollutants = st.multiselect('Select pollutants to plot:', pollutants, default=["CO(GT)", "NOx(GT)"], key=0)
st.plotly_chart(plotTimeSeries(df, selectedpollutants))
st.divider()

st.markdown('### Correlation Heatmap of Air Quality Measurements:')
st.plotly_chart(plotCorrelationHeatmap(df, columns))
st.divider()

st.markdown('### Histogram of Pollutant Concentration:')
selectedhistogrampollutant = st.selectbox('Select a pollutant:', pollutants, index=0)
st.plotly_chart(plotHistogram(df, selectedhistogrampollutant))
st.divider()

st.markdown('### Box Plot for Monthly Pollutant Concentration:')
selectedboxpollutant = st.selectbox('Select a pollutant:', pollutants, index=1)
st.plotly_chart(plotBoxplot(df, selectedboxpollutant))
st.divider()

st.markdown('### Scatter Plot of Pollutant Concentration vs Climate:')
selectedscatterpollutant = st.selectbox('Select a pollutant:', pollutants, index=2)
selectedclimate = st.selectbox('Select a climate variable:', ['Temperature', 'Relative Humidity', 'Absolute Humidity'], index=0)
st.plotly_chart(plotScatterplot(df, selectedclimate, selectedscatterpollutant))
st.divider()

st.markdown('### Stacked Area Chart for Average Daily Levels:')
selectedareapollutants = st.multiselect('Select pollutants to plot:', pollutants, default=["CO(GT)", "NOx(GT)"],key=1)
st.plotly_chart(plotStackedAreaChart(df, selectedareapollutants))
st.divider()

st.markdown('### Calculate Statistics:')
selectedstatpollutant = st.selectbox('Select a pollutant:', pollutants, index=3)
st.write(calculateStats(df, selectedstatpollutant))
st.divider()

st.markdown('### This project was created by [Debajit Kanungo](https://github.com/barondebajit).')