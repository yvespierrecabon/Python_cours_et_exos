def tri(tab):
    print(tab)
    #i est le premier indice de la zone non triee, j le dernier indice. 
    #Au debut, la zone non triee est le tableau entier.
    i= 0
    j= len(tab)-1;
    while i != j :
        if tab[i]== 0:
            i= i+1
        else :
            valeur = tab[j]
            tab[j] = tab[i]
            tab[i] = valeur
            j= j-1
    print(tab)

tri([0,1,0,1,0,1,0,1,0])

def moyenne(tab):
    if len(tab) >0:
        moy = 0
        for val in tab:
            moy = moy + val
        moy = moy/len(tab)
        print( moy)
    else:
        print("erreur")

moyenne([1,2,3,4,5,6,7,8,9,10])
moyenne([])
