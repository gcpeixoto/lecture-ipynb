Ferramentas funcionais
================

A linguagem Python fornece alguns comandos predefinidos, tais como `map`, `filter`, `reduce`, bem como `lambda` (para criar funções anônimas) e compreensões de lista. Tais comandos são típicos de linguagens funcionais, das quais LISP provavelmente é a mais conhecida.

A programação funcional pode ser extremamente poderosa e um dos pontos fortes da linguagem Python é que ela permite programar usando (i) o estilo de programação procedural (ou imperativa), (ii) o estilo orientado a objetos e (iii) o estilo funcional. São os programadores quem escolhem quais ferramentas selecionar, qual estilo e como misturá-los para resolver melhor um determinado problema.

Neste capítulo, fornecemos alguns exemplos para o uso dos comandos listados acima.

Funções anônimas
-------------------

Todas as funções que vimos em Python até agora foram definidas através da palavra-chave `def`. Por exemplo:

def f(x):
     return x ** 2

Esta função tem o nome `f`. Uma vez que a função está definida (ou seja, o interpretador Python encontrou a linha `def`), podemos chamar a função usando seu nome. Por exemplo:

y = f(6)

Às vezes, precisamos definir uma função que só é usada uma vez, ou queremos criar uma função, mas não precisamos de um nome para ela (como para criar fechamentos). Neste caso, isso é chamado de *função anônima*, pois não possui um nome. Em Python, a palavra-chave `lambda` pode criar uma função anônima.

Criamos uma função (nomeada) primeiro, verificamos seu tipo e comportamento:

def f(x):
    return x ** 2

f

type(f)

f(10)

Agora fazemos o mesmo com uma função anônima:

lambda x: x ** 2

type(lambda x: x ** 2)

(lambda x: x ** 2)(10)

Isto funciona exatamente da mesma maneira, mas - como a função anônima não tem um nome - precisamos definir a função (através da expressão `lambda`) - toda vez que precisamos dela.

Funções anônimas podem levar mais de um argumento:

(lambda x, y: x + y)(10, 20)

(lambda x, y, z: (x + y) * z )(10, 20, 2)

Veremos alguns exemplos usando `lambda` que esclarecerão os casos típicos de uso.

`map`
---

A função `lst2 = map(f, s)` aplica uma função `f` a todos os elementos em uma seqüência `s`. O resultado de `map` pode ser convertido em uma lista com o mesmo comprimento que `s`:

def f(x): 
    return x ** 2
lst2 = list(map(f, range(10)))
lst2

list(map(str.capitalize, ['banana', 'maçã', 'laranja']))

Frequentemente, isto é combinado com a função anônima`lambda`:

list(map(lambda x: x ** 2, range(10) ))

list(map(lambda s: s.capitalize(), ['banana', 'maçã', 'laranja']))

`filter`
------

A função `lst2 = filter(f, lst)` aplica a função `f` a todos os elementos em uma sequencia `s`. A função `f` deve retornar `True` ou `False`. Isto faz com que uma lista contenha somente aqueles elementos *s*<sub>*i*</sub> da sequencia `s` para os quais `f`(*s*<sub>*i*</sub>) tem valor de retorno `True`.

def maior_que_5(x):
    if x > 5:
            return True
    else:
            return False

list(filter(maior_que_5, range(11)))

O uso de `lambda` pode simplificar isto significativamente:

list(filter(lambda x: x > 5, range(11)))

nomes_conhecidos = ['smith', 'miller', 'bob']
list(filter( lambda nome : nome in nomes_conhecidos, \
     ['ago', 'smith', 'bob', 'carl']))

Compreensões de lista
------------------

Compreensões de lista fornecem uma maneira concisa de criar e modificar listas sem recorrer ao uso de `map()`, `filter()` e/ou `lambda`. A definição da lista resultante tende a ser mais clara do que as listas criadas usando essas construções. Cada compreensão de lista consiste de uma expressão seguida por uma cláusula `for`, zero ou mais cláusulas ` for` ou `if`. O resultado será uma lista resultante da avaliação da expressão no contexto das cláusulas `for` e `if` que a seguem. Se a expressão for avaliada para uma tupla, ela deverá estar entre parênteses.

Alguns exemplos tornarão isso mais claro:

frutas_frescas = ['  banana', '  framboesa ', 'maracujá  ']
[weapon.strip() for weapon in frutas_frescas]

vec = [2, 4, 6]
[3 * x for x in vec]

[3 * x for x in vec if x > 3]

[3 * x for x in vec if x < 2]

[[x, x ** 2] for x in vec]

Podemos também usar compreensões de lista para modificar a lista de inteiros retornada pelo comando `range`, de modo que nossos elementos subsequentes na lista aumentem por frações não-inteiras. 

[x*0.5 for x in range(10)]

Vamos agora revisitar os exemplos da seção `filter`.

[x for x in range(11) if x>5 ]

[nome for nome in ['ago','smith','bob','carl'] \
      if nome in nomes_conhecidos]

e os exemplos da seção `map`

[x ** 2 for x in range(10) ]

[fruta.capitalize() for fruta in ['banana', 'maçã', 'laranja'] ]

todas podem ser expressas através de compreensões de lista.

Mais detalhes

