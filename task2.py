# Classification with Decision Tree and Random Forest
# Apply Decision tree and Random forest and get good accurecy
# (https://www.kaggle.com/datasets/nishathakkar/100-sales)


#import necessary libraries:
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import LabelEncoder
from sklearn.utils.class_weight import compute_class_weight

#load dataset
data = '100_Sales.csv'
df = pd.read_csv(data)

#preprocess data
# print(df.isnull().sum())
# print(df.head())
# print(df.info())

df['Ship_Date'] = pd.to_datetime(df['Ship_Date'])

#take y, m, d, w from date column
df['Ship_Year'] = df['Ship_Date'].dt.year
df['Ship_Month'] = df['Ship_Date'].dt.month
df['Ship_Day'] = df['Ship_Date'].dt.day
df['Ship_DayOfWeek'] = df['Ship_Date'].dt.dayofweek

#encoding
encoder = LabelEncoder()
for col in ['Region', 'Country', 'Item_Type', 'Sales_Channel']:
    df[col] = encoder.fit_transform(df[col])

# Define features and target
X = df.drop(columns=['Order_Priority', 'Ship_Date'])
y = df['Order_Priority']

# Encode target variable
y = encoder.fit_transform(y)

# Compute class weights for handling class imbalance
class_weights = compute_class_weight('balanced', classes=np.unique(y), y=y)
class_weights_dict = dict(enumerate(class_weights))

#split data for traing(70%) and testing(30%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

#decision tree with GridSearchCV(for hyperparameter tuning)
param_grid_dtc = {
    'max_depth': [5, 10, 15, 20, None],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4],
    'class_weight': [class_weights_dict]
}

dtc = DecisionTreeClassifier(random_state=42)
grid_search_dtc = GridSearchCV(estimator=dtc, param_grid=param_grid_dtc, cv=5, n_jobs=-1, scoring='accuracy')
grid_search_dtc.fit(X_train, y_train)

#decision tree evaluate
best_dtc = grid_search_dtc.best_estimator_
y_pred_dtc = best_dtc.predict(X_test)

print("Decision Tree Best Parameters:", grid_search_dtc.best_params_)
print("\nDecision Tree Accuracy:", accuracy_score(y_test, y_pred_dtc))
print("\nDecision Tree Classification Report:\n", classification_report(y_test, y_pred_dtc))
print("\nDecision Tree Confusion Matrix:\n", confusion_matrix(y_test, y_pred_dtc))

#random forest with GridSearchCV(for hyperparameter tuning)
param_grid_rfc = {
    'n_estimators': [100, 200, 300],
    'max_depth': [10, 20, 30, None],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4],
    'class_weight': [class_weights_dict]
}

rfc = RandomForestClassifier(random_state=42)
grid_search_rfc = GridSearchCV(estimator=rfc, param_grid=param_grid_rfc, cv=5, n_jobs=-1, scoring='accuracy')
grid_search_rfc.fit(X_train, y_train)

#random forest evaluate
best_rfc = grid_search_rfc.best_estimator_
y_pred_rfc = best_rfc.predict(X_test)

print("Random Forest Best Parameters:", grid_search_rfc.best_params_)
print("\nRandom Forest Accuracy:", accuracy_score(y_test, y_pred_rfc))
print("\nRandom Forest Classification Report:\n", classification_report(y_test, y_pred_rfc))
print("\nRandom Forest Confusion Matrix:\n", confusion_matrix(y_test, y_pred_rfc))
