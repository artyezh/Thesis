import os


for filename in os.listdir('data_raman'):
    if not filename.endswith(".txt"):
        continue

    if filename.startswith("pivo"):
        os.rename(f'data_raman/{filename}', f'data_raman/{filename[4:]}')