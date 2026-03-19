import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/product_usage.csv")

# Convert dates
df["event_date"] = pd.to_datetime(df["event_date"])
df["signup_date"] = pd.to_datetime(df["signup_date"])

# Create cohort (signup date)
df["cohort"] = df["signup_date"].dt.to_period("D")

# Days since signup
df["days_since_signup"] = (df["event_date"] - df["signup_date"]).dt.days

# Create retention table
cohort_data = df.groupby(["cohort", "days_since_signup"])["user_id"].nunique().reset_index()

# Pivot into retention matrix
retention_table = cohort_data.pivot(index="cohort", columns="days_since_signup", values="user_id")

# Normalize by cohort size
cohort_sizes = retention_table.iloc[:, 0]
retention_rate = retention_table.divide(cohort_sizes, axis=0)

print("\nRetention Table:\n", retention_rate)

# Plot retention curves
retention_rate.T.plot(legend=False)
plt.title("Retention Curve")
plt.xlabel("Days Since Signup")
plt.ylabel("Retention Rate")
plt.show()

# ---- CHURN CALCULATION ----

# Total users who signed up
total_users = df["user_id"].nunique()

# Users who returned AFTER signup
returning_users = df[df["days_since_signup"] > 0]["user_id"].nunique()

# Avoid division by zero
if total_users == 0:
    churn_rate = 0
else:
    churn_rate = 1 - (returning_users / total_users)

print(f"Total Users: {total_users}")
print(f"Returning Users: {returning_users}")
print(f"Churn Rate: {churn_rate:.2%}")
