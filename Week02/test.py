from sklearn.metrics import classification_report, confusion_matrix
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
import seaborn as sns
import pandas

url = "Admission_Prediction_Challenge.csv"
print("Downloading data from", url)
data = pandas.read_csv(url)

################# CLEANING DATA #################

cleaned_data = data.drop_duplicates()
#,GRE Score,TOEFL Score,University Rating,SOP,LOR ,CGPA,Research,Chance of Admit 
cleaned_data = cleaned_data.dropna()


################# SPLIT DATA #################

cleaned_data.columns = cleaned_data.columns.str.strip()

X = cleaned_data[['GRE Score','TOEFL Score','University Rating','SOP','LOR','CGPA','Research' ]]
y = (cleaned_data['Chance of Admit'] > 0.75).astype(int)

X_train, X_test, y_train, y_test  = train_test_split(X, y, test_size=0.2, random_state=42)

################### TRAIN MODEL #################

model = LogisticRegression(max_iter=1000)

model.fit(X_train, y_train)


################### EVALUATE MODEL #################

importance = pandas.DataFrame({'Feature': X.columns, 'Weight': model.coef_[0]})
print(importance.sort_values(by='Weight', ascending=False))

from sklearn.preprocessing import StandardScaler

# ... (after your train_test_split) ...

# 1. Initialize the Scaler
scaler = StandardScaler()

# 2. Scale the features
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 3. Train on SCALED data with more iterations
model = LogisticRegression(max_iter=1000)
model.fit(X_train_scaled, y_train)

# 4. Check the results again
importance = pandas.DataFrame({'Feature': X.columns, 'Weight': model.coef_[0]})
print(importance.sort_values(by='Weight', ascending=False))

# Make predictions on the test set
predictions = model.predict(X_test_scaled)


# This shows how many were correctly 'Admitted' vs 'Not Admitted'
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, predictions))

# This shows Precision, Recall, and F1-score for both classes
# Add 'target_names' to make it readable for humans
print("\nClassification Report:")
print(classification_report(y_test, predictions, target_names=['Not Admitted', 'Admitted']))

################# HOLOGRAMS #################

features_to_plot = ['GRE Score', 'TOEFL Score', 'CGPA']
cleaned_data[features_to_plot].hist(bins=20, figsize=(10, 8), color='skyblue', edgecolor='black')
plt.suptitle("Distribution of Academic Scores")
plt.show()

