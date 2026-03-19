import pandas as pd

df = pd.read_csv("data/product_usage.csv")

# Convert dates
df["event_date"] = pd.to_datetime(df["event_date"])
df["signup_date"] = pd.to_datetime(df["signup_date"])

# Feature adoption
feature_adoption = df.groupby("feature_name")["user_id"].nunique()
print("Feature Adoption:\n", feature_adoption)

# Daily active users (DAU)
dau = df.groupby("event_date")["user_id"].nunique()
print("\nDaily Active Users:\n", dau)

# Adoption by plan
plan_adoption = df.groupby(["plan", "feature_name"])["user_id"].nunique().unstack()
print("\nAdoption by Plan:\n", plan_adoption)

# Retention (users active after signup)
df["days_since_signup"] = (df["event_date"] - df["signup_date"]).dt.days
retention = df[df["days_since_signup"] > 0]["user_id"].nunique()
print("\nReturning Users:", retention)
