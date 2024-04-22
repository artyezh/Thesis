import os


for filename in os.listdir('data_test'):
    if not filename.endswith(".txt"):
        continue

    with open(f'data_test/{filename}', 'r') as file:
        lines = file.readlines()

    with open(f'data_test/{filename}', 'w') as file:
        for line in lines:
            if line.startswith('#'):
                continue
            
            values = line.split()
            if len(values) == 3:
                zeros, lambda_, intensity_ = values
            
                line = f'{lambda_} {intensity_}\n'
                file.write(line)
            else:
                raise ValueError(f'{line}')
    
    if filename.startswith("pivo"):
        os.rename(f'data_test/{filename}', f'data_test/{filename[4:]}')

            
