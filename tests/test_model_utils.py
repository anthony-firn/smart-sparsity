import unittest
from unittest.mock import patch, MagicMock, mock_open
from model_utils import ModelHandler
import os

class TestModelHandler(unittest.TestCase):

    @patch('model_utils.AutoTokenizer.from_pretrained')
    @patch('model_utils.AutoModelForCausalLM.from_pretrained')
    @patch('model_utils.torch.save', side_effect=lambda obj, path: None)  # Mock torch.save to do nothing
    @patch('model_utils.os.path.getsize', return_value=100)  # Mock getsize to return a size value
    @patch('model_utils.os.path.exists', return_value=True)  # Mock exists to always return True
    def setUp(self, MockPathExists, MockPathGetSize, MockTorchSave, MockAutoModel, MockAutoTokenizer):
        mock_tokenizer = MockAutoTokenizer.return_value
        mock_tokenizer.encode.return_value = [101, 102]
        mock_tokenizer.decode.return_value = "Mocked output"

        mock_model = MockAutoModel.return_value
        mock_model.return_value = MagicMock()
        
        self.model_handler = ModelHandler("gpt2")

    def test_initialization(self):
        self.assertIsNotNone(self.model_handler.tokenizer)
        self.assertIsNotNone(self.model_handler.model_parts)

    @patch('model_utils.ModelHandler._load_model_part', return_value=MagicMock())
    @patch('model_utils.open', new_callable=mock_open)  # Mock open to handle file operations
    def test_inference(self, MockOpen, MockLoadModelPart):
        input_text = "Hello, world!"
        with patch('model_utils.os.path.getsize', return_value=100):  # Ensure getsize returns a value
            with patch('model_utils.os.path.exists', return_value=True):  # Ensure exists returns True
                output = self.model_handler.run_inference(input_text)
        self.assertEqual(output, "Mocked output")

if __name__ == '__main__':
    unittest.main()