# 🏠 House Price Prediction

A Machine Learning project that predicts California house prices using Linear Regression and provides an interactive web interface built with Streamlit.

## 🌐 Live Demo

https://house-price-predection.streamlit.app/

## 📌 Project Overview

This project uses the California Housing Dataset to predict house prices based on features such as:

- Longitude
- Latitude
- Housing Median Age
- Total Rooms
- Total Bedrooms
- Population
- Households
- Median Income
- Ocean Proximity

The trained model is saved using Pickle and deployed as a Streamlit web application.

---

## 🚀 Features

- Interactive Streamlit User Interface
- Real-time House Price Prediction
- Linear Regression Model
- One-Hot Encoding for Categorical Features
- Model Deployment using Pickle
- Clean and User-Friendly Design

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-Learn
- Streamlit
- Pickle

---

## 📂 Project Structure

```text
house_price_prediction_project/
│
├── app.py
├── House_price.pkl
├── requirements.txt
├── README.md
├── .gitignore
│
├── DataSet/
│   └── housing.csv
│
└── NoteBook/
    └── House_price_prediction.ipynb
```

---

## 📊 Dataset

Dataset: California Housing Dataset

Features:

- longitude
- latitude
- housing_median_age
- total_rooms
- total_bedrooms
- population
- households
- median_income
- ocean_proximity

Target Variable:

- median_house_value

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/tejasbabar06/house_price_prediction_project.git
```

Move to the project directory:

```bash
cd house_price_prediction_project
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

---

## 📈 Model Performance

| Metric | Value |
|----------|----------|
| R² Score | ~0.64 |
| MAE | ~50076 |
| RMSE | ~68796 |

---

## 🔮 Future Improvements

- Random Forest Regressor
- XGBoost Regressor
- Hyperparameter Tuning
- Advanced Feature Engineering
- Model Comparison Dashboard
- Deployment with Docker

---

## 👨‍💻 Author

**Tejas Babar**

B.Tech Computer Science & Engineering (AIML)

GitHub: https://github.com/tejasbabar06

---

⭐ If you found this project useful, consider giving it a star.
