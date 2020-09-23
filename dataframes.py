## The following are useful scripts or operations to be done upon a pandas df
import pandas as pd

# 1 Transform string column to datetime Y-M-D
csv['date'] = pd.to_datetime(csv['date'])
csv['date'] = csv["date"].dt.strftime('%Y-%m-%d')

# 2 Useful operator for finding the first or last NANS in a pd series e.g. df column
df.last_valid_index()
df.first_valid_index

# 3 create a file which can be used to fill the body of an SQL query used by athena
# useful for cloud migrations
csv = pd.read_csv('facttable.csv', sep = ';')

types = list(csv.dtypes)

names = list(csv.columns.values)

with open('listfile.txt', 'w') as filehandle:
    for name, typ in zip(names, types):
        filehandle.write('`%s`\t' % name)
        filehandle.write('%s,\n' % typ)

print("Athena template file created")

# 4 conditional selecting of collumn values based upon loc
res = actuals.loc[actuals['date'] >= '2020-01-01', ['date','Sales']]

# 5 conditional filter out column value based on date

df.loc[df['date'] < '01-12-2021', 'sales base upper'] = None

#    May require the following step to add a month year column in between
df['month_year'] = pd.to_datetime(df['date']).dt.to_period('M')
df.loc[df['month_year'] < '2021-12', 'sales base upper'] = None

# 6 change format of df date column & ensure date comes first in the result
print(pd.to_datetime(df.date, dayfirst=True).dt.strftime('%Y-%m-%d'))

# 7 indexing values in pandas df (interestingly it seems loc uses row then column for this stuff)
index = action_impact_result['actual sales'].last_valid_index()
value = action_impact_result.loc[index,['actual sales']].values[0]