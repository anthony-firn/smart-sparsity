import unittest
from kivy.uix.textinput import TextInput
from app import ChatApp

class TestChatApp(unittest.TestCase):

    def setUp(self):
        self.app = ChatApp()
        self.app.build()

    def test_ui_elements(self):
        self.assertIsInstance(self.app.input_text, TextInput)
        self.assertIsNotNone(self.app.send_button)
        self.assertIsNotNone(self.app.output_label)

    def test_send_message(self):
        input_text = "Test message"
        self.app.input_text.text = input_text
        self.app.send_message(None)
        output = self.app.output_label.text
        self.assertGreater(len(output), 0)

if __name__ == '__main__':
    unittest.main()