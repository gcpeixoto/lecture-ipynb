Funções e módulos
=====================

Introdução
------------

As funções nos permitem agrupar várias declarações em um bloco lógico. Comunicamo-nos com uma função através de uma interface claramente definida, fornecendo certos parâmetros para a função e recebendo algumas informações de volta. Além dessa interface, geralmente não sabemos como, exatamente, uma função faz o trabalho dela para obter o valor que retorna.

Por exemplo, a função `math.sqrt`: não sabemos, na totalidade, como ela calcula a raiz quadrada, mas sabemos sobre a interface: se passarmos `x` para a função, ela retornará (uma aproximação de) $\sqrt{x}$.

Esta abstração é uma coisa útil: é uma técnica comum na engenharia para quebrar um sistema em componentes menores (caixa preta) que trabalham juntos através de interfaces bem definidas, mas que não precisam saber sobre as realizações internas da funcionalidade uns dos outros. Na verdade, não ter que se preocupar com esses detalhes de implementação pode nos ajudar a ter uma visão mais clara do sistema composto por muitas dessas componentes.

As funções fornecem os blocos básicos de funcionalidade em programas maiores (e simulações computacionais) e ajudam a controlar a complexidade inerente ao processo.

Podemos agrupar funções em um módulo Python e, assim, criar nossas próprias bibliotecas de funcionalidades.

Usando funções
---------------

A palavra "função" tem diferentes significados em matemática e programação. Na programação, ela se refere a uma sequência de operações que executam uma computação. Por exemplo, a função `sqrt()`, definida no módulo de matemática `math`, calcula a raiz quadrada de um determinado valor:

from math import sqrt
sqrt(4)

O valor que passamos para a função `sqrt` é 4 neste exemplo. Esse valor é chamado de *argumento* da função. Uma função pode ter mais de um argumento.

A função retorna o valor 2.0 (o resultado de sua computação) para o "contexto de chamada". Esse valor é chamado de *valor de retorno* da função.

É comum dizer que uma função "leva" um argumento e "retorna"" um resultado, o chamado *valor de retorno*.

#### Confusão comum sobre a impressão e os valores de retorno 

É um erro comum do principiante confundir a *impressão* de valores com *valores de retorno*. No exemplo a seguir, é difícil ver se a função `math.sin` retorna um valor ou se ela imprime o valor:

import math
math.sin(2)

Nós importamos o módulo `math` e chamamos a função `math.sin` com o argumento `2`. A chamada `math.sin(2)` realmente *retornará* o valor `0.909...`, não o imprimirá. No entanto, como não foi atribuído o valor de retorno a uma variável, o prompt do Python imprimirá o objeto retornado.

A seguinte sequência alternativa funciona apenas se o valor for retornado:

x = math.sin(2)
print(x)

O valor de retorno da chamada da função `math.sin(2)` é atribuído à variável `x` e `x` é impresso na linha seguinte.

Geralmente, as funções devem executar "silenciosamente" (ou seja, não imprimir nada) e reportar o resultado de sua computação através do valor de retorno.

Parte da confusão sobre valores impressos versus valores de retorno no prompt do Python vem da impressão rápida do Python (uma representação) dos objetos retornados *se* os objetos retornados não são atribuídos. Geralmente, ver os objetos retornados é exatamente o que queremos (como normalmente nos preocupamos com o objeto retornado), apenas ao aprender Python. Isso pode causar confusão leve sobre funções que retornam valores ou valores de impressão.

##### Informação adicional

