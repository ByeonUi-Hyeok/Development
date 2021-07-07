# pip install xlrd
from leaning import anticipate, finalopen
# 3분 정도 걸림 다 돌리는데

columns = ['SEOUL', 'PUSAN', 'DEAGU', 'INCHEON', 'KWANG_JU', 'DAEJEON', 'ULSAN',
       'KYEONG_GI', 'KANGONE', 'CHUNG_BUK', 'CHUNG_NAM', 'JEON_BUK',
       'JEON_NAM', 'KYUNG_BUK', 'KYUNG_NAM', 'JE_JU', 'SEJONG']

for column in columns:
    globals()[f'{column}'] = finalopen(column)
    anticipate(globals()[f'{column}'], 'PM10', column)
    anticipate(globals()[f'{column}'], 'PM2.5', column)
    anticipate(globals()[f'{column}'], 'PRECIPITATION', column)
    anticipate(globals()[f'{column}'], 'WIND SPEED', column)
    anticipate(globals()[f'{column}'], 'RELATIVE HUMIDITY', column)
    anticipate(globals()[f'{column}'], 'CENTIGRADE', column)