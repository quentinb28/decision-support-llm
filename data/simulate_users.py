import pandas as pd
import numpy as np
from datetime import datetime, timedelta

np.random.seed(42)

N_USERS = 10000

def simulate_users(n=N_USERS):

    # -----------------------------
    # Signup dates
    # -----------------------------
    signup_dates = [
        datetime.today() - timedelta(days=np.random.randint(0, 60))
        for _ in range(n)
    ]

    # -----------------------------
    # Experiment split
    # -----------------------------
    group = np.random.choice(["control", "treatment"], size=n)

    # -----------------------------
    # Activation probability
    # Treatment improves activation
    # -----------------------------
    activation_prob = np.where(group == "treatment", 0.55, 0.50)
    activated = np.random.binomial(1, activation_prob)

    # -----------------------------
    # Weekly usage
    # Higher for activated users
    # -----------------------------
    weekly_usage = np.where(
        activated == 1,
        np.random.poisson(5, size=n),
        np.random.poisson(1, size=n)
    )

    # -----------------------------
    # 4-week retention
    # Treatment slightly hurts retention
    # -----------------------------
    retention_prob = np.where(group == "treatment", 0.35, 0.38)
    retained_4w = np.random.binomial(1, retention_prob)

    # -----------------------------
    # Paid conversion
    # Activated + retained users more likely
    # -----------------------------
    paid_prob = (
        0.05 +
        0.10 * activated +
        0.10 * retained_4w
    )
    paid = np.random.binomial(1, paid_prob)

    # -----------------------------
    # Revenue (monthly)
    # Treatment slightly improves ARPU
    # -----------------------------
    base_revenue = np.random.normal(10, 2, size=n)
    treatment_bonus = np.where(group == "treatment", 1.0, 0.0)
    revenue = paid * (base_revenue + treatment_bonus)

    # -----------------------------
    # Final dataframe
    # -----------------------------
    df = pd.DataFrame({
        "user_id": range(n),
        "signup_date": signup_dates,
        "group": group,
        "activated": activated,
        "weekly_usage": weekly_usage,
        "retained_4w": retained_4w,
        "paid": paid,
        "revenue": revenue
    })

    return df


if __name__ == "__main__":
    df = simulate_users()
    df.to_csv("simulated_users.csv", index=False)
    print("Simulated user data saved as simulated_users.csv")

