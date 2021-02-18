Entrada e Saída de Dados
================

Nesta seção, descrevemos o processo de impressão na tela, o qual inclui o uso da função `print`, o especificador de formato do estilo antigo `%` e o especificador de formato do novo estilo `{}`.

Imprimindo na saída padrão (normalmente a tela)
-------------------------------------------------

A função `print` é o comando mais usado para imprimir informações para o "dispositivo de saída padrão", que normalmente é a tela.

Existem dois modos de usar a impressão.

### Impressão simples

A maneira mais fácil de usar o comando de impressão é listando as variáveis a serem impressas, separadas por vírgulas. Aqui estão alguns exemplos:

a = 10
b = 'texto de teste'
print(a)

print(b)

print(a, b)

print("A resposta é", a)

print("A resposta é", a, "e a string contém", b)

print("A resposta é", a, "e a string lida como", b)

Em Python, um espaço é adicionado entre cada objeto que está sendo impresso. Uma nova linha é impressa após cada chamada. Para suprimir isso, use o parâmetro `end =`:

print("Imprimindo na linha", end ='')
print("... ainda imprimindo na mesma linha.")

### Impressão formatada

A forma mais sofisticada de formatar a saída usa uma sintaxe muito semelhante ao `fprintf` do Matlab (e, portanto, também, semelhante ao `printf` da linguagem C). A estrutura geral é a de uma *string* contendo especificadores de formato, seguida por um sinal de porcentagem e uma tupla que contém as variáveis a serem impressas no lugar dos especificadores de formato.

print("a = %d b = %d" % (10,20))

Uma *string* pode conter identificadores de formato (ex: `%f` para formatar como `float`,`%d` para formatar como número inteiro e `%s` para formatar como *string*, isto é, uma sequência de caracteres):

from math import pi
print("Pi = %5.2f" % pi)

print("Pi = %10.3f" % pi)

print("Pi = %10.8f" % pi)

print("Pi = %d" % pi)

O especificador de formato do tipo `%W.Df` significa que um `float` deve ser impresso com uma largura total de *W* caracteres e *D* digitos após o ponto decimal. (Isto é idêntico ao Matlab e C, por exemplo).

Para imprimir mais de um objeto, forneça vários especificadores de formato e liste vários objetos na tupla:

print("Pi = %f, 142*pi = %f e pi^2 = %f." % (pi,142*pi,pi**2))

Note que a conversão de um especificador de formato e uma tupla de variáveis para uma *string* não depende do comando `print`:

from math import pi
"pi = %f" % pi

Isso significa que podemos converter objetos em *strings* onde quer que precisemos, e podemos decidir imprimir as *strings* mais tarde - não há necessidade de acoplar a formatação ao código que faz a impressão.

Visão geral dos especificadores de formato comumente usados (exemplo: unidade astronômica):

AU = 149597870700  # unidade astronomica [m]
"%f" % AU          # linha1 na tabela

| especificador     |         estilo        |examplo da saída para AU|
|:------------------|:---------------------:|-----------------------:|
| `%f` |     ponto flutante          |  `149597870700.000000`|
| `%e` |  notação exponencial        |         `1.495979e+11`|
| `%g` |  mais curta entre `%e` ou `%f`|          `1.49598e+11`|
| `%d` |        inteiro              |         `149597870700`|
| `%s` |  `str()` |         `149597870700`|
| `%r` | `repr()` |        `149597870700L`|

### `str` e `__str__`

Todos os objetos em Python devem fornecer um método `__str__` que retorne uma boa representação de *string* do objeto. Este método `a.__str__()` é chamado quando aplicamos a função `str` ao objeto `a`:

a = 3.14
a.__str__()

str(a)

A função `str` é extremamente conveniente já que nos permite escrever objetos mais complicados, tais como

b = [3, 4.2, ['maçã', 'banana'], (0, 1)]
str(b)

