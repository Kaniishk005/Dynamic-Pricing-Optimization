from services.analytics_service import get_dashboard_metrics


def generate_recommendations():

    metrics = get_dashboard_metrics()

    recommendations = []

    revenue_lift = metrics["revenue_lift"]
    average_price = metrics["average_price"]
    total_revenue = metrics["total_revenue"]

    # Revenue Recommendation
    if revenue_lift >= 20:

        recommendations.append({

            "title": "Pricing Opportunity",

            "priority": "High",

            "confidence": 96,

            "business_impact": "High",

            "estimated_revenue_gain":
                int(total_revenue * 0.08),

            "owner":
                "Pricing Team",

            "action":
                "Increase premium product pricing.",

            "reason":
                "Revenue lift indicates low price sensitivity."
        })

    elif revenue_lift >= 10:

        recommendations.append({

            "title":"Average Selling Price",

            "priority":"Medium",

            "confidence":88,

            "business_impact":"Medium",

            "estimated_revenue_gain":
                int(total_revenue*0.03),

            "owner":
                "Pricing Team",

            "action":
                "Evaluate premium pricing strategy.",

            "reason":
                "Average selling price remains relatively low."
        })
    else:

        recommendations.append({
            "title": "Pricing Opportunity",
            "priority": "Low",
            "action": "Maintain current pricing.",
            "reason": "Current pricing appears balanced."
        })

    # Revenue Recommendation
    if total_revenue > 5_000_000:

        recommendations.append({

    "title":"Business Growth",

    "priority":"High",

    "confidence":91,

    "business_impact":"High",

    "estimated_revenue_gain":
        int(total_revenue*0.05),

    "owner":
        "Marketing",

    "action":
        "Expand marketing investment.",

    "reason":
        "Revenue performance supports scaling."
})

    # Pricing Recommendation
    if average_price < 2000:

        recommendations.append({
            "title": "Average Selling Price",
            "priority": "Medium",
            "action": "Evaluate premium pricing strategy.",
            "reason": "Average selling price remains relatively low."
        })

    return recommendations