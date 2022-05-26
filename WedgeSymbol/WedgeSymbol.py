# -*- coding: utf-8 -*-

"""
    @Author: Laza Celio
    @Date: 04/05/2022
    @Links: https://github.com/madaracelio

    Une fonction qui affiche la forme d'un symbole véctoriel ^ à partir des étoiles.
    n: un entier, qui est la dimension
    Exemple: n = 5
                        *
                       * *
                      *   *
                     *     *
                    *       *
"""

def create_wedge_symbol(n):
    if n < 3:
        raise Exception("Dimension n must be at least 3.")

    if n % 2 == 0:
        raise Exception("Dimension n must be an odd number.") 

    # Parcourir tous les lignes de total n+1 divisé par deux (ex: n = 5, dont 5 colonnes et 3 lignes)
    LINE_NUMBER = (n+1)//2

    # Milieu
    mid = (n - 1)/2
    
    for i in range(LINE_NUMBER):
        # Parcourir les n nombre de colonne
        for j in range(0, n):
            if i == 0: # i arrive est à la première ligne
                # si on est à la moitié de la colonne de j
                if j == mid:
                    print("*", end="")
                else:
                    print(" ", end="")
            else:
                # on prend ce qui est à gauche et à droite par rapport au milieu, jusqu'à la l'extremité gauche et droite
                if j == mid - i or j == mid + i:
                    print("*", end="")
                else:
                    print(" ", end="")
        print("\r")