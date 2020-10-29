import pandas as pd

csv = pd.read_csv('indicator_data.csv', sep = ';')

csv.columns = csv.columns.str.replace(' ','_')

types = list(csv.dtypes)

names = list(csv.columns.values)

with open('listfile.txt', 'w') as filehandle:
    for name, typ in zip(names, types):
        filehandle.write('`%s`\t' % name)
        filehandle.write('%s,\n' % typ)