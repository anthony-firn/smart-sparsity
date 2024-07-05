import unittest
from model_utils import ModelHandler

class TestModelHandler(unittest.TestCase):

    def setUp(self):
        self.model_handler = ModelHandler("path_to_dummy_model")

    def test_initialization(self):
        self.assertIsNotNone(self.model_handler.tokenizer)
        self.assertIsNotNone(self.model_handler.model_parts)

    def test_inference(self):
        input_text = "Hello, world!"
        output = self.model_handler.run_inference(input_text)
        self.assertIsInstance(output, str)
        self.assertGreater(len(output), 0)

if __name__ == '__main__':
    unittest.main()