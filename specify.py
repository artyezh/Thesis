import pandas as pd


df = pd.read_excel(f'Beer_table_23_02.xlsx', engine='openpyxl')

IBU = df['IBU']
Alcohol = df['Alcohol']
FermentType = df['FermentType'] # Top - ale, Bottom - lager


