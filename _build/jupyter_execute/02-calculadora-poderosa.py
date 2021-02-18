# Uma calculadora poderosa 

O prompt do Python e o Ciclo Ler-Avaliar-Imprimir (LAI) 
---------------------------------------------

Python é uma linguagem *interpretada*. Podemos coletar sequencias de comandos em texto e salvá-los em um arquivo como um *programa Python*. A convenção é que estes arquivos tenham a extensão `.py`, como, por exemplo, `hello.py`.

Podemos também entrar com comandos individuais no `prompt` Python que são imediatamente avaliados e executados pelo interpretador Python. Isto é muito útil para o programador/aprendiz entender como usar certos comandos e depois estendê-los para obter um programa maior. O papel da linguagem Python pode ser descrito como segue: *Ler* o comando, *Avaliar* este comando, *Imprimir* o valor avaliado e repetir o ciclo (*loop*) - isto dá origem à abreviatura LAI. O *prompt* Python é um terminal básico onde você introduz comandos após o marcador `>>>`, como no exemplo a seguir: 

    >>> 2 + 2
    4

A interface LAI que estamos usando é um *notebook Jupyter*. Blocos de código aparecem com um `In` à esquerda deles.

4 + 5

Para editar o código, clique na área de código (célula). Uma borda verde indica que a célula está selecionada (consulte o menu de ajuda, `Help`, do Jupyter Notebook para saber mais sobre os modos de *comando* e *edição*). Em seguida, pressione `shift-enter`.

Calculadora
----------

Operações básicas tais como adição (`+`), subtração (`-`), multiplicação (`*`), divisão (`/`) e exponenciação (`**`) funcionam (na maioria das vezes) como esperado:

10 + 10000

42 - 1.5

47 * 11

10 / 0.5

2**2   # O operador de exponenciação ('à potência de') é **, e NÃO ^

2**3

2**4

2 + 2

# Linhas começando com a tralha (#) indicam um comentário
2 + 2

2 + 2  # é um comentário na mesma linha de código

e, usando o fato que $\sqrt[n]{x} = x^{1/n}$, podemos computar $\sqrt{3} = 1.732050\dots$ usando `**`:

3**0.5

Parentêses podem ser usados para agrupamento:

2 * 10 + 5

2 * (10 + 5)

Divisão inteira
----------------

Em Python 3, a divisão funciona como você esperaria:

15/6

Em Python 2, no entanto, `15/6` retornará `2`.


Este fenômeno é conhecido (em muitas linguages de programação, incluindo C) como *divisão inteira*: pelo fato de termos fornecido dois números inteiros (`15` e `6`) para o operador de divisão, a hipótese é que o valor de retorno seja também do tipo inteiro. A resposta matematicamente correta é um número em ponto flutuante. 

A convenção para divisão inteira é truncar os dígitos fracionários e retornar a parte inteira apenas (i.e., `2` neste exemplo). Ela também pode ser chamada de "divisão por baixo" (*floor division*).


### Como evitar a divisão inteira

Há duas maneiras de evitar o problema da divisão inteira:

1. Use o estilo de divisão do Python 3: isto está disponível mesmo no Python 2 com uma declaração especial de importação:

   ```python
   >>> from __future__ import division
   >>> 15/6
   2.5
   ```

Caso você queira usar `from __future__ import division` em um programa Python, a declaração seria incluída normalmenteno no início do arquivo.

2. Alternativamente, se você assegurar que, pelo menos um número (numerador ou denominador) seja do tipo `float` (ou `complex`), o operador de divisão retornará um número em ponto flutuante. Isto pode ser feito escrevendo `15.` em vez de `15`, ou forçando a conversão do número para `float`, i.e. usando `float(15)` em vez de, simplesmente, `15`:

   ```python
   >>> 15./6
   2.5
   >>> float(15)/6
   2.5
   >>> 15/6.
   2.5
   >>> 15/float(6)
   2.5
   >>> 15./6.
   2.5
   ```

Se você realmente quiser a divisão inteira, poderá usar `//`. Por exemplo, `1//2` retornará `0` tanto em Python 2 quanto em Python 3.

### Por que devo me importar com este problema de divisão?

A divisão inteira pode resultar em problemas surpreendentes: suponha que você esteja escrevendo código para calcular a média $m = (x + y)/2$ de dois números $x$ e  $y$. A primeira tentativa de escrever isto pode ser dada como:

```python
m = (x + y) / 2
```

Suponha que isto seja testado com $x = 0.5$, $y = 0.5$. Então, a linha acima computaria a resposta correta $m  = 0.5$ (porque `0.5 + 0.5 = 1.0`, i.e. 1.0 é um número de ponto flutuante, e assim `1.0/2` seria avaliado como `0.5`). Além disso, poderíamos usar $x = 10$, $y  = 30$, e porque `10 + 30 = 40` e `40/2` seria `20`, obtemos a resposta correta $m = 20$. Entretanto, se tentássemos com os inteiros $x  = 0$ e $y = 1$, então o código retornaria $m  = 0$ (porque `0 + 1 = 1` e `1/2` seria avaliado como `0`), quando, na verdade, $m = 0.5$ seria a resposta correta.

Temos muitas possibilidades para fazer a linha de código acima funcionar seguramente, incluindo estas três formas:
```python
m = (x + y) / 2.0

m = float(x + y) / 2

m = (x + y) * 0.5
```

