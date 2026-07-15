import streamlit as st
import pandas as pd

from services.data_service import load_data
from services.recommendation_service import generate_recommendations

st.set_page_config(
    page_title="Decision Intelligence",
    layout="wide"
)

st.title("Decision Intelligence Center")

st.caption(
    "AI-driven business recommendations for pricing and product teams."
)

# -----------------------------
# Load Data
# -----------------------------

data = load_data()
recommendations = generate_recommendations()

customers = data["customers"]
pricing = data["pricing"]
revenue = data["revenue"]

# -----------------------------
# Business Priority
# -----------------------------

high_priority = sum(
    1 for r in recommendations
    if r["priority"] == "High"
)

medium_priority = sum(
    1 for r in recommendations
    if r["priority"] == "Medium"
)

low_priority = sum(
    1 for r in recommendations
    if r["priority"] == "Low"
)

if high_priority > 0:
    st.error("Business Priority : HIGH")

elif medium_priority > 0:
    st.warning("Business Priority : MEDIUM")

else:
    st.success("Business Priority : LOW")

# -----------------------------
# Recommendation Summary
# -----------------------------

st.subheader("Recommendation Summary")

c1, c2, c3 = st.columns(3)

with c1:
    st.metric("High Priority", high_priority)

with c2:
    st.metric("Medium Priority", medium_priority)

with c3:
    st.metric("Low Priority", low_priority)

# -----------------------------
# Estimated Business Value
# -----------------------------

total_gain = sum(
    r["estimated_revenue_gain"]
    for r in recommendations
)

st.info(
f"""
### Estimated Business Value

If all recommendations are implemented successfully,

Estimated Revenue Impact

## ₹{total_gain:,.0f}
"""
)

# -----------------------------
# Opportunity Ranking
# -----------------------------

ranking = pd.DataFrame({
    "Recommendation": [
        r["title"] for r in recommendations
    ],
    "Priority": [
        r["priority"] for r in recommendations
    ],
    "Business Impact": [
        r["business_impact"] for r in recommendations
    ],
    "Owner": [
        r["owner"] for r in recommendations
    ],
    "Estimated Revenue Gain": [
        f"₹{r['estimated_revenue_gain']:,.0f}"
        for r in recommendations
    ]
})

st.subheader("Opportunity Ranking")

st.dataframe(
    ranking,
    use_container_width=True,
    hide_index=True
)

# -----------------------------
# AI Decision Recommendations
# -----------------------------

st.subheader("AI Decision Recommendations")

for recommendation in recommendations:

    message = f"""
### {recommendation['title']}

**Priority**

{recommendation['priority']}

**Confidence**

{recommendation['confidence']}%

**Business Impact**

{recommendation['business_impact']}

**Recommended Owner**

{recommendation['owner']}

**Estimated Revenue Gain**

₹{recommendation['estimated_revenue_gain']:,.0f}

**Recommended Action**

{recommendation['action']}

**Reason**

{recommendation['reason']}
"""

    if recommendation["priority"] == "High":
        st.error(message)

    elif recommendation["priority"] == "Medium":
        st.warning(message)

    else:
        st.info(message)