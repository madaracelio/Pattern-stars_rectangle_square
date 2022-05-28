"""
    @Author: Laza Celio
    @Date: 04/05/2022
    @Links: https://github.com/madaracelio

    Une fonction permettant de déssiner une étoile
    n: un entier, qui est la dimension
    Exemple: n = 5

          *
         * *
    * * *   * * *
      *       *
    * * *   * * *
         * *
          *
"""   
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

from WedgeSymbol import InvertedWedgeSymbol, WedgeSymbol
from SigmaSymbol import InvertedSigma, Sigma


dim = 5
moitie = dim//2

def chapeau(n):
    # Parcourir tous les lignes de total n+1 divisé par deux (ex: n = 5, dont 5 colonnes et 3 lignes)
    LINE_NUMBER = (n+1)//2
    
    for i in range(LINE_NUMBER):
        # Parcourir les n nombre de colonne
        for j in range(0, n):
            if i == 0: # i arrive est à la première ligne
                # si on est à la moitié de la colonne de j
                if j == (n - 1)/2:
                    print("*", end="")
                else:
                    print(" ", end="")
            else:
                # on prend ce qui est à gauche et à droite par rapport au milieu, jusqu'à la l'extremité gauche et droite
                if j == n//2 - i or j == n//2 + i:
                    print("*", end="")
                if j < n - 1:
                    print(" ", end="")
        print("\r")


def chapeau_inverse(n):
    # Parcourir tous les lignes de total n+1 divisé par deux (ex: n = 5, dont 5 colonnes et 3 lignes)
    LINE_NUMBER = (n+1)//2
    
    for i in range(LINE_NUMBER):
        # Parcourir les n nombre de colonne
        for j in range(0, n):
            # print("*", end="")
            if i == LINE_NUMBER-1: # i arrive à la dernière ligne
                # si on est à la moitié de la colonne de j
                if j == (n - 1)/2:
                    print("*", end="")
                else:
                    print(" ", end="")
            else:
                # on prend la 1ere position et la dernière, puis on passe sur la 2nde et l'avant dernière, et ainsi de suite
                if j == i or j == n - i - 1:
                    print("*", end="")
                if j < n - 1:
                    print(" ", end="")
        print("\r")


def sigma(n):
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1: # Premier et dernier ligne pour une barre horizontale
                print("*", end="")
            else:
                if i == n // 2:
                    if j == n // 2:
                        print("*", end="")
                else:
                    if i == j and i < n // 2:
                        print("*", end="")
                    if i == n - j - 1 and i > n //2:
                        print("*", end="")
                print(" ", end="")
        print("\r")


def sigma_inverse(n):
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1: # Premier et dernier ligne pour une barre horizontale
                print("*", end="")
            else:
                if i == n // 2:
                    if j == n // 2:
                        print("*", end="")
                else:
                    if i == n - 1 - j and i < n // 2:
                        print("*", end="")
                    if i == n - 1  and i > n // 2:
                        print("*", end="")
                print(" ", end="")
        print("\r")


def etoile():
    for i in range(dim):
        for j in range(0, i+1):
            if i == 0 or i == dim-1:
                if j == moitie - 1:
                    print(" * ", end="")
                else:
                    print("", end="")
            if i == moitie - 1:
                if j == 0 or j == dim-1:
                    print(" * ")
                else:
                    print("", end="")
            # print("+", end="")
        print("\r")


def carre():
    for i in range(dim):
        for j in range(0, dim):
            print("*", end="")
        print("\r")

num = 9
# chapeau(num)
# chapeau_inverse(num)
# sigma(num)
# sigma_inverse(num)


line_number = (dim * 2) - 3
column_number = (dim * 2) - 1
wedge_dimension = (dim//2) + 1
sigma_dimension = (dim//2) + 1
mid = (column_number)//2
print(mid)
print(line_number, column_number, wedge_dimension)
for i in range(line_number):
    for j in range(column_number):
        if i == 0: # i arrive est à la première ligne
            # si on est à la moitié de la colonne de j
            if j == mid:
                print("*", end="")
            else:
                print(" ", end="")
        elif i < wedge_dimension:
            # on prend ce qui est à gauche et à droite par rapport au milieu, jusqu'à la l'extremité gauche et droite
            if j == mid - i or j == mid + i:
                print("*", end="")
            else:
                print(" ", end="")
        # Sigma symbol
            # print("ijw: ", i, j, wedge_dimension)
        elif i == wedge_dimension:
            if i == wedge_dimension or i == wedge_dimension + (mid//2): # Premier et dernier ligne pour une barre horizontale
                print("*", end="")
            else:
                if i > wedge_dimension:
                    if j == wedge_dimension // 2:
                        print("*", end="")
                else:
                    if i == j and i < wedge_dimension // 2:
                        print("*", end="")
                    if i == wedge_dimension - j - 1 and i > wedge_dimension //2:
                        print("*", end="")
                print(" ", end="")
        # print("-", end="")
    print("\r")