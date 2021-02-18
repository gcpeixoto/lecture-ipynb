Tipos de Dados e Estruturas de Dados
==============================

O que é um tipo de dado?
----------------

A linguagem Python reconhece diferentes tipos de dados. Para encontrar o tipo de uma variável, use a função `type()`: 

a = '45'
b = 45

int(a)+b

print(a)
print(b)
type(a),type(b)


b = 'Isto é uma string'
type(b)

Devo me lembrar que um número complexo é composto de uma parte real e um a parte imaginária. Em Python, eu escrevo um NC assim:

c = 2 + 1j
type(c)

d = [1, 3, 56]
type(d)

Números
-------

##### Informação adicional

-   Introdução informal aos números. [Python tutorial, seção 3.1.1](http://docs.python.org/tutorial/introduction.html#using-python-as-a-calculator)

-   Python Library Reference: visão geral formal de tipos numéricos, <http://docs.python.org/library/stdtypes.html#numeric-types-int-float-long-complex>

-   Pense em Python, [Seção 2.1](http://penseallen.github.io/PensePython2e/02-vars-expr-instr.html)

Os tipos de dados predefinidos são números inteiros, ponto flutuante e ponto flutuante complexos.

### Inteiros

Se precisarmos converter uma *string* contendo um número inteiro para um inteiro, podemos usar a função `int()`:

a = '34'       # a é uma string contendo os caracteres 3 e 4
x = int(a)     # x é um número inteiro

A função `int()` também converterá números em ponto flutuante para inteiros:

int(7.0)

int(7.9)

Note que `int` truncará qualquer parte não inteira de um número em ponto flutuante. Para arredondar um número em ponto flutuante para inteiro, use o comando `round()`:

round(7.9)

### Limites de Inteiro

Inteiros em Python 3 são ilimitados; o interpretador Python automaticamente atribuirá tanta memória quanto necessária à medida que os números ficarem maiores. Isto significa que calculamos números muito grandes sem passos especiais.

35**42

Em muitas outras linguagens de programação, tais como C e FORTRAN, inteiros ocupam um tamanho fixo de 4 bytes, permitindo $2^{32}$ valores diferentes, mas tipos diferentes estão disponíveis com diferentes tamanhos. Para números que cabem dentro desses limites, os cálculos podem ser mais rápidos, mas você pode ter de verificar que os números não excedam os limites. Calcular um número além dos limites é o mesmo que incorrer em *overflow de inteiro*, e pode produzir resultados estranhos.

Mesmo em Python, precisamos estar cientes disto quando usamos o NumPy. O NumPy usa inteiros com um tamanho fixo porque ele armazena muitos deles juntos e precisa calculá-los eficientemente. A documentação sobre [tipos de dados do NumPy](http://docs.scipy.org/doc/numpy/user/basics.types.html) inclui uma gama de tipos inteiros denominados pelo tamanho deles. Então, `int16`, por exemplo, é um inteiro de 16 bits, com $2^{16}$ valores possíveis. 

Inteiros podem também ser do tipo *signed*, quando permitem valores positivos ou negativos, ou do tipo *unsigned*, quando permitem apenas valores positivos. Por exemplo:

* `uint16` (*unsigned*) varia de 0 a $2^{16}-1$
* `int16` (*signed*) varia de $-2^{15}$ a $2^{15}-1$

### Números em Ponto Flutuante

Uma string contendo um número em ponto flutuante pode ser convertida em um ponto flututante usando o comando `float()`:

a = '35.342'
b = float(a)
b

type(b)

### Números Complexos 

A linguagem Python (assim como Fortran e Matlab) possui números complexos predefinidos. Aqui estão alguns exemplos sobre como usá-los:

x = 1 + 3j
x

abs(x)               # calcula o valor absoluto 

x.imag

x.real

x * x

x * x.conjugate()

3 * x

Note que se você desejar executar operações mais complicadas (tais como calcular a raiz quadrada, etc.) você terá que usar o módulo `cmath` (Complex MATHematics):

import cmath

cmath.sqrt(x)

### Funções aplicáveis a todos os tipos de números

A função `abs()` retorna o valor absoluto (módulo) de um número:

a = -45.463
abs(a)

Note que `abs()` também funciona para números complexos (veja acima).

Sequencias
---------

Sequencias de caracteres (`string`), listas (`lists`) e tuplas (`tuples`) são *sequencias*. Elas podem ser *indexadas* e *fatiadas* da mesma maneira.

Tuplas e *strings* são “imutáveis” (*immutable*). Basicamente, isto significa que não podemos alterar elementos individuais dentro da tupla, nem alterar caracteres individuais dentro de uma *string*, ao passo que listas são "mutáveis" (*mutable*), ou seja, podemos alterar seus elementos.

As sequencias compartilham as seguintes operações:

<table>
<tr><td>`a[i]`</td><td>retorna o *i*-ésimo elemento de `a`</td></tr>
<tr><td>`a[i:j]`</td><td>retorna elementos de *i* até *j* − 1</td></tr>
<tr><td>`len(a)`</td><td>retorna o número de elementos na sequencia</td></tr>
<tr><td>`min(a)`</td><td>retorna o menor valor na sequencia</td></tr>
<tr><td>`max(a)`</td><td>retorna o maior valor na sequencia</td></tr>
<tr><td>`x in a`</td><td>retorna verdadeiro (`True`) se `x` for um elemento de `a`</td></tr>
<tr><td>`a + b`</td><td>concatena `a` e `b`</td></tr>
<tr><td>`n * a`</td><td>cria `n` cópias da sequencia `a`</td></tr>
</table>

### Tipo de Sequencia 1: String

##### Informação adicional

-   Introdução às strings, [Python tutorial 3.1.2](http://docs.python.org/tutorial/introduction.html#strings)

Uma *string* (imutável) pode ser definida usando aspas simples:

a = 'Hello World'

aspas duplas:

a = "Hello World"

ou aspas triplas da mesma espécie

a = """Hello World"""
a = '''Hello World'''

O tipo de uma *string* é `str` e uma *string* vazia é dada por `""`:

a = "Hello World"
type(a)

b = ""
type(b)

type("Hello World")

type("")

O número de caracteres em uma *string* (isto é, seu *comprimento*) pode ser obtido usando a função `len()`:

a = "Hello Moon"
len(a)

a = 'teste'
len(a)

len('outro teste')

Você pode combinar (“concatenar”) duas *strings* usando o operador `+`:

'Hello ' + 'World'

*Strings* possuem um número de métodos úteis, incluindo, por exemplo `upper()`, que retorna a *string* em maiúsculas:

a = "Esta é uma sentença de teste."
a.upper()

Uma lista de métodos disponíveis para *strings* pode ser encontrada na documentação de referência. Se um *prompt* Python estiver disponível, deve-se usar as funções `dir` e `help` para recuperar esta informação, i.e. `dir()` fornece a lista de métodos; `help` pode ser usada para aprender sobre cada método. 

Um método particularmente útil é `split()`, o qual converte uma string em uma lista de strings:

a = "Esta é uma sentenca de teste."
a.split()

O método `split()` separará a string onde ele encontrar um *espaço em branco*. Um espaço em branco signifca qualquer caracter que é impresso como um espaço em branco, tais como um espaço, vários espaços ou uma indentação de parágrafo (tab).  

Se um caracter separador for passaado como argumento para o método `split()`, uma string pode ser dividida em diferentes partes. Suponha que, por exemplo, queiramos obter uma lista de sentenças completas:

a = "O cão está com fome. O gato está entendiado. A cobra está acordada."
a.split(".")

O método oposto a `split` é `join`, o qual pode ser usado como segue:

a = "O cão está com fome. O gato está entendiado. A cobra está acordada."
s = a.split('.')
s

".".join(s)

" PARE".join(s)

### Tipo de sequencia 2 : Lista

##### Informação adicional

-   Introdução a Listas, [Python tutorial, seção 3.1.4](http://docs.python.org/tutorial/introduction.html#lists)

Uma lista é uma sequencia de objetos. Os objetos podem ser de qualquer tipo. Por exemplo, inteiros:

a = [34, 12, 54]

ou *strings*:

a = ['cão', 'gato', 'rato']

Uma lista vazia é contruída com `[]`:

a = []

O tipo é `list`:

type(a)

type([])

Assim como *strings*, o número de elementos em uma lista pode ser obtido usando a função `len()`:

a = ['cão', 'gato', 'rato']
len(a)

Também é possível *misturar* diferentes tipos de dados em uma mesma lista:

a = [123, 'pato', -42, 17, 0, 'elefante']

Em Python, uma lista é um objeto. Portanto, é possível que uma lista contenhaoutras listas (porque uma lista guarda uma sequencia de objetos):

a = [1, 4, 56, [5, 3, 1], 300, 400]

Você pode combinar (“concatenar”) duas listas usando o operator `+`:

[3, 4, 5] + [34, 35, 100]

Ou você pode adicionar um objeto ao fim de uma lista usando o método `append()`:

a = [34, 56, 23]
a.append(42)
a

Você pode deletar um objeto a partir de uma lista chamando o método `remove()` e passando o objeto a ser deletado. Por exemplo:

a = [34, 56, 23, 42]
a.remove(56)
a

#### O comando range()

Um tipo especial de lista é frequentemente requerido (na maioria das vezes, junto com laços `for`) e, portanto, existe um comando para gerar essa lista: o comando `range(n)` gera inteiros começando de 0 e indo até n, exclusive (n não entra). Aqui estão alguns exemplos:

list(range(3))

list(range(10))

Este comando é frequentemente usando com laços `for`. Por exemplo, para imprimir os números 0<sup>2</sup>,1<sup>2</sup>,2<sup>2</sup>,3<sup>2</sup>,…,10<sup>2</sup>, o seguinte programa pode ser usado:

for i in range(11):
    print(i ** 2)

O comando `range` toma um parâmetro opcional para ser o início da sequencia de inteiros (start) e outro parâmetro opcional para o tamanho do passo. Isto é frequentemente escrito como `range([start],stop,[step])`, onde os argumentos entre colchetes (*i.e.* start e step) são opcionais. Aqui estão alguns exemplos:

list(range(3, 10))            # start=3

list(range(3, 10, 2))         # start=3, step=2

list(range(10, 0, -1))        # start=10,step=-1

Por que estamos invocando `list(range())`?

Em Python 3, `range()` gera os números sob demanda. Quando você usa `range()` em um laço `for`, isto é mais eficiente 
porque ele não utiliza memória com uma lista de números. Passando-o para `list()`, nós o forçamos a gerar todos os seus números, assim vendo o que ele faz.

Para obter o mesmo comportamento eficiente em Python 2, use `xrange()` em vez de `range()`.

### Tipo de Sequencia 3: Tuplas

Uma tupla (*tuple*) é  uma sequencia (imutável) de objetos. Tuplas são muito similares em comportamento a listas com a exceção de que não podem ser modificadas (i.e. são imutáveis).

Por exemplo, os objetos em uma sequencia podem ser de qualquer tipo:

a = (12, 13, 'cão')
a

a[0]

Os parênteses não são necessários para definir uma tupla: apenas uma sequencia de objetos separadas por vírgulas é suficiente para definir uma tupla:

a = 100, 200, 'pato'
a

embora seja boa prática de programação incluir os parênteses onde eles ajudam a mostrar que uma tupla está definida.
Tuplas podem também ser usadas para fazer duas atribuições ao mesmo tempo:

x, y = 10, 20
x

y

Isto pode ser usado para fazer um *swap* dos objetos. Por exemplo,

x = 1
y = 2
x, y = y, x
x

y

A tupla vazia é dada por `()`

t = ()
len(t)

type(t)

A notação para uma tupla contendo um valor pode parecer um pouco estranha, em princípio:

t = (42,)
type(t)

len(t)

A vírgula adicional é necessária para distinguir `(42,)` de `(42)`, em que, no segundo caso, os parênteses seriam interpretados como um operador de precedência: `(42)` simplifica-se para `42`, que é apenas um número:

t = (42)
type(t)

Este exemplo mostra a imutabilidade de uma tupla:

a = (12, 13, 'cão')
a[0]

a[0] = 1 # tenta-se alterar o primeiro elemento da tupla de 12 para 1

A imutabilidade é a principal diferença entre uma tupla e uma lista, que é mutável. Devemos usar tuplas quando não quisermos que o conteúdo seja alterado.

Note que as funções em Python que retornam mais do que um valor, os retornam em tuplas (isto faz sentido porque você não deseja que estes valores sejam alterados).

### Indexando sequencias

##### Informação adicional

-   Introdução a *strings* e indexação: [Python tutorial, seção 3.1.2](http://docs.python.org/tutorial/introduction.html#strings), a seção relevante está começando depois que as strings foram apresentadas.

Objetos individuais em listas podem ser acessados usando o índice do objeto e colchetes (`[` e `]`):

a = ['cão', 'gato', 'rato']
a[0]

a[1]

a[2]

Note que em Python (assim como em C, mas diferentemente de Fortran e Matlab), o *índice começa a contar a partir de zero!*

Python fornece um atalho bastante útil para recuperar o último elemento em uma lista: para isto, usa-se o índice “-1”, onde o sinal de menos indica que é um elemento *do final* da lista. Semelhantemente, o índice “-2” retornará o penúltimo elemento:

a = ['cão', 'gato', 'rato']
a[-1]

a[-2]

Se você preferir, você pode pensar no índice `a[-1]` como uma notação compacta para `a[len(a) - 1]`.

Lembre-se que *strings* (assim como listas) também são um tipo de sequencia e podem ser indexadas da mesma maneira:

a = "Hello World!" 
a[0]

a[1]

a[10]

a[-1]

a[-2]

### Fatiando sequencias

#####  Informação adicional

-   Introdução a *strings*, indexação e fatiamento no [Python tutorial, seção 3.1.2](http://docs.python.org/tutorial/introduction.html#strings)

O fatiamento (*slicing*) de sequencias pode ser usado para recuperar mais do que um elemento. Por exemplo:

a = "Hello World!"
a[0:3]

Escrevendo `a[0:3]`, buscamos os 3 primeiros elementos começando do índice 0. Semelhantemente:

a[1:4]

a[0:2]

a[0:6]

Podemos usar índices negativos para nos referirmos ao fim da sequencia:

a[0:-1]

Também é possível ignorar índices do início ou fim da sequencia, assim retornando todos os elementos exceto os ignorados. Aqui estão alguns exemplos para tornar isto mais claro:

a = "Hello World!"
a[:5]

a[5:]

a[-2:]

a[:]
b = a

Note que `a[:]` gerará uma *cópia* de `a`. O uso de índices no fatiamento é feito por pessoas experientes em contagem intuitiva. Se você se sentir desconfortável com o fatiamento, dê uma olhada nesta citação do [Python tutorial (seção 3.1.2)](http://docs.python.org/tutorial/introduction.html#strings):

> A melhor maneira de lembrar como as fatias funcionam é pensar como se os índices apontassem entre os caracteres, com a aresta esquerda do primeiro caracter numerada de 0. Então, a aresta direita do último caracter de uma *string* de 5 caracteres tem índice 5. Por exemplo:
>
>      +---+---+---+---+---+ 
>      | H | e | l | l | o |
>      +---+---+---+---+---+ 
>      0   1   2   3   4   5   <-- use para INDEXAÇÃO
>     -5  -4  -3  -2  -1       <-- use para INDEXAÇÃO a partir do final
>
> A primeira linha de números fornece a posição dos índices de fatiamento 0...5 na string; a segunda linha fornece os índices negativos correspondentes. A fatia de i até j consiste de todos os caracteres entre as arestas rotuladas de i e j, respectivamente.

Assim, o ponto importante é que para o fatiamento (*slicing*), devemos pensar os índices como se apontassem entre os caracteres.

Para indexação (*indexing*), é melhor pensar como se os índices apontassem para os caracteres. Aqui está um pequeno resumo gráfico dessas regras:

       0   1   2   3   4    <-- use para INDEXAÇÃO
      -5  -4  -3  -2  -1    <-- use para INDEXAÇÃO a partir do final
     +---+---+---+---+---+          
     | H | e | l | l | o |
     +---+---+---+---+---+ 
     0   1   2   3   4   5  <-- use para FATIAMENTO
    -5  -4  -3  -2  -1      <-- use para FATIAMENTO a partir do final
                             

Se você não estiver certo sobre qual é o índice correto, é sempre uma boa técnica brincar um pouco com um pequeno exemplo no *prompt* do Python para testar as coisas antes e/ou durante a escrita de seus programas.

### Dicionários

Dicionários são também chamados de “arrays associativos” ou "tabelas hash" (“hash tables”). Dicionários são conjuntos *não-ordenados* de pares *palavra-chave/valor* (*key/value*).

Um dicionário vazio pode ser criado usando chaves:

d = {}

Pares palavra-chave/valor podem ser adicionados como:

d['hoje'] = '22 graus C'    # 'hoje' é a palavra-chave

d['ontem'] = '19 graus C'

`d.keys()` retorna uma lista de todas as palavras-chave:

d.keys()

Podemos recuperar valores usando a palavra-chave como índice:

d['hoje']

Outras maneiras de preencher um dicionário se os dados são conhecidos no momento da criação são:

d2 = {2:4, 3:9, 4:16, 5:25}
d2

d3 = dict(a=1, b=2, c=3)
d3

A função `dict()` cria um dicionário vazio.

Outros métodos úteis de dicionário incluem `values()`, `items()` e `get()`. Você pode usar `in` para verificar a presença de valores.

d.values()

d.items()

d.get('hoje','desconhecido')

d.get('amanhã','desconhecido')

'hoje' in d

'amanhã' in d

O método `get(key,default)` fornecerá o valor para uma dada `key` se essa palavra-chave existir, caso contrário ela retornará o objeto `default`. Aqui está um exemplo mais complexo:

order = {}        # cria um dicionário vazio

#adiciona pedidos à medida que chegam 
order['Pedro'] = 'Uma lata de cerveja'
order['Paulo'] = 'Um suco de laranja'
order['Maria'] = 'Uma lata de agua tônica'

#entrega pedidos no bar
for person in order.keys():
    print(person, "solicita", order[person])

Algumas tecnicalidades adicionais:

-   A palavra-chave pode ser qualquer objeto Python (imutável). Nisto incluem:

    -   números

    -   strings

    -   tuplas.

-   dicionários são muito rápidos na recuperação de valores (uma vez dada a palavra-chave)

Um outro exemplo para demonstrar a vantagem de se usar dicionários em vez de pares de listas:

dic = {}                        # cria dicionário vazio

dic["Helio"]   = "sala 1033"    # preenche dicionário
dic["Anderson C"] = "sala 1031" # "Anderson C" é a chave
dic["Kennedy"]    = "sala 1027" # "sala 1027" é o valor

for key in dic.keys():
    print(key, "trabalha na", dic[key])

Sem o dicionário:

pessoas = ["Helio","Anderson C","Kennedy"]
salas  = ["sala 1033","sala 1031","sala 1027"]

# possivel inconsistencia aqui visto que temos duas listas
if not len( pessoas ) == len( salas ):
    raise RuntimeError("pessoas e salas diferem em comprimento")

for i in range( len( salas ) ):
    print(pessoas[i],"trabalha na",salas[i])

Passando argumentos para funções
------------------------------

Esta seção contém algumas ideias mais avançadas e faz uso de conceitos que serão somente apresentados mais tarde neste texto. A seção pode ser mais facilmente acessível em um estágio posterior.

Quando objetos são passados para uma função, o Python sempre passa (o valor da) referência do objeto para a função. Efetivamente, isto significa chamar a função *por referência*, embora nos refiramos a isto como chamar por *valor* (da referência).

Revisaremos a passagem de argumentos por valor e por referência antes de discutirmos outras situação em Python com maiores detalhes.

### Passagem de argumento por valor

Pode-se esperar que, se passarmos um objeto por valor para uma função, as modificações desse valor dentro da função não afetarão o objeto (porque não passamos o objeto em si, mas apenas seu valor, que é uma cópia). Aqui está um exemplo desse comportamento (em C):

```c
#include <stdio.h>

void pass_by_value(int m) {
  printf("in pass_by_value: received m=%d\n",m);
  m=42;
  printf("in pass_by_value: changed to m=%d\n",m);
}

int main(void) {
  int global_m = 1;
  printf("global_m=%d\n",global_m);
  pass_by_value(global_m);
  printf("global_m=%d\n",global_m);
  return 0;
}
```

juntamente com a saída correspondente:

    global_m=1
    in pass_by_value: received m=1
    in pass_by_value: changed to m=42
    global_m=1


O valor `1` da variável global `global_m` não é modificado quando a função `pass_by_value` altera seu argumento de entrada para 42.

### Passagem de argumento por referência

Chamar uma função por referência, por outro lado, significa que o objeto fornecido a uma função é uma referência ao objeto. Isso significa que a função verá o mesmo objeto que no código de chamada (porque eles estão referenciando o mesmo objeto: podemos pensar na referência como um ponteiro para o local na memória onde o objeto está localizado). Qualquer alteração que atue sobre o objeto dentro da função, será visível no objeto no nível de chamada (porque a função realmente opera no mesmo objeto, e não em uma cópia dele).

Aqui está um exemplo que mostra isso usando ponteiros em C:

```c
#include <stdio.h>

void pass_by_reference(int *m) {
  printf("in pass_by_reference: received m=%d\n",*m);
  *m=42;
  printf("in pass_by_reference: changed to m=%d\n",*m);
}

int main(void) {
  int global_m = 1;
  printf("global_m=%d\n",global_m);
  pass_by_reference(&global_m);
  printf("global_m=%d\n",global_m);
  return 0;
}
```

juntamente com a saída correspondente:

    global_m=1
    in pass_by_reference: received m=1
    in pass_by_reference: changed to m=42
    global_m=42

O C++ fornece a capacidade de passar argumentos como referências adicionando um "&" à frente do nome do argumento na definição da função:


```cpp
#include <stdio.h>

void pass_by_reference(int &m) {
  printf("in pass_by_reference: received m=%d\n",m);
  m=42;
  printf("in pass_by_reference: changed to m=%d\n",m);
}

int main(void) {
  int global_m = 1;
  printf("global_m=%d\n",global_m);
  pass_by_reference(global_m);
  printf("global_m=%d\n",global_m);
  return 0;
}
```

juntamente com a saída correspondente:

    global_m=1
    in pass_by_reference: received m=1
    in pass_by_reference: changed to m=42
    global_m=42

### Passagem de argumento em Python

Em Python, os objetos são passados como o valor de uma referência (ponteiro) para o objeto. Dependendo da forma como a referência é usada na função e, dependendo do tipo de objeto que ele referencia, isso pode resultar em um comportamento de "passagem por referência" (onde qualquer alteração no objeto recebido como argumento de função é imediatamente refletida no nível de chamada).

Aqui estão três exemplos para discutir isso. Começamos passando uma lista para uma função que itera através de todos os elementos na sequência e dobra o valor de cada elemento:

def double_the_values(l):
    print("in double_the_values: l = %s" % l)
    for i in range(len(l)):
        l[i] = l[i] * 2
    print("in double_the_values: changed l to l = %s" % l)

l_global = [0, 1, 2, 3, 10]
print("In main: s=%s" % l_global)
double_the_values(l_global)
print("In main: s=%s" % l_global)

A variável `l` é uma referência ao objeto lista. A linha `l[i] = l[i] * 2` avalia primeiro o lado direito e lê o elemento com o índice `i`, depois multiplica por dois. Uma referência a este novo objeto é então armazenada no objeto lista `l` na posição com o índice `i`. Por isso, modificamos o objeto lista, que é referenciado através de `l`.

A referência ao objeto lista nunca muda: a linha `l[i] = l[i] * 2` muda os elementos `l[i]` da lista `l` mas nunca a referência `l` para a lista. Assim, tanto a função como o nível de chamada estão operando no mesmo objeto através das referências `l` e` global_l`, respectivamente.

Em contraste, aqui está um exemplo que não modifica os elementos da lista dentro da função, o que produz esta saída:

def double_the_list(l):
    print("in double_the_list: l = %s" % l)
    l = l + l
    print("in double_the_list: changed l to l = %s" % l)

l_global = "Hello"
print("In main: l=%s" % l_global)
double_the_list(l_global)
print("In main: l=%s" % l_global)

O que acontece aqui é que, durante a avaliação de `l = l + l`, um novo objeto é criado que contém ` l + l`, e que, em seguida, vinculamos o nome `l` a ele. No processo, perdemos as referências à lista `l` que foi passada à função (e, portanto, não alteramos a lista passada à função).

Finalmente, vejamos o que essa saída produz:

def double_the_value(l):
    print("in double_the_value: l = %s" % l)
    l = 2 * l
    print("in double_the_values: changed l to l = %s" % l)

l_global = 42
print("In main: s=%s" % l_global)
double_the_value(l_global)
print("In main: s=%s" % l_global)

Neste exemplo, também duplicamos o valor (de 42 a 84) dentro da função. No entanto, quando vinculamos o objeto 84 ao nome `l` (que é a linha `l = l * 2`), criamos um novo objeto (84), e nós vinculamos o novo objeto a `l`. No processo, perdemos a referência ao objeto 42 dentro da função. Isso não afeta o próprio objeto 42, nem a referência `l_global` para ele.

Em resumo, o comportamento em Python de passar argumentos para uma função pode parecer variável (se o visualizarmos a partir do ponto de vista de _passagem por valor_ versus _passagem por referência_). No entanto, ele é sempre feito como uma chamada por valor, onde o valor é uma referência ao objeto em questão, e o comportamento pode ser explicado pelo mesmo raciocínio em todos os casos.

### Considerações de desempenho

As chamadas de função por valor requerem a cópia do valor antes de ele ser passado à função. Sob o ponto de vista de desempenho (tempo de execução e requisitos de memória), isso pode ser um processo caro se o valor for grande. (Imagine que o valor é um objeto `numpy.array` que pode ser de vários Megabytes ou Gigabytes de tamanho.)

Geralmente se preferem chamadas por referência para objetos grandes, pois neste caso apenas um ponteiro para os objetos é passado, independentemente do tamanho real do objeto e, portanto, isso geralmente é mais rápido do que a chamada por valor.

A abordagem em Python de (efetivamente) chamar por referência é, portanto, eficiente. No entanto, precisamos ter cuidado para que nossa função não modifique os dados que ela receber quando isso não é desejado.

### Modificação de dados por desatenção

Geralmente, uma função não deve modificar os dados passados como entrada para ela.

Por exemplo, o código a seguir demonstra a tentativa de determinar o valor máximo de uma lista, e uma modificação - desatenta - da lista no processo:

def mymax(s):  # demonstrando efeito colateral
    if len(s) == 0:
        raise ValueError('mymax() arg is an empty sequence')
    elif len(s) == 1:
        return s[0]
    else:
        for i in range(1, len(s)):
            if s[i] < s[i - 1]:
                s[i] = s[i - 1]
        return s[len(s) - 1]

s = [-45, 3, 6, 2, -1]
print("in main before caling mymax(s): s=%s" % s)
print("mymax(s)=%s" % mymax(s))
print("in main after calling mymax(s): s=%s" % s)

O usuário da função `mymax()` não esperaria que o argumento de entrada fosse modificado quando a função fosse executada. Em geral, devemos evitar isso. Existem várias maneiras de encontrar melhores soluções para o problema dado:

- Neste caso particular, poderíamos usar a função predefinida `max()` para obter o valor máximo de uma sequência.

- Se sentirmos que precisamos nos ater ao armazenamento de valores temporários dentro da lista \[isso na verdade não é necessário\], podemos criar uma cópia da lista de entrada `s` primeiro e, em seguida, proceder com o algoritmo (veja adiante sobre cópia de objetos).

- Escolha outro algoritmo, o qual use uma variável temporária extra ao invés de abusar da lista para isso. Por exemplo:

- Podemos passar uma tupla (em vez de uma lista) para a função: uma tupla é *imutável* e, portanto, nunca pode ser modificada (isso resultaria em uma exceção sendo gerada quando a função tentasse escrever nos elementos da tupla).

### Copiando objetos

Python fornece a função `id()`, a qual retorna um número inteiro que é exclusivo para cada objeto. (Na implementação atual do CPython, este é o endereço da memória.) Podemos usá-la para identificar se dois objetos são iguais.

Para copiar um objeto cujo tipo é uma sequência (incluindo listas), podemos fatiá-lo, i.e. se `a` for uma lista, então `a[:]` retornará uma cópia de `a`. Aqui está uma demonstração:

a = list(range(10))
a

b = a
b[0] = 42
a              # alterando-se b, altera-se a

id(a)

id(b)

c = a[:] 
id(c)          # c é um objeto diferente

c[0] = 100       
a              # altera-se c, mas a permanece inalterado

A biblioteca padrão em Python fornece o módulo `copy`, o qual provê funções de cópia que podem ser usadas para criar  cópias de objetos. Poderíamos ter usado `import copy; c = copy.deepcopy(a)` em vez de `c = a[:]`.

Igualdade e Identidade
------------------------------

Uma questão relacionada diz respeito à igualdade de objetos.

### Igualdade

Os operadores `<`, `>`, `==`, `>=`, `<=`, e `!=` comparam os *valores* de dois objetis. Os objetos não precisam ter o mesmo tipo. Por exemplo:

a = 1.0; b = 1
type(a)

type(b)

a == b

Então, o operador `==` verifica se os valores de dois objetos são iguais.

### Identidade/Semelhança

Para verificar se dois objetos `a` e `b` são os mesmos (i.e. se `a` e `b` fazem referência ao mesmo local na memória), podemos usar o operator `is` (continuação do exemplo anterior):

a is b

Certamente, eles são diferentes aqui, já que não são do mesmo tipo.

Também podemos lançar mão da função `id` que, de acordo com a documentação da versão Python 2.7: "*Retorna a identidade de um objeto, única entre objetos existindo simultaneamente. (Dica: é o endereço do objeto na memória.)*"

id(a)

id(b)

que mostra que `a` e `b` são armazenados em diferentes locais na memória.

### Exemplo: Igualdade e identidade

Fechamos com um exemplo envolvendo listas:

x = [0, 1, 2]
y = x
x == y

x is y

id(x)

id(y)

Aqui, `x` e `y` são referências ao mesmo endereço na memória. Eles são idênticos e o operador `is` confirma isso. O ponto importante a lembrar é que a linha 2 (`y = x`) cria uma nova referência `y` para a mesma lista da qual `x` já é uma referência.

Consequentemente, podemos alterar os elementos de `x` que `y` mudará simultaneamente, pois `x` e `y` se referem ao mesmo objeto:

x

y

x is y

x[0] = 100
y

x

Em contraste, se usarmos `z = x [:]` (em vez de `z = x`) para criar um novo objeto `z`, então a operação de fatiamento `x[:]` criará uma cópia da lista `x`, e a nova referência `z` apontará para esta cópia. O *valor* de `x` e `z` será o mesmo, mas `x` e `z` não serão o mesmo objeto (eles não serão idênticos):

x

z = x[:]            # cria cópia de x antes de atribui-lo a z
z == x              # mesmo valor

z is x              # nao sao o mesmo objeto

id(z)               # confirmacao pela id()

id(x)

x

z

Consequentemente, podemos alterar `x` sem que `z` seja alterado. Por exemplo (continuação):

x[0] = 42
x

z