import csv
import glob
import os
import shutil


PATH = r'D:\Scripts\school_project\data'
allFiles = glob.glob(PATH + "/*.csv")

#print(os.path.exists('D:\Scripts\school_project\data'))


merged_data = 'merged_out.csv'

with open(merged_data, 'wb') as outfile:
    for i, fname in enumerate(allFiles):
        with open(fname, 'rb') as infile:
            if i != 0:
                infile.readline()
            shutil.copyfileobj(infile, outfile)
            print(fname + " has been imported.")