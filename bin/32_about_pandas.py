"""
About pandas
- pandas is library
- Inside pandas, we have
    -- Many functions
    -- Many classes
- Main class is 'DataFrame'


About 'DataFrame' class
- 'DataFrame' class is written for tabular data processing, csv, xlsx, db etc
 """
print("Inside pandas library")
print("-"*20)
# ------------

import pandas as pd
print(dir(pd))

print("#"*40, end="\n\n")
#################################

print("Inside DataFrame class")
print("-"*20)
# ------------

import pandas as pd
print(dir(pd.DataFrame))

print("#"*40, end="\n\n")
#################################

print('DataFrame class example -1')
print("Store the values")
print("-"*20)
# ------------

my_df = pd.DataFrame([[10, 20, 30, 40], [50, 60, 70, 80]])
print(my_df)

print("#"*40, end="\n\n")
#################################


print('DataFrame class example -2')
print("Store the values")
print("-"*20)
# ------------

my_df = pd.DataFrame([[10, 20, 30, 40], [50, 60, 70, 80]], index=["r1", "r2"], columns=["c1", "c2", "c3", "c4"])
print(my_df)

print("#"*40, end="\n\n")
#################################