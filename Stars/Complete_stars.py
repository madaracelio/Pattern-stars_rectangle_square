"""
    @Author: Laza Celio
    @Date: 04/05/2022
    @Links: https://github.com/madaracelio

    n: un entier, qui est la dimension
    Exemple: n = 5
"""

dim = 8
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