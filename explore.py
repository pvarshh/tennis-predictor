import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv('atp_tennis.csv')
print(dataset.head())

# Check for missing values
print(dataset.isnull().sum())