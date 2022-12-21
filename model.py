# LOGISTIC REGRESSION for  binary classifcation
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
df = pd.read_csv("Diabetes_dataset.csv")
print(df.info())

df.describe(include="all").to_csv("Summary_stats_diabetes.csv")

## data cleaning for glucose.
# Replace missing values with mean/median
print(list(df.Glucose).count(0))
df.Glucose = df.Glucose.replace(0, df.Glucose.mean())
print(list(df.Glucose).count(0))

y = df.Outcome
x = df.drop("Outcome", axis=1)
import sklearn.preprocessing import StandardScaler
x_scaled = StandardScaler().fit_transform
x_train, x_test, y_train, y_test = train_test_split(x_scaled, y, train_size=0.7, random_state=None)
model = LogisticRegression()
model.fit(x_train, y_train)
x_new = [2, 100, 60, 20, 30, 30, 0.7, 25]
y_new = model.predict([x_new])
print(y_new)

# Confusing metrics later becomes accuracy
y_pred = model.predict(x_test)
cnfm = confusion_matrix(y_test, y_pred)
print(cnfm)
acc = accuracy_score(y_test, y_pred)
print(acc)

clf = classification_report(y_test, y_pred)
print("metrics losgistric repgression")
print(clf)

# how to balance dataset. Augment data by adding rows
# by randomisogn the data. You can also reeuce it

# normal distribuited data when Gaussin NB naybe bayes when we have good data

model_nb = GaussianNB()
model_nb.fit(x_train,y_train)
print("metrics gaussian nb")
y_predict_nb = model_nb.predict(x_test)
clf_nb = classification_report(y_test, y_predict_nb)
print(clf_nb)


# decision tree
print("decision tree")
model_dt = DecisionTreeClassifier()
model_dt.fit(x_train,y_train)
y_predict_dt = model_dt.predict(x_test)
print("dt")
cnfm_dt = confusion_matrix(y_test, y_pred)
clf_dt = classification_report(y_test, y_predict_nb)
acc_dt = accuracy_score(y_test, y_pred)
print(cnfm)
print(acc)
print(clf_dt)

