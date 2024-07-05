from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup

from model_utils import ModelHandler
from config import Config
from logging_utils import setup_logger

logger = setup_logger(Config.LOG_LEVEL)

class ChatApp(App):
    def build(self):
        self.model_handler = ModelHandler(Config.MODEL_NAME, Config.MEMORY_BUFFER)

        layout = BoxLayout(orientation='vertical')
        self.input_text = TextInput(hint_text='Enter your message here', size_hint=(1, 0.1))
        self.send_button = Button(text='Send', size_hint=(1, 0.1))
        self.send_button.bind(on_press=self.send_message)
        self.output_label = Label(text='Output will be displayed here', size_hint=(1, 0.8))

        layout.add_widget(self.input_text)
        layout.add_widget(self.send_button)
        layout.add_widget(self.output_label)
        
        return layout

    def send_message(self, instance):
        input_text = self.input_text.text
        try:
            output = self.model_handler.run_inference(input_text)
            self.output_label.text = output
        except MemoryError as e:
            logger.error(f"Memory error: {e}")
            self.show_error_popup("Memory Error", str(e))

    def show_error_popup(self, title, message):
        popup = Popup(title=title, content=Label(text=message), size_hint=(None, None), size=(400, 200))
        popup.open()

if __name__ == '__main__':
    ChatApp().run()