import os
import torch
import pandas as pd
import librosa
import numpy as np
from torch.utils.data import Dataset, DataLoader
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
import torch.nn.functional as F
from torch.optim import AdamW
import whisper

# Define paths
data_dir = "ai_model/data"
processed_data_dir = r"E:\AI-Driven-Call-Center-Issue-Analysis-System---FYP\ai_model\data\processed_data"
train_file = r"E:\AI-Driven-Call-Center-Issue-Analysis-System---FYP\ai_model\data\processed_data\train_data.csv"
test_file = r"E:\AI-Driven-Call-Center-Issue-Analysis-System---FYP\ai_model\data\processed_data\test_data.csv"
audio_dir = r"E:\AI-Driven-Call-Center-Issue-Analysis-System---FYP\ai_model\data\limited_wav_files\limited_wav_files"

# Load processor (tokenizer + feature extractor)
processor = Wav2Vec2Processor.from_pretrained(data_dir)
#processor = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-large-xlsr-53")

# Custom dataset class
class SpeechDataset(Dataset):
    def __init__(self, csv_file, audio_dir, processor):
        self.data = pd.read_csv(csv_file)
        self.audio_dir = audio_dir
        self.processor = processor

    def __getitem__(self, idx):
        row = self.data.iloc[idx]
        audio_path = os.path.join(self.audio_dir, row["path"])
        
        # Load only one file at a time
        waveform, sample_rate = librosa.load(audio_path, sr=16000)  
        
        inputs = self.processor(waveform, sampling_rate=sample_rate, return_tensors="pt", padding=True)

        label_ids = eval(row["encoded_text"])
        labels = torch.tensor(label_ids, dtype=torch.long)

        return {
            "input_values": inputs.input_values.squeeze(0),
            "attention_mask": inputs.attention_mask.squeeze(0),
            "labels": labels
        }

    def __len__(self):
        return len(self.data)

# Load datasets
train_dataset = SpeechDataset(train_file, audio_dir, processor)
test_dataset = SpeechDataset(test_file, audio_dir, processor)

# DataLoader
train_loader = DataLoader(train_dataset, batch_size=2, shuffle=True, collate_fn=lambda x: x)
test_loader = DataLoader(test_dataset, batch_size=2, shuffle=False, collate_fn=lambda x: x)

# Load pretrained Wav2Vec2 model
model = Wav2Vec2ForCTC.from_pretrained(
    "facebook/wav2vec2-large-xlsr-53",
    vocab_size=len(processor.tokenizer)
)

# data_collator = DataCollatorForSeq2Seq(processor, model=model, padding=True)

# # Define training arguments
# training_args = TrainingArguments(
#     output_dir="./results",
#     eval_strategy="epoch",
#     save_strategy="epoch",
#     learning_rate=5e-5,
#     per_device_train_batch_size=8,
#     per_device_eval_batch_size=8,
#     num_train_epochs=3,
#     weight_decay=0.01,
#     logging_dir="./logs",
#     logging_steps=500,  # Reduced logging noise
#     save_total_limit=2,
#     fp16=True,  # Mixed precision for better performance
#     push_to_hub=False,
# )

# # Trainer
# trainer = Trainer(
#     model=model,
#     args=training_args,
#     train_dataset=train_dataset,
#     eval_dataset=test_dataset,
#     tokenizer=processor,
#     data_collator=data_collator,
# )

# # Train the model
# trainer.train()

optimizer = AdamW(model.parameters(), lr=5e-5)

# Loss Function
def compute_loss(logits, labels):
    loss_fct = torch.nn.CTCLoss(blank=processor.tokenizer.pad_token_id)
    log_probs = F.log_softmax(logits, dim=-1)
    
    # Compute lengths
    input_lengths = torch.full(
        size=(logits.shape[0],),
        fill_value=logits.shape[1],
        dtype=torch.long
    ).to(logits.device)

    target_lengths = torch.tensor([len(label) for label in labels], dtype=torch.long).to(logits.device)
    labels = torch.cat(labels).to(logits.device)

    return loss_fct(log_probs.permute(1, 0, 2), labels, input_lengths, target_lengths)

# Training Loop
num_epochs = 3
device = "cuda" if torch.cuda.is_available() else "cpu"

for epoch in range(num_epochs):
    model.train()
    total_loss = 0
    
    for batch in train_loader:
        # Handle variable-length padding manually
        batch_inputs = [item["input_values"] for item in batch]
        batch_labels = [item["labels"] for item in batch]

        # Find max length for padding
        max_len = max([x.shape[0] for x in batch_inputs])

        # Pad inputs manually
        batch_inputs = torch.stack([
            F.pad(x, (0, max_len - x.shape[0]), "constant", 0) for x in batch_inputs
        ]).to(device)

        # Forward pass
        optimizer.zero_grad()
        outputs = model(batch_inputs).logits

        # Compute loss
        loss = compute_loss(outputs, batch_labels)
        loss.backward()
        optimizer.step()

        total_loss += loss.item()

    avg_loss = total_loss / len(train_loader)
    print(f"Epoch {epoch+1}/{num_epochs}, Loss: {avg_loss:.4f}")


# Save final model
model.save_pretrained("ai_model/models")
processor.save_pretrained("ai_model/models")

print("training complete. Model saved to 'ai_model/models'.")
