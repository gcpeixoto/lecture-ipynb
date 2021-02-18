Para onde ir a partir daqui?
======================

Aprender uma linguagem de programação é o primeiro passo para tornar-se um "computacionalista" que queira fazer avançar a ciência e a engenharia através de modelagem computacional e simulação.

Enumeramos algumas habilidades adicionais que podem ser muito benéficas para o trabalho diário do cientista computacional, mas é claro que elas não são exaustivas.

Programação avançada
--------------------

Este texto enfatizou a formação de uma base sólida em termos de programação, abrangendo fluxo de controle, estruturas de dados e elementos da programação procedural e funcional. Não falamos de Orientação a Objetos em grande detalhe, nem discutimos alguns dos recursos mais avançados do Python, como iteradores e decoradores, por exemplo.

Linguagem de programação compilada
-----------------------------

Quando o desempenho começa a ser a prioridade máxima, talvez seja necessário usar código compilado, e provavelmente incorporá-lo em um código Python para realizar os cálculo nas partes onde há deficiência de desempenho (*bottlenecks*).

Fortran, C e C++ são escolhas sensíveis por enquanto. Talvez Julia num futuro próximo.

Também precisamos aprender a integrar código compilado com Python usando ferramentas como Cython, Boost, Ctypes e Swig.

Teste
-------

Uma boa codificação é suportada por uma série de testes de unidades e sistemas que podem ser executados rotineiramente para verificar se o código funciona corretamente. Ferramentas como `doctest`, `nose` e `pytest` são inestimáveis, e devemos aprender, pelo menos, como usar o `pytest` (ou o `nose`).

Modelos de simulação
-----------------

Uma série de ferramentas-padrão para simulações, como Monte Carlo, Dinâmica Molecular, modelos baseados em *lattice*, diferenças finitas e elementos finitos, são comumente usados para resolver desafios específicos de simulação - é útil ter pelo menos uma visão geral deles.

Engenharia de software para códigos de pesquisa
---------------------------------------

Os códigos de pesquisa trazem desafios particulares: os requisitos podem mudar durante o tempo de execução do projeto. Precisamos de grande flexibilidade e reprodutibilidade. Uma série de técnicas estão disponíveis para dar suporte de forma eficaz.

Dados e visualização
----------------------

Lidar com grandes quantidades de dados, processá-los e visualizá-los pode ser um desafio. Conhecimento fundamental de projeto de banco de dados, visualização 3D e ferramentas modernas de processamento de dados, como o pacote Pandas do Python, ajudam com isso.

Controle de versão
---------------

O uso de uma ferramenta de controle de versão, como git ou mercurial, deve ser uma abordagem padrão e melhora significativamente a eficácia da escrita de código, ajuda com o trabalho em equipe e - talvez o mais importante - suporta a reprodutibilidade de resultados computacionais.

Execução paralela
------------------

A execução paralela de códigos é uma maneira de tornar códigos em grande escala mais ágeis. Isso pode ser pelo uso de MPI para a comunicação *inter-node* ou OpenMP para a paralelização *intra-node*, ou um modo híbrido que integre ambos.

O recente aumento da computação GPU fornece ainda outra via de paralelização, e também os processadores multinúcleo, como o Intel Phi.

### Agradecimentos

- Marc Molinari, por revisar este manuscrito em 2007.

- Neil O'Brien, por contribuir para a seção SymPy.

- Jacek Generowicz, por me apresentar o Python no último milênio, e por gentilmente compartilhar inúmeras idéias de seu curso de Python.

- EPSRC, pelo suporte parcial deste trabalho (GR/T09156/01 e EP/G03690X/1).

- Estudantes e outros leitores que comentaram e/ou apontaram erros de digitação,  etc.

[1] a linha vertical é mostrar apenas a divisão entre os componentes originais apenas; matematicamente, a matriz aumentada comporta-se como qualquer outra matriz 2 × 3, e nós a codificamos no SymPy como faríamos com qualquer outra.

[2] a partir da documentação <span>`help(preview)`</span>: "Atualmente isso depende do pexpect, que não está disponível para Windows".

[3] O valor exato para o limite superior está disponível em `sys.maxint`.

[4] Adicionamos, por completeza, que um programa C (ou C++/Fortran) que execute o mesmo laço será cerca de 100 vezes mais rápido do que o laço `float` do Python e, portanto, cerca de 100\*200 = 20000 vezes mais rápido que o laço simbólico.

[5] Neste texto, geralmente fazemos a importação do `numpy` com o nome `N` assim: `import numpy as N`. Se você não tiver `numpy` na sua máquina, você pode substituir esta linha por `import Numeric as N`, ou `import numarray as N`.

[6] Nota histórica: isso mudou da versão Scipy 0.7 para 0.8. Antes da 0,8, o valor de retorno era um `float` se um problema unidimensional fosse resolvido.