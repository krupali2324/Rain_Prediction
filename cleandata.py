import pandas as pd
from sklearn.preprocessing import LabelEncoder,MinMaxScaler


df = pd.read_csv("weather.csv")

print(df.head())
print(df.isnull().sum())

df['Sunshine'].fillna(df['Sunshine'].mean().round(),inplace=True)
df['WindGustDir'].fillna(df['WindGustDir'].mode()[0],inplace=True)
df['WindDir9am'].fillna(df['WindDir9am'].mode()[0],inplace=True)
df['WindDir3pm'].fillna(df['WindDir3pm'].mode()[0],inplace=True)
df['WindGustSpeed'].fillna(df['WindGustSpeed'].mean().round(),inplace=True)
df['WindSpeed9am'].fillna(df['WindSpeed9am'].mean().round(),inplace=True)
dr = df.dropna()
dr.to_csv("cleandata.csv",index=False)
print(df.isnull().sum())

