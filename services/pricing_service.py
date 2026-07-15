import pandas as pd

from services.model_service import get_models


def simulate_pricing(
    competitor_price,
    demand,
    inventory,
    marketing,
    season,
):

    models = get_models()

    optimizer = models["price_optimizer"]
    feature_columns = models["feature_columns"]

    sample_customer = {
        "income": 90000,
        "credit_score": 740,
        "debt_to_income": 0.28,
        "age": 34,
        "savings_rate": 0.18,
    }

    X = pd.DataFrame([sample_customer])[feature_columns]

    predicted_price = optimizer.predict_price(X)[0]
    optimized_price = optimizer.optimize_price(X)[0]

    optimized_price = max(500, min(2000, optimized_price))
    predicted_price = max(500, min(2000, predicted_price))

    recommended_price = optimized_price

    if demand > 80:
        recommended_price *= 1.05

    if inventory < 30:
        recommended_price *= 1.03

    if marketing > 70:
        recommended_price *= 1.02

    if season == "Festival":
        recommended_price *= 1.04

    elif season == "Holiday":
        recommended_price *= 1.03

    expected_revenue = recommended_price * demand * 120
    expected_profit = expected_revenue * 0.38
    conversion = optimizer.predict_conversion(X)[0]

    return {
        "ml_price": predicted_price,
        "optimized_price": optimized_price,
        "recommended_price": recommended_price,
        "expected_revenue": expected_revenue,
        "expected_profit": expected_profit,
        "conversion": conversion,
    }