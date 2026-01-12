from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix
import pandas as pd

df = pd.read_csv("weather/encodeddata.csv")

print(df.head())

x = df[['MinTemp',
    'MaxTemp',
    'Rainfall',
    'Evaporation',
    'Sunshine',
    'WindGustSpeed',
    'WindSpeed9am',
    'WindSpeed3pm',
    'Humidity9am',
    'Humidity3pm',
    'Pressure9am',
    'Pressure3pm',
    'Cloud9am',
    'Cloud3pm',
    'Temp9am',
    'Temp3pm',
    'RISK_MM']]
y  = df['RainTomorrow_Encoded']

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=2)
print(x_train)
print(y_test)

model = LogisticRegression()
model.fit(x_train,y_train)

pre = model.predict(x_test)
a=accuracy_score(y_test,pre)
print("accuracy score :",a*100,"%")
print("confusion metrix : ")
print(confusion_matrix(y_test,pre))
