# -*- coding: utf-8 -*-

"""
    @Author: Laza Celio
    @Date: 04/05/2022
    @Links: https://github.com/madaracelio

    Une fonction qui affiche la forme d'un rectangle à partir des étoiles.
    rect_length: longueur
    rect_width: largeur
    Exemple: rect_length = 5, rect_width = 3
                    *****
                    *   *
                    *****
"""

def create_rectangle(rect_length, rect_width):
    """
        rect_length: lenght (longueur)
        rect_width: width (largeur)
    """
    if rect_length < 3:
        raise Exception("rect_length (length) must be at least 3.")
    if rect_width < 2:
        raise Exception("rect_width (width) must be at least 2")

    for i in range(rect_width):
        for j in range(rect_length):
            if i == 0 or i == rect_width - 1:
                print("*", end="")
            else:
                if j == 0 or j == rect_length - 1:
                    print("*", end="")
                else:
                    print(" ", end="")
        print("\r")


def full_rectangle(rect_length, rect_width):
    if rect_length < 3:
        raise Exception("rect_length (length) must be at least 3.")
    if rect_width < 2:
        raise Exception("rect_width (width) must be at least 2")

    for i in range(rect_width):
        for j in range(rect_length):
            print("*", end="")
        print("\r")