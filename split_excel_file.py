import pandas as pd
from xlrd import open_workbook
from xlwt import Workbook

xl = pd.ExcelFile('C:/Users/user1/Documents/OLAWALE/LEARN/PYTHON/Internet Tuts/combined.xlsx')


for sheet in xl.sheet_names:
    df = pd.read_excel(xl,sheet_name=sheet)
    df.to_excel(f"{sheet}.xls",index=False)