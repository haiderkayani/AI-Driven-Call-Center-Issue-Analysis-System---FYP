import pandas as pd

# Load dataset
dataset_path = 'ai_model\data\dataset.tsv'
df = pd.read_csv(dataset_path, sep='\t')

# Replace .mp3 extensions with .wav
df['path'] = df['path'].str.replace('.mp3', '.wav')

# Save the updated dataset
df.to_csv(dataset_path, sep='\t', index=False)
print("Updated dataset file paths to use .wav extensions.")