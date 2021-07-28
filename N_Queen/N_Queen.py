def RecursiveNQueens(Q,r):
    if r == len(Q):
        print(Q)
    else:
        for j in range(len(Q)):
            legal = True
            for i in range(r):
                if(Q[i]==j or Q[i]==j+r-i or Q[i]==j-r+i):
                    legal = False
            if legal:
                Q[r] = j
                RecursiveNQueens(Q,r+1)

N = 8
Q = [0] * N
RecursiveNQueens(Q,0)