import streamlit as st
import pandas as pd
import plotly.express as px

from services.data_service import load_data
from services.analytics_service import get_dashboard_metrics

st.set_page_config(
    page_title="Product Growth Analytics",
    layout="wide"
)

st.title("Product Funnel & Growth Analytics")

st.caption(
    "Analyze customer journeys, conversion funnels, retention, and product growth metrics."
)

data = load_data()
metrics = get_dashboard_metrics()

st.header("Executive KPIs")

k1, k2, k3, k4 = st.columns(4)

with k1:
    st.metric(
        "Visitors",
        "120,540",
        "+8.2%"
    )

with k2:
    st.metric(
        "Signups",
        "18,640",
        "+6.4%"
    )

with k3:
    st.metric(
        "Conversion",
        "15.5%",
        "+1.3%"
    )

with k4:
    st.metric(
        "30-Day Retention",
        "68%",
        "+4.1%"
    )

funnel = pd.DataFrame({

    "Stage":[
        "Visitors",
        "Product View",
        "Started Application",
        "Approved",
        "Purchased",
        "Retained"
    ],

    "Users":[
        120000,
        82000,
        36000,
        24000,
        18000,
        12200
    ]
})

fig = px.funnel(
    funnel,
    x="Users",
    y="Stage",
    title="Customer Journey Funnel"
)

st.plotly_chart(
    fig,
    use_container_width=True
)
st.divider()

st.header("Growth Metrics")
growth = pd.DataFrame({

    "Metric":[
        "Revenue",
        "Customers",
        "Conversion",
        "Retention"
    ],

    "Current":[
        12.4,
        18.6,
        15.5,
        68
    ],

    "Previous":[
        10.9,
        17.1,
        14.2,
        64
    ]
})

growth["Growth"] = (
    (growth["Current"]-growth["Previous"])
    /growth["Previous"]*100
)
fig = px.bar(
    growth,
    x="Metric",
    y="Growth",
    color="Growth",
    title="Month-over-Month Growth"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

st.header("Feature Impact Analysis")
impact = pd.DataFrame({

    "Feature":[
        "Dynamic Pricing",
        "Customer Segmentation",
        "Recommendation Engine",
        "A/B Testing"
    ],

    "Revenue Lift":[
        12.6,
        8.3,
        5.7,
        4.1
    ]
})
fig = px.bar(
    impact,
    x="Feature",
    y="Revenue Lift",
    color="Revenue Lift",
    title="Business Impact of Product Features"
)

st.plotly_chart(
    fig,
    use_container_width=True
)
st.divider()

st.header("AI Product Insights")
st.success("""
Customer retention has increased steadily over the last three months,
indicating improved engagement after pricing optimization.
""")

st.success("""
The largest drop in the funnel occurs between Product View and
Started Application, suggesting an onboarding optimization opportunity.
""")

st.success("""
Revenue growth is primarily driven by the Dynamic Pricing Engine,
which currently contributes the highest business impact.
""")

st.success("""
A/B testing indicates that premium pricing improves profitability
without significantly affecting conversion rates.
""")