A forma como isto é impresso em Python é usando o método `__str__` do objeto da lista. O interpretador imprimirá o colchete de abertura `[` e depois chamará o método `__str__` do primeiro objeto, ou seja, o inteiro 3, produzindo `3`. Em seguida, o método `__str__` do objeto da lista imprime a vírgula `,`,  move-se para chamar o método `__str__` do próximo elemento da lista (ou seja,`4.2`) para imprimi-lo. Desta forma, qualquer objeto composto pode ser representado como uma *string*, pedindo aos objetos que ele guarda para convertê-los em *strings*.

O método *string* do objeto `x` é chamado de forma implícita quando

- usamos o especificador de formato `%s` para imprimir `x`;

- passamos o objeto `x` diretamente para o comando de impressão:

print(b)

print("%s" % b)

### `repr` e ` __repr__`

Uma segunda função, `repr`, deve converter um determinado objeto em uma representação de string *para que essa sequencia de caracteres possa ser usada para recriar o objeto usando a função `eval`*. A função `repr` geralmente fornecerá uma string mais detalhada do que `str`. A aplicação de `repr` ao objeto `x` tentará chamar `x.__repr__()`.

from math import pi as a1
str(a1)

repr(a1)

numero_como_string = repr(a1)
a2 = eval(numero_como_string)  # avalia a string 
a2

a2-a1                      # -> repr é uma representação exata

a1-eval(repr(a1))

a1-eval(str(a1))           # -> str perdeu alguns dígitos

Podemos converter um objeto para a sua forma `str()` ou `repr()` usando os especificadores de formato `%s` e `%r`, respectivamente.

import math
"%s" % math.pi

"%r" % math.pi

### Nova formatação

Um novo sistema predefinido de formatação permite mais flexibilidade para casos complexos, com o custo de ser um pouco mais longo.

Idéias básicas em exemplos:

"{} precisa de {} chocolates".format('Pedro', 4)     # insere valores na ordem

"{0} precisa de {1} chocolates".format('Pedro', 4)   # indexa elemento

"{1} precisa de {0} chocolates".format('Pedro', 4)

# referencia elemento para impressão por nome
"{nome} precisa de {numero} chocolates".format(nome='Pedro',numero=4)               

"Pi é aproximadamente {:f}.".format(math.pi)     # podemos usar opções de formatação no estilo antigo para float

"Pi é aproximadamente {:.2f}.".format(math.pi)   # e precisao

"Pi é aproximadamente {:6.2f}.".format(math.pi)  # e largura


Esta é uma maneira poderosa e elegante de formatação de *strings* que está tendo seu uso crescendo gradualmente.

##### Outras informações

