import tabula
from tabula import read_pdf
import pandas as pd
import os
import numpy as np

def extract_data (pdf):
    data = tabula.read_pdf_with_template(pdf, template_path = 'layout1.json')
    global df_1
    df_1 = pd.DataFrame(data[0])
    df_1.loc[5,'Category'] = 'Securities Lending Utility Ratio'
    df_1.rename(columns = {'Category':'Category','Exchange Traded Fund': 'Fund_info'}, inplace = True)
    df_1.loc[9,'Fund_info'] = df_1.loc[9,'Fund_info'] + df_1.loc[10,'Fund_info']
    df_1.drop([6,10], inplace = True)
    df_1.reset_index(drop = True)
    fund_info = pd.concat([df_1, sort_dfs(data[2]),sort_dfs(data[3]),sort_dfs(data[4])], ignore_index = True)
    return fund_info

def sort_dfs (data):
    global df_1
    df = pd.DataFrame(data)
    df.loc[-1] = df.columns
    df.index = df.index + 1
    df.sort_index(inplace = True)
    df.rename(columns = {df.columns[0] : df_1.columns[0], df.columns[1] : df_1.columns[1]}, inplace = True)
    return df   

fund_info = pd.DataFrame()
for file in os.listdir(os.getcwd()):
    if '.pdf' in (os.path.basename(file)):
        try:
            temp_df = pd.DataFrame(extract_data(file)['Fund_info'])
            fund_info = pd.concat([fund_info,temp_df],axis = 1)
        except:
            pass
fund_info.insert(loc=0,column = 'Description', value = extract_data('STX40.pdf')['Category'])
fund_info.loc[[16,17],'Description'] = ['Highest Annual %','Lowest Annual %']
fund_info.columns = list(fund_info.loc[0])
fund_info.drop(0, inplace = True)
fund_info.reset_index(drop = True, inplace = True)
for i in [3,5,6]:
    fund_info.iloc[19,i] = np.nan
    fund_info.iloc[19:,i] = fund_info.iloc[19:,i].shift(-1)
fund_info.iloc[5,3] = '11 August 2021'
fund_info.iloc[7,3] = fund_info.iloc[7,3] + fund_info.iloc[8,3]
fund_info.iloc[8,3] = fund_info.iloc[9,3]
fund_info.iloc[9,3] = fund_info.iloc[11,3]
fund_info.iloc[11,3] = np.nan
fund_info.iloc[11:16,3] = fund_info.iloc[11:16,3].shift(-1)
fund_info.iloc[17,3] = 1.67
fund_info.iloc[17,3] = 98.33
fund_info.iloc[7,4] = 'Sept 2021: n/a'
fund_info.iloc[14,4] = np.nan
fund_info.iloc[8:15,4] = fund_info.iloc[8:15,4].shift(1)
fund_info.iloc[16:,4] = fund_info.iloc[16:,4].shift(1)
fund_info.iloc[8,4]  = 'South African – Equity – General'
fund_info.drop(fund_info.index[-1], inplace = True)
fund_info = fund_info.replace(['n/a', 'N/A'],np.nan)
fund_info.to_csv('fund_info.csv', index = False)