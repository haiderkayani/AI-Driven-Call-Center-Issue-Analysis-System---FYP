import os
import pandas as pd
import numpy as np
import pickle
from tqdm import tqdm
from feature_extraction import extract_features  #importing function from feature_extraction

#defining paths
data_dir = 'ai_model\data\limited_wav_files'
audio_dir = os.path.join(data_dir, 'limited_wav_files')
output_dir = 'ai_model\data\processed_data'
encoded_data_path = os.path.join(output_dir, 'encoded_dataset.csv')
features_path = os.path.join(output_dir, "audio_features.npy")

os.makedirs(output_dir, exist_ok=True)

#loading encoded dataset
df = pd.read_csv(encoded_data_path)

features = []

print("extracting features from audio files...")
for idx, row in tqdm(df.iterrows(), total=len(df)): 
    audio_file = os.path.join(audio_dir, row['path'])
    #audio_file = os.path.normpath(audio_file)
    feature = extract_features(audio_file)
    if feature is not None:
        features.append(feature)
    else:
        features.append(np.zeros((128, 157)))  #placeholder for failed extractions

#converting to numpy array and save
features = np.array(features)
np.save(features_path, features)

print(f"audio features saved to {features_path}")
