from pandas import Series, DataFrame
import pandas as pd
import numpy as np
from faker import Faker
from sklearn.model_selection import train_test_split, cross_val_score, StratifiedKFold, KFold, cross_val_predict, GridSearchCV
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.linear_model import LinearRegression
from sklearn import linear_model
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, roc_auc_score
from sklearn.datasets import load_digits
#from adspy_shared_utilities import plot_feature_importances
import matplotlib.pyplot as plt
fake = Faker()
digits = load_digits


df = pd.read_csv('D:/talent.csv', sep=';')
genre= pd.get_dummies(df["genre"])
df = pd.concat([df, genre], axis=1)
#print(df[['genre', 'F', 'M']].head())
background= pd.get_dummies(df["background"])
df = pd.concat([df, background], axis=1)
cohorte= pd.get_dummies(df["cohorte"])
df = pd.concat([df, cohorte], axis=1)
retards= pd.get_dummies(df["retards"])
df = pd.concat([df, retards], axis=1)
absences= pd.get_dummies(df["absences"])
df = pd.concat([df, absences], axis=1)

id = df["id"]
prenom = df["prenom"]
nom = df["nom"]
genre = df["genre"]
background = df["background"]
cohorte = df["cohorte"]
retards = df["retards"]
absences = df["absences"]

del df["id"]
del df["prenom"]
del df["nom"]
del df["genre"]
del df["background"]
del df["cohorte"]
del df["retards"]
del df["absences"]

df = pd.concat([df, id], axis=1)

feat = df.drop(columns=['parti'],axis=1)
label = df["parti"]

X_train, X_test, y_train, y_test = train_test_split(feat, label, test_size=0.3, shuffle=True)

clf = RandomForestClassifier(max_depth=6, n_estimators=100)
clf = clf.fit(X_train, y_train)

prediction = clf.predict(X_train)

accuracy_train = accuracy_score(y_train, prediction)
print(accuracy_train)

prediction = clf.predict(X_test)

accuracy_test = accuracy_score(y_test, prediction)
print(accuracy_test)

probs = clf.predict_proba(X_test)
#print(probs)

list=[]
for i in range(len(probs)):
    list.append(probs[i][0])
#print(list)

liste=pd.DataFrame(list)
predicts = pd.concat([X_test, liste], axis=1)
#print(predicts.head())

drop=predicts.dropna()
drop = drop.rename(columns={0: 'predictions'})
drop['predictions']=drop['predictions'].map(lambda n: '{:.2%}'.format(n))

resul = drop[['id','predictions']]
print(resul)

#print(df.head())