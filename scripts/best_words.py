import pandas as pd

# Load the data
data = pd.read_csv("../data/processed/top_hacker_news_stories.csv")


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


best_words = get_best_words(data)


# Sort the dictionary by value
best_words = dict(sorted(best_words.items(), key=lambda item: item[1], reverse=True))


# Print best 30 words
print("Best Scoring 30 words:")
print(list(best_words.keys())[:30])
