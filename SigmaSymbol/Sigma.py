# -*- coding: utf-8 -*-

"""
    @Author: Laza Celio
    @Date: 04/05/2022
    @Links: https://github.com/madaracelio

    Une fonction permettant d'afficher la forme mathématique "sigma".
    n: un entier, qui est la dimension
    Exemple: n = 5, on aura
                                *****
                                 *
                                  *
                                 *
                                *****
"""

def create_sigma(n):
    if n < 3:
        raise Exception("Dimension must be at least 3.")

    if n % 2 == 0:
        raise Exception("Dimension must be an odd number.", str(n) + " is even")

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