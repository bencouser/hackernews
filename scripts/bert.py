import keras
import pandas as pd
import tensorflow as tf
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
    # Get Data
    df = load_data()

    # Set random seed
    tf.random.set_seed(69)

    # Load Model and tokenize
    berty, tokenizer = load_model()
    encoded_titles = encode_titles(df["title"].values, tokenizer)

    # Sort Bert out
    optimizer = tf.keras.optimizers.legacy.Adam(learning_rate=5e-5)
    loss = keras.losses.MeanSquaredError()
    metrics = [
        tf.keras.metrics.MeanSquaredError(),
        tf.keras.metrics.MeanAbsoluteError(),
    ]
    berty.compile(optimizer=optimizer, loss=loss, metrics=metrics)
    print(berty.summary())

    # Training
    history_berty = berty.fit(encoded_titles, df["score"], epochs=16, batch_size=8)

    # Save Model
    berty.save("../models/berty_v2")

    # Evaluation
    evaluation = berty.evaluate(encoded_titles, df["score"])

    # Prediction
    test_titles = ["uber for dogs", "apple new chip"]
    for title in test_titles:
        encoded_title = encode_titles([title], tokenizer)
        prediction = berty.predict(encoded_title)
        print(f"Title: {title}, Prediction: {prediction}")


if __name__ == "__main__":
    main()
