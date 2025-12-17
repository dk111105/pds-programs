# -*- coding: utf-8 -*-
"""
Created on Tue Dec 16 11:52:04 2025

@author: 23csc11
"""

import pandas as pd

diamond = pd.read_csv("Diamonds.csv")
print(diamond)

print("Count of each diamond cut type:\n",diamond.groupby("cut")["x"].count())

vs1_diamonds = diamond[diamond['clarity'] == 'VS1']
sorted_vs1_diamonds = vs1_diamonds.sort_values(by='depth', ascending=True)
print("\nDetails for the diamonds in sorted order of their depth for the clarity type VS1:\n",sorted_vs1_diamonds)

carat = diamond[diamond['carat'] >= 0.5]
sorted_carat = carat.sort_values(by="price", ascending=False)
print("\nDiamonds with carat greater than 0.5 along with their prices in descending order:\n",sorted_carat)

mean = diamond["price"].mean()
below_mean = diamond[diamond["price"] > mean]
print("\nDetails of diamonds with below average price:\n",below_mean)

