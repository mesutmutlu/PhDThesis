# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import wbgapi as wb
import pandas as pd
import openpyxl

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.je
# tbrains.com/help/pycharm/

indicators = pd.DataFrame()

for index, value in wb.source.Series().items():
    wb.db = index
    length = len(wb.series.Series())
    list_of_db_i = [index] * length
    list_of_db_v = [value] * length
    pd_ind = pd.DataFrame()
    pd_ind['db_id'] = list_of_db_i
    pd_ind['db_name'] = list_of_db_v
    pd_ind.index = wb.series.Series().index
    pd_ind['description'] = wb.series.Series().to_list()
    indicators = pd.concat([indicators,pd_ind])
    print(index, value, length, indicators.shape)
print(indicators)
indicators.to_excel("wb_ind_list.xlsx")

quit()
print(wb.economy.info(['CAN', 'USA', 'MEX']) )
quit()
wb.db = 69
print(wb.series.info())