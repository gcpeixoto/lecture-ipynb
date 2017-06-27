from __future__ import division
import math
import numpy as N

def norma(x):
    """retorna a magnitude de um vetor x"""
    return math.sqrt(sum(x ** 2))


def vetor_unitario(x):
    """retorna um vetor unitario x/|x|. x requer um tipo numpy array."""
    xnorm = norma(x)
    if xnorm == 0:
        raise ValueError("Vetor nulo nao pode ser normalizado")
    return x / norma(x)


if __name__ == "__main__":
    # uma pequena demonstracao de como as funcoes neste modulo podem ser usadas:
    x1 = N.array([0, 1, 2])
    print("A norma de " + str(x1) + " eh " + str(norma(x1)) + ".")
    print("O vetor unitario na direcao de " + str(x1) + " eh " \
        + str(vetor_unitario(x1)) + ".")
