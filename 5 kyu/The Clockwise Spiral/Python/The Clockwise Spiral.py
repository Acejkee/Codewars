def create_spiral(n):
    if type(n) != int:
        return []
    elif n < 1:
        return []
    else:
        mat = [[0]*n for i in range(n)]
        mat[n//2][n//2]=(n*n)
        st, m = 1, 0
        for v in range(n//2):
            for i in range(n-m): # горизонталь
                mat[v][i+v]=st
                st +=1
            for i in range(v+1, n-v): # вертикаль
                mat[i][-v-1] = st
                st += 1
            for i in range(v+1,n-v): # горизонталь
                mat[-v-1][-i-1] = st
                st += 1
            for i in range(v+1, n-(v+1)): # вертикаль
                mat[-i-1][v] = st
                st +=1
            m += 2
    return mat      