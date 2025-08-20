import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

df = pd.read_csv('data/WA_Fn-UseC_-Telco-Customer-Churn.csv')

# Preprocessing
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df.dropna(inplace=True)
df.drop(['customerID'], axis=1, inplace=True)

# Encode categorical variables
categorical_cols = df.select_dtypes(include=['object']).columns
le = LabelEncoder()

for col in categorical_cols:
    df[col] = le.fit_transform(df[col])


x = df.drop(['Churn'], axis=1)
y = df['Churn']


# Split the dataset into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestClassifier(n_estimators=100)
model.fit(x_train, y_train)

# save the model
joblib.dump(model, 'churn_model.pkl')

predictions = model.predict(x_test)
acc = accuracy_score(y_test, predictions)
print(f'Model Accuracy: {acc:.2f}')


