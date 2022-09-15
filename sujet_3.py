#Exercice 1
def delta(liste) :
    assert isinstance(liste,list)
    resultat = [liste[0]]
    for i in range(len(liste)-1) :
        resultat.append(liste[i+1]-liste[i])
    return resultat
chiffres = [1000, 800, 802, 1000, 1003]

#Exercice 2

#VOIR CLASSES