Este comportamento de divisão inteira é comum entre a maioria das linguagens de programação (incluindo as importantes C, C++ e Fortran). Portanto, devemos estar cientes deste fato.

Funções matemáticas
----------------------

Pelo fato de Python ser uma linguagem de programação com propósitos gerais, funções matemáticas comumente usadas, tais como seno, cosseno, exponencial, logaritmo e muitas outras, estão localizadas no módulo de matemática chamado `math`. Podemos fazer uso delas assim que importarmos este módulo. Por exemplo:

import math
math.exp(1.0)

Usando a função `dir`, podemos listar o diretório de objetos disponíveis no módulo `math`:

dir(math)

Como de costume, a função `help` pode fornecer mais informação acerca do módulo (use `help(math)`) ou de objetos individuais: 

help(math.exp)

O módulo de matemática define as constantes $\pi$ and $e$:

math.pi

math.e

math.cos(math.pi)

math.log(math.e)

Variáveis
---------

Uma *variável* pode ser usada para armazenar um certo valor ou objeto. Em Python, todos os números (e todas as outras coisas mais, incluindo funções, módulos e arquivos) são objetos. Uma variável é criada por atribuição:

x = 0.5

Uma vez que a variável `x` tiver sido criada através da atribuição de 0.5 neste exemplo, podemos fazer uso dela:

x*3

x**2

y = 111
y + 222

Uma variável é substituída se um novo valor for atribuído a ela:

y = 0.7
math.sin(y) ** 2 + math.cos(y) ** 2

O sinal de igual (`=`) é usado para atribuir um valor à uma variável.

largura = 20
altura = 5 * 9
largura * altura

Um valor pode ser atribuído a várias variáveis simultaneamente:

x = y = z = 0  # inicializa x, y e z com 0
x

y

z

Variáveis devem ser criadas com atribuição de valor antes de serem usadas, senão um erro ocorrerá:

# tenta acessar uma variável indefinada
n

Em modo interativo, a última expressão impressa é atribuída à variável `_`. Isto significa que quando você está usando Python como uma calculadora de mesa, é um tanto fácil continuar os cálculos. Por exemplo:

taxa = 12.5 / 100
preco = 100.50
preco * taxa

preco + _

Esta variável deve ser tratada como "somente leitura" pelo usuário. Não atribua, explicitamente, um valor a ela - você criaria uma variável local independente com o mesmo nome assim mascarando o comportamento "mágico" da variável pré-construída.

### Terminologia

Estritamente falando, o seguinte acontece quando escrevemos algo como:

x = 0.5

Primeiro, o Python cria o objeto `0.5`. Tudo em Python é um objeto, e assim o é o número em ponto flutuante 0.5. Este objeto é armazenado em algum lugar na memória. Em seguida, o Python *vincula um nome ao objeto*. O nome é `x`, e nos referimos a `x` casual e frequentemente como uma variável, um objeto, ou mesmo o valor 0.5. Entretanto, tecnicamente, `x` é um nome que é limitado ao objeto `0.5`. Outro modo de dizer isto é que `x` é uma *referência* para o objeto.

Enquanto é frequentemente suficiente pensar em atribuir 0.5 à uma variável `x`, existem situações nas quais precisamos lembrar o que realmente ocorre. Em particular, quando passamos referências de objetos para funções, precisamos ter em mente que a função pode operar sobre o objeto (em vez de uma cópia do objeto).

Equações impossíveis
--------------------

Em programas computacionais, frequentemente encontramos declarações como

x = x + 1

Se lêssemos esta equação do modo como estamos acostumados da matemática, poderíamos subtrair $x$ de ambos os lados de $x = x + 1$ para descobrir que $0 = 1$. Todavia, sabemos que isto não é verdadeiro. Então, algo está errado aqui...

A resposta é que "equações“ em códigos computacionais não são realmente equações, mas *atribuições*. Elas tem de ser lidas em dois passos:

1.  Avaliando o valor no membro direito do sinal de igual;

2.  Atribuindo este valor à variável cujo nome é mostrado no membro esquerdo. (Em Python: vincula-se o nome à esquerda ao objeto mostrado à direita).

Na literatura de ciência da computação, a notação seguinte é usada para expressar atribuições a fim de se evitar confusão com equações matemáticas:

$$x \leftarrow x + 1$$

Vamos aplicar a nossa regra de dois passos à atribuição `x = x + 1` dada acima:

1.  Avalie o valor no membro direito do sinal de igual: para isto, precisamos saber o valor atual de `x`. Assumamos que o valor atual de `x` é `4`. Neste caso, o membro direito, `x+1` é avaliado para `5`.

2.  Atribua este valor (i.e. `5`) à variável cujo nome é mostrado no membro esquerdo (`x`).

Confirmemos com o *prompt* do Python que esta é a interpretação correta:

x = 4     
x = x + 1
x

### A notação `+=` 

Por ser uma operação bastante comum aumentar uma variável `x` por alguma quantidade fixa `c`, podemos escrevê-la como: 

```python
x += c
```

em vez de

```python
x = x + c
```

Nosso exemplo inicial acima poderia, assim, ter sido escrito como:

x = 4
x += 1
x

Os mesmos operadores são definidos para multiplicação por uma constante (`*=`), subtração de uma constante (`-=`) e divisão por uma constante (`/=`).

Note que a ordem de `+` e `=` importa:

x = 1
x += 4
x

aumentará a variável `x` de um, ao passo que

x =+ 1

atribuirá o valor `+1` à variável `x`.