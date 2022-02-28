# les conversions de base (décimale, binaire, hexadécimale)

## Binaire
### 05_1 !!! 
On modélise la représentation binaire d'un entier non signé par un tableau d'entiers dont
les éléments sont 0 ou 1. Par exemple, le tableau [1, 0, 1, 0, 0, 1, 1] représente
l'écriture binaire de l'entier dont l'écriture décimale est
2**6 + 2**4 + 2**1 + 2**0 = 83.
À l'aide d'un parcours séquentiel, écrire la fonction convertir répondant aux
spécifications suivantes :
def convertir(T):
"""
T est un tableau d'entiers, dont les éléments sont 0 ou 1 et
représentant un entier écrit en binaire. Renvoie l'écriture
décimale de l'entier positif dont la représentation binaire
est donnée par le tableau T
"""
Exemple :
>>> convertir([1, 0, 1, 0, 0, 1, 1])

83

>>> convertir([1, 0, 0, 0, 0, 0, 1, 0])

130

### 11_1
Écrire une fonction conv_bin qui prend en paramètre un entier positif n et renvoie un
couple (b,bit) où :
- b est une liste d'entiers correspondant à la représentation binaire de n;

- bit correspond aux nombre de bits qui constituent b.
Exemple :
>>> conv_bin(9)
([1,0,1,1],4)
Aide :
- l'opérateur // donne le quotient de la division euclidienne : 5//2 donne 2 ;
- l'opérateur % donne le reste de la division euclidienne : 5%2 donne 1 ;
- append est une méthode qui ajoute un élément à une liste existante :
Soit T=[5,2,4], alors T.append(10) ajoute 10 à la liste T. Ainsi, T devient
[5,2,4,10].
- reverse est une méthode qui renverse les éléments d'une liste.
Soit T=[5,2,4,10]. Après T.reverse(), la liste devient [10,4,2,5].

On remarquera qu’on récupère la représentation binaire d’un entier n en partant de la
gauche en appliquant successivement les instructions :
b = n%2
n = n//2
répétées autant que nécessaire.




### 16_2
On considère la fonction dec_to_bin ci-dessous qui prend en paramètre un entier positif
a en écriture décimale et qui renvoie son écriture binaire sous la forme d'une chaine de
caractères.

def dec_to_bin(a):
	bin_a = ...
	a = a//2
	while a ... :
		bin_a = ... + bin_a
	return bin_a
	
Compléter la fonction dec_to_bin.

Exemples :

>>> dec_to_bin(83)
'1010011'

>>> dec_to_bin(127)
'1111111'


### 21_2
Pour rappel, la conversion d’un nombre entier positif en binaire peut s’effectuer à l’aide
des divisions successives comme illustré ici : voir le pdf

Voici une fonction python basée sur la méthode des divisions successives permettant de
convertir un nombre entier positif en binaire :

def binaire(a):

	bin_a = str(...)
	a = a // 2
	while a ... :
		bin_a = ...(a%2) + ...
		a = ...
	return bin_a

Compléter la fonction binaire.
Exemples :

>>> binaire(0)
'0'

>>> binaire(77)
'1001101'




### 26_2 !!!
 On considère une image en 256 niveaux de gris que l’on représente par une grille de
nombres, c’est-à-dire une liste composée de sous-listes toutes de longueurs identiques.
La largeur de l’image est donc la longueur d’une sous-liste et la hauteur de l’image est le
nombre de sous-listes.

Chaque sous-liste représente une ligne de l’image et chaque élément des sous-listes est
un entier compris entre 0 et 255, représentant l’intensité lumineuse du pixel.
Compléter le programme ci-dessous :

 
 
 
# les algorithmes de base :
 
## recherche du max ou du min d'une liste
### 15_1
Écrire une fonction RechercheMinMax qui prend en paramètre un tableau de nombres non triés tab, et qui renvoie la plus petite et la plus grande valeur du tableau sous la forme d’un dictionnaire à deux clés ‘min’ et ‘max’. Les tableaux seront représentés sous forme de liste Python.

Exemples :
>>> tableau = [0, 1, 4, 2, -2, 9, 3, 1, 7, 1]

>>> resultat = rechercheMinMax(tableau)

>>> resultat
{'min': -2, 'max': 9}

>>> tableau = []

>>> resultat = rechercheMinMax(tableau)

>>> resultat
{'min': None, 'max': None}

### 17_1
Écrire une fonction RechercheMin qui prend en paramètre un tableau de nombres non trié tab, et qui renvoie l'indice de la première occurrence du minimum de ce tableau. Les tableaux seront représentés sous forme de liste Python.

Exemples :
>>> indice_du_min([5])
0

>>> indice_du_min([2, 4, 1])
2

>>> indice_du_min([5, 3, 2, 2, 4])
2

### 24_1
Écrire une fonction recherche qui prend en paramètres elt un nombre et tab un
tableau de nombres, et qui renvoie l’indice de la dernière occurrence de elt dans tab si elt est dans tab et le -1 sinon.

Exemples :
>>>
-1

>>>
2

>>>
2

>>>
5


## tris d'une liste
Déja fait
## recherche par dichotomie
Déjà fait
## parcours d'un arbre
Déjà fait
   
   
   
# la récursivité
### 08_2 Glouton + récursivité !!!
On s’intéresse à un algorithme récursif qui permet de rendre la monnaie à partir d’une liste donnée de valeurs de pièces et de billets 
- le système monétaire est donné sous forme d’une liste pieces=[100, 50, 20, 10, 5, 2, 1]
- (on supposera qu’il n’y a pas de limitation quant à leur nombre), on cherche à donner la liste de pièces à rendre pour une somme donnée en argument.

Compléter le code Python ci-dessous de la fonction rendu_glouton qui implémente cet algorithme et renvoie la liste des pièces à rendre

 
# le vocabulaire de base sur les réseaux
### 24_2
On définit une classe gérant une adresse IPv4.

On rappelle qu’une adresse IPv4 est une adresse de longueur 4 octets, notée en décimale à point, en séparant chacun des octets par un point. On considère un réseau privé avec une plage d’adresses IP de 192.168.0.0 à 192.168.0.255.

On considère que les adresses IP saisies sont valides.

Les adresses IP 192.168.0.0 et 192.168.0.255 sont des adresses réservées.

Le code ci-dessous implémente la classe AdresseIP.

class AdresseIP: ...




