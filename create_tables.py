import os
from shutil import copyfile


data = {}

for filename in sorted(os.listdir('data_raman'), key=lambda x: int(x.split('.')[0])):
    with open(f'./data_raman/{filename}', 'r') as file:
        for line in file:
            if line.startswith('Unnamed'):
                continue
            lambda_, intensity_ = line.split()
            if lambda_ not in data and filename != '1.txt':
                print(f'Error: lambda = {lambda_} in file {filename} not found in data')

            data[lambda_] = data.get(lambda_, []) + [intensity_]


z = zip(*data.values())

with open('Dataset.csv', 'w') as table1:
    for lambda_, intensities in data.items():
        table1.write(lambda_ + ',')
    table1.write('\n')
    for intensities in z:
        for intensity in intensities:
            table1.write(intensity + ',')
        table1.write('\n')

#copyfile('Dataset.csv', 'IBU_Dataset.csv')
#copyfile('Dataset.csv', 'Type_Dataset.csv')
#copyfile('Dataset.csv', 'Alcohol_Percentages_Dataset.csv')

