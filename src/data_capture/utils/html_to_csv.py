import pandas as pd


df = pd.read_html("daily.xls", header=2,encoding = 'utf-8', decimal=',', thousands='.')[0]

print(df)