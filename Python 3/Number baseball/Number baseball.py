import random
filename_hidden = 0

if filename_hidden == 0 : 
    filename_hidden = random.randint(100, 999)
    print(filename_hidden)
else : 
    filename_hidden = 0

filename_anwser = str ( filename_hidden )
filename_input  = input('3자리 숫자 입력하세요')
filename_strike = 0
filename_ball   = 0

# 첫번째 숫자 확인
if filename_input [ 0 ] == filename_anwser [ 0 ]:
    filename_strike += 1 # 스트라이크
elif filename_input [ 0 ] in filename_anwser :
     filename_ball += 1 # 볼
# 두번째 숫자 확인
if filename_input[1] == filename_anwser[1]:
    filename_strike += 1 # 스트라이크
elif filename_input[1] in filename_anwser:
    filename_ball += 1 # 볼
# 세번째 숫자 확인
if filename_input[2] == filename_anwser[2]:
    filename_strike += 1 # 스트라이크
elif filename_input[2] in filename_anwser:
    filename_ball += 1 # 볼
if filename_strike == 0 and filename_ball == 0:
    print('아웃')
else :
    
    print('%sS %sB' % (filename_strike, filename_ball))
    
#    print( f'{filename_strike} + 'S' + {filename_ball} + 'B'')

#    print( '{0}' + 'S' + '{1}'+ 'B'.format(filename_strike, filename_ball))

# 수정요망