-   Tutorial Python [5.1.4 Compreensões de lista](http://docs.python.org/tutorial/datastructures.html#list-comprehensions)

`reduce`
------

A função `reduce` assume uma função binária `f(x, y)`, uma sequência `s` e um valor de início `a0`. Em seguida, aplica a função `f` ao valor de início` a0` e o primeiro elemento na seqüência: `a1 = f(a, s[0])`. O segundo elemento (`s [1]`) da sequência é processado da seguinte forma: a função `f` é chamada com argumentos `a1` e `s[1]`, ou seja, `a2 = f (a1, s[1])`. Desta forma, toda a sequência é processada. `reduce` retorna um único número.

Isso pode ser usado, por exemplo, para calcular uma soma de números em uma seqüência se a função `f(x, y)` retornar `x + y`:

from functools import reduce

def add(x,y):
    return x+y

reduce(add, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0)

reduce(add, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 100)

Podemos modificar a função `add` para fornecer algum detalhe a mais sobre o processo:

def add_verbose(x, y):
    print("add(x=%s, y=%s) -> %s" % (x, y, x+y))
    return x+y

reduce(add_verbose, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0)

Pode ser instrutivo usar uma função assimétrica `f`, tal como `add_len(n,s)`, onde `s` é uma sequencia e a função retorna `n+len(s)` (sugestão de Thomas Fischbacher):

def add_len(n,s):
    return n+len(s)

reduce(add_len, ["Este","é","um","teste."],0)

Como antes, usaremos uma versão mais prolixa (verbosa) da função binária para vermos o que está acontecendo:

def add_len_verbose(n,s):
    print("add_len(n=%d, s=%s) -> %d" % (n, s, n+len(s)))
    return n+len(s)

reduce(add_len_verbose, ["Este","é","um","teste."],0)

Outra maneira de entender o que a função `reduce` faz é examinar a seguinte função (gentilmente fornecida por Thomas Fischbacher), que se comporta como `reduce`, mas explica o que ela faz:

Aqui está um exemplo usando a função `explain_reduce`.

cd code/

from explain_reduce import explain_reduce
def f(a,b):
    return a+b

reduce(f, [1,2,3,4,5], 0)

explain_reduce(f, [1,2,3,4,5], 0)

`reduce` é frequentemente combinado com `lambda`:

reduce(lambda x,y:x+y, [1,2,3,4,5], 0)

Existe também o módulo `operator` que fornece operadores Python padrão como funções. Por exemplo, a função `operator.__add__(a, b)` é executada quando o Python avalia o código como `a + b`. Estes geralmente são mais rápidos do que as expressões `lambda`. Poderíamos escrever o exemplo acima como

import operator
reduce(operator.__add__, [1,2,3,4,5], 0)

Use `help(’operator’)` para ver a lista completa de funções `operator`.

Por que não usar apenas laços `for`?
---------------------------

Vamos comparar o exemplo apresentado no início do capítulo escrito (i) usando um laço `for` e (ii) compreensão de lista. Mais uma vez, queremos calcular os números 0<sup>2</sup>, 1<sup>2</sup>, 2<sup>2 </sup>, 3<sup>2</sup>,... até (*n* - 1)<sup>2</sup> para um dado *n*.

Implementação (i) usando um laço `for` com *n* = 10:

y = []
for i in range(10):
    y.append(i ** 2)

Implementação (ii) usando compreensão de lista:

y = [x ** 2 for x in range(10)]

ou usando `map`:

y = map(lambda x: x ** 2, range(10))

As versões que utilizam compreensão de lista e `map` encaixam-se em uma linha de código, enquanto um laço `for` precisa de três linhas. Este exemplo mostra que o código funcional resulta em expressões *concisas*. Normalmente, o número de erros que um programador comete é por linha de código escrita, de modo que quanto menos linhas de código tivermos, menos *bugs* teremos de encontrar.

Muitas vezes, os programadores descobrem que, inicialmente, as ferramentas de processamento de lista apresentadas neste capítulo parecem menos intuitivas do que o uso de laços `for` para processar cada elemento em uma lista individualmente, mas isso - ao longo do tempo - tende a ser valorizado por eles como um estilo de programação mais funcional.

Rapidez
-----

As ferramentas funcionais descritas neste capítulo também podem ser mais rápidas do que laços explícitos (`for` ou `while`) sobre os elementos da lista.

O programa `rapidez_compreensao_lista.py` abaixo calcula $\sum_{i=0}^{N-1} i^2$ para um grande valor de *N* usando 4 métodos diferentes e registra o tempo de execução:

- Método 1: laço `for` (com lista pré-alocada, armazenamento de *i*<sup>2</sup> na lista, em seguida, usando a função predefinida `sum`)

- Método 2: laço `for` sem lista (atualizando `sum` à medida que o laço `for` progride)

- Método 3: usando compreensão de lista

- Método 4: usando `numpy`.

O programa produz a seguinte saída:

!python static/data/rapidez_compreensao_lista.py

O desempenho de execução real depende do computador. O desempenho relativo pode depender de versões do Python e suas bibliotecas de suporte (como `numpy`) que usamos.

Com a versão atual (python 3.4, numpy 1.10, em uma máquina x64 que executa o OSX), vemos que os métodos 1 e 2 (para laço sem lista e com lista pré-alocada) são mais lentos, seguidos um tanto mais próximos de uma compreensão de lista levemente mais rápida. O método mais rápido é o número 4 (usando numpy).

Para referência, aqui está o código-fonte do programa:

!cat static/data/rapidez_compreensao_lista.py