from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import os
import psutil

class ModelHandler:
    def __init__(self, model_name, memory_buffer=0.8):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)
        self.available_memory = psutil.virtual_memory().available
        self.memory_buffer = memory_buffer

    def run_inference(self, input_text):
        messages = [{"role": "user", "content": input_text}]
        input_ids = self.tokenizer.apply_chat_template(messages, tokenize=True, add_generation_prompt=True, return_tensors="pt")
        output = self.model.generate(
            input_ids,
            max_new_tokens=100,
            do_sample=True,
            temperature=0.3,
        )
        return self.tokenizer.decode(output[0], skip_special_tokens=True)

    def _can_load_part(self, part_path):
        part_size = os.path.getsize(part_path)
        return part_size < self.available_memory * self.memory_buffer

    def _load_model_part(self, part_path):
        return torch.load(part_path)

    def _unload_model_part(self, model_part):
        del model_part
        torch.cuda.empty_cache()