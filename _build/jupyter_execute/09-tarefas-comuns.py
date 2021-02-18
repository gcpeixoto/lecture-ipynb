Tarefas comuns
============

Aqui fornecemos uma seleção de pequenos exemplos de programas que abordam algumas tarefas e um pouco mais de códigos em Python aos quais podemos recorrer enquanto buscamos inspiração para atacar um determinado problema.

Muitas maneiras de computar uma série
-----------------------------

As an example, we compute the sum of odd numbers in different ways.

Como um exemplo, computamos a soma de números ímpares de diferentes maneiras.

def calcula_soma1(n):
    """computa e retorna a soma de 2,4,6,...,m, onde m 
    é o maior número par menor do que n.
    
    Por exemplo, com n = 7, computamos 0+2+4+6 = 12.
    
    Esta implementação usa a variável 'soma' que é 
    incrementada a cada iteração do laço `for`.
    """    
    soma = 0
    for i in range(0, n, 2):
        soma = soma + i
    return soma


def calcula_soma2(n):
    """Idem...

    Esta implementação usa um loop `while`:
    """

    contador = 0
    soma = 0
    while contador < n:
        soma = soma + contador
        contador = contador + 2

    return soma


def calcula_soma3(n, inicio=0):
    """Idem... Esta é uma implementação recursiva:"""

    if n <= inicio:
        return 0
    else:
        return inicio + calcula_soma3(n, inicio + 2)


def calcula_soma4a(n):
    """Uma abordagem funcional... Este parece ser 
    o código mais curto e conciso.
    """
    return sum(range(0, n, 2))

from functools import reduce
def calcula_soma4b(n):
    """Uma abordagem funcional... não faz uso de 
    'sum' mas conveniente aqui.
    """
    return reduce(lambda a, b: a + b, range(0, n, 2))


def calcula_soma4c(n):
    """Uma abordagem funcional... um pouco mais rápida do 
    que `calcula_soma4b` uma vez que evitamos o uso de `lambda`
    """
    import operator
    return reduce(operator.__add__, range(0, n, 2))


def calcula_soma4d(n):
    """Usando compreensão de lista."""
    return sum([k for k in range(0, n, 2)])


def calcula_soma4e(n):
    """Usando outra variação de compreensão de lista."""
    return sum([k for k in range(0, n) if k % 2 == 0])


