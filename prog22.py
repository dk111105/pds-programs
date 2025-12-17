# -*- coding: utf-8 -*-
"""
Created on Tue Dec 16 12:30:01 2025

@author: 23csc11
"""

import pandas as pd
company_sales = pd.read_csv("company_sales.csv")
print(company_sales)

month1 = company_sales["bathingsoap"].idxmax()
month2 = company_sales["moisturizer"].idxmin()

print(company_sales.iloc[month1], "\n\n", company_sales.iloc[month2])

print("\nTotal sale of all products of all months:",company_sales["total_profit"].sum())