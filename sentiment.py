import tensorflow as tf
from transformers import pipeline

sentiment_task = pipeline("sentiment-analysis", model="sentiment-roberta-large-english", tokenizer="sentiment-roberta-large-english")

def get_sentiment(text):
    return sentiment_task(text)
