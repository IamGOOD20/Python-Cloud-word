import os
import pandas as pd

coloms1 = list()
coloms2 = list()

for i in range(1, 11):
    os.chdir('E:\TEST FROM COMPANIES\CIVISION\Test-CIVI\Jobs')
    with open(f'vacancy_{i}.txt', encoding='utf-8') as f:
        title = f.readlines(1)
        description = f.readlines()[0:]
    coloms1.append(''.join(title).rstrip('\n'))
    coloms2.append(''.join(description).replace('\n', ' '))

data = {'Vocancy': coloms1,
        'Discription': coloms2}

df = pd.DataFrame(data)
print(df)