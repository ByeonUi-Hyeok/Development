from numpy import append
import pandas as pd
import datetime

def excelappend(aa, yy, mm):
    '''
    aa = 파일경로
    yy = 년도 4자리(ex: 2020)
    mm = 월 2자리 (ex : 01, 11, 12)
    '''
    filepath = f'C:/Users/minipojectweb/data/{aa}/{yy}{mm}.xls'
    excel_df = pd.read_excel(filepath, header=3)
    print (filepath)
    return(excel_df)
def appendname(aa):
    '''
    aa는 excelappend의 aa (파일 경로를 뜻함)
    '''
    RENAME_ALL = {
    '서울':'SEOUL', '부산':'PUSAN', '대구':'DEAGU', '인천':'INCHEON', '광주':'KWANG_JU', '대전':'DAEJEON',
    '울산':'ULSAN', '경기':'KYEONG_GI', '강원':'KANGONE', '충북':'CHUNG_BUK', '충남':'CHUNG_NAM', '전북':'JEON_BUK',
    '전남':'JEON_NAM', '경북':'KYUNG_BUK','경남':'KYUNG_NAM','제주':'JE_JU','세종':'SEJONG'}
    
    CURRENTTIME = datetime.datetime.today()           # 오늘 날짜 / 시간 /초
    CURRENTTIME = int(CURRENTTIME.strftime('%m'))     # 오늘 날짜의 월을 추출
    globals()[f'{aa}DF'] = pd.DataFrame()
    for yy in [2020, 2021]:                                                   # 2020 ~ 2021
        for mm in range (1, 13):                                              # 1 ~ 12
            if yy == 2020 and mm < 4 or yy == 2021 and mm > CURRENTTIME :     # 2020 1~3월/ 2021 현재월보다 크면 제외
                print(f'{yy}{str(mm).zfill(2)} fail')                         # zfill 문자열의 빈칸을 0으로 채워줌
            else:    
                temp = excelappend(aa, str(yy), str(mm).zfill(2))
                globals()[f'{aa}DF'] = globals()[f'{aa}DF'].append(temp, ignore_index=True)
                print(f'{aa} {yy}{str(mm).zfill(2)} success')

    globals()[f'{aa}DF'].sort_values( by = '날짜', ascending=False, inplace=True)
    save_PATH = f'C:/Users/ad/Desktop/test/tot/KOR_{aa}' # 저장경로
    globals()[f'{aa}DF'].to_excel(save_PATH + '.xlsx', index=False)
    globals()[f'{aa}DF'].to_csv(save_PATH + '.csv', index=False, encoding='utf-8-sig')
    globals()[f'{aa}DF_I'] = globals()[f'{aa}DF'].rename(RENAME_ALL, axis='columns')

for i in ['pm10', 'pm25', 'co', 'no2', 'o3', 'so2']:
    appendname(i)

def cutcity(what):
    for city in globals()[f'{what}DF_I'].columns[1:]:
        globals()[f'{what}{city}DF_II'] = globals()[f'{what}DF_I'][ [ '날짜',city ] ].rename({ city: what}, axis='columns')

append_list = ['pm10', 'pm25', 'co', 'no2', 'o3', 'so2']
for i in append_list:
    cutcity(i)

def mergecity(what, afterwhat):
    for city in globals()[f'{what}DF_I'].columns[1:]:
        globals()[f'{what}{city}DF_II'] = pd.merge(left = globals()[f'{what}{city}DF_II'], right = globals()[f'{afterwhat}{city}DF_II'], how = 'left', left_on ='날짜', right_on='날짜')
        globals()[f'{what}{city}DF_II'].drop_duplicates() # 중복 행제거 모든열기준
        globals()[f'{what}{city}DF_II'].sort_values( by = '날짜', ascending=False, inplace=True)
        pppath    = f'{city}_FIN'
        save_PATH = f'C:/Users/ad/Desktop/test/{pppath}'
        globals()[f'{what}{city}DF_II'].to_excel(save_PATH + '.xlsx', index=False)
        globals()[f'{what}{city}DF_II'].to_csv(save_PATH + '.csv', index=False, encoding='utf-8-sig')

