# to install pandas lib for working with csv # pip install pandas
import pandas as pd

f = pd.read_csv('example.csv')

# print(f.head(10)) # to show first 10 rows excluding header

# print(f.tail(10)) # to show last 10 rows

# to clean csv file

# to remove null from file
# this will remove row that contains NaN
# new_file = f.dropna()
# print(new_file)

# to get specific data
yam_kino_data = f[f['city'] == 'Yamkino']
female_data = f[f['gender'] == 'Female']

print(yam_kino_data)
print(female_data)

# export data into csv file
female_data.to_csv('female_data.csv')
