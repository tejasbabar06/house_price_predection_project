import streamlit as st
import pandas as pd
import pickle

# Page Config
st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="wide"
)

# Load Model
with open("House_price.pkl", "rb") as file:
    model = pickle.load(file)

# Title
st.title("🏠 California House Price Prediction")
st.write(
    "Predict California house prices using a Machine Learning Linear Regression model."
)

st.markdown("---")

# Input Section
col1, col2 = st.columns(2)

with col1:
    longitude = st.number_input(
        "Longitude",
        value=-122.23
    )

    latitude = st.number_input(
        "Latitude",
        value=37.88
    )

    housing_median_age = st.number_input(
        "Housing Median Age",
        value=41.0
    )

    total_rooms = st.number_input(
        "Total Rooms",
        value=880.0
    )

with col2:
    total_bedrooms = st.number_input(
        "Total Bedrooms",
        value=129.0
    )

    population = st.number_input(
        "Population",
        value=322.0
    )

    households = st.number_input(
        "Households",
        value=126.0
    )

    median_income = st.number_input(
        "Median Income",
        value=8.3252
    )

# Ocean Proximity
ocean = st.selectbox(
    "Ocean Proximity",
    ["<1H OCEAN", "INLAND", "ISLAND", "NEAR BAY", "NEAR OCEAN"],
    index=3
)

# One Hot Encoding
ocean_inland = 1 if ocean == "INLAND" else 0
ocean_island = 1 if ocean == "ISLAND" else 0
ocean_near_bay = 1 if ocean == "NEAR BAY" else 0
ocean_near_ocean = 1 if ocean == "NEAR OCEAN" else 0

st.markdown("")

# Predict Button
if st.button("Predict Price"):

    data = pd.DataFrame(
        [[
            longitude,
            latitude,
            housing_median_age,
            total_rooms,
            total_bedrooms,
            population,
            households,
            median_income,
            ocean_inland,
            ocean_island,
            ocean_near_bay,
            ocean_near_ocean
        ]],
        columns=[
            'longitude',
            'latitude',
            'housing_median_age',
            'total_rooms',
            'total_bedrooms',
            'population',
            'households',
            'median_income',
            'ocean_proximity_INLAND',
            'ocean_proximity_ISLAND',
            'ocean_proximity_NEAR BAY',
            'ocean_proximity_NEAR OCEAN'
        ]
    )

    prediction = model.predict(data)[0]

    st.success(
        f"🏡 Predicted House Price: ${prediction:,.2f}"
    )

    st.info(
        f"Approximate Price in INR: ₹{prediction * 86:,.0f}"
    )

    # House Category
    if prediction < 150000:
        st.warning("🏠 Budget House")

    elif prediction < 400000:
        st.info("🏡 Mid-Range House")

    else:
        st.success("🏘️ Premium House")

    # Input Summary
    st.subheader("Input Summary")

    st.dataframe(data)

# Sidebar
st.sidebar.header("📊 Model Information")

st.sidebar.metric("Algorithm", "Linear Regression")
st.sidebar.metric("R² Score", "0.64")
st.sidebar.metric("MAE", "50,076")

# Footer
st.markdown("---")
st.write("Created by Tejas Babar | AIML Student")