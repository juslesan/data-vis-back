import pandas as pd 
import numpy as np
import csv
import os
import json

def read_data(data_dir="data/"):
    data = {}
    for subdir, dirs, files in os.walk(data_dir):
        dirs.sort()
        files.sort()
        for filename in files:
            if filename.endswith(".csv"):
                df = pd.read_csv(subdir + os.sep + filename, index_col=0, skiprows=3)
                name = df["Indicator Name"][0]
                data[name] = json.loads(df.drop(columns=["Country Code","Indicator Name","Indicator Code"])
                                    .dropna(axis=1, how='all')
                                    .dropna(axis=0, how='all')
                                    .to_json(orient="index"))

                
    return data
