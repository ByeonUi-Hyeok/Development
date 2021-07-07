from django.urls import path

from . import views

app_name = 'pybo'

# 'busan_'
# 'chungbuk_'
# 'chungnam_'
# 'daegu_'
# 'daejeon_'
# 'gangwon_'
# 'gwangju_'
# 'gyeongbuk_'
# 'gyeonggi_'
# 'gyeongnam_'
# 'incheon_'
# 'jeju_'
# 'jeonbuk_'
# 'jeonnam_'
# 'sejong_'
# 'seoul_'
# 'ulsan_'

urlpatterns = [
    path('',views.index, name='index'),
    path('main/', views.main, name='main'),
    path('dustanalysis/', views.dustan, name='dustan'),
    # PM10
    # path('dustanalysis/dataframe/kernel_prewarm_starter.html', views.test, name='test'),
    path('busan/PM10/PASANPM10.html', views.pusan10, name='pusan10'),
    path('chungbuk/PM10/CHUNG_BUKPM10.html', views.chungbuk10, name='chungbuk10'),
    path('chungnam/PM10/CHUNG_NAMPM10.html', views.chungnam10, name='chungnam10'),
    path('daegu/PM10/DEAGUPM10.html', views.daegu10, name='daegu10'),
    path('daejeon/PM10/DAEJEONPM10.html', views.daejeon10, name='daejeon10'),
    path('gangwon/PM10/KANGONEPM10.html', views.gangwon10, name='gangwon10'),
    path('gwangju/PM10/KWANG_JUPM10.html', views.gwangju10, name='gwangju10'),
    path('gyeongbuk/PM10/KYUNG_BUKPM10.html', views.gyeongbuk10, name='gyeongbuk10'),
    path('gyeonggi/PM10/KYEONG_GIPM10.html', views.gyeonggi10, name='gyeonggi10'),
    path('gyeongnam/PM10/KYUNG_NAMPM10.html', views.gyeongnam10, name='gyeongnam10'),
    path('incheon/PM10/INCHEONPM10.html', views.incheon10, name='incheon10'),
    path('jeju/PM10/JE_JUPM10.html', views.jeju10, name='jeju10'),
    path('jeonbuk/PM10/JEON_BUKPM10.html', views.jeonbuk10, name='jeonbuk10'),
    path('jeonnam/PM10/JEON_NAMPM10.html', views.jeonnam10, name='jeonnam10'),
    path('sejong/PM10/SEJONGPM10.html', views.sejong10, name='sejong10'),
    path('seoul/PM10/SEOULPM10.html', views.seoul10, name='seoul10'),
    path('ulsan/PM10/ULSANPM10.html', views.ulsan10, name='ulsan10'),
    # PM25
    path('busan/PM25/PASANPM25.html', views.pusan25, name='pusan25'),
    path('chungbuk/PM25/CHUNG_BUKPM25.html', views.chungbuk25, name='chungbuk25'),
    path('chungnam/PM25/CHUNG_NAMPM25.html', views.chungnam25, name='chungnam25'),
    path('daegu/PM25/DEAGUPM25.html', views.daegu25, name='daegu25'),
    path('daejeon/PM25/DAEJEONPM25.html', views.daejeon25, name='daejeon25'),
    path('gangwon/PM25/KANGONEPM25.html', views.gangwon25, name='gangwon25'),
    path('gwangju/PM25/KWANG_JUPM25.html', views.gwangju25, name='gwangju25'),
    path('gyeongbuk/PM25/KYUNG_BUKPM25.html', views.gyeongbuk25, name='gyeongbuk25'),
    path('gyeonggi/PM25/KYEONG_GIPM25.html', views.gyeonggi25, name='gyeonggi25'),
    path('gyeongnam/PM25/KYUNG_NAMPM25.html', views.gyeongnam25, name='gyeongnam25'),
    path('incheon/PM25/INCHEONPM25.html', views.incheon25, name='incheon25'),
    path('jeju/PM25/JE_JUPM25.html', views.jeju25, name='jeju25'),
    path('jeonbuk/PM25/JEON_BUKPM25.html', views.jeonbuk25, name='jeonbuk25'),
    path('jeonnam/PM25/JEON_NAMPM25.html', views.jeonnam25, name='jeonnam25'),
    path('sejong/PM25/SEJONGPM25.html', views.sejong25, name='sejong25'),
    path('seoul/PM25/SEOULPM25.html', views.seoul25, name='seoul25'),
    path('ulsan/PM25/ULSANPM25.html', views.ulsan25, name='ulsan25'),

    # compare
    path('busan/compare/PASANcpa.html', views.pusancpa, name='pusancpa'),
    path('chungbuk/compare/CHUNG_BUKcpa.html', views.chungbukcpa, name='chungbukcpa'),
    path('chungnam/compare/CHUNG_NAMcpa.html', views.chungnamcpa, name='chungnamcpa'),
    path('daegu/compare/DEAGUcpa.html', views.daegucpa, name='daegucpa'),
    path('daejeon/compare/DAEJEONcpa.html', views.daejeoncpa, name='daejeoncpa'),
    path('gangwon/compare/KANGONEcpa.html', views.gangwoncpa, name='gangwoncpa'),
    path('gwangju/compare/KWANG_JUcpa.html', views.gwangjucpa, name='gwangjucpa'),
    path('gyeongbuk/compare/KYUNG_BUKcpa.html', views.gyeongbukcpa, name='gyeongbukcpa'),
    path('gyeonggi/compare/KYEONG_GIcpa.html', views.gyeonggicpa, name='gyeonggicpa'),
    path('gyeongnam/compare/KYUNG_NAMcpa.html', views.gyeongnamcpa, name='gyeongnamcpa'),
    path('incheon/compare/INCHEONcpa.html', views.incheoncpa, name='incheoncpa'),
    path('jeju/compare/JE_JUcpa.html', views.jejucpa, name='jejucpa'),
    path('jeonbuk/compare/JEON_BUKcpa.html', views.jeonbukcpa, name='jeonbukcpa'),
    path('jeonnam/compare/JEON_NAMcpa.html', views.jeonnamcpa, name='jeonnamcpa'),
    path('sejong/compare/SEJONGcpa.html', views.sejongcpa, name='sejongcpa'),
    path('seoul/compare/SEOULcpa.html', views.seoulcpa, name='seoulcpa'),
    path('ulsan/compare/ULSANcpa.html', views.ulsancpa, name='ulsancpa'),

    # predict
    path('busan/predict/PASANpred.html', views.pusanpred, name='pusanpred'),
    path('chungbuk/predict/CHUNG_BUKpred.html', views.chungbukpred, name='chungbukpred'),
    path('chungnam/predict/CHUNG_NAMpred.html', views.chungnampred, name='chungnampred'),
    path('daegu/predict/DEAGUpred.html', views.daegupred, name='daegupred'),
    path('daejeon/predict/DAEJEONpred.html', views.daejeonpred, name='daejeonpred'),
    path('gangwon/predict/KANGONEpred.html', views.gangwonpred, name='gangwonpred'),
    path('gwangju/predict/KWANG_JUpred.html', views.gwangjupred, name='gwangjupred'),
    path('gyeongbuk/predict/KYUNG_BUKpred.html', views.gyeongbukpred, name='gyeongbukpred'),
    path('gyeonggi/predict/KYEONG_GIpred.html', views.gyeonggipred, name='gyeonggipred'),
    path('gyeongnam/predict/KYUNG_NAMpred.html', views.gyeongnampred, name='gyeongnampred'),
    path('incheon/predict/INCHEONpred.html', views.incheonpred, name='incheonpred'),
    path('jeju/predict/JE_JUpred.html', views.jejupred, name='jejupred'),
    path('jeonbuk/predict/JEON_BUKpred.html', views.jeonbukpred, name='jeonbukpred'),
    path('jeonnam/predict/JEON_NAMpred.html', views.jeonnampred, name='jeonnampred'),
    path('sejong/predict/SEJONGpred.html', views.sejongpred, name='sejongpred'),
    path('seoul/predict/SEOULpred.html', views.seoulpred, name='seoulpred'),
    path('ulsan/predict/ULSANpred.html', views.ulsanpred, name='ulsanpred'),

    # 메인 맵 페이지
    path('main/dataframe/pm10_map.html', views.map10, name='map10'),
    path('main/dataframe/pm25_map.html', views.map25, name='map25'),

    # 지역 페이지
    path('busan/', views.busan, name='busan'),
    path('chungbuk/', views.chungbuk, name='chungbuk'),
    path('chungnam/', views.chungnam, name='chungnam'),
    path('daegu/', views.daegu, name='daegu'),
    path('daejeon/', views.daejeon, name='daejeon'),
    path('gangwon/', views.gangwon, name='gangwon'),
    path('gwangju/', views.gwangju, name='gwangju'),
    path('gyeongbuk/', views.gyeongbuk, name='gyeongbuk'),
    path('gyeonggi/', views.gyeonggi, name='gyeonggi'),
    path('gyeongnam/', views.gyeongnam, name='gyeongnam'),
    path('incheon/', views.incheon, name='incheon'),
    path('jeju/', views.jeju, name='jeju'),
    path('jeonbuk/', views.jeonbuk, name='jeonbuk'),
    path('jeonnam/', views.jeonnam, name='jeonnam'),
    path('sejong/', views.sejong, name='sejong'),
    path('seoul/', views.seoul, name='seoul'),
    path('ulsan/', views.ulsan, name='ulsan'),
]