def calcula_soma5(n):
    """Usando python numérico (numpy). Esta é muito rápida
    (mas não tem o mesmo efeito para n muito maior do que 10)."""
    import numpy
    return numpy.sum(2 * numpy.arange(0, (n + 1) // 2))


def teste_consistencia():
    """Verifica todas as funções `calcula_soma`. As funções neste arquivo
    produzem a mesma resposta para todo n >= 2 and < N.
    """
    def verificacao_1_n(n):
        """Compara a saida de `compute_sum1` com todas as outras funções 
        para um dado n>=2. Lança exceção do tipo `AssertionError` se houver discordância na saída."""
        funcs = [calcula_soma1, calcula_soma2, calcula_soma3,
                 calcula_soma4a, calcula_soma4b, calcula_soma4c,
                 calcula_soma4d, calcula_soma4e, calcula_soma5]
        resp1 = calcula_soma1(n)
        for f in funcs[1:]:
            assert resp1 == f(n), "%s(n)=%d diferente de %s(n)=%d " \
                                  % (funcs[0], funcs[0](n), f, f(n))

    # laço principal de teste na funcao teste_consistencia
    for n in range(2, 1000):
        verificacao_1_n(n)

if __name__ == "__main__": 
    m = 7
    resultado_correto = 12
    resultado_atual = calcula_soma1(m)
    print("este resultado eh {}, esperado {}".format(
        resultado_atual, resultado_correto))
    # compara com resultado correto
    assert resultado_atual == resultado_correto
    # verifica todos os outros metodos 
    assert calcula_soma2(m) == resultado_correto
    assert calcula_soma3(m) == resultado_correto
    assert calcula_soma4a(m) == resultado_correto
    assert calcula_soma4b(m) == resultado_correto
    assert calcula_soma4c(m) == resultado_correto
    assert calcula_soma4d(m) == resultado_correto
    assert calcula_soma4e(m) == resultado_correto
    assert calcula_soma5(m) == resultado_correto

    # verificação mais sistemática para muitos valores
    teste_consistencia()

Todas as implementações diferentes mostradas acima calculam o mesmo resultado. Há algumas coisas a serem aprendidas com isso:

- Há um número grande (provavelmente infinito) de soluções para um determinado problema. (Isso significa que escrever programas é uma tarefa que exige criatividade!)

- Estes podem atingir o mesmo "resultado" (neste caso, o cálculo de um número).

- Diferentes soluções podem ter características diferentes. Elas podem:

     - ser mais rápidas ou mais lentas

     - usar menos ou mais memória

     - ser mais fáceis ou mais difíceis de entender (quando se lê o código-fonte)

     - podem ser consideradas mais ou menos elegantes.

Classificação (*Sorting*)
-------

Suponha que precisamos classificar uma lista de tuplas com pares de identificadores de usuário e nomes, i.e.

minha_lista = [("tarso", "Paulo de Tarso",),
          ("admin", "O Administrador"),
          ("visitante", "O Visitante")]

a qual queremos classificar em ordem crescente de identificadores de usuário. Se houverem dois ou mais identificadores de usuários idênticos, eles devem ser classificados pela ordem dos nomes associados com esses identificadores. Este comportamento é apenas o comportamento padrão de `sort` (que volta ao assunto de como sequencias são comparadas).

coisas = minha_lista # colete seus dados
coisas.sort()        # classifique
print(coisas)        # inspecione os dados classificados

As sequências são inicialmente comparadas pelos primeiros elementos apenas. Se eles diferirem, então uma decisão é tomada com base apenas nesses elementos. Se os elementos forem iguais, somente então os próximos elementos na seqüência são comparados... e assim por diante, até que uma diferença for encontrada, ou ficarmos sem elementos. Por exemplo:

(2,0) > (1,0)

(2,1) > (1,3)

(2,1) > (2,1)

(2,2) > (2,1)

É também possível fazer:

coisas = sorted(coisas)

Quando a lista não é particularmente grande, geralmente é aconselhável usar a função `sorted` (que *retorna uma cópia ordenada* da lista) sobre o método `sort` de uma lista (que altera a lista para uma classificação ordenada de elementos, e retorna `None`).

No entanto, e se os dados que temos forem armazenados de tal forma que, em cada uma das tuplas da lista, o nome venha primeiro, seguido do identificador, isto é,

minha_lista2 = [("Paulo de Tarso", "tarso"),
           ("O Administrador", "admin"),
           ("O Visitante", "visitante")]

We want to sort with the id as the primary key. The first approach to do this is to change the order of `mylist2` to that of `mylist`, and use `sort` as shown above.

The second, neater approach relies on being able to decypher the cryptic help for the sorted function. `list.sort()` has the same options, but its help is less helpful.

Queremos ordenar tomando o identificador como chave primária. A primeira abordagem para fazer isto é mudar a ordem de `minha_lista2` para aquela de `minha_lista`, e usar `sort` como mostrado acima.

help(sorted)

Você deve notar que `sorted` e `list.sort` têm dois parâmetros. O primeiro deles é chamado `key` (palavra-chave, ou simplesmente chave). Você pode usar isso para fornecer uma *função-chave*, que será usada para transformar os itens para ser comparados via `sort`.

Vamos ilustrar isso no contexto do nosso exercício, assumindo que nós armazenamos uma lista de pares como este

    par = nome, id

(i.e. como em `minha_lista_2`) e que queiramos classificar de acordo com `id`, ignorando `nome`. Podemos atingir isto escrevendo uma função que recupere apenas o segundo elemento do par que ela recebe: 

def minha_chave(par):
    return par[1]

minha_lista2.sort(key=minha_chave)

Isto também funciona com uma função anônima:

minha_lista2.sort(key=lambda p: p[1]) 

### Eficiência

A função `key` será chamada exatamente uma vez para cada elemento da lista. Isso é muito mais eficiente do que chamar uma função em cada *comparação* (que era como você personalizava a classificação em versões antigas do Python). Mas se você tiver uma grande lista para ordenar, a sobrecarga de chamada de uma função Python (que é relativamente grande em comparação com a sobrecarga de uma função em C) pode ser notável.

Se a eficiência for realmente importante (e você provou que uma proporção significativa de tempo é gasta nessas funções), você tem a opção de recodificá-las em C (ou em outra linguagem de baixo nível).