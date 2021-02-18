Computação numérica
=====================

Números e números
-------------------

Já vimos que o Python reconhece diferentes *tipos* de números:

- números em ponto flutuante (`float`), como 3.14

- inteiros (`int`) como 42

- números complexos (`complex`), como 3.14 + 1*j

### Limitações dos tipos de números

#### Limitações de `int`s

A matemática fornece o conjunto infinito dos números naturais $\mathbb{ℕ} = \{1, 2, 3,\dots \}$. Como o computador opera de modo *finito*, é impossível que ele represente todos esses números. Em vez disso, apenas um pequeno subconjunto de números é representado.

O tipo `int` (geralmente [3]) representa números entre -2147483648 e +2147483647, e corresponde a 4 *bytes* (isto é 4\*8 *bits* e 2<sup>32</sup> = 4294967296, que é o intervalo de -2147483648 a +2147483647).

Você pode imaginar que o hardware usa uma tabela como esta para codificar inteiros usando bits (suponha, por simplicidade, que usemos apenas 8 *bits*):

| número natural |representação binária|
|---------------:|-------------------:|
|               0|            00000000|
|               1|            00000001|
|               2|            00000010|
|               3|            00000011|
|               4|            00000100|
|               5|            00000101|
|               ⋮|                   ⋮|
|             254|            11111110|
|             255|            11111111|

Usando 8 *bits*, podemos representar 256 números naturais (por exemplo, de 0 a 255), pois temos 2<sup>8</sup> = 256 formas diferentes de combinar oito 0s e 1s.

Poderíamos também usar uma tabela ligeiramente diferente para descrever 256 números inteiros que variem, por exemplo, de -127 a +128.

Assim é, *em princípio*, como os números inteiros são representados no computador. Dependendo do número de *bytes* utilizados, apenas números inteiros entre um valor mínimo e um máximo podem ser representados. Nos hardwares de hoje, é comum usar 4 ou 8 *bytes* para representar um número inteiro, o que leva exatamente aos valores mínimo e máximo de -2147483648 e +2147483647, como mostrado acima para 4 *bytes*, e +9223372036854775807 como o inteiro máximo para 8 *bytes* (isto é ≈ 9.2⋅10<sup>18</sup>).

#### Limitações de `float`s

Os números em ponto flutuante em um computador não são os mesmos que os números em ponto flutuante da matemática. (Isto é exatamente o mesmo que dize que os números inteiros (matemáticos) não são os mesmos em um computador: apenas um *subconjunto* do conjunto infinito dos números inteiros pode ser representado pelo tipo `int`, como mostrado anteriormente). Então, como os números em ponto flutuante são representados no computador?

- Qualquer número real $x$ pode ser escrito como
     $$x  = a \cdot 10^b,$$

onde $a$ é a mantissa e $b$ o expoente.
      
- Exemplos: 

| $x$                               | $a$     | $b$|
|-----------------------------------|---------|----|
| 123.45 = 1.23456 ⋅ 10<sup>2</sup> | 1.23456 |  2 |
| 1000000 = 1.0 ⋅ 10<sup>6</sup>    | 1.00000 |  6 |
| 0.0000024 = 2.4 ⋅ 10<sup>-6</sup> | 2.40000 | -6 |

- Portanto, podemos usar 2 inteiros para codificar um número em ponto flutuante!

- Seguindo (aproximadamente) o padrão IEEE-754, usa-se 8 *bytes* para um `float` $x$: estes 64 bits são divididos entre

     - 10 bits para o expoente $b$ e

     - 54 bits para a mantissa $a$.

Isto resulta em

- maior número em ponto flutuante possível ≈ 10 <sup>308</sup> (medida de qualidade para *b*)

- menor número em ponto flutuante possível (positivo) ≈ 10 <sup>-308</sup> (medida de qualidade para $b$)

