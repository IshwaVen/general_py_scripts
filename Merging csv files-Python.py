## Python - Merging all the csv files in a folder

## importing necessary python packages
import glob
import os
import pandas as pd

### method 1 - to access the files from the folder
## combines directory and file path names into one complete path with all the files name starting with '2023-05-' (regex)
cwd = os.path.join("D:\\CBM_POC\\30May2023_NewNew V-cutter-Accelerometer\\', "2023-05-*.csv")  

## returns list of files or folders that matches the specified path 
cwd = glob.glob(cwd)

### method 2 - to access the files from the folder

# cwd = glob.glob(os.path.join("D:\\CBM_POC\\30May2023_NewNew V-cutter-Accelerometer\\", "2023-05-*.csv"))

## Applying map function to read and concat the files and saving to a dataframe
df = pd.concat(map(pd.read_csv, cwd), ignore_index=True)

## Saving the concatenated file to a specific directory in csv file
df.to_csv("D:\\CBM_POC\\30May2023_NewNew V-cutter-Accelerometer\\merged_file.csv")

