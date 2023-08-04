# review_classifier/models.py

import torch
import transformers
from transformers import pipeline, AutoTokenizer

class MovieReviewClassifier:
    def __init__(self):
        model_path = "/home/maxem/Downloads/tuned_multiclass_classification_actual"
        self.model = pipeline("sentiment-analysis", model=model_path)

        self.tokenizer = AutoTokenizer.from_pretrained(model_path)
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    def predict(self, review_text):
        mapping = {
            "LABEL_0": 1, "LABEL_1": 2, "LABEL_2": 3, "LABEL_3": 4,
            "LABEL_4": 7, "LABEL_5": 8, "LABEL_6": 9, "LABEL_7": 10
        }
        label = self.model(review_text)[0]['label']
        return mapping[label]
