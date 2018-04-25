import unittest
from src.sentiment_processing import SentimentProcessor


class TestSentimentProcessing(unittest.TestCase):

    def test_type(self):
        sp = SentimentProcessor()
        result = sp.get_polarity('hello world')
        self.assertEqual(type(result), float)

    def test_range(self):
        sp = SentimentProcessor()
        result = sp.get_polarity('hello world')
        self.assertGreater(result, -1)
        self.assertLess(result, 1)

    def test_positive(self):
        sp = SentimentProcessor()
        text = 'happy good nice cool'
        result = sp.get_polarity(text)
        self.assertGreater(result, 0)

    def test_negative(self):
        sp = SentimentProcessor()
        text = 'ugly bad worse aufull terrible'
        result = sp.get_polarity(text)
        self.assertLess(result, 0)


if __name__ == '__main__':
    unittest.main()