- [Exemplos](http://docs.python.org/library/string.html#format-examples)

- [Python Enhancement Proposal 3101](http://www.python.org/dev/peps/pep-3101/)

- [Biblioteca Python, String Formatting Operations](http://docs.python.org/library/stdtypes.html#string-formatting-operations)

- [Formatação antiga de *strings*](http://docs.python.org/tutorial/inputoutput.html#old-string-formatting)

- [Introdução à formatação de saída mais elegante, tutorial Python, seção 7.1](http://docs.python.org/tutorial/inputoutput.html)

### Mudanças de Python 2 para Python 3: `print`

Uma (talvez a mais óbvia) mudança da versão Python 2 para a 3 é perda do status especial do comando `print`. Em Python 2, poderíamos imprimir "Hello world" usando:

```python
print "Hello world"             # válida em Python 2.x
```

Efetivamente, chamamos a função `print` com o argumento `Hello World`. Todas as outras funções em Python são chamadas com o argumento acompanhado por parênteses, i.e.

print("Hello World")               # válida em Python 3.x

Esta é a nova convenção *necessária* em Python 3 e *permitida* para a versão recente de Python 2.x.

Tudo o que aprendemos sobre a formatação de *strings* usando o operador de porcentagem ainda funciona da mesma maneira:

import math
a = math.pi
"meu pi = %f" % a           # formatação de string

print("meu pi = %f" % a)    # impressão valida em Python 2.7 e 3.x

"Curto pi = %.2f, mais longo pi = %.12f." % (a, a)

print("Curto pi = %.2f, mais longo pi = %.12f." % (a, a))

print("Curto pi = %.2f, mais longo pi = %.12f." % (a, a))

Leitura e escrita de arquivos
-------------------------

Aqui está um programa que

1. escreve algum texto para um arquivo com o nome `teste.txt`,

2. e depois lê o texto novamente e

3. imprime na tela.

Os dados armazenados no arquivo `teste.txt` são:

```
Escrevendo texto no arquivo. Esta é a primeira linha.
E a segunda linha.
```

<!-- -->

# 1. Escrever um arquivo 
out_file = open("teste.txt", "w")         # 'w' significa Writing (modo de escrita)
out_file.write("Escrevendo texto no arquivo. Esta é a primeira linha.\n"+\
               "E a segunda linha.")
out_file.close()                          # fecha o arquivo
 
# 2. Ler um arquivo
in_file = open("teste.txt", "r")          # 'r' significa Reading (modo de leitura)
text = in_file.read()                     # lê todo o arquivo em na string 'text'
                                          
in_file.close()                           # fecha o arquivo
 
# 3. Mostrar os dados
print(text)

Mais detalhadamente, abrimos um arquivo com o comando `open` e atribuimos este objeto de abertura de arquivo à variável `out_file`. Depois, escrevemos dados no arquivo usando o método `out_file.write`. Observe que, no exemplo acima, passamos uma *string* para o método `write`. Podemos, naturalmente, usar toda a formatação que discutimos antes. Por exemplo, para escrever este arquivo com o nome `tabela.txt`, podemos usar este programa Python. É uma boa prática fechar (`close()`) arquivos quando terminamos de operar em modo de leitura ou escrita. Se um programa Python for encerrado de forma controlada (ou seja, não por causa de um corte de energia ou de um *bug* improvável profundo na linguagem Python ou no sistema operacional), ele fechará todos os arquivos abertos assim que os objetos de manipulação de arquivo forem destruídos. No entanto, fechá-los ativamente o mais rápido possível é um estilo melhor.

### Exemplos de leitura de arquivos

Usamos um arquivo chamado `meu-arquivo.txt` contendo as seguintes 3 linhas de texto para os exemplos abaixo:

    Esta é a primeira linha.
    Esta é a segunda linha.
    Esta é uma terceira e última linha.    

f = open('meu-arquivo.txt', 'w')
f.write('Esta e a primeira linha.\n'
        'Esta e a segunda linha.\n'
        'Esta e uma terceira e ultima linha.')
f.close()

#### fileobject.read()

O método `fileobject.read()` lê o arquivo inteiro e o retorna como uma *string* (incluindo caracteres de nova linha - `\n`).

f = open('meu-arquivo.txt', 'r')
f.read()

f.close()

#### fileobject.readlines()

O método `fileobject.readlines()` retorna uma lista de *strings*, onde cada elemento da lista corresponde a uma linha na *string*:

f = open('meu-arquivo.txt', 'r')
f.readlines()

f.close()

Isto é frequentemente usado para iterar nas linhas, e para fazer alguma coisa com cada linha. Por exemplo:

f = open('meu-arquivo.txt', 'r')
for line in f.readlines():
    print("%d caracteres" % len(line))
f.close()

Observe que isso irá ler o arquivo completo em uma lista de *strings* quando o método `readlines ()` for chamado. Isso não é problema se sabemos que o arquivo é pequeno e se encaixa na memória da máquina.

Se assim for, também podemos fechar o arquivo antes de processarmos os dados, ou seja:

f = open('meu-arquivo.txt', 'r')
lines = f.readlines()
f.close()
for line in lines:
    print("%d caracteres" % len(line))

#### Iterando em linhas (objeto arquivo)

Existe uma possibilidade mais legal de ler uma linha de arquivo por linha que (i) somente lerá uma linha por vez (e também é adequada para arquivos grandes) e (ii) resulta em código mais compacto:

f = open('meu-arquivo.txt', 'r')
for line in f:
    print("%d caracteres" % len(line))
f.close()

Aqui, o manipulador de arquivo `f` atua como um iterador e retornará a próxima linha em cada iteração subsequente do laço `for` até o final do arquivo ser alcançado (e então o laço `for` é encerrado).

##### Leitura adicional

[Métodos para arquivos, Tutorial, Seção 7.2.1](http://docs.python.org/tutorial/inputoutput.html#methods-of-file-objects)