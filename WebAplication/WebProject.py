import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
import pickle

base = pd.read_csv('insurance.csv')
base.Age.unique()
base.RiskAversion.unique()
base.MakeModel.unique()
base.Accident.unique()

x = base.iloc[:, [2, 4, 9]].values
y = base.iloc[:, 8].values

labelEncoder = LabelEncoder()
x[:, 0] = labelEncoder.fit_transform(x[:, 0])
x[:, 1] = labelEncoder.fit_transform(x[:, 1])
x[:, 2] = labelEncoder.fit_transform(x[:, 2])

modelo = GaussianNB()
modelo.fit(x, y)

previsoes = modelo.predict(x)
accuracy_score(y, previsoes)

pickle.dump(modelo, open('naivebayes_finalizado.sav', 'wb'))