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
print(produto([[2,3],[1,0],[4,5]],[[3,1],[2,4]]))

            


