"""
use merge.py to merge all .csv files together into one
- add two more columns
    - match id (1 - 53571)
    - year (2000, 2001 ... 2017)
"""

import pandas as pd
import numpy as np

df = pd.DataFrame()
for i in range(2000, 2018):
    tmp = pd.read_csv(f"./archive/atp_matches_{i}.csv")
    tmp['year'] = i
    tm
    df = pd.concat([df, tmp], ignore_index=True)
    
    
df['match_id'] = np.arange(0, df.shape[0])
print(df.head())