append_list = ['pm25', 'co', 'no2', 'o3', 'so2']
for what in ['pm10']:
    pass
    for afterwhat in append_list:
        mergecity(what, afterwhat) 

# pm10CHUNG_NAMDF_II


# 기상불러오기
def excelappend2(a):
    filepath = f'C:/Users/minipojectweb/data/weather/{a}.xlsx'
    excel_df = pd.read_excel(filepath, usecols='B:F' ,header=0)
    excel_df.sort_values( by = '날짜', ascending=False, inplace=True)
    #excel_df.set_index('날짜', inplace=True)
    print (filepath)
    return(excel_df)

 # 기상불러오기 함수 호출

for i in pm10DF_I.columns[1:]:
    globals()[f'{i}WDF'] =   excelappend2(i)
    globals()[f'{i}WDF'] =   globals()[f'{i}WDF'].drop(index=range(0,91), axis=0,)
    globals()[f'{i}WDF'].reset_index(drop=True, inplace=True)
    ####globals()[f'{i}WDF']['날짜'] = globals()[f'{i}WDF']['날짜'].dt.date
    globals()[f'{i}WDF'].날짜=globals()[f'{i}WDF'].날짜.astype(str)

def mergeWcity(what):
     for wcity in pm10DF_I.columns[1:]:
         if what == wcity :
            print(what, wcity)
            globals()[f'{what}WFIN'] = pd.merge(
                left = globals()[f'pm10{what}DF_II'], right = globals()[f'{wcity}WDF'], how = 'left', left_on ='날짜',
                    right_on='날짜')

            globals()[f'{what}WFIN'].drop_duplicates() # 중복 행제거 모든열기준
            globals()[f'{what}WFIN'].sort_values( by = '날짜', ascending=False, inplace=True)
            pppath    = f'{what}FIN'
            save_PATH = f'C:/Users/ad/Desktop/test/fin/{pppath}'
            globals()[f'{what}WFIN'].to_excel(save_PATH + '.xlsx', index=False)
            globals()[f'{what}WFIN'].to_csv(save_PATH + '.csv', index=False, encoding='utf-8-sig')
     # 결측치 제거      
     for i in pm10DF_I.columns[1:]:
        globals()[f'{i}WFIN'].fillna({'일강수량(mm)': 0.0}, inplace=True)
        globals()[f'{i}WFIN']['평균기온(°C)'].ffill(inplace=True)
        globals()[f'{i}WFIN']['평균 풍속(m/s)'].ffill(inplace=True)
        globals()[f'{i}WFIN']['평균 상대습도(%)'].bfill(inplace=True)

        globals()[f'{i}WFIN'].drop_duplicates() # 중복 행제거 모든열기준
        globals()[f'{i}WFIN'].sort_values( by = '날짜', ascending=False, inplace=True)
     for  i in pm10DF_I.columns[1:]:
        globals()[f'{i}WFIN'].fillna({'일강수량(mm)': 0.0}, inplace=True)
        globals()[f'{i}WFIN']['평균기온(°C)'].ffill(inplace=True)
        globals()[f'{i}WFIN']['평균기온(°C)'].bfill(inplace=True)
        globals()[f'{i}WFIN']['평균 풍속(m/s)'].ffill(inplace=True)
        globals()[f'{i}WFIN']['평균 풍속(m/s)'].bfill(inplace=True)
        globals()[f'{i}WFIN']['평균 상대습도(%)'].ffill(inplace=True)
        globals()[f'{i}WFIN']['평균 상대습도(%)'].bfill(inplace=True)                   
        pppath    = f'{i}FIN'
        save_PATH = f'C:/Users/ad/Desktop/test/fin/{pppath}'
        globals()[f'{i}WFIN'].to_excel(save_PATH + '.xlsx', index=False)
        globals()[f'{i}WFIN'].to_csv(save_PATH + '.csv', index=False, encoding='utf-8-sig')

for i in pm10DF_I.columns[1:]:
    mergeWcity(i)


print(pm10DF_I.columns[1:])
if __name__ == '__main__':   
    main()