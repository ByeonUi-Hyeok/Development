import pandas as pd
import datetime
RENAME_ALL = {
    '서울':'SEOUL', '부산':'PUSAN', '대구':'DEAGU', '인천':'INCHEON', '광주':'KWANG_JU', '대전':'DAEJEON',
    '울산':'ULSAN', '경기':'KYEONG_GI', '강원':'KANGONE', '충북':'CHUNG_BUK', '충남':'CHUNG_NAM', '전북':'JEON_BUK',
    '전남':'JEON_NAM', '경북':'KYUNG_BUK','경남':'KYUNG_NAM','제주':'JE_JU','세종':'SEJONG'}


# pm2.5-----------------------------------------------------------------------------
def excelappend(yy, mm):
    filepath = 'C:/Users/minipojectweb/data/pm25/{}{}.xls'.format(yy, mm)
    excel_df = pd.read_excel(filepath, header=3)
    return(excel_df)
CURRENTTIME = datetime.datetime.today()
CURRENTTIME = int(CURRENTTIME.strftime('%m'))
PH25DF      = pd.DataFrame()
for yy in [2020, 2021]:
    for mm in range (1, 13):
        if yy == 2020 and mm < 4 or yy == 2021 and mm > CURRENTTIME :
            print(f'{yy}{str(mm).zfill(2)} fail')
        else:    
            temp = excelappend(str(yy), str(mm).zfill(2))
            PH25DF = PH25DF.append(temp, ignore_index=True)
            print(f'{yy}{str(mm).zfill(2)} success')
PH25DF.sort_values( by = '날짜', ascending=False, inplace=True)
save_PATH = 'C:/Users/ad/Desktop/test/tot/KOR_PH2_5' # 저장경로
PH25DF.to_excel(save_PATH + '.xlsx', index=False)
PH25DF.to_csv(save_PATH + '.csv', index=False, encoding='utf-8-sig')
PH25DF_I = PH25DF.rename(RENAME_ALL, axis='columns')

# pm10-----------------------------------------------------------------------------
def excelappendph10(yy, mm):
    filepath = 'C:/Users/minipojectweb/data/pm10/{}{}.xls'.format(yy, mm)
    excel_df = pd.read_excel(filepath, header=3)
    return(excel_df)
CURRENTTIME = datetime.datetime.today()
CURRENTTIME = int(CURRENTTIME.strftime('%m'))
PH10DF      = pd.DataFrame()
for yy in [2020, 2021]:
    for mm in range (1, 13):
        if yy == 2020 and mm < 4 or yy == 2021 and mm > CURRENTTIME :
            print(f'{yy}{str(mm).zfill(2)} fail')
        else:    
            temp = excelappendph10(str(yy), str(mm).zfill(2))
            PH10DF = PH10DF.append(temp, ignore_index=True)
            print(f'{yy}{str(mm).zfill(2)} success')
PH10DF.sort_values( by = '날짜', ascending=False, inplace=True)
save_PATH = 'C:/Users/ad/Desktop/test/tot/KOR_PH10' # 저장경로
PH10DF.to_excel(save_PATH + '.xlsx', index=False)
PH10DF.to_csv(save_PATH + '.csv', index=False, encoding='utf-8-sig')
PH10DF_I = PH10DF.rename(RENAME_ALL, axis='columns')

# o3오존-----------------------------------------------------------------------------
def excelappendpho3(yy, mm):
    filepath = 'C:/Users/minipojectweb/data/o3/{}{}.xls'.format(yy, mm)
    excel_df = pd.read_excel(filepath, header=3)
    return(excel_df)
CURRENTTIME = datetime.datetime.today()
CURRENTTIME = int(CURRENTTIME.strftime('%m'))
O3DF        = pd.DataFrame()
for yy in [2020, 2021]:
    for mm in range (1, 13):
        if yy == 2020 and mm < 4 or yy == 2021 and mm > CURRENTTIME :
            print(f'{yy}{str(mm).zfill(2)} fail')
        else:    
            temp = excelappendpho3(str(yy), str(mm).zfill(2))
            O3DF = O3DF.append(temp, ignore_index=True)
            print(f'{yy}{str(mm).zfill(2)} success')
