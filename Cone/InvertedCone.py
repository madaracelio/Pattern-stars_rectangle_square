# -*- coding: utf-8 -*-

"""
    @Author: Laza Celio
    @Date: 04/05/2022
    @Links: https://github.com/madaracelio

    Une fonction qui affiche la forme d'une cône à partir des étoiles mais à l'envers.
    n: un entier, qui est la dimension
    Exemple: n = 5
                    *       *
                     *     *
                      *   *
                       * *
                        *
"""

def create_inverted_cone(n):
    if n < 3:
        raise Exception("Dimension must be at least 3.")

    if n % 2 == 0:
        raise Exception("Dimension must be an odd number.", str(n) + " is even")

    # Parcourir tous les lignes de total n+1 divisé par deux (ex: n = 5, dont 5 colonnes et 3 lignes)
    LINE_NUMBER = (n+1)//2

    # Milieu
    mid = (n - 1)/2
    
    for i in range(LINE_NUMBER):
        # Parcourir les n nombre de colonne
        for j in range(0, n):
            # print("*", end="")
            if i == LINE_NUMBER-1: # i arrive à la dernière ligne
                # si on est à la moitié de la colonne de j
                if j == mid:
                    print("*", end="")
                else:
                    print(" ", end="")
            else:
                # on prend la 1ere position et la dernière, puis on passe sur la 2nde et l'avant dernière, et ainsi de suite
                if j == i or j == n - i - 1:
                    print("*", end="")
                else:
                    print(" ", end="")
        print("\r")
create_inverted_cone(5)