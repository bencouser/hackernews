import pandas as pd


def main(file_path="../data/processed/joined_data_clean_titles.csv"):
    df = pd.read_csv(file_path)
    # Convert scores to floats
    df["score"] = df["score"].astype(float)
    # Print head
    print(df.head())
    # Save cleaned data
    df.to_csv(file_path)


if __name__ == "__main__":
    main()
