import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn import model_selection, metrics
from sklearn import preprocessing
from sklearn.utils import shuffle
from sklearn.preprocessing import StandardScaler

# read .csv files from dataset
csv_a1r = "./Dataset/a1_raw.csv"
csv_a1v = "./Dataset/a1_va3.csv"
csv_a2r = "./Dataset/a2_raw.csv"
csv_a2v = "./Dataset/a2_va3.csv"
csv_a3r = "./Dataset/a3_raw.csv"
csv_a3v = "./Dataset/a3_va3.csv"
csv_b1r = "./Dataset/b1_raw.csv"
csv_b1v = "./Dataset/b1_va3.csv"
csv_b3r = "./Dataset/b3_raw.csv"
csv_b3v = "./Dataset/b3_va3.csv"
csv_c1r = "./Dataset/c1_raw.csv"
csv_c1v = "./Dataset/c1_va3.csv"
csv_c3r = "./Dataset/c3_raw.csv"
csv_c3v = "./Dataset/c3_va3.csv"

# create dataframes for .csv files
df_a1r = pd.read_csv(csv_a1r)
df_a1v = pd.read_csv(csv_a1v)
df_a2r = pd.read_csv(csv_a2r)
df_a2v = pd.read_csv(csv_a2v)
df_a3r = pd.read_csv(csv_a3r)
df_a3v = pd.read_csv(csv_a3v)
df_b1r = pd.read_csv(csv_b1r)
df_b1v = pd.read_csv(csv_b1v)
df_b3r = pd.read_csv(csv_b3r)
df_b3v = pd.read_csv(csv_b3v)
df_c1r = pd.read_csv(csv_c1r)
df_c1v = pd.read_csv(csv_c1v)
df_c3r = pd.read_csv(csv_c3r)
df_c3v = pd.read_csv(csv_c3v)

# unprocessed files have timestamp and phase labels
# they are not mandatory to us, so we should remove these two labels
df_a1r.drop('timestamp', axis=1, inplace=True)
df_a1r.drop('phase', axis=1, inplace=True)
df_a2r.drop('timestamp', axis=1, inplace=True)
df_a2r.drop('phase', axis=1, inplace=True)
df_a3r.drop('timestamp', axis=1, inplace=True)
df_a3r.drop('phase', axis=1, inplace=True)
df_b1r.drop('timestamp', axis=1, inplace=True)
df_b1r.drop('phase', axis=1, inplace=True)
df_b3r.drop('timestamp', axis=1, inplace=True)
df_b3r.drop('phase', axis=1, inplace=True)
df_c1r.drop('timestamp', axis=1, inplace=True)
df_c1r.drop('phase', axis=1, inplace=True)
df_c3r.drop('timestamp', axis=1, inplace=True)
df_c3r.drop('phase', axis=1, inplace=True)

