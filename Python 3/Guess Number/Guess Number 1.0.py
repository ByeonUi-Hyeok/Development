# 21.05.31 ver 1.0


# #1. 기능 1 : 시작번호와 마지막번호를 입력한다.
# • 기능 2 : 카드번호를 랜덤으로 추출한다.
# • 기능 3 : 랜덤으로 추출된 카드번호는
# 시작번호와 마지막 번호 사이의 숫자이어야 한다.
# • 기능 4 : 카드번호를 맞힐 때까지 반복해서 숫자를 입력한다.





# 1. 시작번호,끝번호, 정답
# 1-1. 시작번호, 끝번호 정수로 변환
# 1-2. 정답값 생성( 범위 : 시작 번호 ~ 끝 번호 )1
import random
filename_start = input( '시작값을 입력하세요' )
filename_end   = input( '끝값을 입력하세요')
filename_start = int( filename_start )
filename_end   = int( filename_end )
filename_hidden = random.randint(filename_start, filename_end)
print(filename_hidden)   # 체크용

# 2. 숫자를 비교하기
# 2-1. input으로 입력받는 값은 문자열이기 때문에 정수로 변환
# 2-2. 
while True : 
    filename_userinput = input( '정답 값을 예측하세요' )
    filename_userinput = int( filename_userinput )
    if filename_userinput == filename_hidden :                  # 정답값과 입력값이 같으면 스톱 
        print('정답')
        break