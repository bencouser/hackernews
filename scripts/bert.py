import numpy as np
import pandas as pd
from transformers import BertTokenizer, TFBertForSequenceClassification


def load_data(file_path="../data/raw/joined_data.csv"):
    df = pd.read_csv(file_path)
    return df


def load_model():
    model_name = "bert-base-uncased"
    tokenizer = BertTokenizer.from_pretrained(model_name)

    model = TFBertForSequenceClassification.from_pretrained(model_name, num_labels=1)
    return model, tokenizer


def encode_titles(titles, tokenizer, max_length=128):
    titles = [str(title) for title in titles if pd.notnull(title)]
    return tokenizer(
        titles,
        padding="max_length",
        truncation=True,
        max_length=max_length,
        return_tensors="tf",
    )


def main():
    df = load_data()
    model, tokenizer = load_model()
    encoded_titles = encode_titles(df["title"].values, tokenizer)
    # Print first 5 encoded titles wth inputs
    for i in range(5):
        print(df["title"].values[i])
        print(encoded_titles["input_ids"][i])


if __name__ == "__main__":
    main()
