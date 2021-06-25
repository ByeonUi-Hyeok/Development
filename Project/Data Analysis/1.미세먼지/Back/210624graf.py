import pandas as pd 
import numpy as np
import bokeh
import webbrowser
from bokeh.io import output_notebook, show, save, output_notebook, curdoc, output_file
from bokeh.plotting import figure, show
from bokeh.models import Select, CheckboxButtonGroup, ColumnDataSource, DataTable, TableColumn, WMTSTileSource, FactorRange, PanTool
from bokeh.models import BoxZoomTool, PanTool, ResetTool
from bokeh.layouts import row, column
from bokeh import layouts
from bokeh.resources import INLINE
from bokeh.models import *
from bokeh.plotting import *
from bokeh.io import *
from bokeh.tile_providers import *
from bokeh.palettes import *
from bokeh.transform import *
from bokeh.layouts import *


# 최종파일 오픈 최종

def finalopen(a):
    filepath = f'C:/Users/ad/Desktop/test/fin/{a}FIN.xlsx'
    excel_df = pd.read_excel(filepath)
    print (filepath)
    return(excel_df)
    
columns = ['SEOUL', 'PUSAN', 'DEAGU', 'INCHEON', 'KWANG_JU', 'DAEJEON', 'ULSAN',
       'KYEONG_GI', 'KANGONE', 'CHUNG_BUK', 'CHUNG_NAM', 'JEON_BUK',
       'JEON_NAM', 'KYUNG_BUK', 'KYUNG_NAM', 'JE_JU', 'SEJONG']

for column in columns:
     globals()[f'{column}FINAL'] = finalopen(column)
     globals()[f'{column}FINAL_cop'] = globals()[f'{column}FINAL'].copy()
     globals()[f'{column}FINAL_cop']['DATE'] = pd.to_datetime(globals()[f'{column}FINAL_cop']['DATE'])


# 최종파일 오픈 최종

