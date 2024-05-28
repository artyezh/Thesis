import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import KFold
from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import numpy as np

# Read the CSV file "Type_Dataset.csv" into a Pandas DataFrame
df = pd.read_csv("./datasets/Type_Dataset.csv")

# Define x by dropping the FermentType column from the DataFrame df
x = df.drop('FermentType', axis=1)

# Define y as the FermentType column of the DataFrame df
y = df['FermentType']

# Create a new k-fold cross validator object with 5 folds
kf = KFold(n_splits=5, shuffle=True, random_state=2)

accuracy_scores = []
precision_scores = []
recall_scores = []
f1_scores = []

# Iterate through the folds
for train_index, val_index in kf.split(x):
    x_train, x_val = x.iloc[train_index], x.iloc[val_index]
    y_train, y_val = y.iloc[train_index], y.iloc[val_index]

    # Initialize a scaler, fit it on the training data, and transform both the training and validation data
    scaler = MinMaxScaler()
    x_train_scaled = scaler.fit_transform(x_train)
    x_val_scaled = scaler.transform(x_val)

    # Initialize a PCA object to retain 95% of the variance, fit it on the scaled training data, and transform both the scaled training and validation data
    pca = PCA(n_components=0.95)
    x_train_pca = pca.fit_transform(x_train_scaled)
    x_val_pca = pca.transform(x_val_scaled)

    # Initialize a KNN classifier with 5 neighbors, fit it on the transformed training data, and predict on the transformed validation data
    knn = KNeighborsClassifier(n_neighbors=7)
    knn.fit(x_train_pca, y_train)
    y_pred = knn.predict(x_val_pca)

    # Calculate accuracy, precision, recall, and F1 score for the current fold and append them to the respective lists
    accuracy_scores.append(accuracy_score(y_val, y_pred))
    precision_scores.append(precision_score(y_val, y_pred, average='weighted'))
    recall_scores.append(recall_score(y_val, y_pred, average='weighted'))
    f1_scores.append(f1_score(y_val, y_pred, average='weighted'))

# Calculate and print the mean and standard deviation of each metric across all folds
print("Accuracy: {:.2f} (+/- {:.2f})".format(np.mean(accuracy_scores), np.std(accuracy_scores)))
print("Precision: {:.2f} (+/- {:.2f})".format(np.mean(precision_scores), np.std(precision_scores)))
print("Recall: {:.2f} (+/- {:.2f})".format(np.mean(recall_scores), np.std(recall_scores)))
print("F1-score: {:.2f} (+/- {:.2f})".format(np.mean(f1_scores), np.std(f1_scores)))

# Create a new figure with four subplots (1 row, 4 columns) sharing a y-axis
fig, axs = plt.subplots(1, 4, figsize=(15, 5), sharey=True)

# Create a bar plot on the first subplot showing the mean accuracy for each fold, with error bars representing standard deviation
axs[0].bar(range(1, 6), accuracy_scores, yerr=np.std(accuracy_scores))
axs[0].set_xlabel('Fold')
axs[0].set_ylabel('Score')
axs[0].set_title('Accuracy by Fold')
axs[0].set_ylim([0, 1])

# Repeat for precision, recall, and F1 score on the remaining subplots
axs[1].bar(range(1, 6), precision_scores, yerr=np.std(precision_scores))
axs[1].set_xlabel('Fold')
axs[1].set_title('Precision by Fold')
axs[1].set_ylim([0, 1])

axs[2].bar(range(1, 6), recall_scores, yerr=np.std(recall_scores))
axs[2].set_xlabel('Fold')
axs[2].set_title('Recall by Fold')
axs[2].set_ylim([0, 1])

axs[3].bar(range(1, 6), f1_scores, yerr=np.std(f1_scores))
axs[3].set_xlabel('Fold')
axs[3].set_title('F1 Score by Fold')
axs[3].set_ylim([0, 1])

# Display all plots
plt.show()
