#!/usr/bin/env python
# coding: utf-8

# %%
import pandas as pd
import seaborn as sns

# fetch csv from https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv
# %%
df = pd.read_csv(
    'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv')

# %%
df.head()

# %%
df.info()

# %%
