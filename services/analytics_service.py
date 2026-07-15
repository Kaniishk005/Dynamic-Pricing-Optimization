from services.data_service import load_data


def get_dashboard_metrics():

    data = load_data()

    customers = data["customers"]
    revenue = data["revenue"]
    pricing = data["pricing"]

    total_revenue = revenue["optimized_revenue"].sum()

    avg_revenue = revenue["optimized_revenue"].mean()

    avg_revenue_lift = revenue["revenue_lift_pct"].mean()

    avg_credit = customers["credit_score"].mean()

    total_customers = len(customers)

    avg_price = (
        pricing["Personal Loan"]["optimal_price"].mean()
        + pricing["Credit Card"]["optimal_price"].mean()
        + pricing["Mortgage"]["optimal_price"].mean()
    ) / 3

    return {

        "total_revenue": total_revenue,

        "average_revenue": avg_revenue,

        "revenue_lift": avg_revenue_lift,

        "average_credit": avg_credit,

        "customers": total_customers,

        "average_price": avg_price,
    }