def make_graphs():

    columns = ['SEOUL', 'PUSAN', 'DEAGU', 'INCHEON', 'KWANG_JU', 'DAEJEON', 'ULSAN',
       'KYEONG_GI', 'KANGONE', 'CHUNG_BUK', 'CHUNG_NAM', 'JEON_BUK',
       'JEON_NAM', 'KYUNG_BUK', 'KYUNG_NAM', 'JE_JU', 'SEJONG']

    for column in columns:
        globals()[f'{column}FINAL_cop'] =globals()[f'{column}FINAL'].copy()
        globals()[f'{column}FINAL_cop']['DATE'] = pd.to_datetime(globals()[f'{column}FINAL_cop']['DATE'])
        # 라인그래프
        globals()[f'{column}ap'] = figure(
            plot_width=500, plot_height=400, 
            x_axis_type='datetime', output_backend="svg",
            sizing_mode='stretch_width', title=f"{column}'s PM 2.5")

        globals()[f'{column}ap'].line(globals()[f'{column}FINAL_cop']['DATE'], globals()[f'{column}FINAL_cop']['PM2.5'], color='navy', alpha=0.5)

        # 표
        source = ColumnDataSource(globals()[f'{column}FINAL_cop'])
        columns = [ TableColumn( field=col, title=col ) for col in globals()[f'{column}FINAL'].columns ]
        globals()[f'{column}data_table'] = DataTable(source=source, columns = columns, background='red',width=900,sizing_mode='scale_both' )


        # 3일 평균
        tdata = globals()[f'{column}FINAL']['DATE'].to_list()[:3]
        tvalue = globals()[f'{column}FINAL'][['PM10','PM2.5','CO','CENTIGRADE','PRECIPITATION']][:3]

        data = {
                'PM10'   : globals()[f'{column}FINAL']['PM10'].to_list()[:3],
                'PM2.5'  : globals()[f'{column}FINAL']['PM2.5'].to_list()[:3],
                'CO'     : globals()[f'{column}FINAL']['CO'].to_list()[:3],
                'C'      : globals()[f'{column}FINAL']['CENTIGRADE'].to_list()[:3],
                'PPTN'   : globals()[f'{column}FINAL']['PRECIPITATION'].to_list()[:3]
                }

        # this creates [ ("Apples", "2015"), ("Apples", "2016"), ("Apples", "2017"), ("Pears", "2015), ... ]
        x = [ (tdat, tval) for tdat in tdata for tval in tvalue ]
        counts = sum(zip(data['PM10'], data['PM2.5'], data['CO'], data['C'], data['PPTN']), ()) # like an hstack

        source = ColumnDataSource(data=dict(x=x, counts=counts))

        globals()[f'{column}p'] = figure(
            x_range=FactorRange(*x), 
            plot_height=400,
            plot_width=400, 
            title= f"Change in {column} for the last three days",
            #toolbar_location=None,
            tools="xwheel_pan, reset"
            )

        globals()[f'{column}p'].vbar(x='x', top='counts', width=0.9, source=source)

        globals()[f'{column}p'].y_range.start = 0
        globals()[f'{column}p'].x_range.range_padding = 0.01
        globals()[f'{column}p'].xaxis.major_label_orientation = 1
        #p.xgrid.grid_line_color = None
        globals()[f'{column}p'].add_tools(PanTool(dimensions="width"))
        globals()[f'{column}cb_op'] = ['open','high','low','close']
        globals()[f'{column}cb'] = CheckboxButtonGroup(labels=globals()[f'{column}cb_op'], active=[0], button_type="success")

        # 3개 병합
        # globals()[f'{column}G']= column(
        #                             column(row(globals()[f'{column}ap'],globals()[f'{column}p'])),
        #                             row(column(globals()[f'{column}data_table'])))
        # #show(checkbox_grp)
        #show(ap)
        #show(scatter)
        #show(data_table)
        #show(layout_with_widgets)
        #save(obj=layout_with_widgets, filename= f'{column}.html')
        #webbrowser.open('layout_with_widgets.html')
        #break    


make_graphs()

  
layout_with_widgets_SEOUL = column(
                            column(row(SEOULap,SEOULp)),
                            row(column(SEOULdata_table)))
#show(layout_with_widgets)
#show(DEAGUdata_table)
save(obj=layout_with_widgets_SEOUL, filename= 'SEOULPM25.html')

layout_with_widgets_PUSAN = column(
                            column(row(PUSANap,PUSANp)),
                            row(column(PUSANdata_table)))
#show(layout_with_widgets)
#show(DEAGUdata_table)
save(obj=layout_with_widgets_PUSAN, filename= 'PUSANPM25.html')


layout_with_widgets_DEAGU = column(
                            column(row(DEAGUap,DEAGUp)),
                            row(column(DEAGUdata_table)))
#show(layout_with_widgets)
#show(DEAGUdata_table)
save(obj=layout_with_widgets_DEAGU, filename= 'DEAGUPM25.html')

layout_with_widgets_INCHEON = column(
                            column(row(INCHEONap,INCHEONp)),
                            row(column(INCHEONdata_table)))
#show(layout_with_widgets)
#show(INCHEONdata_table)
save(obj=layout_with_widgets_INCHEON, filename= 'INCHEONPM25.html')

layout_with_widgets_KWANG_JU = column(
                            column(row(KWANG_JUap,KWANG_JUp)),
                            row(column(KWANG_JUdata_table)))
#show(layout_with_widgets)
#show(KWANG_JUdata_table)
save(obj=layout_with_widgets_KWANG_JU, filename= 'KWANG_JUPM25.html')

layout_with_widgets_DAEJEON = column(
                            column(row(DAEJEONap,DAEJEONp)),
                            row(column(DAEJEONdata_table)))
