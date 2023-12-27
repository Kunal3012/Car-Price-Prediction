# Car Price Prediction Project
![Dataset Cover](images/dataset-cover.jpg)

## About the Dataset

The Car Price Prediction Dataset is a valuable resource for machine learning analysis within the automotive, finance, and marketing domains. It includes crucial information such as car details, S price, present price, kilometers driven, fuel type, seller type, transmission, and owner count.
## Key Features

- **Car_Name:** Brand or company name with the specific model of each vehicle.
- **Year:** Manufacturing year, essential for assessing depreciation and technology advancements.
- **Selling_Price:** Current selling price of the car.
- **Present_Price:** Original price of the car.
- **Kms_Driven:** Mileage, indicating wear and tear and potential maintenance requirements.
- **Fuel_Type:** Petrol or diesel.
- **Seller_Type:** Dealer or individual.
- **Transmission:** Automatic, manual, or other.
- **Owner:** Number of previous owners.
![Dataset Cover](images\PBI_Analysis.jpg)

    ```bash
   To view analytics report  vist at:  https://app.powerbi.com/groups/me/reports/8e1acaf1-3209-495d-89b7-a2d7082e6ad2/ReportSection?experience=power-bi
    ```

## Car Price Prediction Web App

This project comprises a Flask web application that predicts the selling price of a car based on user-inputted details. It employs a pre-trained Gradient Boosting Regressor model to make accurate predictions.

### Features

- Input car details: Present Price, Kilometers Driven, Number of Owners, Manufacturing Year.
- Predict the selling price based on the entered information.
- Display the predicted selling price.

### Technologies Used

- Python
- Flask
- Pandas
- Scikit-learn

## Installation and Usage

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/car-price-prediction.git
    ```

2. **Install necessary libraries:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Flask app:**

    ```bash
    python app.py
    ```

4. **Access the application:**

    Navigate to `http://127.0.0.1:5000/` in your web browser.

5. **Use the app:**

    Fill in the car details and click "Predict" to see the selling price prediction.

## Folder Structure

- `app.py`: Main Flask application file.
- `templates/`: HTML templates (index.html and result.html).
- `images/`: Image directory.
- `GradientBoostingRegressor`: Pre-trained model file.

```
Car-Price-Prediction/
│
├── README.md
│
├── images/
│   ├── dataset-cover.jpg
│   └── PBI_Analysis.jpg
│
├── app.py
├── templates/
│   ├── index.html
│   └── result.html
│
└── GradientBoostingRegressor  # Model file
├── templates/
│   ├── index.html
│   └── result.html
│
└── GradientBoostingRegressor  # Model file
```
## Contributing

Contributions, bug reports, or feature requests are welcome! Feel free to open issues or pull requests.

## License

This project is licensed under the [MIT License](LICENSE).
