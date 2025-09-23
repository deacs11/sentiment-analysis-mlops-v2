 # tests/test_model.py
import unittest
import os


from model import SentimentModel

class TestSentimentModel(unittest.TestCase):

    def setUp(self):
        """Questo metodo viene eseguito prima di ogni test."""
        self.model = SentimentModel()

    def test_positive_sentiment(self):
        """Testa che una recensione con parole chiave positive restituisca 'positive'."""
        sentiment, confidence = self.model.predict_sentiment("This is an amazing product!")
        self.assertEqual(sentiment, "positive")
        print(f"\n[Unit Test] Positive Sentiment -> OK")

    def test_negative_sentiment(self):
        """Testa che una recensione con parole chiave negative restituisca 'negative'."""
        sentiment, confidence = self.model.predict_sentiment("This is a terrible experience.")
        self.assertEqual(sentiment, "negative")
        print(f"[Unit Test] Negative Sentiment -> OK")

    def test_neutral_sentiment(self):
        """Testa che una recensione senza parole chiave specifiche restituisca 'neutral'."""
        sentiment, confidence = self.model.predict_sentiment("The product was delivered on time.")
        self.assertEqual(sentiment, "neutral")
        print(f"[Unit Test] Neutral Sentiment -> OK")

if __name__ == '__main__':
    unittest.main()
