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

# 8 filtering date values
## FY Example

## FY 20
df.loc[df['month_year'] < '2020-07', 'fiscal year'] = 'FY 20'

## FY 21
df.loc[((df['month_year'] > '2020-06') & (df['month_year'] < '2021-07')), 'fiscal year'] = 'FY 21'

##  Masks
start = df['month_year'] > '2020-06'
end = df['month_year'] <= '2021-06'
between = start & end
df.loc[between]['fiscal year'] = 'FY 21'

# 9 using .apply() to multiply many columns by a value e.g. by -1

cols = ['sales base upper', 'sales base middle', 'costs base middle', 'capex base middle', 'capex base upper', \
        'costs base upper', 'sales base lower', 'capex base lower', 'costs base lower', 'ebitda base lower' \
        ,'fcf base lower', 'ebitda base upper', 'fcf base middle', 'roi base middle', 'ebitda base middle', 'fcf base upper' \
        , 'roi base upper', 'roi base lower', 'sales impact lower', 'costs impact lower', 'capex impact lower', 'ebitda impact lower'
        , 'fcf impact lower', 'roi impact lower', 'sales impact middle', 'costs impact middle', 'capex impact middle', 'ebitda impact middle'
        , 'fcf impact middle', 'roi impact middle', 'sales impact upper', 'costs impact upper', 'capex impact upper', 'ebitda impact upper'
        , 'fcf impact upper', 'roi impact upper']


df_sub[cols] = df_sub[cols].apply(lambda x: x* -1)

# 10 Merge df using list of inputs
########## 2. Combine and merge data ##########
list_simulation = [cc_simulation_low, cc_simulation_high,\
                    gdp_simulation_low, gdp_simulation_high,\
                    un_emp_low, un_emp_high,
                    pur_int_low, pur_int_high]
    

    #merge simulation data     
    df_merged = reduce(lambda  left,right: pd.merge(left,right,on=['date'],how='outer'), list_simulation) 

# Reset the format of a pesky datetime column
# If the desired format is Y-M-D but column keeps giving Y-D-M then we have to use dt.strftime 
# We set the string output to read the column in its current format and then reset it with dayfirst
dfSource['date'] = dfSource["date"].dt.strftime("%Y-%d-%m")
dfSource['date'] = pd.to_datetime(dfSource['date'], dayfirst=True, infer_datetime_format=False)
