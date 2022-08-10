# Sentiment Analysis with Daisies

## How to Call

First, we simply load the PyDaisi package:

```python
import pydaisi as pyd
```

Next, we connect to the Daisi:

```python
sentiment_analysis = pyd.Daisi("erichare/Sentiment Analysis")
```

Now, we simply pass in any text string we want:

```python
sentiment_analysis.get_sentiment(text="I am so happy right now.").value
```

Or we can even bulk-pass in sentences:

```python
sentiment_analysis.get_sentiment(text=["I am so happy right now!", "But i'm a little unsure", "And i'm really really mad"]).value
```
