def Edit_memoi(x,y, m, n, ed):
    for i in range(0, m+1):
        ed[i][0] = i 
    for j in range(0, n+1):
        ed[0][j] = j
    
    for i in range(1, m+1):
        for j in range(1, n+1):
            ed[i][j] = - 1
    return Edit_rec(x,y,i,j, ed)

#Coração do algoritmo recursivo para o problema da edição 

def Edit_rec(x, y , i, j, ed):
    if ed[i][j] >= 0:
        return ed[i][j]
    else:
        if x[i-1] == y[j-1]:
            a = Edit_rec(x,y,i-1,j-1,ed) + 0
        else:
            a = Edit_rec(x,y,i-1,j-1,ed) + 1

        b = Edit_rec(x,y,i,j-1,ed) + 1
        c = Edit_rec(x,y,i-1,j,ed) + 1
        ed[i][j] = min(a,b,c)
        
        return ed[i][j]