from transformers import MarianMTModel, MarianTokenizer

class UrduToEnglishTranslator:
    def __init__(self, model_path):
        self.tokenizer = MarianTokenizer.from_pretrained(model_path)
        self.model = MarianMTModel.from_pretrained(model_path)

    def translate(self, urdu_text):
        inputs = self.tokenizer(urdu_text, return_tensors="pt", padding=True, truncation=True)
        translated_tokens = self.model.generate(**inputs)
        translated_text = self.tokenizer.batch_decode(translated_tokens, skip_special_tokens=True)
        return translated_text[0]

# Example usage
if __name__ == "__main__":
    model_path = r"E:\\Urdu-To-English-Machine-Translation\\opus-mt-ur-en-finetuned-ur-to-en\\checkpoint-1260"
    translator = UrduToEnglishTranslator(model_path)

    urdu_text = "پاکستان ایک خوبصورت ملک ہے۔"
    print("Translated Text:", translator.translate(urdu_text))
