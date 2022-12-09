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
            
def pegarDiagonal(m):
    n = min(len(m),len(m[0]))
    return [m[i][i] for i in range(n)]



