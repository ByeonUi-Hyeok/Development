import pandas as pd
from fbprophet import Prophet # conda install -c conda-forge fbprophet -> pip install --upgrade plotly

columns = ['SEOUL', 'PUSAN', 'DEAGU', 'INCHEON', 'KWANG_JU', 'DAEJEON', 'ULSAN',
       'KYEONG_GI', 'KANGONE', 'CHUNG_BUK', 'CHUNG_NAM', 'JEON_BUK',
       'JEON_NAM', 'KYUNG_BUK', 'KYUNG_NAM', 'JE_JU', 'SEJONG']

def anticipate(dataframe, data, name):  
    dic = {'ds':dataframe.DATE,
    'y':dataframe[data]}
    df = pd.DataFrame(dic)
    df.reset_index(inplace=False)
    model = Prophet( daily_seasonality=True )
    model.fit(df)
    future = model.make_future_dataframe( periods=7 )
    forecast = model.predict(future)
    forecast = forecast[['ds', 'yhat']]
    # forecast.to_excel('C:/Users/ad/Desktop/data/PM10/dd.xlsx', index=False)
    if data == 'PM10':
        forecast.to_excel(f'C:\work\project\data\PM10/{name}.xlsx', index=False)
    elif data == 'PM2.5':
        forecast.to_excel(f'C:\work\project\data\PM25/{name}.xlsx', index=False)
    elif data == 'CENTIGRADE':
        forecast.to_excel(f'C:\work\project\data\CENTIGRADE/{name}.xlsx', index=False)
    elif data == 'PRECIPITATION':
        forecast.to_excel(f'C:\work\project\data\PRECIPITATION/{name}.xlsx', index=False)
    elif data == 'WIND SPEED':
        forecast.to_excel(f'C:\work\project\data\WIND SPEED/{name}.xlsx', index=False)
    elif data == 'RELATIVE HUMIDITY':
        forecast.to_excel(f'C:\work\project\data\RELATIVE HUMIDITY/{name}.xlsx', index=False)
    else:
        print('저장안됨')
    return forecast

def finalopen(a):
    filepath = f'data/{a}FIN.xlsx'
    excel_df = pd.read_excel(filepath)
    # print (filepath)
    return(excel_df)