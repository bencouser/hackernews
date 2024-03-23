import pandas as pd

# Load the data
data = pd.read_csv("../data/raw/top_hacker_news_stories.csv")


# Display the shape of the data
print("Data shape:", data.shape)


# Display the first few rows of the data
print(data.head())


# Get vocabulary size
vocabulary_size = len(set(data["title"].str.cat(sep=" ").split()))
print("Vocabulary size:", vocabulary_size)


# Get most common words
word_counts = data["title"].str.cat(sep=" ").split()
word_counts = pd.Series(word_counts).value_counts()
print("Most common words:", word_counts.head(10))


# Show counts of Show, Ask, and Launch HN Titles
print("Show HN Titles:", data["title"].str.contains("Show HN").sum())
print("Ask HN Titles:", data["title"].str.contains("Ask HN").sum())
print("Launch HN Titles:", data["title"].str.contains("Launch HN").sum())


# Show max, min, average, and median scores
print("Max score:", data["score"].max())
print("Min score:", data["score"].min())
print("Average score:", data["score"].mean())
print("Median score:", data["score"].median())


# Show quartiles of scores
print("25th percentile score:", data["score"].quantile(0.25))
print("50th percentile score:", data["score"].quantile(0.5))
print("75th percentile score:", data["score"].quantile(0.75))
