import pandas as pd
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("weather/cleandata.csv")

df_label = df.copy()

le_RainTomorrow = LabelEncoder()
le_RainToday = LabelEncoder()

df_label['RainToday_Encoded'] = le_RainToday.fit_transform(df['RainToday'])
df_label['RainTomorrow_Encoded'] = le_RainToday.fit_transform(df['RainTomorrow'])

df_label.to_csv("encodeddata.csv",index=False)