#Exercice 1
def moyenne(liste) :
    assert isinstance(liste,list)
    somme = 0
    coeff_tot = 0
    for i in range(len(liste)) :
        somme += liste[i][0] * liste[i][1]
        coeff_tot += liste[i][1]
    return somme/coeff_tot

notes = [(20,2),(10,1)]

#Exercice 2
def pascal(n) :
    C = [[1]]
    for k in range(1,n+1) :
        Ck = [1]
        for i in range(1,k) :
            Ck.append(C[k-1][i-1]+C[k-1][i])
        Ck.append(1)
        C.append(Ck)
    return C