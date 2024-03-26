import pandas as pd


def load_data(file_path="../data/processed/joined_data_clean_titles.csv"):
    # Load the data
    data = pd.read_csv(file_path)
    return data


# Get words with highest score
def get_best_words(data):
    best_words = {}
    for index, row in data.iterrows():
        words = row["title"].split()
        for word in words:
            if word not in best_words:
                best_words[word] = row["score"]
            else:
                best_words[word] += row["score"]
    return best_words


if __name__ == "__main__":
    # Load the data
    data = load_data()

    # Get the best words
    best_words = get_best_words(data)

    # Sort the dictionary by value
    best_words = dict(
        sorted(best_words.items(), key=lambda item: item[1], reverse=True)
    )

    # Print best 30 words
    print("Best Scoring 30 words:")
    print(list(best_words.keys())[:30])
