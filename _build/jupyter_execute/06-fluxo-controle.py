Fluxo de Controle
============

Básico
------

Para um dado arquivo com um programa Python, o interpretador Python começará no topo e depois processará o arquivo. Demonstramos isso com um programa simples. Por exemplo:

def f(x):
    """funcao que computa e retorna x*x"""
    return x * x

print("O Programa principal comeca aqui")
print("4 * 4 = %s" % f(4))
print("Ultima linha do programa -- adeus")

A regra básica é que os comandos em um arquivo (ou função ou qualquer sequência de comandos) são processados de cima para baixo. Se vários comandos forem dados na mesma linha (separados por <span>`;`</span>), eles serão processados da esquerda para a direita (embora seja desencorajado ter múltiplas declarações por linha a fim de manter boa legibilidade de código.)

Neste exemplo, o interpretador começa no topo (linha 1). Ele encontra a palavra-chave <span>`def`</span> e lembra para o futuro que a função <span>`f`</span> está definida aqui. (Ainda não executará o corpo da função, ou seja, a linha 3 - isso só acontece quando chamamos a função). O interpretador pode ver a partir do recuo onde o corpo da função acaba: o recuo na linha 5 é diferente do da primeira linha no corpo da função (linha 2), e assim o corpo da função terminou, e a execução deve continuar com essa linha. (Linhas vazias não são importantes para essa análise).

Na linha 5, o intérprete imprimirá a saída `O programa principal comeca aqui`. Então, a linha 6 é executada. Esta linha contém a expressão <span>`f(4)`</span>, a qual chamará a função <span>`f(x)`</span>, definida na linha 1, em que <span>`x`</span> tomará o valor <span>`4`</span>. \[Atualmente <span>`x`</span> é uma referência ao objeto <span>`4`</span>.\] A função <span>`f`</span> é então executada, retornando <span>`4*4`</span> na linha 3. Este valor <span>`16`</span> é usado na linha 6 para substituir <span>`f(4)`</span>. Por fim, a representação *string* <span>`%s`</span> do objeto 16 é impressa como parte do comando de impressão na linha 6. O interpretador então passa para a linha 7 antes de o programa terminar.

Agora vamos aprender sobre diferentes possibilidades para direcionar esse fluxo de controle ainda mais.

### Condicionais

Os valores <span>`True`</span> e <span>`False`</span> são objetos predefinidos especiais:

a = True
print(a)

type(a)

b = False
print(b)

type(b)

Podemos operar com esses dois valores lógicos usando a lógica booleana, por exemplo, a lógica e a operação (<span>`and`</span>):

True and True          # lógica e operação

True and False

False and True

True and True

c = a and b
print(c)

Há também o *ou* lógico (<span>`or`</span>) e a negação (<span>`not`</ span>):

True or False

not True

not False

True and not False

Em códigos computacionais, muitas vezes precisamos avaliar alguma expressão que seja verdadeira ou falsa (às vezes 
chamada de "predicado"). Por exemplo:

x = 30          # atribui 30 a x
x > 15          # x é maior do que 15?

x > 42

x == 30         # x é igual a 30?

x == 42

not x == 42     # x não é o mesmo que 42?

x != 42         # x não é o mesmo que 42?

x > 30          # x é maior do que 30?

x >= 30         # x é maior do que ou igual a 30?

Se-então-senão
------------

##### Informação adicional

