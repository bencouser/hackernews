import glob

import pandas as pd


def join_data(directory="../data/raw/"):
    """
    Read each csv file in a directory. eg "../data/raw/"
    Join them into a single csv file.
    Save the file within the same directory.
    """
    # Read all csv files in the directory
    csv_pattern = directory + "*.csv"
    csv_files = glob.glob(csv_pattern)
    csv_data = {}
    for file_path in csv_files:
        file_name = file_path.split("/")[-1]
        csv_data[file_name] = pd.read_csv(file_path)

    print(list(csv_data.keys()))

    # Join the data
    joined_data = pd.concat(csv_data.values(), ignore_index=True)

    # Save the joined data
    joined_data.to_csv(directory + "joined_data.csv", index=False)
    print("Data joined and saved to", directory + "joined_data.csv")


if __name__ == "__main__":
    join_data()
