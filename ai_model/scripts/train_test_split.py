import pandas as pd
from sklearn.model_selection import train_test_split
import os

#defining paths
processed_data_dir = 'ai_model\data\processed_data'
encoded_data_path = os.path.join(processed_data_dir, 'encoded_dataset.csv')

#loading encoded dataset and splitting into train test
df = pd.read_csv(encoded_data_path)
train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)

#saving
train_path = os.path.join(processed_data_dir, 'train_dataset.csv')
test_path = os.path.join(processed_data_dir, 'test_dataset.csv')
train_df.to_csv(train_path, index=False)
test_df.to_csv(test_path, index=False)
print(f"train dataset saved to {train_path}")
print(f"test dataset saved to {test_path}")
