from django.shortcuts import render
from django.contrib.auth.decorators import login_required



# Create your views here.

def index(request):
    return render(request, 'main/start.html')


@login_required(login_url='common:login')
def main(request):
    return render(request, 'pybo/main.html')

@login_required(login_url='common:login')
def dustan(request):
    return render(request, 'pybo/dust_analysis.html')

@login_required(login_url='common:login')
def test(request):
    return render(request, 'pybo/dataframe/kernel_prewarm_starter.html')

# map에 대한 url
@login_required(login_url='common:login')
def map10(request):
    return render(request, 'pybo/dataframe/pm10_map.html')

@login_required(login_url='common:login')
def map25(request):
    return render(request, 'pybo/dataframe/pm25_map.html')

# PM10
@login_required(login_url='common:login')
def pusan10(request):
    return render(request, 'pybo/PM10/PUSANPM10.html')

@login_required(login_url='common:login')
def chungbuk10(request):
    return render(request, 'pybo/PM10/CHUNG_BUKPM10.html')

@login_required(login_url='common:login')
def chungnam10(request):
    return render(request, 'pybo/PM10/CHUNG_NAMPM10.html')

@login_required(login_url='common:login')
def daegu10(request):
    return render(request, 'pybo/PM10/DEAGUPM10.html')

@login_required(login_url='common:login')
def daejeon10(request):
    return render(request, 'pybo/PM10/DAEJEONPM10.html')

@login_required(login_url='common:login')
def gangwon10(request):
    return render(request, 'pybo/PM10/KANGONEPM10.html')

@login_required(login_url='common:login')
def gwangju10(request):
    return render(request, 'pybo/PM10/KWANG_JUPM10.html')

@login_required(login_url='common:login')
def gyeongbuk10(request):
    return render(request, 'pybo/PM10/KYUNG_BUKPM10.html')

@login_required(login_url='common:login')
def gyeonggi10(request):
    return render(request, 'pybo/PM10/KYEONG_GIPM10.html')

@login_required(login_url='common:login')
def gyeongnam10(request):
    return render(request, 'pybo/PM10/KYUNG_NAMPM10.html')

@login_required(login_url='common:login')
def incheon10(request):
    return render(request, 'pybo/PM10/INCHEONPM10.html')

@login_required(login_url='common:login')
def jeju10(request):
    return render(request, 'pybo/PM10/JE_JUPM10.html')

@login_required(login_url='common:login')
def jeonbuk10(request):
    return render(request, 'pybo/PM10/JEON_BUKPM10.html')

@login_required(login_url='common:login')
def jeonnam10(request):
    return render(request, 'pybo/PM10/JEON_NAMPM10.html')

@login_required(login_url='common:login')
def sejong10(request):
    return render(request, 'pybo/PM10/SEJONGPM10.html')

@login_required(login_url='common:login')
def seoul10(request):
    return render(request, 'pybo/PM10/SEOULPM10.html')

@login_required(login_url='common:login')
def ulsan10(request):
    return render(request, 'pybo/PM10/ULSANPM10.html')

# PM25
@login_required(login_url='common:login')
def pusan25(request):
    return render(request, 'pybo/PM25/PUSANPM25.html')

@login_required(login_url='common:login')
def chungbuk25(request):
    return render(request, 'pybo/PM25/CHUNG_BUKPM25.html')

@login_required(login_url='common:login')
def chungnam25(request):
    return render(request, 'pybo/PM25/CHUNG_NAMPM25.html')

@login_required(login_url='common:login')
def daegu25(request):
    return render(request, 'pybo/PM25/DEAGUPM25.html')

@login_required(login_url='common:login')
def daejeon25(request):
    return render(request, 'pybo/PM25/DAEJEONPM25.html')

@login_required(login_url='common:login')
def gangwon25(request):
    return render(request, 'pybo/PM25/KANGONEPM25.html')

