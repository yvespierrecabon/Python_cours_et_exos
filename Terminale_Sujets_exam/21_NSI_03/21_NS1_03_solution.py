def multiplication(a, b):
    signe = "+"
    if (a < 0 < b) or (b < 0 < a):
        signe = "-"
    res = 0
    for i in range(abs(a)):
        res = res + abs(b)
        # print(i, res)
    if signe == "-":
        res = -res
    print(res)


multiplication(3, 5)
multiplication(-4, -8)
multiplication(-2, 6)
multiplication(-2, 0)


def dichotomie(tab, x):
    """
    tab : tableau d’entiers trié dans l’ordre croissant
    x : nombre entier
    La fonction renvoie True si tab contient x et False sinon
    """
    debut = 0
    fin = len(tab) - 1
    while debut <= fin:
        m = debut
        if x == tab[m]:
            print("True")
            return True
        if x > tab[m]:
            debut = m + 1
        else:
            fin = debut -1
    print("False")
    return False


dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33],28)
dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33],27)