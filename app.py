import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from utils.data_generator import generate_customer_data, generate_market_data
from utils.models import CustomerSegmentation, PriceOptimizer
from utils.metrics import calculate_clv, calculate_conversion_rate

# Configure page
st.set_page_config(
    page_title="PricePilot AI",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Main title    
st.title("PricePilot AI")
st.info(
"""
### Executive Summary

Revenue increased **12.6%** compared to last month.

AI has identified **3 pricing opportunities** capable of improving
profitability while maintaining customer conversion.

Latest pricing experiment generated an estimated **8.7% revenue lift**.
"""
)
st.markdown("### Dynamic Pricing Intelligence & Product Analytics Platform")

# Sidebar navigation
st.sidebar.title("Navigation")
st.sidebar.markdown("Use the pages in the sidebar to explore different aspects of the pricing optimization platform.")

# Executive KPI Dashboard
st.header("Executive Dashboard")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Revenue",
        "₹12.45M",
        "+12.6%"
    )

with col2:
    st.metric(
        "Profit",
        "₹4.82M",
        "+7.9%"
    )

with col3:
    st.metric(
        "Conversion Rate",
        "5.84%",
        "+0.9%"
    )

with col4:
    st.metric(
        "Average Selling Price",
        "₹1,048",
        "+₹34"
    )

# Generate sample data for overview
@st.cache_data
def load_overview_data():
    np.random.seed(42)
    customers = generate_customer_data(1000)
    market_data = generate_market_data()
    return customers, market_data

customers_df, market_df = load_overview_data()

# AI Pricing Recommendations

st.header("AI Pricing Recommendations")

left, right = st.columns([2,1])

with left:

    st.success("""
### Recommendation 1

**Increase Premium Product pricing by 4.5%**

Reason

• Demand has increased significantly

• Competitor prices remain higher

• Inventory is reducing rapidly

Expected Revenue Lift

**+9.4%**

Confidence

**95%**
""")

with right:

    st.warning("""
### Immediate Opportunities

📈 Premium Pricing

High Impact

----------------

🛍 Flash Sale

Medium Impact

----------------

📦 Inventory Alert

Restock within 4 days
""")
# Key Insights Section
st.header("Key Business Insights")
st.caption(
    "Interactive business intelligence to support pricing decisions and product strategy."
)

col1, col2 = st.columns(2)

with col1:
    st.subheader("Customer Distribution by Segment")
    
    # Simple segmentation for overview
    segmentation_model = CustomerSegmentation()
    numeric_features = ['income', 'credit_score', 'debt_to_income', 'age', 'savings_rate']
    segments = segmentation_model.fit_predict(customers_df[numeric_features])
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
        'Personal Loans': np.random.normal(15000, 3000, 100).clip(5000, 25000).mean(),
        'Credit Cards': np.random.normal(8000, 2000, 100).clip(2000, 15000).mean(),
        'Mortgages': np.random.normal(250000, 50000, 100).clip(150000, 400000).mean()
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
