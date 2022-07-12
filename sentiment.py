import tensorflow as tf
from transformers import pipeline

sentiment_task = pipeline("sentiment-analysis", model="model", tokenizer="model")

def get_sentiment(text):
    return sentiment_task(text)