@login_required(login_url='common:login')
def gwangju25(request):
    return render(request, 'pybo/PM25/KWANG_JUPM25.html')

@login_required(login_url='common:login')
def gyeongbuk25(request):
    return render(request, 'pybo/PM25/KYUNG_BUKPM25.html')

@login_required(login_url='common:login')
def gyeonggi25(request):
    return render(request, 'pybo/PM25/KYEONG_GIPM25.html')

@login_required(login_url='common:login')
def gyeongnam25(request):
    return render(request, 'pybo/PM25/KYUNG_NAMPM25.html')

@login_required(login_url='common:login')
def incheon25(request):
    return render(request, 'pybo/PM25/INCHEONPM25.html')

@login_required(login_url='common:login')
def jeju25(request):
    return render(request, 'pybo/PM25/JE_JUPM25.html')

@login_required(login_url='common:login')
def jeonbuk25(request):
    return render(request, 'pybo/PM25/JEON_BUKPM25.html')

@login_required(login_url='common:login')
def jeonnam25(request):
    return render(request, 'pybo/PM25/JEON_NAMPM25.html')

@login_required(login_url='common:login')
def sejong25(request):
    return render(request, 'pybo/PM25/SEJONGPM25.html')

@login_required(login_url='common:login')
def seoul25(request):
    return render(request, 'pybo/PM25/SEOULPM25.html')

@login_required(login_url='common:login')
def ulsan25(request):
    return render(request, 'pybo/PM25/ULSANPM25.html')

# compare
@login_required(login_url='common:login')
def pusancpa(request):
    return render(request, 'pybo/compare/PUSANcpa.html')

@login_required(login_url='common:login')
def chungbukcpa(request):
    return render(request, 'pybo/compare/CHUNG_BUKcpa.html')

@login_required(login_url='common:login')
def chungnamcpa(request):
    return render(request, 'pybo/compare/CHUNG_NAMcpa.html')

@login_required(login_url='common:login')
def daegucpa(request):
    return render(request, 'pybo/compare/DEAGUcpa.html')

@login_required(login_url='common:login')
def daejeoncpa(request):
    return render(request, 'pybo/compare/DAEJEONcpa.html')

@login_required(login_url='common:login')
def gangwoncpa(request):
    return render(request, 'pybo/compare/KANGONEcpa.html')

@login_required(login_url='common:login')
def gwangjucpa(request):
    return render(request, 'pybo/compare/KWANG_JUcpa.html')

@login_required(login_url='common:login')
def gyeongbukcpa(request):
    return render(request, 'pybo/compare/KYUNG_BUKcpa.html')

@login_required(login_url='common:login')
def gyeonggicpa(request):
    return render(request, 'pybo/compare/KYEONG_GIcpa.html')

@login_required(login_url='common:login')
def gyeongnamcpa(request):
    return render(request, 'pybo/compare/KYUNG_NAMcpa.html')

@login_required(login_url='common:login')
def incheoncpa(request):
    return render(request, 'pybo/compare/INCHEONcpa.html')

@login_required(login_url='common:login')
def jejucpa(request):
    return render(request, 'pybo/compare/JE_JUcpa.html')

@login_required(login_url='common:login')
def jeonbukcpa(request):
    return render(request, 'pybo/compare/JEON_BUKcpa.html')

@login_required(login_url='common:login')
def jeonnamcpa(request):
    return render(request, 'pybo/compare/JEON_NAMcpa.html')

@login_required(login_url='common:login')
def sejongcpa(request):
    return render(request, 'pybo/compare/SEJONGcpa.html')

@login_required(login_url='common:login')
def seoulcpa(request):
    return render(request, 'pybo/compare/SEOULcpa.html')

@login_required(login_url='common:login')
def ulsancpa(request):
    return render(request, 'pybo/compare/ULSANcpa.html')

# predict
@login_required(login_url='common:login')
def pusanpred(request):
    return render(request, 'pybo/predict/PUSANpred.html')

