from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model_name = "facebook/nllb-200-distilled-600M"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

tokenizer.src_lang = "urd_Latn"
forced_bos_token_id = tokenizer.convert_tokens_to_ids("eng_Latn")  # ▁ is the underscore character for sentencepiece

def translate_urdu_to_english(text):
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
    translated_tokens = model.generate(**inputs, forced_bos_token_id=forced_bos_token_id)
    return tokenizer.batch_decode(translated_tokens, skip_special_tokens=True)[0]