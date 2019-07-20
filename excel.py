import pandas as pd 
import glob
import os

directory = glob.glob("/Users/elangreen/Documents/ConstructAct/ExcelToSql/*.xlsx")
print(directory)

for file in directory:
  df = pd.read_excel(file)
  print(df)