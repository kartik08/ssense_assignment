import pandas as pd
import numpy as np
import joblib
from datetime import datetime, timedelta
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, roc_auc_score


#Read data 
data = pd.read_csv("D:\SSense\data.csv")

#Data Cleaning and prep
data.drop(["transaction_id", "user_id", "timestamp", "status"], axis=1, inplace=True)
for col in ["device_type", "location", "card_type"]:
    le = LabelEncoder()
    data[col] = le.fit_transform(data[col])

data["is_vpn"] = data["is_vpn"].astype(int)

#SplitData
features = data.drop("is_fraud", axis=1)
output = data["is_fraud"]
x_train,x_test,y_train,y_test = train_test_split(features,output,test_size=.25)

# ScaleFeatures
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)


# TrainLogisticModel
model = LogisticRegression()
model.fit(x_train, y_train)


# MakePredictions
y_pred = model.predict(x_test)
y_prob = model.predict_proba(x_test)[:, 1]


# Model Evaluation
print("accuracy:", accuracy_score(y_test, y_pred))
print("confusion natrix:\n", confusion_matrix(y_test, y_pred))
print("classificaion report:\n", classification_report(y_test, y_pred))
print("ROC AUC Score:", roc_auc_score(y_test, y_prob))


#Saving model
joblib.dump(model,"D:/SSense/model.pkl")