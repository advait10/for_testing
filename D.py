# Databricks notebook source
! pip install yfinance

# COMMAND ----------

import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta
import time
import json

df = yf.download(tickers=['TCS.NS'], period='1d', interval='1m')
df.reset_index(inplace=True)
df['Timestamp'] = pd.to_datetime(df['Datetime'])
df['Timestamp'] = df['Timestamp'] + pd.to_timedelta(df.groupby('Timestamp').cumcount(), unit='m')
df['Daily Change %'] = df['Close'].pct_change() * 100
for i in df['Daily Change %']:
    avg = sum(i)/len(df['Daily Change %'])
    print(avg)

