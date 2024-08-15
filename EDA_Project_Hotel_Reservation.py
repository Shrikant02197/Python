import pandas as pd
import numpy as np

df = pd.read_csv("C:\\Users\\LENOVO\\OneDrive\\Desktop\\shri\\Dataset-master\\hotel_bookings.csv")

print(df.shape)
print(df.dtypes)

#Numeric columns
df_numeric = df.select_dtypes(include=[np.number])
numeric_cols = df_numeric.columns.values
print(numeric_cols)

#non numeric columns
df_non_numeric = df.select_dtypes(exclude=[np.number])
non_numeric_cols = df_non_numeric.columns.values
print(non_numeric_cols)

import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib

plt.style.use('ggplot')

cols = df.columns[:30]
colours = ['#000099','#ffff00']
sns.heatmap(df[cols].isnull(),cmap=sns.color_palette(colours))
#plt.show()

for col in df.columns:
    pct_missing = np.mean(df[col].isnull())
    print('{} - {}%'.format(col, round(pct_missing*100)))

for col in df.columns:
    missing = df[col].isnull()
    num_missing = np.sum(missing)

    if num_missing > 0:
        print('Created missing indicator for: {}'.format(col))
        df['{}_ismissing'.format(col)] = missing

ismissing_cols = [col for col in df.columns if 'ismissing' in col]
df['num_missing'] = df[ismissing_cols].sum(axis=1)

df_num_missing_counts = df['num_missing'].value_counts().reset_index()

# Rename columns so that 'index' column actually has a name 'index'
df_num_missing_counts.columns = ['num_missing', 'count']

# Sort values by 'num_missing' and plot
df_num_missing_counts.sort_values(by='num_missing').plot.bar(x='num_missing', y='count')

#plt.show()

ind_missing = df[df['num_missing'] > 12].index
print("Rows with more than 12 missing values: \n",ind_missing)

df = df.drop(ind_missing,axis=0)

cols_to_drop = ['company']

df = df.drop(cols_to_drop,axis=1)

print("Percentage of missing data after technique 1 and 2:")

for col in df.columns:
    pct_missing = np.mean(df[col].isnull())
    if pct_missing > 0:
        print('{} - {:.3f}%'.format(col,round(pct_missing*100)))

print(df.dtypes)

df['meal'] = pd.Categorical(df.meal)
df['deposit_type'] = pd.Categorical(df.deposit_type)
df['agent'] = pd.Categorical(df.agent)

med = df['children'].median()
df['children'] = df['children'].fillna(med)

med1 = df['babies'].median()
df['babies'] = df['babies'].fillna(med1)

df_numeric = df.select_dtypes(include=[np.number])
numeric_cols = df_numeric.columns.values

for col in numeric_cols:
    missing = df[col].isnull()
    num_missing = np.sum(missing)

    if num_missing > 0:
        print("Imputing missing values for: {}".format(col))
        df['{}_ismissing'.format(col)] = missing
        med = df[col].median()
        df[col] = df[col].fillna(med)

df_non_numeric = df.select_dtypes(exclude=[np.number])
non_numeric_cols = df_non_numeric.columns.values

for col in non_numeric_cols:
    missing = df[col].isnull()
    num_missing = np.sum(missing)

    if num_missing > 0:
        print("Imputing missing value for: {}".format(col))
        df['{}_ismissing'.format(col)] = missing

        top = df[col].describe()['top']
        df[col] = df[col].fillna(top)

df['country'] = df['country'].fillna('_MISSING_')

df['babies'] = df['babies'].fillna(-999)

ismissing_cols = [col for col in df.columns if 'ismissing' in col]
df = df.drop(ismissing_cols,axis=1)

ismissing_cols = [col for col in df.columns if 'ismissing' in col]
df['num_missing'] = df[ismissing_cols].sum(axis=1)

df_num_missing_counts = df['num_missing'].value_counts().reset_index()

df_num_missing_counts.columns = ['num_missing', 'count']

df_num_missing_counts.sort_values(by='num_missing').plot.bar(x='num_missing', y='count')
#plt.show()

df['total_of_special_requests'].hist(bins=100)
df.boxplot(column=['total_of_special_requests'])
#plt.show()

print(df['total_of_special_requests'].describe())

df['deposit_type'].value_counts().plot.bar(x='deposit_type',y='count')
#plt.show()

num_rows = len(df.index)
low_information_cols = []

for col in df.columns:
    cnts = df[col].value_counts(dropna=False)
    top_pct = (cnts / num_rows).iloc[0]

    if top_pct > 0.95:
        low_information_cols.append(col)
        print('{0} - {1:.5f}'.format(col, top_pct * 100))
        print(cnts)
        print(low_information_cols)

print(df['reservation_status'].value_counts(dropna=False))

df['reservation_status_lower'] = df['reservation_status'].str.lower()

print(df['reservation_status_lower'].value_counts(dropna=False))

from nltk.metrics import edit_distance

df_city_ex = pd.DataFrame(data={'city':['delhiii','dalhi','delhi'
    ,'mumbai','moombai','mumbhai','hyderabad','kolkata']})

df_city_ex['city_distance_delhi'] = df_city_ex['city'].map(lambda x: edit_distance(x, 'delhi'))
df_city_ex['city_distance_mumbai'] = df_city_ex['city'].map(lambda x: edit_distance(x, 'mumbai'))

print(df_city_ex)

msk = df_city_ex['city_distance_delhi'] <= 2
df_city_ex.loc[msk, 'city'] = 'delhi'

msk = df_city_ex['city_distance_mumbai'] <= 2
df_city_ex.loc[msk,'city'] = 'mumbai'

df_city_ex['city_distance_delhi'] = df_city_ex['city'].map(lambda x: edit_distance(x, 'delhi'))
df_city_ex['city_distance_mumbai'] = df_city_ex['city'].map(lambda x: edit_distance(x, 'mumbai'))

print(df_city_ex)