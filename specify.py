import pandas as pd


df = pd.read_excel(f'Beer_table_23_02.xlsx', engine='openpyxl')

IBU = df['IBU']
Alcohol = df['Alcohol']
FermentType = df['FermentType'] # 1 - ale, 0 - lager


with open('Dataset.csv', 'r') as r_file:
    with open('IBU_Dataset.csv', 'w') as w_file:
        for k, line in enumerate(r_file):
            if k == 0:
                w_file.write(line[:-1] + 'IBU' + '\n')
            else:
                w_file.write(line[:-1] + str(IBU[k - 1]) + '\n')

with open('Dataset.csv', 'r') as r_file:
    with open('Type_Dataset.csv', 'w') as w_file:
        for k, line in enumerate(r_file):
            if k == 0:
                w_file.write(line[:-1] + 'FermentType' + '\n')
            else:
                w_file.write(line[:-1] + f'{1 if str(FermentType[k - 1]) == "Top" else 0}' + '\n')

with open('Dataset.csv', 'r') as r_file:
    with open('Alcohol_Percentages_Dataset.csv', 'w') as w_file:
        for k, line in enumerate(r_file):
            if k == 0:
                w_file.write(line[:-1] + 'Alcohol' + '\n')
            else:
                w_file.write(line[:-1] + str(Alcohol[k - 1]) + '\n')