@login_required(login_url='common:login')
def chungbukpred(request):
    return render(request, 'pybo/predict/CHUNG_BUKpred.html')

@login_required(login_url='common:login')
def chungnampred(request):
    return render(request, 'pybo/predict/CHUNG_NAMpred.html')

@login_required(login_url='common:login')
def daegupred(request):
    return render(request, 'pybo/predict/DEAGUpred.html')

@login_required(login_url='common:login')
def daejeonpred(request):
    return render(request, 'pybo/predict/DAEJEONpred.html')

@login_required(login_url='common:login')
def gangwonpred(request):
    return render(request, 'pybo/predict/KANGONEpred.html')

@login_required(login_url='common:login')
def gwangjupred(request):
    return render(request, 'pybo/predict/KWANG_JUpred.html')

@login_required(login_url='common:login')
def gyeongbukpred(request):
    return render(request, 'pybo/predict/KYUNG_BUKpred.html')

@login_required(login_url='common:login')
def gyeonggipred(request):
    return render(request, 'pybo/predict/KYEONG_GIpred.html')

@login_required(login_url='common:login')
def gyeongnampred(request):
    return render(request, 'pybo/predict/KYUNG_NAMpred.html')

@login_required(login_url='common:login')
def incheonpred(request):
    return render(request, 'pybo/predict/INCHEONpred.html')

@login_required(login_url='common:login')
def jejupred(request):
    return render(request, 'pybo/predict/JE_JUpred.html')

@login_required(login_url='common:login')
def jeonbukpred(request):
    return render(request, 'pybo/predict/JEON_BUKpred.html')

@login_required(login_url='common:login')
def jeonnampred(request):
    return render(request, 'pybo/predict/JEON_NAMpred.html')

@login_required(login_url='common:login')
def sejongpred(request):
    return render(request, 'pybo/predict/SEJONGpred.html')

@login_required(login_url='common:login')
def seoulpred(request):
    return render(request, 'pybo/predict/SEOULpred.html')

@login_required(login_url='common:login')
def ulsanpred(request):
    return render(request, 'pybo/predict/ULSANpred.html')



@login_required(login_url='common:login')
def chungbuk(request):
    return render(request, 'pybo/chungbuk.html')

@login_required(login_url='common:login')
def chungnam(request):
    return render(request, 'pybo/chungnam.html')

@login_required(login_url='common:login')
def daegu(request):
    return render(request, 'pybo/daegu.html')

@login_required(login_url='common:login')
def daejeon(request):
    return render(request, 'pybo/daejeon.html')

@login_required(login_url='common:login')
def gangwon(request):
    return render(request, 'pybo/gangwon.html')

@login_required(login_url='common:login')
def gwangju(request):
    return render(request, 'pybo/gwangju.html')

@login_required(login_url='common:login')
def gyeongbuk(request):
    return render(request, 'pybo/gyeongbuk.html')

@login_required(login_url='common:login')
def gyeonggi(request):
    return render(request, 'pybo/gyeonggi.html')

@login_required(login_url='common:login')
def gyeongnam(request):
    return render(request, 'pybo/gyeongnam.html')

@login_required(login_url='common:login')
def incheon(request):
    return render(request, 'pybo/incheon.html')

@login_required(login_url='common:login')
def jeju(request):
    return render(request, 'pybo/jeju.html')

@login_required(login_url='common:login')
def jeonbuk(request):
    return render(request, 'pybo/jeonbuk.html')

@login_required(login_url='common:login')
def jeonnam(request):
    return render(request, 'pybo/jeonnam.html')

@login_required(login_url='common:login')
def sejong(request):
    return render(request, 'pybo/sejong.html')

@login_required(login_url='common:login')
def seoul(request):
    return render(request, 'pybo/seoul.html')

@login_required(login_url='common:login')
def ulsan(request):
    return render(request, 'pybo/ulsan.html')

@login_required(login_url='common:login')
def busan(request):
    return render(request, 'pybo/busan.html')


