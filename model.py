import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor

data = pd.read_csv("crops.csv")

le = LabelEncoder()
data["crop_encoded"] = le.fit_transform(data["crop"])

X = data[["crop_encoded"]]
y = data["price"]

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

pickle.dump((model, le), open("model.pkl", "wb"))

print("Model created successfully")