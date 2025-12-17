# -*- coding: utf-8 -*-
"""
Created on Tue Dec 16 12:54:11 2025

@author: 23csc11
"""

import pandas as pd
planets = pd.read_csv("Planets.csv")
print(planets)

print(planets.groupby("method")["year"].max())

