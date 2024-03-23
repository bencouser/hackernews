import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split
from tensorflow.keras.layers import (
    LSTM,
    Bidirectional,
    Conv1D,
    Dense,
    Dropout,
    Embedding,
    GlobalMaxPooling1D,
)
from tensorflow.keras.models import Sequential
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer

# Load the data
data = pd.read_csv("../data/processed/top_hacker_news_stories.csv")

VOCAB_SIZE = 2580

# Set the seed for reproducibility
tf.random.set_seed(42)

# Preprocess the data
tokenizer = Tokenizer(num_words=VOCAB_SIZE, oov_token="<OOV>")
tokenizer.fit_on_texts(data["title"])
sequences = tokenizer.texts_to_sequences(data["title"])
padded_sequences = pad_sequences(sequences, maxlen=20)

# Splitting the dataset
X_train, X_val, y_train, y_val = train_test_split(
    padded_sequences, data["score"], test_size=0.2, random_state=42
)

# Model building
model_2 = Sequential(
    [
        Embedding(input_dim=VOCAB_SIZE, output_dim=300, input_length=20),
        Dropout(0.2),
        Conv1D(64, 5, activation="relu"),
        Bidirectional(LSTM(64, return_sequences=True)),
        GlobalMaxPooling1D(),
        Dense(64, activation="relu"),
        Dropout(0.2),
        Dense(1),
    ]
)

# Compile the model
model_2.compile(
    optimizer="adam", loss="mean_squared_error", metrics=["mean_absolute_error"]
)

# Train the model
model_2.fit(X_train, y_train, epochs=20, validation_data=(X_val, y_val))

# Evaluate the model
evaluation = model_2.evaluate(X_val, y_val)
print("Evaluation:", evaluation)

# Make a prediction
test_title = ["apple is releasing a new product"]
test_seq = tokenizer.texts_to_sequences(test_title)
test_pad = pad_sequences(test_seq, maxlen=20)
predicted_score = model_2.predict(test_pad)

print("Predicted Score:", predicted_score)