O3DF.sort_values( by = '날짜', ascending=False, inplace=True)
save_PATH = 'C:/Users/ad/Desktop/test/tot/KOR_O3' # 저장경로
O3DF.to_excel(save_PATH + '.xlsx', index=False)
O3DF.to_csv(save_PATH + '.csv', index=False, encoding='utf-8-sig')
O3DF_I = O3DF.rename(RENAME_ALL, axis='columns')

# so2아황산가스-----------------------------------------------------------------------------
def excelappendso2(yy, mm):
    filepath = 'C:/Users/minipojectweb/data/so2/{}{}.xls'.format(yy, mm)
    excel_df = pd.read_excel(filepath, header=3)
    return(excel_df)
CURRENTTIME = datetime.datetime.today()
CURRENTTIME = int(CURRENTTIME.strftime('%m'))
SO2DF      = pd.DataFrame()
for yy in [2020, 2021]:
    for mm in range (1, 13):
        if yy == 2020 and mm < 4 or yy == 2021 and mm > CURRENTTIME :
            print(f'{yy}{str(mm).zfill(2)} fail')
        else:    
            temp = excelappendso2(str(yy), str(mm).zfill(2))
            SO2DF = SO2DF.append(temp, ignore_index=True)
            print(f'{yy}{str(mm).zfill(2)} success')
SO2DF.sort_values( by = '날짜', ascending=False, inplace=True)
save_PATH = 'C:/Users/ad/Desktop/test/tot/KOR_SO2' # 저장경로
SO2DF.to_excel(save_PATH + '.xlsx', index=False)
SO2DF.to_csv(save_PATH + '.csv', index=False, encoding='utf-8-sig')
SO2DF_I = SO2DF.rename(RENAME_ALL, axis='columns')

#일산화탄소co---------------------
def excelappendCO(yy, mm):
    filepath = 'C:/Users/minipojectweb/data/co/{}{}.xls'.format(yy, mm)
    excel_df = pd.read_excel(filepath, header=3)
    return(excel_df)
CURRENTTIME = datetime.datetime.today()
CURRENTTIME = int(CURRENTTIME.strftime('%m'))
CODF      = pd.DataFrame()
for yy in [2020, 2021]:
    for mm in range (1, 13):
        if yy == 2020 and mm < 4 or yy == 2021 and mm > CURRENTTIME :
            print(f'{yy}{str(mm).zfill(2)} fail')
        else:    
            temp = excelappendCO(str(yy), str(mm).zfill(2))
            CODF = CODF.append(temp, ignore_index=True)
            print(f'{yy}{str(mm).zfill(2)} success')
CODF.sort_values( by = '날짜', ascending=False, inplace=True)
save_PATH = 'C:/Users/ad/Desktop/test/tot/KOR_CO' # 저장경로
CODF.to_excel(save_PATH + '.xlsx', index=False)
CODF.to_csv(save_PATH + '.csv', index=False, encoding='utf-8-sig')
CODF_I = CODF.rename(RENAME_ALL, axis='columns')

#일산화질소NO2---------------------
def excelappendNO2(yy, mm):
    filepath = 'C:/Users/minipojectweb/data/no2/{}{}.xls'.format(yy, mm)
    excel_df = pd.read_excel(filepath, header=3)
    return(excel_df)
CURRENTTIME = datetime.datetime.today()
CURRENTTIME = int(CURRENTTIME.strftime('%m'))
NO2DF      = pd.DataFrame()
for yy in [2020, 2021]:
    for mm in range (1, 13):
        if yy == 2020 and mm < 4 or yy == 2021 and mm > CURRENTTIME :
            print(f'{yy}{str(mm).zfill(2)} fail')
        else:    
            temp = excelappendNO2(str(yy), str(mm).zfill(2))
            NO2DF = NO2DF.append(temp, ignore_index=True)
            print(f'{yy}{str(mm).zfill(2)} success')
