# -*- coding: utf-8 -*-
"""Compara cálculos de \sum_i x_i^2 for i = 0,...N-1

Usamos (i) laços for e list, (ii) laço for, (iii) compreensão de lista
e (iv) numpy.

Usamos números em ponto flutuante para evitar usar os longos inteiros do
Python (que provavelmente fariam a medição do tempo menos representativa)
"""

import time
import numpy
N = 10000000


def timeit(f, args):
    """ Dada uma função f e uma tupla contendo argumentos para f, 
    esta funcao chama f(*args), e mede e retorna o tempo de 
    execucao em segundos.
    
    O valor de retorno é uma tupla: a entrada 0 é o tempo, 
    a entrada 1 é o valor de retorno de f."""

    starttime = time.time()
    y = f(*args)    # usa tupla de argumentos como entrada
    endtime = time.time()
    return endtime - starttime, y


def forloop1(N):
    s = 0
    for i in range(N):
        s += float(i) * float(i)
    return s


def forloop2(N):
    y = [0] * N
    for i in range(N):
        y[i] = float(i) ** 2
    return sum(y)


def listcomp(N):
    return sum([float(x) * x for x in range(N)])


def numpy_(N):
    return numpy.sum(numpy.arange(0, N, dtype='d') ** 2)

# inicio do programa principal
timings = []
print("N =", N)
forloop1_time, f1_res = timeit(forloop1, (N,))
timings.append(forloop1_time)
print("for-loop1", forloop1_time)
forloop2_time, f2_res = timeit(forloop2, (N,))
timings.append(forloop2_time)
print("for-loop2", forloop2_time)
listcomp_time, lc_res = timeit(listcomp, (N,))
timings.append(listcomp_time)
print("listcomp", listcomp_time)
numpy_time, n_res = timeit(numpy_, (N,))
timings.append(numpy_time)
print("numpy", numpy_time)

#assegura que metodos diferentes forneçam resultados idênticos
assert f1_res == f2_res
assert f1_res == lc_res

# Permite um pouco de diferença para o cálculo via numpy
numpy.testing.assert_approx_equal(f1_res, n_res)

print("O metodo mais lento eh {:.1f} vezes mais lento do que o metodo mais rapido.".format(
    max(timings)/min(timings)))