- [Pense em Python](https://penseallen.github.io/PensePython2e/) apresenta uma introdução gentil às funções (em que se baseia o parágrafo anterior) nos Capítulo 3 e 6.

Definindo funções
------------------

Formato genérico de definição de uma função:

```python
def minha_funcao(arg1, arg2, ..., argn):
    """Docstring opcional"""

    # Implementação da função

    return resultado  # opcional

# isto nao é parte da função
algum_comando
```

A terminologia de Allen Downey (em seu livro [Pense em Python](https://penseallen.github.io/PensePython2e/)) de funções frutíferas e infrutíferas distingue funções que retornam um valor daquelas que não retornam valor algum. A distinção refere-se à característica de uma função fornecer um valor de retorno (=frutífera) ou não retornar explicitamente um valor (=infrutífera). Se as funções não usam a instrução `return`, tendemos a dizer que a função não retorna nada (enquanto que, na realidade, sempre retornará o objeto `None` quando ele termina - mesmo que nela falte a instrução `return`).

Por exemplo, a função `cumprimento` imprimirá "Olá, mundo!" quando chamada (e é infrutífero, pois não retorna um valor).

def cumprimento():
    print("Olá, mundo!")

Quando chamamos essa função:

cumprimento()

ela imprime “Olá, Mundo!” para `stdout`, como esperado. Se atribuírmos o valor de retorno da função para a variável `x`, poderemos inspecioná-lo:

x = cumprimento()

print(x)

e encontrarmos que a função `cumprimento`, de fato, retornou, o objeto `None`.

Outro exemplo para uma função que não retorna valor algum (isso significa que não há palavra-chave `return` na função) seria:

def printpluses(n): 
    print(n * "+")

Geralmente, funções que retornam valores são mais úteis, pois podem ser usadas para montar código (talvez como outra função) combinando-as de maneira "esperta". Vejamos alguns exemplos de funções que retornam um valor.

Suponhamos que precisemos definir uma função que calcule o quadrado de uma determinada variável. O código-fonte da função poderia ser:

def quadrado(x):
    return x * x

A palavra-chave `def` diz ao Python que estamos *definindo* uma função naquele ponto. A função leva um argumento, a saber `x`. A função retorna `x*x`, que é, claramente, $x^2$. Aqui está um exemplo que mostra como a função pode ser definida e usada:

def quadrado(x):
    return x * x

for i in range(5):
    i_quadrado = quadrado(i)
    print(i, '*', i, '=', i_quadrado)

Vale mencionar que as linhas 1 e 2 definem a função `quadrado`, ao passo que as de linhas 4 a 6 são o programa principal.

Podemos definir funções que levam mais do que um argumento:

import math

def hipotenusa(x, y):
    return math.sqrt(x * x + y * y)

Também é possível retornar mais de um argumento. Aqui está um exemplo de uma função que converte uma determinada *string* retornando-a em duas versões: com todos os caracteres em letras maiúsculas e todos os caracteres em letras minúsculas. Incluímos o programa principal para mostrar como esta função pode ser chamada:

def maiusculasEMinusculas(string):
    return string.upper(), string.lower()

palavra = 'Banana'

uppercase, lowercase = maiusculasEMinusculas(palavra)

print(palavra, 'em minúsculas:', lowercase,
      'e em maiúsculas', uppercase)

Podemos definir múltiplas funções em Python em um arquivo. Aqui está um exemplo com duas funções:

def retorna_estrelas( n ):
    return n * '*'

def imprime_centrado_estrelas( string ):
    linelength = 46 
    starstring = retorna_estrelas((linelength - len(string)) // 2)

    print(starstring + string + starstring)

imprime_centrado_estrelas('Olá, Mundo!')

##### Leitura complementar

-   [Python Tutorial: Seção 4.6 Definindo Funções](http://docs.python.org/tutorial/controlflow.html#defining-functions)


Módulos
-------

- Agrupam funcionalidade;

- Fornecem espaço de nomes;

- A biblioteca padrão do Python contém uma vasta coleção de módulos (tente `help('modules')`);

- Extensão da linguagem Python.

### Importando módulos

import math

Isto introduzirá o nome `math` no espaço de nomes no qual o comando de importação foi lançado. Os nomes dentro do módulo `math` não aparecerão diretamente: eles devem ser acessados através do nome `math`. Por exemplo: `math.sin`.

import math, cmath

Mais de um módulo pode ser importado na mesma declaração, embora o [Python Style Guide](http://www.python.org/dev/peps/pep-0008/) recomende não fazer isso. Em vez disso, devemos escrever

import math
import cmath

import math as matematica

O nome pelo qual o módulo é conhecido localmente pode ser diferente do seu nome "oficial". Os usos típicos deste são:

- evitar conflitos de nomes com nomes existentes, e

- mudar o nome para algo mais gerenciável. Por exemplo, `import SimpleHTTPServer as shs`. Isto é desencorajado para código de produção (visto que nomes longos e mais significativos tornam os programas muito mais compreensíveis do que os curtos e crípticos), mas para testar experiências de forma interativa, ser capaz de usar um sinônimo curto pode tornar sua vida muito mais fácil. Dado que os módulos (importados) são objetos de primeira classe, você pode, claro, simplesmente fazer `shs = SimpleHTTPServer` a fim de obter o identificador mais facilmente identificável no módulo.

from math import sin

Esta declaração importará a função `sin` do módulo `math`, mas não irá introduzir o nome `math` no espaço de nomes corrente, senãp apenas o nome `sin`. É possível extrair mais de um nome do módulo de uma só vez:

from math import sin, cos

Finalmente, vejamos esta notação:

from math import *

Mais uma vez, isso não introduz o nome `math` no espaço de nomes corrente, mas *todos os nomes públicos* do módulo `math`. Em termos gerais, é uma má idéia fazer isso:

- Muitos nomes novos serão despejados no espaço de nomes corrente.

- Você tem certeza de que eles não sobrescreverão nenhum nome já presente?

- Será muito difícil rastrear de onde esses nomes vieram

- Dito isto, alguns módulos (incluindo os da biblioteca padrão, recomendam que sejam importados dessa maneira). Use com cuidado!

- Isso é bom para testes rápidos interativos ou pequenos cálculos.

### Criando módulos

Um módulo é, em princípio, nada mais do que um arquivo Python. Aqui está um exemplo de um arquivo de módulo que é salvo em `modulo1.py`:

```python
def alguma_funcao_util():
    pass

print("Meu nome é", __name__)
```

Podemos executar este arquivo (módulo) como um programa em Python normal (por exemplo: `python modulo1.py`):

cd static/data

!python modulo1.py

Observamos que a variável mágica `__name__` leva o valor `__main__` se o arquivo de programa `modulo1.py` for executado.

Por outro lado, podemos *importar* `modulo1.py` em outro arquivo (que poderia ter o nome `prog.py`), por exemplo, como este:

import modulo1            # em um certo arquivo prog.py

Quando o Python depara-se com a instrução `import modulo1` em `prog.py`, ele procura o arquivo `modulo1.py` no diretório de trabalho atual (e se ele não conseguir encontrá-lo em todos os diretórios em `sys.path`) e abre o arquivo `modulo1.py`. Ao fazer o *parsing* do arquivo `modulo1.py` de cima para baixo, ele adicionará quaisquer definições de função neste arquivo no espaço de nome `modulo1` no contexto de chamada (esse é o programa principal em `prog.py`). Neste exemplo, existe apenas a função `alguma_funcao_util`. Uma vez que o processo de importação esteja completo, podemos fazer uso de `modulo1.algum_funcao_util` em `prog.py`. Se o Python encontrar instruções diferentes das definições de função (e classe) durante a importação de `modulo1.py`, ele executará isso imediatamente. Neste caso, ele se deparará com a declaração `print(Meu nome eh, __name __)`.

Observe a diferença na saída se importarmos `modulo1.py` em vez de executá-lo por conta própria: `__name__` dentro de um módulo leva o valor do nome do módulo se o arquivo for importado.

### Uso de \_\_name\_\_

Em suma,

- `__name__` é `__main__` se o arquivo do módulo for executado sozinho;

- `__name__` é o nome do módulo (ou seja, o nome do arquivo do módulo sem o sufixo `.py`) se o arquivo do módulo for importado.

Podemos, portanto, usar a seguinte instrução `if` em `modulo1.py` para escrever o código que é *apenas executado* quando o módulo é executado por conta própria: isto é útil para manter programas de teste ou demonstrações das habilidades de um módulo neste programa principal "condicional". É prática comum para qualquer arquivo de módulo ter um programa principal condicional que demonstre suas capacidades.

### Exemplo 1

O próximo exemplo mostra um programa principal para outro arquivo (`vetorial.py`) que é usado para demonstrar as habilidades das funções definidas naquele arquivo:

```python
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
```

Se este arquivo for executado usando `python vetorial.py`, entao `__name__==__main__` é verdadeiro, e a saída será

!python vetorial.py

Se este arquivo for importado (ou seja, usado como um módulo) em outro arquivo Python, então `__name __ == __ main__` é falso, e esse bloco de declaração não será executado (e nenhuma saída será produzida).

Esta é uma forma bastante comum de executar o código condicionalmente em arquivos que fornecem funções semelhantes às da biblioteca. O código que é executado se o arquivo for executado por conta própria geralmente consiste em uma série de testes (para verificar se as funções do arquivo realizam as operações certas - *testes de regressão* ou *testes de unidade*), ou alguns exemplos de como as funções da biblioteca no arquivo podem ser usadas.

### Exemplo 2

Mesmo que um programa Python não se destine a ser usado como um arquivo de módulo, é uma boa prática usar sempre um programa principal condicional:

- muitas vezes, verifica-se, mais tarde, que as funções no arquivo podem ser reutilizadas (assim, economiza-se trabalho)

- isso é conveniente para testes de regressão.

Suponha que um determinado exercício seja escrever uma função que retorne os primeiros 5 números primos e além disso, os imprima. (Há, claro, uma solução trivial para isso, como sabemos, os números primos, e devemos imaginar que o cálculo necessário é mais complexo). Podemos ser tentados a escrever:

def primos5():
    return (2, 3, 5, 7, 11)

for p in primos5():
    print("%d" % p), 

É um estilo melhor usar uma função principal condicional, i.e.:

def primos5():
    return (2, 3, 5, 7, 11)

if __name__=="__main__":
    for p in primos5():
        print("%d" % p),

Um purista pode argumentar que o seguinte ainda é mais "limpo":

def primos5():
    return (2, 3, 5, 7, 11)

def main():
    for p in primos5():
        print("%d" % p),

if __name__=="__main__":
    main()

mas qualquer uma das duas opções é boa.

####  Leitura complementar

-   [Python Tutorial Seção 6](http://docs.python.org/tutorial/modules.html#modules)