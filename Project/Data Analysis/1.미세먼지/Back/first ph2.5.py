import pandas as pd
import datetime
#!pip install xlrd
#!pip install pandas
#!pip install openyxl


# 엑셀 경로 받아오는 함수(pm2.5)
def excelappend(yy, mm):
    
    # 엑셀경로
    filepath = 'C:/Users/minipojectweb/data/pm25/{}{}.xls'.format(yy, mm)
    # 엑셀불러오기"
    excel_df = pd.read_excel(filepath, header=3)

    return(excel_df)


# 데이터프레임 만드는 반복문 (pm2.5)
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


# 경로에 저장  
save_PATH = 'C:/Users/ad/Desktop/test/KOR_PH2_5.xlsx' # 저장경로
PH25DF.to_excel(save_PATH)