#show(layout_with_widgets)
#show(DAEJEONdata_table)
save(obj=layout_with_widgets_DAEJEON, filename= 'DAEJEONPM25.html')

layout_with_widgets_ULSAN = column(
                            column(row(ULSANap,ULSANp)),
                            row(column(ULSANdata_table)))
#show(layout_with_widgets)
#show(ULSANdata_table)
save(obj=layout_with_widgets_ULSAN, filename= 'ULSANPM25.html')

layout_with_widgets_KYEONG_GI = column(
                            column(row(KYEONG_GIap,KYEONG_GIp)),
                            row(column(KYEONG_GIdata_table)))
#show(layout_with_widgets)
#show(KYEONG_GIdata_table)
save(obj=layout_with_widgets_KYEONG_GI, filename= 'KYEONG_GIPM25.html')

layout_with_widgets_KANGONE = column(
                            column(row(KANGONEap,KANGONEp)),
                            row(column(KANGONEdata_table)))
#show(layout_with_widgets)
#show(KANGONEdata_table)
save(obj=layout_with_widgets_KANGONE, filename= 'KANGONEPM25.html')

layout_with_widgets_CHUNG_BUK = column(
                            column(row(CHUNG_BUKap,CHUNG_BUKp)),
                            row(column(CHUNG_BUKdata_table)))
#show(layout_with_widgets)
#show(CHUNG_BUKdata_table)
save(obj=layout_with_widgets_CHUNG_BUK, filename= 'CHUNG_BUKPM25.html')

layout_with_widgets_CHUNG_NAM = column(
                            column(row(CHUNG_NAMap,CHUNG_NAMp)),
                            row(column(CHUNG_NAMdata_table)))
#show(layout_with_widgets)
#show(CHUNG_NAMdata_table)
save(obj=layout_with_widgets_CHUNG_NAM, filename= 'CHUNG_NAMPM25.html')

layout_with_widgets_JEON_BUK = column(
                            column(row(JEON_BUKap,JEON_BUKp)),
                            row(column(JEON_BUKdata_table)))
#show(layout_with_widgets)
#show(JEON_BUKdata_table)
save(obj=layout_with_widgets_JEON_BUK, filename= 'JEON_BUKPM25.html')

layout_with_widgets_JEON_NAM = column(
                            column(row(JEON_NAMap,JEON_NAMp)),
                            row(column(JEON_NAMdata_table)))
#show(layout_with_widgets)
#show(JEON_NAMdata_table)
save(obj=layout_with_widgets_JEON_NAM, filename= 'JEON_NAMPM25.html')

layout_with_widgets_KYUNG_BUK = column(
                            column(row(KYUNG_BUKap,KYUNG_BUKp)),
                            row(column(KYUNG_BUKdata_table)))
#show(layout_with_widgets)
#show(KYUNG_BUKdata_table)
save(obj=layout_with_widgets_KYUNG_BUK, filename= 'KYUNG_BUKPM25.html')

layout_with_widgets_KYUNG_NAM = column(
                            column(row(KYUNG_NAMap,KYUNG_NAMp)),
                            row(column(KYUNG_NAMdata_table)))
#show(layout_with_widgets)
#show(KYUNG_NAMdata_table)
save(obj=layout_with_widgets_KYUNG_NAM, filename= 'KYUNG_NAMPM25.html')

layout_with_widgets_JE_JU = column(
                            column(row(JE_JUap,JE_JUp)),
                            row(column(JE_JUdata_table)))
#show(layout_with_widgets)
#show(JE_JUdata_table)
save(obj=layout_with_widgets_JE_JU, filename= 'JE_JUPM25.html')

layout_with_widgets_SEJONG = column(
                            column(row(SEJONGap,SEJONGp)),
                            row(column(SEJONGdata_table)))
#show(layout_with_widgets)
#show(SEJONGdata_table)
save(obj=layout_with_widgets_SEJONG, filename= 'SEJONGPM25.html')