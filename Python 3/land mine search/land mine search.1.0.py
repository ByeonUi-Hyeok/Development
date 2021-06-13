# 21.06.09
# ver 1.0
# . = Not mine / * = mine
# 지뢰 주변의 .이 지뢰 숫자를 출력
# 오류가많아서 수정요망

from pprint import pprint

tmp = []
row = set(map(int, input().split(' ')))
row = row.pop()
for i in range(row):
        tmp.append(list(input()))
pprint(tmp, indent=1, width= row*10)

# row 수만큼 1차 배열의 개수, row수 만큼 2차 리스트는 맴버를 가지는데 그 값은 v이다 
temp = [ [ 0 for i in range( row ) ] for j in range( row ) ]
pprint( temp, width = row *10 )

for i in range(row):
    for j in range(row):
        if tmp[i][j] == '.':
            if i == (row-row) :                       # [0][x]
                if tmp[i+1][j] == '*':                # [1][x] == *        
                    temp[i][j] += 1                   # [x][x] += 1  
                    if j == 0 :                       # [x][0] 
                        if tmp[i][j+1] == '*':        # [x][1]
                            temp[i][j] += 1         
                    elif j == (row-1) :               # [x][-1]
                        if tmp[i][j-1] == '*':        # [x][-2]
                            temp[i][j] += 1                
                    else : 
                        if tmp[i][j-1] == '*' and tmp[i][j+1] == '*' :
                            temp[i][j] += 2
                        elif tmp[i][j-1] == '*' or tmp[i][j+1] == '*' :
                            temp[i][j] += 1
        
            if 0 < i < row-1 :                     
                if tmp[i-1][j] == '*' and tmp[i+1][j] == '*':                       
                    temp[i][j] += 2
                elif tmp[i-1][j] == '*' or tmp[i+1][j] == '*':
                    temp[i][j] += 1
                    if j == 0 :                      
                        if tmp[i][j+1] == '*':      
                            temp[i][j] += 1         
                    elif j == (row-1) :             
                        if tmp[i][j-1] == '*':        
                            temp[i][j] += 1                
                    else : 
                        if tmp[i][j-1] == '*' and tmp[i][j+1] == '*' :
                            temp[i][j] += 2
                        elif tmp[i][j-1] == '*' or tmp[i][j+1] == '*' :
                            temp[i][j] += 1
                            
            if i == row-1:
                if tmp[i-1][j] == '*':                # [1][x] == *        
                    temp[i][j] += 1                   # [x][x] += 1  
                    if j == 0 :                       # [x][0] 
                        if tmp[i][j+1] == '*':        # [x][1]
                            temp[i][j] += 1         
                    elif j == (row-1) :               # [x][-1]
                        if tmp[i][j-1] == '*':        # [x][-2]
                            temp[i][j] += 1                
                    else : 
                        if tmp[i][j-1] == '*' and tmp[i][j+1] == '*' :
                            temp[i][j] += 2
                        elif tmp[i][j-1] == '*' or tmp[i][j+1] == '*' :
                            temp[i][j] += 1