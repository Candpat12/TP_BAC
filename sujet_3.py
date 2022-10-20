#Exercice 1
def delta(liste) :
    assert isinstance(liste,list)
    resultat = [liste[0]]
    for i in range(len(liste)-1) :
        resultat.append(liste[i+1]-liste[i])
    return resultat
chiffres = [1000, 800, 802, 1000, 1003]

#Exercice 2

class Noeud :
    
    def __init__(self,g,v,d) :
        self.gauche = g
        self.droite = d
        self.valeur = v
        
        def __str__(self) :
            return str(self.valeur)
        
        def est_une_feuille(self) :
            return self.gauche is None and self.droit is None
        
def expression_infixe(e) :
    s = ...
    if e.gauche is not None :
        s = '(' + s + expression_infixe(...)
    s += ...
    if ... is not None :
        s = s + ... + ...
    if ... :
        return s