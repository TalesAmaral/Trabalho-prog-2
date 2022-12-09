def produto(mA,mB):
    if len(mA[0]) != len(mB):
        raise Exception("colunas da primeira diferente das linhas da segunda.")
    mR = []
    for i in range(len(mA)):
        mR.append([])
        for g in range(len(mB[0])):
            soma = 0
            for k in range(len(mB)):
                soma+= mA[i][k]*mB[k][g]
            mR[i].append(soma)
    return mR

def isEqual(mA,mB):
    if len(mA)!=len(mB):
        return 0
    if len(mA[0]) != len(mB[0]):
        return 0
    for i in range(len(mA)):
        for g in range(len(mB)):
            if mA[i][g] != mB[i][g]:
                return 0
    return 1
            
def somaDiagonal(m):
    n = min(len(m),len(m[0]))
    return sum([m[i][i] for i in range(n)])
def somaMatriz(m):
    return sum([sum(i) for i in m])
def trocarDiagonal(matriz):
    m = matriz[:]
    for i in range(len(m)):
        m[i][i], m[len(m) -1 -i][len(m[0]) -1 -i] =m[len(m) -1 -i][len(m[0]) -1 -i], m[i][i] 
    return m
def isTriangularSup(m):
    if len(m) != len(m[0]):
        return 0
    for i in range(len(m)):
        for g in range(i+1,len(m)):
            if m[i][g] != 0:
                return 0
    return 1
def isTriangularInf(m):
    if len(m) != len(m[0]):
        return 0
    for i in range(len(m)):
        for g in range(i-1,-1, -1):
            if m[i][g] != 0:
                return 0
    return 1
def trocarLinhas(matriz,l1,l2):
    m = matriz[:]
    m[l1],m[l2] = m[l2],m[l1]
    return m

def trocarColunas(matriz,c1,c2):
    m = matriz[:]
    m[l1],m[l2] = m[l2],m[l1]
    return m

print(trocarLinhas([[2,0],[0,2]], 0,1)) 



