import matplotlib.pyplot as plt
import pandas as pd

# Load the data
data = pd.read_csv("../data/raw/top_hacker_news_stories.csv")


# Plot histogram of title lengths
title_lengths = data["title"].str.len()
plt.hist(title_lengths, bins=25)
plt.xlabel("Title Length")
plt.ylabel("Frequency")
plt.title("Histogram of Title Lengths")
plt.savefig("../images/title_length_histogram.jpeg")
plt.close()


# Plot histogram of scores
plt.hist(data["score"], bins=25)
plt.xlabel("Score")
plt.ylabel("Frequency")
plt.title("Histogram of Scores")
plt.savefig("../images/score_histogram.jpeg")
plt.close()
