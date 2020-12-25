import pandas as pd
from xlrd import open_workbook
from xlwt import Workbook

baselocation = 'C:/Users/user1/Documents/OLAWALE/PROJECTS/PYTHON/Excel/2019/'

workbooks = [f'{baselocation}/JANUARY 2019/JANUARY 2019 NOTES.xlsx', 
f'{baselocation}/FEBRUARY 2019/FEBRUARY 2019 NOTES.xlsx',
f'{baselocation}/MARCH 2019/MARCH 2019 NOTES.xlsx',
f'{baselocation}/APRIL 2019/APRIL 2019 NOTES.xlsx',
f'{baselocation}/MAY 2019/MAY 2019 NOTES.xlsx',
f'{baselocation}/JUNE 2019/JUNE 2019 NOTES.xlsx',
f'{baselocation}/JULY 2019/JULY 2019 NOTES.xlsx',
f'{baselocation}/AUGUST 2019/AUGUST 2019 NOTES.xlsx',
f'{baselocation}/SEPTEMBER 2019/SEPTEMBER 2019 NOTES.xlsx',
f'{baselocation}/OCTOBER 2019/OCTOBER 2019 NOTES.xlsx',
f'{baselocation}/NOVEMBER 2019/NOVEMBER 2019 NOTES.xlsx',
f'{baselocation}/DECEMBER 2019/DECEMBER 2019 NOTES.xlsx']

for workbook in workbooks:
    xl = pd.ExcelFile(workbook)

    for sheet in xl.sheet_names:
        df = pd.read_excel(xl,sheet_name=sheet)
        df.to_excel(f"{workbook}{sheet}.xlsx",index=False)
        print(f"Saving... {workbook}{sheet}.xlsx")