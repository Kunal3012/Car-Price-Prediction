import pickle
import pandas as pd
# Load the trained model
model = pickle.load(open('GradientBoostingRegressor', 'rb'))

# Get user input for car details
present_price = float(input("Enter the present price of the car: "))
kms_driven = int(input("Enter the total kilometers driven: "))
owner = int(input("Enter the number of previous owners: "))
year = int(input("Enter the manufacturing year of the car: "))

# Calculate car age
current_year = 2023
car_age = current_year - year

# Create a DataFrame from user inputs
input_data = {
    'Present_Price': [present_price],
    'Kms_Driven': [kms_driven],
    'Owner': [owner],
    'Car_age': [car_age]
}
input_df = pd.DataFrame(input_data)

# Make predictions using the model
predicted_price = model.predict(input_df)

# Display the predicted selling price
print(f"The predicted selling price of the car is: {predicted_price[0]}")
