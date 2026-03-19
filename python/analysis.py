import pandas as pd

df = pd.read_csv("data/product_usage.csv")

# Feature adoption
adoption = df.groupby("feature_name")["user_id"].nunique()

print("Feature Adoption:")
print(adoption)

# Daily active users
daily_users = df.groupby("event_date")["user_id"].nunique()

print("\nDaily Active Users:")
print(daily_users)
