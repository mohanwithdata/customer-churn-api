import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib


df = pd.read_csv('customer_churn_api/data/WA_Fn-UseC_-Telco-Customer-Churn.csv')
df.head(3)