from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

# Load the trained model
model = pickle.load(open('GradientBoostingRegressor', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        present_price = float(request.form['present_price'])
        kms_driven = int(request.form['kms_driven'])
        owner = int(request.form['owner'])
        year = int(request.form['year'])

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
        return render_template('result.html', prediction=predicted_price[0])

if __name__ == '__main__':
    app.run(debug=True)
