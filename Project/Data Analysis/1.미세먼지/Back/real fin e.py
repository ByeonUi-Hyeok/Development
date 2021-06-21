from numpy import append
import pandas as pd
import datetime
#from .realfin import excelappend, appendname, cutcity, mergecity
import realfin
append_list = ['pm10', 'pm25', 'co', 'no2', 'o3', 'so2']

for i in append_list:
    realfin.appendname(i)


for i in append_list:
    realfin.cutcity(i)

for what in ['pm10']:
    pass
    for afterwhat in ['pm25', 'co', 'no2', 'o3', 'so2']:
        realfin.mergecity(what, afterwhat) 


columnsss = ['SEOUL', 'PUSAN', 'DEAGU', 'INCHEON', 'KWANG_JU', 'DAEJEON', 'ULSAN',
       'KYEONG_GI', 'KANGONE', 'CHUNG_BUK', 'CHUNG_NAM', 'JEON_BUK',
       'JEON_NAM', 'KYUNG_BUK', 'KYUNG_NAM', 'JE_JU', 'SEJONG']
for i in columnsss :
    globals()[f'{i}WDF'] =   realfin.excelappend2(i)
    globals()[f'{i}WDF'] =   globals()[f'{i}WDF'].drop(index=range(0,91), axis=0,)
    globals()[f'{i}WDF'].reset_index(drop=True, inplace=True)
    ####globals()[f'{i}WDF']['날짜'] = globals()[f'{i}WDF']['날짜'].dt.date
    globals()[f'{i}WDF'].날짜=globals()[f'{i}WDF'].날짜.astype(str)

for i in columnsss:
    realfin.mergeWcity(i)

#print(pm10CHUNG_NAMDF_II)