- distância entre 1.0 e o número imediatamente superior ≈ 10<sup>-16</sup> (medida de qualidade para $a$)

Observe que, *a priori*, é assim como os números em ponto flutuante são armazenados (na realidade, é um pouco mais complicado).


#### Limitações dos números complexos

O tipo `complex` tem essencialmente as mesmas limitações que o tipo `float` porque um número complexo consiste de dois números `float`: um representa a parte real, o outro a parte imaginária.

#### ... são esses tipos de números de valor prático?

Na prática cotidiana, geralmente não encontramos números que excedam 10<sup>300</sup> (este é um número com 300 zeros!). Portanto, os números em ponto flutuante cobrem o intervalo de números de que geralmente precisamos.

No entanto, você precisa estar ciente de que, em computação científica, números pequenos e grandes são usados, os quais podem (geralmente em resultados intermediários) exceder o intervalo de números em ponto flutuante.

- Imagine, por exemplo, que tenhamos de calcular a quarta potência da constante ℏ = 1.0545716 ⋅ 10 <sup>-34</sup> *kg. m<sup>2</sup>/s*: 

- ℏ <sup>4</sup> = 1.2368136958909421 ⋅ 10 <sup>-136</sup> *kg<sup>4</sup>.m<sup>8</sup>/s<sup>4</sup>*, que está a "meio caminho" de nosso menor `float` positivo representável da ordem de 10<sup>-308</sup>.

Se houver algum perigo de que possamos exceder os limites dos números em ponto flutuante, teremos que *escalonar* nossas equações de modo que (idealmente) todos os números sejam da ordem de 1. Escalonar nossas equações para que todos os números relevantes sejam próximos de 1 (normalização) também é útil para a depuração de código: se números muito maiores ou menores do que 1 surgirem, isso pode ser uma indicação de erro.

### Usando números de ponto flutuante (sem o devido cuidado)

Já sabemos que precisamos ter cuidado para que nossos valores em ponto flutuante não excedam os limites que podem ser representados no computador (*underflow* e *overflow*). Há outra complicação devido à forma como os números em ponto flutuante têm de ser representados internamente: nem todos eles podem ser representados exatamente no computador. O número 1.0 pode ser representado exatamente, mas os números 0.1, 0.2 e 0.3 não:

'%.20f' % 1.0

'%.20f' % 0.1

'%.20f' % 0.2

'%.20f' % 0.3

Em vez disso, o número em ponto flutuante "mais próximo" do número real é escolhido.

Isso pode causar problemas. Suponha que precisemos de um laço onde `x` tome os valores 0,1, 0,2, 0,3, ..., 0,9, 1,0. Podemos ser tentados a escrever algo como:

```python
x = 0.0
while not x == 1.0:
    x = x + 0.1
    print (" x = %19.17f" % ( x ))
```

Entretanto, este laço nunca terminará. Aqui estão as primeiras 11 linhas de saída do programa:

    x=0.10000000000000001
    x=0.20000000000000001
    x=0.30000000000000004
    x=0.40000000000000002
    x=                0.5
    x=0.59999999999999998
    x=0.69999999999999996
    x=0.79999999999999993
    x=0.89999999999999991
    x=0.99999999999999989
    x=1.09999999999999987

Como a variável `x` nunca assume exatamente o valor 1.0, o laço `while` continuará infinitamente.

Portanto: **Nunca compare dois números em ponto flutuante por igualdade!**

### Usando números de ponto flutuante sem o devido cuidado - 1

Há várias alternativas para resolver este problema. Por exemplo, podemos comparar a distância entre dois números em ponto flutuante:

x = 0.0
while abs(x - 1.0) > 1e-8:
    x = x + 0.1
    print ( " x =%19.17f" % ( x ))

### Usando números de ponto flutuante sem o devido cuidado - 2

Alternativamente, podemos iterar sobre uma sequência de inteiros e calcular o número em ponto flutuante a partir do inteiro:

for i in range (1 , 11):
    x = i * 0.1
    print(" x =%19.17f" % ( x ))

x=0.10000000000000001
x=0.20000000000000001
x=0.30000000000000004
x=0.40000000000000002
x=                0.5
x=0.60000000000000009
x=0.70000000000000007
x=0.80000000000000004
x=0.90000000000000002
x=                  1

Se compararmos esta saída com aquela do programa do caso 1, veremos que os números em ponto flutuante diferem. Isto significa que - em cálculo numérico - não é verdade que 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 = 1.0.

### Cálculo simbólico

Usando o pacote SymPy, temos precisão arbitrária. Usando `sympy.Rational`, podemos definir a fração 1/10 exatamente com o cálculo simbólico. Adicionando a fração 10 vezes, seremos levados exatamente ao valor 1, conforme demonstrado por este script:

from sympy import Rational
dx = Rational (1 ,10)
x = 0
while x != 1.0:
    x = x + dx
    print("Atual x=%4s = %3.1f " % (x , x . evalf ()))
    print(" Atingido x=%s " % x)

No entanto, esse cálculo simbólico é muito mais lento, já que é feito através de software em vez de operações de ponto flutuante baseadas em CPU. O próximo programa aproxima os desempenhos relativos:

from sympy import Rational
dx_simbolico = Rational (1 ,10)
dx = 0.1

def loop_sympy (n):
    x = 0
    for i in range(n):
        x = x + dx_simbolico
    return x

def loop_float(n):
    x =0
    for i in range(n):
        x = x + dx
    return x

def medir_tempo(f, n):
    import time
    tempo_inicial = time.time()
    resultado = f(n)
    tempo_final = time.time()
    print(" desvio eh %16.15g" % ( n * dx_simbolico - resultado ))
    return tempo_final - tempo_inicial

n = 100000
print("laço usando float dx:")
tempo_float = medir_tempo(loop_float, n)
print("laço float n=%d leva %6.5f segundos" % (n, tempo_float))
print("laço usando sympy simbólico dx:")
tempo_sympy = medir_tempo(loop_sympy, n)
print("laço sympy n =% d leva %6.5f segundos" % (n , tempo_sympy ))
print("laço simbólico é um fator %.1f mais lento." % ( tempo_sympy / tempo_float ))

Este é, naturalmente, um exemplo artificial: adicionamos o código simbólico para demonstrar que esses erros de arredondamento originam-se da representação aproximada de números em ponto flutuante no hardware (e, portanto, linguagens de programação). Podemos, em princípio, evitar essas complicações através de cálculo com expressões simbólicas, mas, na prática, isso é muito lento. [4]

### Resumo

Em resumo, aprendemos que

- números em ponto flutuante e inteiros utilizados em computação numérica geralmente são bastante diferentes dos "números matemáticos" (os cálculos simbólicos são exatos e usam os "números matemáticos"):

    - há um número máximo e um número mínimo que podem  ser representados (tanto para números inteiros como para ponto flutuante)

    - dentro desse intervalo, nem todo número em ponto flutuante pode ser representado no computador.

- lidamos com essa limitação:

    - nunca comparando dois números em ponto flutuante por igualdade (em vez disso, calculamos o valor absoluto da diferença)

    - uso de algoritmos que são *estáveis* (isto significa que pequenos desvios de números corretos podem ser corrigidos pelo algoritmo. Ainda não mostramos nenhum exemplo desse tipo neste documento.)

- Observe que há muito mais a dizer sobre métodos numéricos e técnicas algorítmicas para tornar a computação numérica tão precisa quanto possível, mas isto está fora do escopo desta seção.

### Exercício: laço finito ou infinito

1.  O que o seguinte fragmento de código computa? O laço terminará? Por quê?

```python
eps = 1.0
while 1.0 + eps > 1.0:
    eps = eps / 2.0
print(eps)
```