import pandas as pd


def main():
    df = pd.read_csv("../data/processed/top_hacker_news_stories.csv")
    # Convert scores to floats
    df["score"] = df["score"].astype(float)
    # Print head
    print(df.head())
    # Save cleaned data
    df.to_csv("../data/processed/top_hacker_news_stories.csv", index=False)


if __name__ == "__main__":
    main()
