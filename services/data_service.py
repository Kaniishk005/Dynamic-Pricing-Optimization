import streamlit as st

from utils.data_generator import (
    generate_customer_data,
    generate_market_data,
    generate_pricing_data,
    generate_revenue_data
)


@st.cache_data(show_spinner=False)
def load_data():

    # Generate master datasets
    customers = generate_customer_data(2000)
    market = generate_market_data()

    pricing = {
        "Personal Loan": generate_pricing_data(customers, "Personal Loan"),
        "Credit Card": generate_pricing_data(customers, "Credit Card"),
        "Mortgage": generate_pricing_data(customers, "Mortgage"),
    }

    revenue = generate_revenue_data(customers)

    return {
        "customers": customers,
        "market": market,
        "pricing": pricing,
        "revenue": revenue,
    }