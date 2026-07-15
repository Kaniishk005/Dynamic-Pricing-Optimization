import streamlit as st
from services.pricing_service import simulate_pricing

st.set_page_config(
    page_title="Scenario Simulator",
    layout="wide"
)

st.title("Scenario Simulator")
st.caption("Evaluate pricing strategies under different business conditions.")


left, right = st.columns([1,2])

with left:

    st.subheader("Business Inputs")

    competitor_price = st.slider(
        "Competitor Price",
        500,
        2000,
        1000
    )

    demand = st.slider(
        "Customer Demand",
        0,
        100,
        70
    )

    inventory = st.slider(
        "Inventory Level",
        0,
        100,
        60
    )

    marketing = st.slider(
        "Marketing Spend",
        0,
        100,
        40
    )

    season = st.selectbox(
        "Season",
        [
            "Normal",
            "Festival",
            "Holiday",
            "Year End"
        ]
    )

result = simulate_pricing(
    competitor_price,
    demand,
    inventory,
    marketing,
    season,
)

recommended_price = result["recommended_price"]
ml_price = result["ml_price"]
expected_revenue = result["expected_revenue"]
expected_profit = result["expected_profit"]
conversion = result["conversion"]

current_price = competitor_price
current_revenue = current_price * demand * 120
current_profit = current_revenue * 0.35
revenue_change = (
    (expected_revenue - current_revenue) / current_revenue
) * 100

profit_change = (
    (expected_profit - current_profit) / current_profit
) * 100

st.divider()

st.subheader("Business Impact")

compare1, compare2 = st.columns(2)

with compare1:
    st.metric(
        "Revenue Lift",
        f"{revenue_change:.1f}%",
        delta=f"{revenue_change:.1f}%"
    )

with compare2:
    st.metric(
        "Profit Improvement",
        f"{profit_change:.1f}%",
        delta=f"{profit_change:.1f}%"
    )

st.divider()

st.subheader("Risk Assessment")

if inventory < 20:

    st.error("High Risk • Inventory shortage may reduce sales.")

elif demand < 30:

    st.warning("Medium Risk • Low demand could impact revenue.")

else:

    st.success("Low Risk • Business indicators look healthy.")

with right:

    st.subheader("Simulation Results")

    c1, c2 = st.columns(2)

    with c1:
        st.metric(
            "Recommended Price",
            f"₹{recommended_price:,.0f}"
        )
        st.metric(
            "ML Suggested Price",
            f"₹{ml_price:,.0f}"
        )
        st.metric(
            "Expected Revenue",
            f"₹{expected_revenue:,.0f}"
        )

    with c2:
        st.metric(
            "Expected Profit",
            f"₹{expected_profit:,.0f}"
        )

        st.metric(
            "Conversion Rate",
            f"{conversion:.2f}%"
        )

recommendation = []

if demand > 80:
    recommendation.append(
        "Demand is strong. A moderate price increase is recommended."
    )

if inventory < 30:
    recommendation.append(
        "Inventory is low. Avoid aggressive discounts."
    )

if competitor_price > recommended_price:
    recommendation.append(
        "Competitors are priced higher, leaving room to increase price."
    )

if season == "Festival":
    recommendation.append(
        "Seasonal demand supports premium pricing."
    )

if not recommendation:
    recommendation.append(
        "Current pricing strategy appears balanced."
    )

st.divider()

st.subheader("Executive Decision")

if revenue_change > 10:
    st.success(
        """
### Recommended Action

Increase product pricing.

Reason

- Strong customer demand
- Revenue expected to increase significantly
- Profitability remains healthy

Priority

High
"""
    )

elif revenue_change > 5:

    st.warning(
        """
### Recommended Action

Run a controlled pricing experiment.

Priority

Medium
"""
    )

else:

    st.info(
        """
### Recommended Action

Maintain current pricing strategy.

Priority

Low
"""
    )

st.divider()

st.subheader("Simulation Summary")

st.write(f"""
Changing the competitor price to **₹{competitor_price}**
with demand at **{demand}%**
results in an AI recommended price of **₹{recommended_price:.0f}**.

Expected revenue becomes **₹{expected_revenue:,.0f}**
while projected profit reaches **₹{expected_profit:,.0f}**.

Overall revenue is projected to improve by **{revenue_change:.1f}%**.
""")