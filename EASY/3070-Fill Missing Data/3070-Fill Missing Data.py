// Problem: Fill Missing Data
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/fill-missing-data/
// Date: 2024-09-29

import pandas as pd

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    c=0
    for i in products["quantity"]:
        if pd.isna(i):
            products.at[c,"quantity"]=0
        c+=1
    return products