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

for i in range(0, 3):                
    if filename_input [ i ] == filename_anwser [ i ]:
        filename_strike += 1 # 스트라이크
    elif filename_input [ i ] in filename_anwser :
        filename_ball   += 1 # 볼

if filename_strike == 0 and filename_ball == 0:
    print('아웃')
else :
    print('%sS %sB' % (filename_strike, filename_ball))
    print( f'{filename_strike}S {filename_ball}B')
    print( '{0}S {1}B'.format(filename_strike, filename_ball))
