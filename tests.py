import unittest
import os
from main import *

test_csv_folder = "D:\collabera_assignment_for_atos\Engineering Test Risk Analytics\Testing Engineering Test Files"

test_csv_file = test_csv_folder + "\\NA Prod.csv"


class CSVTestCase(unittest.TestCase):
    def test_csv_folder_is_exist(self):
        self.assertTrue(os.path.exists(test_csv_folder), "Directory for CSV files is exist.")

    def test_csv_folder_is_dir(self):
        self.assertTrue(os.path.isdir(test_csv_folder), "Given path is directory path")

    def test_csv_folder_contains_files(self):
        self.assertTrue(os.listdir(test_csv_folder), "Directory is not empty")

    def test_read_and_modify_csv(self):
        print("---------Test CSV READ-------------")
        df = pd.read_csv(test_csv_file, usecols=["Source IP"])
        df = df["Source IP"].unique()
        env = os.path.basename(test_csv_file).split(".")[0]
        env_list = []
        env_list.extend(repeat(env, len(df)))
        i_df = pd.DataFrame({"Source IP": df, "Environment": env_list})

        expected_df = read_and_modify_csv(test_csv_file)
        self.assertEqual(type(expected_df), type(i_df))
        self.assertEqual(True, expected_df.equals(i_df), "Results are as expected")


if __name__ == '__main__':
    unittest.main()
