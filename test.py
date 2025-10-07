import unittest
import pandas as pd
from ds_helper.column_detector import column_detector
from ds_helper.text_cleaner import TextCleaner
from ds_helper.auto_visualizer import visualize

class TestDSHelper(unittest.TestCase):

    def test_column_detector(self):
        df = pd.DataFrame({
            'A': [1, 2, 3, 4, 5],
            'B': ['apple', 'banana', 'apple', 'orange', 'banana'],
            'C': [0.1, 0.2, 0.3, 0.4, 0.5]
        })
        result = column_detector(df)
        expected = {'A': 'numerical', 'B': 'categorical', 'C': 'numerical'}
        self.assertEqual(result, expected)

    def test_text_cleaner_clean_text(self):
        cleaner = TextCleaner()
        text = "Um, I think this product is, like, really good!!! But you know, it’s a bit pricey."
        cleaned = cleaner.clean_text(text)
        # Expected after lower, remove punct, remove fillers/stopwords, lemmatize
        expected = "think product really good bit pricey"
        self.assertEqual(cleaned, expected)

    def test_text_cleaner_clean_corpus(self):
        cleaner = TextCleaner()
        corpus = ["Uh, this is an amazing movie!", "I like the acting, but um the plot was weak."]
        cleaned = cleaner.clean_corpus(corpus)
        expected = ["amazing movie", "like acting plot weak"]
        self.assertEqual(cleaned, expected)

    def test_auto_visualizer_runs_without_error(self):
        df = pd.DataFrame({
            "Age": [23, 45, 21, 34, 42, 55],
            "Gender": ["M", "F", "F", "M", "M", "F"],
            "Remarks": ["good", "excellent", "bad", "average", "good", "bad"]
        })
        # Just test that it runs without error, since plotting is hard to test
        try:
            visualize(df)
        except Exception as e:
            self.fail(f"visualize raised an exception: {e}")

if __name__ == '__main__':
    unittest.main()
