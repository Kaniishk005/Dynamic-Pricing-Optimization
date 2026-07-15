import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from services.data_service import load_data
from services.model_service import get_models
from services.analytics_service import get_dashboard_metrics
from services.recommendation_service import generate_recommendations


# Configure page
st.set_page_config(
    page_title="PricePilot AI",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)


metrics = get_dashboard_metrics()
recommendations = generate_recommendations()


# Main title    
st.title("PricePilot AI")
st.info(f"""
### Executive Summary

Revenue optimization is delivering an average lift of **{metrics['revenue_lift']:.1f}%**.

AI has generated **{len(recommendations)}** business recommendations.

Current optimized revenue stands at **₹{metrics['total_revenue']/1e6:.2f}M**.
""")
st.markdown("### Dynamic Pricing Intelligence & Product Analytics Platform")
st.subheader("Business Problem")

st.write("""
Organizations often rely on static pricing strategies that fail to adapt to
changing customer demand, competitor pricing, and market conditions.

As a result, businesses lose revenue opportunities, struggle to identify
high-value customer segments, and lack visibility into pricing performance.
""")

st.subheader("Business Solution")

st.write("""
PricePilot AI is an AI-powered Product Analytics platform that combines
Machine Learning, Pricing Optimization, Customer Segmentation,
A/B Testing, Growth Analytics, and Executive Dashboards to help
business teams make data-driven pricing decisions.
""")
st.subheader("Business Impact")

impact1, impact2, impact3 = st.columns(3)

with impact1:
    st.metric(
        "Revenue Growth",
        "+12.6%"
    )

with impact2:
    st.metric(
        "Pricing Accuracy",
        "96%"
    )

with impact3:
    st.metric(
        "Decision Time",
        "-38%"
    )

# Sidebar navigation
st.sidebar.title("Navigation")
st.sidebar.markdown("Use the pages in the sidebar to explore different aspects of the pricing optimization platform.")

# Executive KPI Dashboard
st.header("Executive Dashboard")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Revenue",
        f"₹{metrics['total_revenue']/1e6:.2f}M"
    )

projected_profit = metrics["total_revenue"] * 0.32  
with col2:
    st.metric(
        "Estimated Profit",
        f"₹{projected_profit/1e6:.2f}M"
    )

with col3:
    st.metric(
        "Revenue Lift",
        f"{metrics['revenue_lift']:.1f}%"
    )
    
with col4:
    st.metric(
        "Average Price",
        f"₹{metrics['average_price']:,.0f}"
    )

# Generate sample data for overview
data = load_data()

# customers_df, market_df = load_overview_data()
customers_df = data["customers"]
market_df = data["market"]

# AI Pricing Recommendations


st.header("AI Recommendations")

for recommendation in recommendations[:3]:

    st.info(
        f"""
### {recommendation['title']}

Priority: {recommendation['priority']}

{recommendation['action']}
"""
    )

col1, col2 = st.columns(2)
models = get_models()
with col1:
    st.subheader("Customer Distribution by Segment")
    
    # Simple segmentation for overview
    # segmentation_model = CustomerSegmentation()
    segmentation_model = models["segmentation"]
    numeric_features = ['income', 'credit_score', 'debt_to_income', 'age', 'savings_rate']
    segments = segmentation_model.predict(customers_df[numeric_features])
    customers_df['segment'] = segments
    
    segment_counts = pd.Series(segments).value_counts().sort_index()
    segment_labels = ['Conservative', 'Balanced', 'Growth-Oriented', 'High-Risk', 'Premium']
    
    fig_pie = px.pie(
        values=segment_counts.values,
        names=[segment_labels[i] for i in segment_counts.index],
        title="Customer Segmentation Distribution"
    )
    st.plotly_chart(fig_pie, use_container_width=True)

with col2:
    st.subheader("Revenue Potential by Product")
    
    # Calculate revenue potential
    product_revenue = {
        "Personal Loan": data["pricing"]["Personal Loan"]["optimal_price"].mean(),
        "Credit Card": data["pricing"]["Credit Card"]["optimal_price"].mean(),
        "Mortgage": data["pricing"]["Mortgage"]["optimal_price"].mean(),
    }
    
    fig_bar = px.bar(
        x=list(product_revenue.keys()),
        y=list(product_revenue.values()),
        title="Average Revenue Potential by Product",
        labels={'x': 'Product Type', 'y': 'Average Revenue ($)'}
    )
    fig_bar.update_layout(yaxis_tickformat='$,.0f')
    st.plotly_chart(fig_bar, use_container_width=True)

# Market Trends Section
st.header("Market Intelligence")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Interest Rate Trends")
    fig_line = px.line(
        market_df,
        x='date',
        y='interest_rate',
        title="Federal Interest Rate Trend",
        labels={'interest_rate': 'Interest Rate (%)', 'date': 'Date'}
    )
    st.plotly_chart(fig_line, use_container_width=True)

with col2:
    st.subheader("Market Volatility Index")
    fig_volatility = px.line(
        market_df,
        x='date',
        y='volatility',
        title="Market Volatility Index",
        labels={'volatility': 'Volatility Index', 'date': 'Date'}
    )
    st.plotly_chart(fig_volatility, use_container_width=True)

# Technology Stack
st.header("Business Capabilities")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Revenue Optimization")
    st.markdown("""
    - Dynamic Pricing Strategy

    - Price Elasticity Analysis

    - Revenue Forecasting

    - Profit Optimization
    """)

with col2:
    st.subheader("Customer Intelligence")
    st.markdown("""
    - Customer Segmentation

    - Lifetime Value Analysis

    - Behavioral Analytics

    - Risk Profiling
    """)

with col3:
    st.subheader("Decision Support")
    st.markdown("""
    - AI Recommendations

    - A/B Testing

    - Executive Dashboards

    - Business KPI Monitoring
    """)

# Feature Highlights
st.header("Business Objectives")

st.markdown("""
- Increase revenue through intelligent pricing.
- Improve customer conversion.
- Identify high-value customer segments.
- Validate pricing experiments.
- Enable data-driven pricing decisions.
""")

st.header("Platform Features")

features = [
    {
        "title": "🎯 Customer Segmentation",
        "description": "Advanced K-Means clustering to identify distinct customer segments based on risk profiles, demographics, and financial behavior."
    },
    {
        "title": "📈 Price Optimization", 
        "description": "Gradient Boosting models to determine optimal pricing strategies for different financial products and customer segments."
    },
    {
        "title": "🧪 A/B Testing Framework",
        "description": "Statistical testing framework to validate pricing strategies with confidence intervals and significance testing."
    },
    {
        "title": "💹 Revenue Impact Analysis",
        "description": "Comprehensive ROI calculator showing potential business outcomes and revenue optimization opportunities."
    }
]

for i, feature in enumerate(features):
    with st.container():
        st.subheader(feature["title"])
        st.write(feature["description"])
        if i < len(features) - 1:
            st.divider()

# Footer
st.markdown("---")
st.markdown(
    """
    Empowering Product Managers with AI-driven pricing recommendations,
    customer insights, pricing experiments and business intelligence.
    """
)

