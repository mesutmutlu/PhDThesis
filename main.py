# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import wbgapi as wb
import pandas as pd
import openpyxl
import numpy as np


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def create_ind_library():
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
        indicators = pd.concat([indicators, pd_ind])
        print(index, value, length, indicators.shape)
    print(indicators)
    indicators.to_excel("wb_ind_list.xlsx")


def get_ind_library():
    return pd.read_excel("wb_ind_list.xlsx")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    pd.set_option('display.max_columns', 10)

    ind_lb = get_ind_library()
    #wb.db = 2
    #print(wb.data.DataFrame(['AG.AGR.TRAC.NO'], time=range(2000, 2022), skipBlanks=True,
                                #columns='series').reset_index())
    #quit()
    for db_id in ind_lb['db_id'].unique():
        wb.db = db_id.astype(int)
        try:
            ind_l = ind_lb[ind_lb['db_id'] == db_id]['Unnamed: 0'].to_list()
            a = wb.data.DataFrame(ind_l, time=range(2000, 2022), skipBlanks=True,
                        columns='series').reset_index()
            print('success db_id: ', str(db_id))
        except:
            print('error db_id: ', str(db_id))




    quit()

    pd_sdg = pd.read_excel('SDR-2022-database.xlsx', sheet_name='Backdated SDG Index')
    pd_sdg['economy'] = pd_sdg['Country Code ISO3']
    pd_sdg = pd_sdg.set_index(['economy','Year'])
    print(pd_sdg.index)
    #print(get_ind_library())
    wb.db = 2


    pd_wdi = wb.data.DataFrame(['TX.VAL.TECH.CD','BX.GSR.CCIS.CD'], time=range(2000, 2022), skipBlanks=True,
                      columns='series').reset_index()

    pd_wdi['Year'] = pd_wdi['time'].str[2:].astype(int)
    pd_wdi = pd_wdi.set_index(['economy','Year']).drop(columns=['time'])
    print(pd_wdi.index)

    print(pd.concat([pd_sdg, pd_wdi],axis=1).to_excel("test.xlsx"))
    #print(pd_wdi.join(pd_sdg))

    quit()
    print(wb.data.DataFrame(['TX.VAL.TECH.CD','BX.GSR.CCIS.CD'], time=range(2000, 2020), skipBlanks=True, columns='series').reset_index())