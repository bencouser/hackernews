import pandas as pd


def main(file_path="../data/raw/joined_data.csv"):
    df = pd.read_csv(file_path)
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
    df.to_csv("../data/processed/joined_data_clean_titles.csv", index=False)


if __name__ == "__main__":
    main()
