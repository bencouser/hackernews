import tensorflow as tf
from transformers import GPT2Tokenizer, TFGPT2LMHeadModel
import sys


def load_model():
    model_name = "gpt2"
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)

    model = TFGPT2LMHeadModel.from_pretrained(model_name)
    return model, tokenizer


def main(input_text: str):
    model, tokenizer = load_model()
    input_ids = tokenizer.encode(input_text, return_tensors="tf")
    output = model.generate(
        input_ids,
        max_length=100,
        # num_return_sequences=5,
        no_repeat_ngram_size=2,
        repetition_penalty=1.5,
        top_p=0.92,
        temperature=0.85,
    )

    print(tokenizer.decode(output[0], skip_special_tokens=True))


if __name__ == "__main__":
    # Get argument
    # if len(sys.argv) != 1:
    #     print("Usage: python gpt2.py <input_text>")
    #     sys.exit(1)
    # else:
    #     input_text = sys.argv[0]
    input_text = sys.argv[0]
    input_text = str(input_text)
    print("input_text: ", input_text)

    main(input_text)
