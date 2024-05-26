import os


for filename in os.listdir('data_test'):
    # if not filename.endswith(".txt"):
    #     continue

    with open(f'data_test/{filename}', 'r') as file:
        lines = file.readlines()

    with open(f'data_test/{filename}', 'w') as file:
        for line in lines:
            if line.startswith('#') or line.startswith('Unnamed'):
                continue
            
            values = line.split()
            if len(values) == 3:
                zeros, lambda_, intensity_ = values
            elif len(values) == 2:
                lambda_, intensity_ = values
            else:
                raise ValueError(f'{line}')
            
            line = f'{float(lambda_)} {float(intensity_)}\n'
            file.write(line)
    print(f'{filename} is done')
    # if filename.startswith("pivo"):
    #     os.rename(f'data_test/{filename}', f'data_test/{filename[4:]}')


            
