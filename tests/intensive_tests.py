# intensive_tests.py
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

def run_intensive_test():
    model_name = "CohereForAI/c4ai-command-r-plus"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)

    input_text = "Hello, how are you?"
    messages = [{"role": "user", "content": input_text}]
    input_ids = tokenizer.apply_chat_template(messages, tokenize=True, add_generation_prompt=True, return_tensors="pt")

    # Ensure that the model runs on GPU if available
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)
    input_ids = input_ids.to(device)

    output = model.generate(
        input_ids,
        max_new_tokens=100,
        do_sample=True,
        temperature=0.3,
    )
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
    print(generated_text)

if __name__ == "__main__":
    run_intensive_test()