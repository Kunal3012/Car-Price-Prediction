import pickle
import pandas as pd

# Load the trained model
model = pickle.load(open('GradientBoostingRegressor', 'rb'))

# Read the new data
df = pd.read_csv('car_prediction_data.csv')

df['Car_age'] = 2023 - df['Year']
X = df[['Present_Price', 'Kms_Driven', 'Owner', 'Car_age']]

predictions = model.predict(X)

print(predictions)
