from sklearn.model_selection import train_test_split
import pandas as pd

# Load encoded dataset again (if needed)
df_encoded = pd.read_csv("ai_model/data/processed_data/processed_data.csv")

# Splitting data (80% train, 20% test)
train_df, test_df = train_test_split(df_encoded, test_size=0.2, random_state=42)

# Save the splits
train_df.to_csv("ai_model/data/processed_data/train_data.csv", index=False)
test_df.to_csv("ai_model/data/processed_data/test_data.csv", index=False)

print(f"Training data saved: {len(train_df)} samples")
print(f"Testing data saved: {len(test_df)} samples")
