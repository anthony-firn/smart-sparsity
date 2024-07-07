import unittest
from unittest.mock import patch, MagicMock
from model_utils import ModelHandler

class TestModelHandler(unittest.TestCase):

    @patch('model_utils.AutoTokenizer.from_pretrained')
    def setUp(self, MockAutoTokenizer):
        mock_tokenizer = MockAutoTokenizer.return_value
        mock_tokenizer.encode.return_value = [101, 102]
        mock_tokenizer.decode.return_value = "Mocked output"
        self.model_handler = ModelHandler("distilbert-base-uncased")

    def test_initialization(self):
        self.assertIsNotNone(self.model_handler.tokenizer)
        self.assertIsNotNone(self.model_handler.model_parts)

    def test_inference(self):
        input_text = "Hello, world!"
        output = self.model_handler.run_inference(input_text)
        self.assertEqual(output, "Mocked output")

if __name__ == '__main__':
    unittest.main()