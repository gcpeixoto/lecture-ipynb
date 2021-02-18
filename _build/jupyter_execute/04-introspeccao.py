Introspecção
=============

Um código Python pode fazer e responder perguntas sobre si mesmo e sobre os objetos que ele manipula.

dir()
-----

<span>`dir()`</span> é uma função predefinida que retorna uma lista de todos os nomes pertencentes a algum espaço de nomes (*namespace*).

- Se nenhum argumento for passado para `dir` (isto é, <span>`dir()`</span>), ele inspeciona o *namespace* no qual foi chamado.

- Se <span>`dir`</span> receber um argumento (ou seja, <span>`dir(<object>)`</span>, ele inspeciona o *namespace* do objeto que foi passado.

Por exemplo:

dir()

nome = "Pedro"
dir(nome)

### Nomes Mágicos

Você encontrará muitos nomes que começam e terminam com um sublinhado duplo (por exemplo, <span>`__name__`</span>). Estes são chamados de *nomes mágicos*. Funções com nomes mágicos fornecem a implementação de funcionalidades particulares da linguagem Python.

Por exemplo, a aplicação de <span>`str`</span> a um objeto <span>`a`</span>, ou seja <span>`str(a)`</span>, resultará - internamente - na chamada do método <span>`a.__str__()`</span>. O método <span>`__str__`</span> geralmente precisa retornar uma *string*. A ideia é que o método <span>`__str__()`</span> deve ser definido para todos os objetos (incluindo aqueles que derivam de novas classes que um programador pode criar) de modo que todos os objetos (independentemente de seu tipo ou classe) pode ser impresso usando a função <span>`str()`</span>. A conversão real de algum objeto <span>`x`</span> para a *string* é então feita através do método específico do objeto <span>`x.__str__()`</span>.

Podemos demonstrar isso criando uma classe <span>`my_int`</span> que herda da classe base de número inteiro do Python e substitui o método <span>`__str__`</span>. (Isto requer mais conhecimento de Python do que o fornecido até este ponto no texto para poder entender este exemplo.)

class my_int(int): 
    """Herdada de int""" 
    def __str__(self): 
        """ Representacao adaptada de str para a classe my_int""" 
        return "my_int: %s" % (int.__str__(self))
 
a = my_int(3)
b = int(4)            # equivalente a b = 4
print("a * b = ", a * b)
print("Type a = ", type(a), "str(a) = ", str(a))
print("Type b = ", type(b), "str(b) = ", str(b))

#### Leitura complementar

Veja [Documentação Python, Modelos de Dados](http://docs.python.org/reference/datamodel.html)

Tipo (*type*)
----

O comando <span>`type(<object>)`</span> retorna o tipo de um objeto:

type(1)

type(1.0)

type("Python")

import math
type(math)

type(math.sin)

isinstance
----------

<span>`isinstance(<object>, <typespec>)`</span> retorna verdadeiro (`True`) se o objeto passado é uma instância do tipo de dado passado, ou de qualquer uma de suas superclasses. Use <span>`help(isinstance`</span>) para a sintaxe completa.

isinstance(2,int)

isinstance(2.,int)

isinstance(a,int)    # a é uma instância de my_int

type(a)

Obtendo ajuda com `help`
----

- A função `help` reportará o *docstring* (atributo mágico com nome `__doc__` do objeto que é passado, às vezes complementado com informação adicional. No caso de funções, `help` também mostrará a lista de argumentos que a função aceita (mas não fornecerá o valor de retorno).

- `help()` inicializa um ambiente interativo de ajuda.

- É comum usar o comando `help` muitas vezes para se lembrar da sintaxe e semântica dos comandos.

help(isinstance)

import math
help(math.sin)

A função <span>`help`</span> depende do nome de um objeto (que deve existir no espaço de nomes corrente). Por exemplo, <span>help(math.sqrt)</span> não funcionará se o módulo <span>`math`</span> não tiver sido importado antes.

del math # desligando o modulo math (omp anteriormente) para destacar o erro.
help(math.sqrt) 

import math
help(math.sqrt)

Em vez de importar o módulo, poderíamos ter também passado a *string* <span>`math.sqrt`</span> para a função `help`, i.e.:

help('math.sqrt')

- <span>`help`</span> é uma função que fornece informações sobre o objeto que é passado como seu argumento. A maioria das coisas em Python (classes, funções, módulos, etc.) são objetos e, por isso, podem ser passados para a função `help`. Há, no entanto, algumas coisas para as quais você gostaria de ajuda, mas que não são objetos existentes em Python. Nesses casos, muitas vezes é possível passar uma *string* contendo o nome da coisa ou conceito para a função `help`, por exemplo.

- <span>`help('modules')`</span> gerará uma lista de todos os módulos que podem ser importados para o interpretador corrente. Note que `help(modules)` (note a ausência de aspas) resultará em um `NameError` (a menos que você tenha a má sorte de ter uma variável chamada módulos em seu ambiente de nomes, caso em que você obterá ajuda a respeito dessa variável).

- <span>`help('algum_modulo')`</span>, onde `algum_modulo` é um módulo que ainda não foi importado (e ainda não é um objeto), lhe dará as informações de ajuda desse módulo.

- <span>`help('alguma_keyword')`</span>: por exemplo <span>'and'</span>, <span>'if'</span> ou <span>'print'</span>, isto é, <span>`help('and')`</span>, <span>`help('if')`</span> e <span>`help('print')`</span>. Estas são palavras-chave especiais reconhecidas em Python: elas não são objetos e, portanto, não podem ser passadas como argumentos para `help`. Passe o nome da palavra-chave como uma *string* para `help` funcionar, mas somente se você tiver a documentação em `html` instalada e se o interpretador Python tiver sido informado da localização da documentação ao se definir a variável de ambiente PYTHONDOCS.

*Docstrings* (*strings* de documentação)
----------

O comando `help(<object>)` acessa as *strings* de documentação de objetos.

Qualquer *string* literal aparecendo como o primeiro item na definição de uma classe, função, método ou módulo, é considerada como sua *docstring*.

<span>`help`</span> inclui a docstring na informação que ela exibe sobre o objeto. Além da *docstring*, ela pode exibir algumas outras informações. Por exemplo, no caso de funções, ela exibe a assinatura da função. A *docstring* é armazenada no atributo `__doc__` do objeto.

help(math.sin) 
# Help on built-in function sin in module math (<-- texto da docstring)

print(math.sin.__doc__)

Para funções, classes tipos, módulos, etc. definidos pelo usuário, deve-se sempre fornecer uma *docstring*.

Documentando uma função definida pelo usuário:

def power2and3(x):
    """Retorna a tupla (x**2, x**3)"""
    return x**2 ,x**3

power2and3(2)

power2and3(4.5)

power2and3(0+1j)

help(power2and3)

print(power2and3.__doc__)