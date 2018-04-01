import unittest
import src.sentiment_processing as sp

class TestSentimentProcessing(unittest.TestCase):

    def test_type(self):
        result = sp.get_polarity('hello world')
        self.assertEqual(type(result), float)

    def test_range(self):
        result = sp.get_polarity('hello world')
        self.assertGreater(result, -1)
        self.assertLess(result, 1)

    def test_positive(self):
        text = 'happy good nice cool'
        result = sp.get_polarity(text)
        self.assertGreater(result, 0)

    def test_negative(self):
        text = 'ugly bad worse aufull terrible'
        result = sp.get_polarity(text)
        self.assertLess(result, 0)


if __name__ == '__main__':
    unittest.main()