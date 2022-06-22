import os
import glob
import pandas as pd
from itertools import repeat


def read_and_modify_csv(file):
    df = pd.read_csv(file, usecols=["Source IP"])
    df = df["Source IP"].unique()
    env = os.path.basename(file).split(".")[0]
    env_list = []
    env_list.extend(repeat(env, len(df)))
    i_df = pd.DataFrame({"Source IP": df, "Environment": env_list})
    print(i_df)
    return i_df


def create_combined_csv(combined_csv, final_df):
    print("Final Dataframe")
    print(final_df.sort_values('Source IP'))
    if os.path.exists(combined_csv):
        os.remove(combined_csv)
        final_df.sort_values('Source IP').to_csv(combined_csv, index=False)


def combine_csv_source_ip(path):
    if os.path.isdir(path):
        files = glob.glob(path + "/*.csv")
        combined_csv = path + "\\Combined.csv"
        files.remove(combined_csv)
        print(files)
        final_df = pd.DataFrame()

        for file in files:
            if not file.endswith("Combined.csv"):
                print("Processing file ----------- " + file)
                i_df = read_and_modify_csv(file)
                final_df = pd.concat([final_df, i_df], ignore_index=True)

        create_combined_csv(combined_csv, final_df)
    else:
        print("Give the valid path of directory")


if __name__ == '__main__':
    csv_folder_path = input("Please enter csv folder path\n")
    combine_csv_source_ip(csv_folder_path)
