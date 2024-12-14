import os
import pandas as pd
import pickle

#defining paths
data_dir = 'ai_model/data'
output_dir = 'ai_model/data/preprocessed'

#ensuring output directory exists
os.makedirs(output_dir, exist_ok=True)

#loading tsv file and converting list to dictionary
tsv_path = os.path.join(data_dir, 'dataset.tsv')
df = pd.read_csv(tsv_path, delimiter='\t')

vocab_path = os.path.join(data_dir, 'char_to_num_vocab.pkl')
with open(vocab_path, 'rb') as f:
    char_to_num = pickle.load(f)

if isinstance(char_to_num, list):
    char_to_num = {char: idx for idx, char in enumerate(char_to_num)}

#encoding function
def encode_text(text, char_to_num):
    return [char_to_num[char] for char in text if char in char_to_num]

df['encoded_text'] = df['sentence'].apply(lambda x: encode_text(x, char_to_num))

#saving encoded data to new csv file
encoded_data_path = os.path.join(output_dir, 'encoded_dataset.csv')
df.to_csv(encoded_data_path, index=False)

print(f"encoded data saved to {encoded_data_path}")
