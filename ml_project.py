# -*- coding: utf-8 -*-
"""ML Project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XiO8o28vWtwFVrtm8Xd1NUenLBqUEWOH

####Name: Shivam Mahajan
####Roll No.: UE203105
####Branch : CSE
"""

from sklearn.datasets import load_breast_cancer
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = load_breast_cancer()
data.keys()

data.target_names

df = pd.DataFrame(data.data)

df.head()

data.feature_names

df.columns = data.feature_names

df.head()

data.target

y = pd.DataFrame(data.target)

y.head()

df.isnull().sum()

df.isna().sum()

from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(df,y,test_size = 0.25,random_state = 42)

from sklearn.preprocessing import StandardScaler

sc=StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.fit_transform(X_test)

from sklearn.linear_model import LogisticRegression
classifier_log = LogisticRegression(random_state = 0)
classifier_log.fit(X_train,Y_train)

from sklearn.neighbors import KNeighborsClassifier
classifier_knn = KNeighborsClassifier(n_neighbors = 5)
classifier_knn.fit(X_train,Y_train)

from sklearn.svm import SVC
classifier_svc = SVC(kernel="linear",random_state=0)
classifier_svc.fit(X_train,Y_train)

from sklearn.naive_bayes import GaussianNB
classifier_gnb = GaussianNB()
classifier_gnb.fit(X_train,Y_train)

from sklearn.tree import DecisionTreeClassifier
classifier_dtc = DecisionTreeClassifier(criterion = 'entropy', random_state=0)
classifier_dtc.fit(X_train,Y_train)

from sklearn.ensemble import RandomForestClassifier
classifier_rfc = RandomForestClassifier(n_estimators = 10, criterion = 'entropy',random_state=0)
classifier_rfc.fit(X_train,Y_train)

classifier_list = [classifier_dtc,classifier_gnb,classifier_knn,classifier_log,classifier_rfc,classifier_svc]

from sklearn.metrics import confusion_matrix, classification_report

def accuracy(X_test,Y_test, classifier):
  print(f"\nClassifier\n{classifier}")
  Y_pred = classifier.predict(X_test)
  correct = 0
  total = len(Y_pred)
  for i,j in zip(Y_pred,Y_test[0]):
    if i == j:
      correct += 1
  acc = (correct/total)*100
  print(str(acc) + '\n' +'-'*30 + '\n')
  print("\n" + '*'*50 + '\n' + classification_report(Y_test, Y_pred) + '\n')
  cm = confusion_matrix(Y_test, Y_pred)
  print(f"Confusion Matrix\n{cm}\n")

for clf in classifier_list:
  accuracy(X_test, Y_test, clf)