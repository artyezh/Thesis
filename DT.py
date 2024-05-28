from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

from sklearn.metrics import classification_report, accuracy_score, precision_score, recall_score, f1_score


# Завантаження даних
df = pd.read_csv("./datasets/Type_Dataset.csv")

print(df.head()) #shows the first 5 rows of the dataset

x = df.drop('FermentType', axis=1)
y = df['FermentType']

scaler = MinMaxScaler()
x_scaled = scaler.fit_transform(x)

x_train, x_test, y_train, y_test = train_test_split(x_scaled, y, test_size=0.2, random_state=42)

# Create and train decision tree model
dt = DecisionTreeClassifier(max_depth=5, random_state=42)
dt.fit(x_train, y_train)

# Predict on test set
y_pred_dt = dt.predict(x_test)

# Evaluate model
accuracy_dt = accuracy_score(y_test, y_pred_dt)
precision_dt = precision_score(y_test, y_pred_dt, average='weighted')
recall_dt = recall_score(y_test, y_pred_dt, average='weighted')
f1_dt = f1_score(y_test, y_pred_dt, average='weighted')

print(f'Decision Tree - Accuracy: {accuracy_dt:.2f}')
print(f'Decision Tree - Precision: {precision_dt:.2f}')
print(f'Decision Tree - Recall: {recall_dt:.2f}')
print(f'Decision Tree - F1-score: {f1_dt:.2f}')

# Classification report
print("Decision Tree Classification Report:")
print(classification_report(y_test, y_pred_dt))