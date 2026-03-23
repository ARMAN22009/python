import numpy as np

a=np.array([2,3,5,8,np.nan,55])                                    # np.nan

print(np.isnan(a))                  # boolean indexing to find missing values by using ----np.isnan
# [False False False False  True False]

print(~np.isnan(a))
# [ True  True  True  True False  True]


# nan and none are different , nan is used only for missing numbers