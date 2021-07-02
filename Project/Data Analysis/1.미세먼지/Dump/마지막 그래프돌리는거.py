import pandas as pd 
import numpy as np
import bokeh
import webbrowser
from bokeh.io import output_notebook, show, save, output_notebook, curdoc, output_file
from bokeh.plotting import figure, show
from bokeh.models import Select, CheckboxButtonGroup, ColumnDataSource, DataTable, TableColumn, WMTSTileSource, FactorRange, PanTool
from bokeh.models import BoxZoomTool, PanTool, ResetTool
from bokeh.layouts import row, column
from bokeh.resources import INLINE
from bokeh.models import *
from bokeh.plotting import *
from bokeh.io import *
from bokeh.tile_providers import *
from bokeh.palettes import *
from bokeh.transform import *
from bokeh.layouts import *
#output_notebook() 

# 최종파일 오픈 최종

import pandas as pd 

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


