import streamlit as st
import pandas as pd
import plotly.express as px

from services.data_service import load_data

st.set_page_config(
    page_title="Executive Analytics",
    layout="wide"
)

st.title("Executive Analytics Dashboard")
st.caption(
    "Enterprise pricing intelligence for product and business leaders."
)

data = load_data()

customers = data["customers"]
market = data["market"]
revenue = data["revenue"]
product_revenue = {
    "Personal Loan":
        data["pricing"]["Personal Loan"]["optimal_price"].sum(),

    "Credit Card":
        data["pricing"]["Credit Card"]["optimal_price"].sum(),

    "Mortgage":
        data["pricing"]["Mortgage"]["optimal_price"].sum(),
}

product_df = pd.DataFrame({
    "Product": product_revenue.keys(),
    "Revenue": product_revenue.values()
})

avg_revenue_lift = revenue["revenue_lift_pct"].mean()
avg_credit = customers["credit_score"].mean()

REVENUE_WEIGHT = 0.5
CREDIT_WEIGHT = 0.5
health_score = (
    REVENUE_WEIGHT * min(avg_revenue_lift, 30)
    + CREDIT_WEIGHT * (avg_credit / 850) * 100
)

health_score = round(min(health_score, 100), 1)

left, right = st.columns([1,3])

with left:

    st.metric(
        "Business Health",
        f"{health_score}/100"
    )

    if health_score >= 85:
        st.success("Excellent")

    elif health_score >= 70:
        st.warning("Stable")

    else:
        st.error("Needs Attention")

total_revenue = revenue["optimized_revenue"].sum()

avg_revenue = revenue["optimized_revenue"].mean()

avg_lift = revenue["revenue_lift_pct"].mean()

k1, k2, k3, k4 = st.columns(4)

with k1:
    st.metric(
        "Total Revenue",
        f"₹{total_revenue/1e6:.2f}M"
    )

with k2:
    st.metric(
        "Average Revenue",
        f"₹{avg_revenue:,.0f}"
    )

with k3:
    st.metric(
        "Revenue Lift",
        f"{avg_lift:.1f}%"
    )

with k4:
    st.metric(
        "Avg Credit Score",
        f"{avg_credit:.0f}"
    )

opportunity = revenue["revenue_lift"].sum()

st.info(
f"""
### Revenue Opportunity

Estimated additional annual revenue

## ₹{opportunity:,.0f}

through optimized pricing.
"""
)

segment_summary = (
    customers
    .groupby("risk_category")
    .agg(
        customers=("customer_id","count"),
        income=("income","mean")
    )
    .reset_index()
)
    
st.subheader("Executive Insights")

insights = []

top_product = max(product_revenue, key=product_revenue.get)

top_risk = (
    customers["risk_category"]
    .value_counts()
    .idxmax()
)

avg_income = customers["income"].mean()


fig = px.bar(
    segment_summary,
    x="risk_category",
    y="income",
    color="customers",
    title="Customer Segment Value"
)
st.subheader("Business Performance Overview")

top_left, top_right = st.columns(2)

with top_left:
    st.plotly_chart(fig, use_container_width=True)


bottom_left, bottom_right = st.columns(2)



fig2 = px.pie(
    product_df,
    values="Revenue",
    names="Product",
    title="Revenue Contribution by Product"
)
with top_right:
    st.plotly_chart(fig2, use_container_width=True)

risk = (
    customers["risk_category"]
    .value_counts()
    .reset_index()
)

risk.columns = [
    "Risk",
    "Customers"
]

fig3 = px.bar(
    risk,
    x="Risk",
    y="Customers",
    color="Customers",
    title="Risk Profile Distribution"
)

with bottom_left:
    st.plotly_chart(fig3, use_container_width=True)

market_fig = px.line(
    market,
    x="date",
    y="interest_rate",
    title="Interest Rate Trend"
)

with bottom_right:
    st.plotly_chart(
        market_fig,
        use_container_width=True
    )

insights = [
    f"**{top_product}** contributes the highest optimized revenue.",
    f"The largest customer group belongs to the **{top_risk}** risk segment.",
    f"Average customer income is **₹{avg_income:,.0f}**, supporting premium pricing opportunities.",
    f"Pricing optimization currently delivers an average revenue lift of **{avg_lift:.1f}%**."
]

st.subheader("AI Executive Insights")

for insight in insights:
    st.success(insight)
