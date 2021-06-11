# 21.05.31 ver 1.0


# 기능 1 : 시작번호와 마지막번호를 입력한다.
# 기능 2 : 카드번호를 랜덤으로 추출한다.
# 기능 3 : 랜덤으로 추출된 카드번호는 시작번호와 마지막 번호 사이의 숫자이어야 한다.
# 기능 4 : 카드번호를 맞힐 때까지 반복해서 숫자를 입력한다.
#추가사항
#시작번호와 마지막번호 벗어나면 에러출력
#종료기능
#시도횟수 추가




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
    #file1name_userint = int( filename_userinput )
    # 숫자 미입력시 내용 추가
    while not filename_userinput :
        filename_userinput = input( '입력하지 않았습니다. 숫자를 입력하세요' )
# 2-3. 범위 벗어나면 에러출력    
    if int(filename_userinput) < filename_start or int(filename_userinput) > filename_end : 
        print('범위를 벗어납니다.')
    else:
        filename_userinput = int( filename_userinput )
        if filename_userinput == filename_hidden :                    # 정답값과 입력값이 같으면 스톱 
            print('정답')
            break
        else :                                                        # 정답과 다른 수를 입력했다면
            if filename_userinput > filename_hidden :                 # 입력값이 정답값보다 크다면
                print (' 정답값보다 큽니다. 더 작은 수를 입력하세요 ')  
            else : 
                print (' 정답값보다 작습니다. 더 큰 수를 입력하세요 ')  # 입력값 보다 정답값이 크다면