-   Introdução à estrutura condicional `if-then` em [Python tutorial, seção 4.1](http://docs.python.org/tutorial/controlflow.html#if-statements)

A declaração <span>`if`</span> permite execução condicional de código. Por exemplo:

a = 34
if a > 0:
    print("a é positivo")

A declaração `if` também pode ter uma ramificação <span>`else`</span> que é executada se a condição estiver errada:

a = 34
if a > 0:
    print("a é positivo")
else:
    print("a é nao-positivo (i.e. negativo ou zero)")

Finalmente, existe a palavra-chave <span>`elif`</span> (leia como "else if") que permite verificar várias possibilidades (exclusivas):

a = 17
if a == 0:
    print("a é zero")
elif a < 0:
    print("a é negativo")
else:
    print("a é positivo")

Laço `for`
--------

##### Informação adicional

-   Introdução a laços `for` [Python tutorial, seção 4.2](http://docs.python.org/tutorial/controlflow.html#for-statements)

O laço <span>`for`</span> permite-nos iterar sobre uma sequencia (isto poderia ser uma *string* ou lista, por exemplo). Aqui está um exemplo:

for animal in ['cão','gato','rato']:
    print(animal, animal.upper())

Juntamente com o comando `range()`, pode-se iterar sobre inteiros crescentes:

for i in range(5,10):
    print(i)

Laço `while`
----------

A palavra-chave <span>`while`</span> permite-nos repetir uma operação enquanto uma condição é verdadeira. Suponha que quiséssemos saber por quantos anos teremos que guardar 100 reais em uma poupança para alcançar 200 reais simplesmente 
por uma taxa de juros de 5% ao ano. Aqui está um programa para computar isso:

montante = 100        # em BRL
taxa = 1.05           # 5% a.a. juros
anos = 0
while montante < 200:  # repita até que 200 seja alcancado
    montante = montante * taxa
    anos = anos + 1
print('Preciso de', anos, 'anos para alcançar', montante, 'reais.')

Operadores relacionais (comparações) nas declarações `if` e `while`
-------------------------------------------------- -----------------------------------------

A forma geral de `if` e `while` é a mesma: seguindo a palavra-chave `if` ou `while`, existe uma *condição* seguida de dois pontos. Na próxima linha, um novo (e, portanto, indentado!) bloco de comandos começa a ser executado se a condição for `True`).

Por exemplo, a condição pode ser a igualdade de duas variáveis <span>`a1`</span> e <span>`a2`</span>, expressa como <span>`a1 == a2`</span>:

a1 = 42
a2 = 42
if a1 == a2:
    print("a1 e a2 são iguais")

Outro exemplo é testar se `a1` e `a2` não são os mesmos. Para isso, temos duas possibilidades. A opção número 1 usa o *operador de desigualdade* `!=`:

if a1 != a2:
    print("a1 e a2 são diferentes")

A opção 2 usa a palavra-chave <span>`not`</span> à frente da condição:

if not a1 == a2:
    print("a1 e a2 são diferentes")

Comparações para "maior" (<span>`>`</span>), "menor" (<span>`<`</span>) e "maior ou igual a" (<span>`>=`</span>) e "menor ou igual a" (<span>`<=`</span>) são diretos.

Finalmente, podemos usar os operadores lógicos "<span>`and`</span>" e "<span>`or`</span>" para combinar condições:

a = 11
b = -3
if a > 10 and b > 20:
    print("A é maior do que 10 e b é maior do que 20")
if a > 10 or b < -5:
    print("Ou a é maior do que 10, ou "
          "b é menor do que -5, ou ambos.")

Use o *prompt* do Python para experimentar estas comparações e expressões lógicas. Por exemplo:

T = -12.5
if T < -20:
    print("muito frio")

if T < -10:
    print("bastante frio")

T < -20

T < -10

Exceções
----------

Mesmo que uma declaração ou expressão seja sintaticamente correta, ela pode causar um erro quando uma tentativa é feita para executá-la. Os erros detectados durante a execução são chamados *exceções* e não são necessariamente fatais: exceções podem ser *capturadas* e tratadas no programa. A maioria das exceções não são tratadas pelos programas, no entanto, e resultam em mensagens de erro como as mostradas aqui:

10 * (1/0)

4 + spam*3

'2' + 2

Excepção esquemática capturando todas as opções

try:
   # corpo de código
except ArithmeticError:
   # o que fazer se houver erro de aritmética
except IndexError, the_exception:
   # the_exception refere-se à exceção neste bloco
except:
   # o que fazer para qualquer outra exceção
else:  # opcional
   # o que fazer se nenhuma exceção for lançada

try:
   # corpo de código
finally:
   # o que fazer SEMPRE

A partir do Python 2.5, você pode usar a instrução `with` para simplificar a escrita do código para algumas funções predefinidas, em particular a função `open` para abrir arquivos: veja  <http://docs.python.org/tutorial/errors.html#predefined-clean-up-actions>.

Exemplo: tentaremos abrir um arquivo que não existe e o Python criará uma exceção do tipo `IOError`, que significa erro de entrada/saída:

f = open("filenamethatdoesnotexist", "r")

Se estivéssemos escrevendo um aplicativo com uma interface onde o usuário deve digitar ou selecionar um nome de arquivo, não gostaríamos que o aplicativo parasse se o arquivo não existisse. Em vez disso, precisamos capturar esta exceção e agir para tratá-la (informando, por exemplo, o usuário que um arquivo com tal nome não existe e perguntar se ele quer tentar outro nome de arquivo). Aqui está o esqueleto para capturar esta exceção:

try:
    f = open("arquivo_inexistente","r")
except IOError:
    print("Arquivo não pode ser aberto.")

Há muito mais para ser dito sobre exceções e o uso delas em programas maiores. Comece lendo o [Capítulo 8 do Python Tutorial: Erros e Exceções](http://docs.python.org/tutorial/errors.html#errors-and-exceptions) se você tiver interesse.

### Lançando Exceções

Possibilidades de lançar uma exceção:

-   `raise OverflowError`

-   `raise OverflowError, Bath is full` (estilo antigo, desencorajado)

-   `raise OverflowError(Bath is full)`

-   `e = OverflowError(Bath is full); raise e`

#### Hierarquia de exceções

As exceções padrão são organizadas em uma hierarquia de herança, e.g. `OverflowError` é uma subclasse de `ArithmeticError`. Isso pode ser visto ao examinarmos `help('exceptions')`, por exemplo. Você pode derivar suas próprias exceções de qualquer um dos padrões. É um bom estilo que cada módulo defina sua própria exceção de base.

### Criando as suas próprias exceções

- Você pode e deve derivar suas próprias exceções a partir de uma exceção predefinida.

- Para ver quais exceções predefenidas existem, procure no módulo de exceções (tente <span>`help('exceptions')`</span>) ou acesse <http://docs.python.org/library/ Exceptions.html # bltin-exceptions>.

### LBYL vs EAFP

- LBYL (Look Before You Leap = Pense duas vezes antes de agir) *versus*

- EAFP (Easer to ask forgiveness than permission = Facilidade de pedir perdão do que permissão)

numerador = 7
denominador = 0

Exemplo para LBYL:

if denominador == 0:
    print("Oops...")
else:
    print(numerador/denominador)

EAFP:

try:
    print(numerador/denominador)
except ZeroDivisionError:
    print("Oops...")

O que a documentação do Python diz sobre EAFP:

Veja <http://docs.python.org/glossary.html#term-eafp>

O que a documentação do Python diz sobre LBYL:

Veja <http://docs.python.org/glossary.html#term-lbyl>

EAFP é a maneira "Pythônica".