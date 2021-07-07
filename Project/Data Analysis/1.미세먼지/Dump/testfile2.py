import random
import time
#import pprint

lt_rank = list()
while True:
    sz_yourname = input("이름을 입력하세요")
    lt_a = ['+','-','*','/']
    n_count = 0
    n_start = time.time() 
    for i in range (5):
        n_a   = random.randint(1, 99)
        n_a2  = random.randint(1, 99)
        lt_a_ = random.choice(lt_a)
        n_input = int(input(str(n_a) + lt_a_ + str(n_a2)))
        n_ta2 = int(eval(str(n_a) + lt_a_ + str(n_a2)))
        if n_input == n_ta2:
            print("정답입니다. 입력값 :", n_input, "정답 :", n_ta2)
            n_count += 1
        else: 
            print("오답입니다. 입력값 :", n_input, "정답 :", n_ta2)

    n_end = time.time()
    n_diff = round(n_end - n_start)
    lt_rank.append([sz_yourname, n_count, n_diff])
    lt_rank = sorted(lt_rank, key=lambda x: x[1],reverse=True)
    rank_index = lt_rank.index([sz_yourname, n_count, n_diff])

    print(f'{sz_yourname}님 총 5문제중에 {n_count}개 맞췄습니다. {n_diff}초 걸리셨습니다.')
    print(f'당신의 등수는 총 {len(lt_rank)}명 중{rank_index+1}등 입니다.' )
    #print("순위는 정답 수만으로 계산합니다. 순위표는 아래와 같습니다.")
    #pprint()
    

    # 5개 정보가 다 입력되야 올바른 순위값이 나오므로 5개 완료 후 종료 삽입
    a = input('종료하고싶으시면 Q를 입력하세요')
    if a.upper() == 'Q':
        break

