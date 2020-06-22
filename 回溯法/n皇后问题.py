#预备知识，把x,y点作为皇后点
def put_down_the_queen(x,y,mark):
    dx = [-1, 1, 0, 0, -1, -1, 1, 1]
    dy = [0, 0, -1, 1, -1, 1, -1, 1]
    mark[x][y] = 1
    for i in range(1,len(mark)):
        for j in range(8):
            new_x = x + i*dx[j]
            new_y = y + i*dy[j]
            if 0<=new_x<len(mark) and 0<=new_y<len(mark):
                mark[new_x][new_y] = 1

def generate(k, n, location, result, mark):
    if k == n:
        #result.append(location)
        temp = []
        for x in location:
            temp.append("".join(x))
        result.append(temp)
        return
    for i in range(n):
        if mark[k][i] == 0:
            import copy
            tmp_mark = copy.deepcopy(mark)#mark[:]
            location[k][i] = 'Q'
            put_down_the_queen(k, i, mark)
            generate(k + 1, n, location, result, mark)
            mark = tmp_mark[:]
            location[k][i] = '.'
#def solveNQueens(n):
result = []
location = [['.'] * 4 for _ in range(4)]
mark = [[0] * 4 for _ in range(4)]
generate(0, 4, location, result, mark)
print(result)
    #return result
#print(solveNQueens(4))
#put_down_the_queen(0,0,mark=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])