NO2DF.sort_values( by = '날짜', ascending=False, inplace=True)
save_PATH = 'C:/Users/ad/Desktop/test/tot/KOR_NO2' # 저장경로
NO2DF.to_excel(save_PATH + '.xlsx', index=False)
NO2DF.to_csv(save_PATH + '.csv', index=False, encoding='utf-8-sig')
NO2DF_I = NO2DF.rename(RENAME_ALL, axis='columns')



for city in PH10DF_I.columns[1:]:
    globals()[f'{city}_df0'] = PH10DF_I[ [ '날짜',city ] ].rename({ city:'PH10'}, axis='columns')
    # print(city)
    # print(globals()[f'{city}_df0'])
for city in PH25DF_I.columns[1:]:
    globals()[f'{city}_df1'] = PH25DF_I[ [ '날짜',city ] ].rename({ city:'PH2.5'}, axis='columns')
    globals()[f'{city}_df1'] = pd.merge(left = globals()[f'{city}_df0'], right = globals()[f'{city}_df1'], how = 'left', left_on ='날짜', right_on='날짜')
    # print(city)
    # print(globals()[f'{city}_df1'])
for city in O3DF_I.columns[1:]:
    globals()[f'{city}_df2'] = O3DF_I[ [ '날짜',city ] ].rename({ city:'O3'}, axis='columns')
    globals()[f'{city}_df2'] = pd.merge(left = globals()[f'{city}_df1'], right = globals()[f'{city}_df2'], how = 'left', left_on ='날짜', right_on='날짜')
    # print(city)
    # print(globals()[f'{city}_df2'])
for city in NO2DF_I.columns[1:]:
    globals()[f'{city}_df3'] = NO2DF_I[ [ '날짜',city ] ].rename({ city:'NO2'}, axis='columns')
    globals()[f'{city}_df3'] = pd.merge(left = globals()[f'{city}_df2'], right = globals()[f'{city}_df3'], how = 'left', left_on ='날짜', right_on='날짜')
    # print(city)
    # print(globals()[f'{city}_df3'])
for city in CODF_I.columns[1:]:
    globals()[f'{city}_df4'] = CODF_I[ [ '날짜',city ] ].rename({ city:'CO'}, axis='columns')
    globals()[f'{city}_df4'] = pd.merge(left = globals()[f'{city}_df3'], right = globals()[f'{city}_df4'], how = 'left', left_on ='날짜', right_on='날짜')
    # print(city)
    # print(globals()[f'{city}_df4'])
for city in SO2DF_I.columns[1:]:
    globals()[f'{city}_df5'] = SO2DF_I[ [ '날짜',city ] ].rename({ city:'SO2'}, axis='columns')
    globals()[f'{city}_df5'] = pd.merge(left = globals()[f'{city}_df4'], right = globals()[f'{city}_df5'], how = 'left', left_on ='날짜', right_on='날짜')
    print(city)
    print(globals()[f'{city}_df5'])
    
    globals()[f'{city}_df5'].sort_values( by = '날짜', ascending=False, inplace=True)

    pppath    = f'{city}_df5'
    save_PATH = f'C:/Users/ad/Desktop/test/{pppath}'
    globals()[f'{city}_df5'].to_excel(save_PATH + '.xlsx', index=False)
    globals()[f'{city}_df5'].to_csv(save_PATH + '.csv', index=False, encoding='utf-8-sig')

JE_JU_df5 = JE_JU_df5.fillna(method='pad')
JE_JU_df5.to_excel(save_PATH + '.xlsx', index=False)
JE_JU_df5.to_csv(save_PATH + '.csv', index=False, encoding='utf-8-sig')
