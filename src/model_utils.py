from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import os
import psutil

class ModelHandler:
    def __init__(self, model_name, memory_buffer=0.8):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model_parts = self._download_and_split_model(model_name)
        self.available_memory = psutil.virtual_memory().available
        self.memory_buffer = memory_buffer

    def _download_and_split_model(self, model_name):
        model = AutoModelForCausalLM.from_pretrained(model_name)
        model_parts = ["part1.pth", "part2.pth", "part3.pth"]
        return model_parts

    def run_inference(self, input_text):
        inputs = self.tokenizer(input_text, return_tensors="pt")
        output = inputs
        for part in self.model_parts:
            if self._can_load_part(part):
                model_part = self._load_model_part(part)
                output = model_part(output)
                self._unload_model_part(model_part)
            else:
                raise MemoryError("Not enough memory to load model part")
        return self.tokenizer.decode(output[0], skip_special_tokens=True)

    def _can_load_part(self, part_path):
        part_size = os.path.getsize(part_path)
        return part_size < self.available_memory * self.memory_buffer

    def _load_model_part(self, part_path):
        return torch.load(part_path)

    def _unload_model_part(self, model_part):
        del model_part
        torch.cuda.empty_cache()