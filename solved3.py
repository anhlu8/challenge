import pandas as pd

my_csv = pd.read_csv('file.csv')
columnA = my_csv['A'].tolist()
columnB = my_csv['B'].tolist()

for i in columnB:
    if i not in columnA:
        print(i)
        
for i in range(1,1000001):
    if i not in columnA and i not in columnB:
        print(i)
    
# For part c, I think if the length of the CSV doubled, the memory usage would also double in auxiliary space