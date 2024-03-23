import pandas as pd


def main():
    df = pd.read_csv("../data/raw/top_hacker_news_stories.csv")
    # Drop null values
    df = df.dropna()
    # Drop duplicates
    df = df.drop_duplicates()
    # Remove symbols
    df["title"] = df["title"].str.replace(r"[^\w\s]", "", regex=True)
    # Lowercase
    df["title"] = df["title"].str.lower()
    # Print head
    print(df.head())
    # Save cleaned data
    df.to_csv("../data/processed/top_hacker_news_stories.csv", index=False)


if __name__ == "__main__":
    main()
