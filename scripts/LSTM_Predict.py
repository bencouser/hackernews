import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split
from tensorflow.keras.layers import LSTM, Dense, Embedding
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
padded_sequences = pad_sequences(sequences, maxlen=10)

# Splitting the dataset
X_train, X_val, y_train, y_val = train_test_split(
    padded_sequences, data["score"], test_size=0.1, random_state=42
)

# Model building
basic_lstm_model = Sequential(
    [
        Embedding(input_dim=VOCAB_SIZE, output_dim=16, input_length=10),
        LSTM(64),
        Dense(1),
    ]
)

# Compile the model
basic_lstm_model.compile(
    optimizer="adam", loss="mean_squared_error", metrics=["mean_absolute_error"]
)

# Train the model
basic_lstm_model.fit(X_train, y_train, epochs=10, validation_data=(X_val, y_val))

# Evaluate the model
evaluation = basic_lstm_model.evaluate(X_val, y_val)
print("Evaluation:", evaluation)

# Make a prediction
test_title = ["apple is releasing a new product"]
test_seq = tokenizer.texts_to_sequences(test_title)
test_pad = pad_sequences(test_seq, maxlen=10)
predicted_score = basic_lstm_model.predict(test_pad)

print("Predicted Score:", predicted_score)
