import streamlit as st
import pandas as pd
from services.data_service import load_data
from utils.models import (
    CustomerSegmentation,
    PriceOptimizer,
)

@st.cache_resource(show_spinner=False)
def get_models():

    data = load_data()

    customers = data["customers"]
    pricing = data["pricing"]["Personal Loan"]

    # Customer Segmentation
    
    segmentation_model = CustomerSegmentation()

    segmentation_features = [
        "income",
        "credit_score",
        "debt_to_income",
        "age",
        "savings_rate",
    ]

    segmentation_model.fit_predict(
        customers[segmentation_features]
    )

    # Price Optimizer

    optimizer = PriceOptimizer()

    training_data = customers.copy()

    training_data["current_price"] = pricing["current_price"]
    training_data["conversion_rate"] = pricing["conversion_rate"]

    feature_columns = [
        "income",
        "credit_score",
        "debt_to_income",
        "age",
        "savings_rate",
    ]

    optimizer.fit(
        training_data[feature_columns],
        pricing["optimal_price"],
        pricing["conversion_rate"],
    )

    return {
        "segmentation": segmentation_model,
        "price_optimizer": optimizer,
        "feature_columns":feature_columns,
    }