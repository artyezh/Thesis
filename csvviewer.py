import numpy as np

import matplotlib

import matplotlib.pyplot as plt

import matplotlib.patches as mpatches

import pandas as pd

import sklearn

from sklearn import neighbors # how methods are imported

from sklearn import metrics


Data = pd.read_csv('./datasets/Dataset.csv')
Al = pd.read_csv('./datasets/Alcohol_Percentages_Dataset.csv')

Type = pd.read_csv('./datasets/Type_Dataset.csv')
print(Al.tail())
print(Data.tail())
print(Type.tail())