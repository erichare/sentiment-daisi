import tensorflow as tf
from transformers import pipeline
# Use this model

sentiment_task = pipeline("sentiment-analysis", model="sentiment-roberta-large-english", tokenizer="sentiment-roberta-large-english")

def get_sentiment(text):
    '''
    Use a Sentiment Detection model on the given text
    
    This function takes a string of text and returns the sentiment (POSITIVE/NEGATIVE)
    along with the associated confidence / probability. 

    :param str text: The text to derive the sentiment of
    
    :return: Results of the sentiment analysis algorithm
    '''

    return sentiment_task(text)
