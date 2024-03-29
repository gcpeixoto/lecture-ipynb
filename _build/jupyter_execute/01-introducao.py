# Introdução

Este texto resume algumas ideias centrais relevantes para a Engenharia Computacional e Computação Científica usando Python. A ênfase está em apresentar alguns conceitos de programação em Python que são importantes para algoritmos numéricos. Os capítulos posteriores versam sobre bibliotecas numéricas, tais como <span>`NumPy`</span> e <span>`SciPy`</span>, as quais, individualmente, merecem muito mais espaço para serem abordadas do que o fornecido aqui. Temos o objetivo de capacitar o leitor para aprender de maneira independente a como usar as funcionalidades dessas bibliotecas através da documentação disponível tanto *online* quanto nos próprios pacotes.

## Modelagem Computacional

### Introdução

Cada vez mais, processos e sistemas são pesquisados ou desenvolvidos através de simulações computacionais: novos protótipos de aeronaves, como o recente A380, são primeiramente projetados e testados virtualmente através de simulações computacionais. Com o crescente poder computacional disponível através de supercomputadores, clusters de computadores e até mesmo de máquinas *desktop* e *laptops*, essa tendência provavelmente permanecerá.

Simulações computacionais são rotineiramente utilizadas na pesquisa básica para ajudar a entender medições experimentais e para substituir - por exemplo - o crescimento e a fabricação de amostras/experiências custosas, sempre que possível. Em um contexto industrial, o projeto de produtos e dispositivos geralmente pode ser feito muito mais eficazmente de modo virtual através de simulações do que através da construção e teste de protótipos. Isto ocorre, em particular, em áreas onde as amostras são custosas, como é o caso da nanociência (onde é custoso criar coisas pequenas) e da indústria aeroespacial (onde é custoso construir coisas grandes). Existem também situações em que certas experiências só podem ser realizadas virtualmente (variando da astrofísica ao estudo de efeitos de acidentes nucleares ou químicos de grande escala). A Modelagem Computacional, incluindo o uso de ferramentas computacionais para pós-processamento, análise e visualização de dados, tem sido utilizada na engenharia, física e química por muitas décadas, mas está se tornando mais importante devido à disponibilidade barata de recursos computacionais. A Modelagem Computacional também está começando a desempenhar um papel mais importante nos estudos de sistemas biológicos, economia, arqueologia, medicina, saúde e muitos outros domínios.

oct(234)

### Modelagem Computacional

Para estudar um processo com simulação computacional, distinguimos duas etapas: a primeira é desenvolver um *modelo* do sistema real; a segunda, resolver as equações envolvidas numericamente. Ao estudar o movimento de um pequeno objeto, como uma moeda, digamos, sob a influência da gravidade, podemos ignorar seu atrito com o ar: nosso modelo - que só pode considerar a força gravitacional e a inércia da moeda, ou seja, $a(t) = F/m = -9.81 \, m/s^2$ - é uma aproximação do sistema real. O modelo normalmente permitir-nos-á expressar o comportamento do sistema (em alguma forma aproximada) através de equações matemáticas, que geralmente envolvem equações diferenciais ordinárias (EDOs) ou equações diferenciais parciais (EDPs).

Nas ciências naturais, como física, química e engenharia, muitas vezes não é tão difícil encontrar um modelo adequado, embora as equações resultantes tendam a ser muito difíceis de resolver e, na maioria dos casos, impossíveis de serem resolvidas analiticamente.

Por outro lado, em assuntos que não são tão bem descritos através de uma estrutura matemática e dependem do comportamento de objetos cujas ações são impossíveis de serem previstas de forma determinística (como os seres humanos), é muito mais difícil encontrar um modelo adequado para descrever a realidade. Como uma regra geral, nestas disciplinas, as equações resultantes são mais fáceis de serem resolvidas, mas difíceis de serem encontradas e a validade de um modelo precisa ser questionada muito mais. Exemplos típicos são as tentativas de simular a economia, o uso de recursos globais, o comportamento de uma multidão em pânico, etc.

Até agora, apenas discutimos o desenvolvimento de *modelos* para descrever a realidade. O uso desses modelos não envolve necessariamente computadores ou algum trabalho numérico. Na verdade, se a equação de um modelo puder ser resolvida de forma analítica, então deve-se fazer isso e registrar a solução para a equação.

Na prática, dificilmente uma equação-modelo de sistemas de interesse pode ser resolvida analiticamente, e é aí que o computador entra: usando métodos numéricos, podemos, pelo menos, estudar o modelo *para um determinado conjunto de condições de contorno*. Para o exemplo considerado acima, talvez não possamos ver facilmente a partir de uma solução numérica que a velocidade da moeda sob a influência da gravidade mudará linearmente com o tempo (o que podemos constatar facilmente a partir da solução analítica disponível para este sistema simples: 
$v(t) = 9.81t + v_0 \, m/s$).

A solução numérica que pode ser calculada usando um computador consistiria de dados que mostram como a velocidade muda ao longo do tempo para uma velocidade inicial particular $v_0$ ($v_0$ é uma condição de contorno aqui). O programa computacional reportaria uma longa lista de dois números mantendo o valor do tempo $t_i$ para o qual um determinado valor da velocidade $v_i$ foi calculado. Ao plotarmos $v_i$ *versus* $t _i$, ou ajustarmos uma curva a partir dos dados, poderemos entender a tendência do comportamento da moeda (que pode ser vista a partir da solução analítica, é claro).

Claramente, é desejável encontrar soluções analíticas sempre que possível, mas o número de problemas onde isso é possível é pequeno. Geralmente, a obtenção do resultado numérico de uma simulação computacional é bastante útil (apesar das deficiências dos resultados numéricos em comparação com uma expressão analítica), porque é a única maneira possível de estudar o sistema.

Em suma, o nome *modelagem computacional* deriva das duas etapas: (i) *modelagem*, em que se busca um modelo que descreva o sistema real, e (ii) a resolução das equações do modelo usando *métodos computacionais*.

### Programação como suporte à modelagem computacional

Existe uma grande quantidade de pacotes que fornecem recursos para modelagem computacional. Se estes satisfizerem as necessidades de pesquisa ou de projeto, e o processamento e a visualização de dados sejam adequadamente suportados através de ferramentas existentes, pode-se realizar estudos de modelagem computacional sem nenhum conhecimento de programação mais aprofundado.

Em um ambiente de pesquisa - tanto na academia quanto na pesquisa por novos produtos e idéias na indústria -, muitas vezes se atinge um ponto em que os pacotes existentes não são capazes de realizar uma determinada tarefa de simulação que surge, ou onde se faz necessário o aprendizado de novas maneiras de analisar os dados existentes.

Nesse ponto, habilidades de programação tornam-se um requisito. Em geral, também é útil ter um entendimento amplo dos blocos de construção de software e idéias básicas de engenharia de software à medida que usamos mais e mais dispositivos que são controlados por software.

Esquecemos, com frequencia, que não há nada que o computador faça que nós, como seres humanos, não possamos fazer. O computador pode fazê-lo muito mais rápido, mas o fará com muitos erros. Portanto, não há mágica nos cálculos que um computador executa: os cálculos poderiam ter sido feitos por seres humanos - na verdade o foram durante muitos anos. Veja, por exemplo, o tópico [*Computador Humano*](https://pt.wikipedia.org/wiki/Computador_humano) da Wikipedia.

Compreender como construir uma simulação computacional reduz-se, grosso modo, a: (i) encontrar o modelo (muitas vezes, isto significa encontrar as equações corretas), (ii) saber como resolver estas equações numericamente, (iii) implementar os métodos para calcular essas soluções (este é o ponto na programação).

## Por que Python para Computação Científica?


O foco do projeto da linguagem Python está na produtividade e legibilidade de código. Por exemplo, através de:

-   console Python interativo;

-   sintaxe muito clara e legível através de indentação;

-   fortes capacidades de introspecção;

-   plena modularidade e pacotes hierárquicos de suporte;

-   manipulação de erros com base em exceções;

-   tipos de dados dinâmicos e gerenciamento de memória automático.

*Como Python é uma linguagem interpretada e, muitas vezes, executada mais lentamente do que código compilado, pode-se perguntar por que alguém deveria considerar essa linguagem "lenta" para simulações computacionais?*

Há duas respostas para esta crítica:

1. *Tempo de implementação versus tempo de execução*: não é apenas o tempo de execução que contribui para o custo de um projeto computacional: também é necessário considerar o custo do trabalho de desenvolvimento e manutenção.

   Nos primórdios da computação científica (digamos, nas decádas de 1960/70/80), o tempo de computação era tão proibitivo que fazia sentido investir muitos meses do tempo de um programador para melhorar o desempenho de um cálculo em qualquer ínfima porcentagem.

   Hoje em dia, no entanto, os ciclos de uma unidade de processamento (CPU) tornaram-se muito mais baratos do que o tempo do programador. Para os códigos de pesquisa, os quais são executados, via de regra, apenas um pequeno número de vezes (antes que os pesquisadores passem para o próximo problema), pode ser econômico aceitar que o código seja executado apenas com 25% da velocidade esperada possível se isto economiza, digamos, um mês do tempo de um pesquisador (ou programador). Por exemplo: se o tempo de execução de parte do código for de 10 horas, com uma previsão de que ele seja executado cerca de 100 vezes, então o tempo total de execução é de aproximadamente 1000 horas. Seria ótimo se  isto pudesse ser reduzido para 25%. Seria uma economia de 750 horas de processamento. Por outro lado, uma espera extra (cerca de um mês) e o custo de 750 horas de CPU valeria o investimento de um mês do tempo de uma pessoa.

   *Legibilidade e manutenção do código - código curto, menos erros*: uma questão relacionada é que um código de pesquisa não é usado apenas para um projeto, mas continua sendo usado repetidas vezes, evolui, cresce, bifurca-se etc. Neste caso, o investimento em mais tempo para tornar o código mais rápido é uma justificativa frequente. Ao mesmo tempo, uma quantidade significativa de tempo do programador concentrar-se-á em (i) introduzir as mudanças necessárias, (ii) testá-las mesmo antes de o trabalho de otimização da velocidade de execução da versão alterada começar. Para manter, estender e modificar um código de modos ainda imprevistos, o uso de uma linguagem que seja fácil de ler e que possua grande poder expressivo é recomendado.

2. *Código Python bem escrito pode ser muito rápido* se partes críticas e demoradas do código forem executadas através de linguagens compiladas: normalmente, menos de 5% do código de um projeto de simulação precisam de mais de 95% do tempo de execução. Desde que esses cálculos sejam feitos de forma muito eficiente, não é necessário se preocupar com todas as outras partes do código, já que o tempo total de sua execução é insignificante.

   A parte do programa onde há intensa computação deve ser ajustada para alcançar o melhor desempenho. Várias opções são oferecidas em Python:

   - Por exemplo, a extensão NumPy fornece uma interface Python para as eficientes bibliotecas compiladas LAPACK, que são quase o padrão em álgebra linear numérica. Se os problemas em estudo puderem ser formulados de forma que, eventualmente, grandes sistemas de equações algébricas tenham que ser resolvidos, ou autovalores computados, etc., o código compilado na biblioteca LAPACK pode ser usado (através do pacote NumPy). Nesta etapa, os cálculos são realizados com o mesmo desempenho do Fortran/C, haja vista que o código usado é essencialmente escrito em Fortran/C. O Matlab, a propósito, explora exatamente isto: a linguagem de *script* Matlab é muito lenta (cerca de 10 vezes mais lenta do que Python), mas o Matlab ganha seu poder ao delegar operações matriciais às bibliotecas compiladas LAPACK.

   - As bibliotecas numéricas C/Fortran existentes podem ser "interfaceadas" (para serem chamadas a partir do programa Python) através de, por exemplo, Swig, Boost.Python e Cython.

   - O Python pode ser estendido através de linguagens compiladas se a parte do problema com grande demanda computacional não for algoritmicamente padronizada e não houver biblioteca existente que possa ser usada. As linguagens comumente utilizadas para implementar extensões rápidas são C, C++ e Fortran.

   - Listamos algumas ferramentas que são usadas para usar código compilado a partir do Python:

       - A extensão <span>`scipy.weave`</span> é útil se apenas uma expressão curta precisar ser expressa em C.
       - A interface Cython está crescendo em popularidade para declarar semi-automaticamente os tipos de variáveis no código Python, para traduzir esse código para C (automaticamente) e depois usar o código C compilado a partir do Python. O Cython também é usado para encapsular rapidamente uma biblioteca C existente com uma interface para que a biblioteca C possa ser usada a partir do Python.

       - Boost.Python é especializado para encapsular código C++ no Python. 

A conclusão é que *Python é “rápida o suficiente” para a maioria das tarefas computacionais e sua linguagem de alto nível amigável ao usuário frequentemente é compensada em velocidade reduzida quando comparada a linguagens compiladas de baixo nível. A combinação de Python com códigos compilados escritos sob medida para desempenho de partes críticas do código resulta em velocidades virtualmente ótimas na maioria dos casos.*  

### Estratégias de otimização

Em geral, entendemos a redução do tempo de execução quando discutimos "otimização de código" no contexto da modelagem computacional e, essencialmente, realizamos os cálculos necessários o mais rápido possível. (Às vezes, precisamos reduzir a quantidade de memória RAM, bem como a quantidade de entrada e saída de dados para o disco ou para a rede). Ao mesmo tempo, precisamos ter certeza de que não investimos quantidades inapropriadas de tempo de programação para acelerar o código. Como sempre, deve haver um equilíbrio entre o tempo dos programadores e a melhoria que podemos obter com isso.

### Primeiro faça certo, depois otimize

Para escrever códigos rápidos de forma eficaz, observamos que a ordem correta é: (i) escrever um programa que realize o cálculo correto. Para isso, escolha uma linguagem/abordagem que lhe permita *escrever o código rapidamente e fazê-lo funcionar rapidamente* - independentemente da velocidade de execução. Então (ii) altere o programa ou reescreva-o do zero na mesma linguagem para tornar a execução mais rápida. Durante o processo, continue comparando os resultados com a versão lenta primeiramente escrita para garantir que a otimização não introduza erros. Uma vez que estivermos familiarizados com o conceito de testes de regressão, eles devem ser usados para comparar o código novo (e esperançosamente mais rápido) com o original.

Um padrão comum em Python é começar a escrever o código Python puro e, em seguida, começar a usar bibliotecas Python que usam código compilado internamente (como os *arrays* rápidos fornecidas pelo NumPy e as rotinas do SciPy, que voltam-se para códigos numéricos já estabelecidos, tais como ODEPACK, LAPACK e outros). Se necessário, pode-se - depois de uma análise de desempenho (*profiling*) cuidadosa - começar a substituir partes do código Python por uma linguagem compilada, como C ou Fortran, a fim de melhorar a velocidade de execução ainda mais (conforme discutido acima).

### Prototipagem em Python

Verifica-se que - mesmo se um código específico tiver que ser escrito em, digamos, C++ - é (frequentemente) mais eficiente prototipar o código em Python, e uma vez que um projeto apropriado (estrutura de classes) for encontrado, transferir o código para C++.


## Literatura

Enquanto este texto inicia-se com uma introdução de alguns aspectos básicos da linguagem de programação Python, você pode achar necessário - dependenddo de sua experiência prévia - buscar fontes secundárias para entender algumas ideias completamante. Nesse caso, os seguintes documentos são indicados:

-   Allen Downey, *Pense em Python*. Disponível online em html e pdf em https://penseallen.github.io/PensePython2e/.

-   A documentação oficial Python: <http://www.python.org/doc/> e

-   O tutorial Python (<http://docs.python.org/tutorial/>)

Os seguintes links também podem ser úteis para você:

-   Homepage do <span>`numpy`</span> (<http://numpy.scipy.org/>)

-   Homepage do <span>`scipy`</span> (<http://scipy.org/>)

-   Homepage do <span>`matplotlib`</span> (<http://matplotlib.sourceforge.net/>).

-   Guia de estilos Python (<http://www.python.org/dev/peps/pep-0008/>

### Vídeo-aulas sobre Python para iniciantes

Você gosta de ouvir/seguir vídeo-aulas? Há uma série de 24 vídeo-aulas intituladas *Introduction to Computer Science and Programming* dadas por Eric Grimsom e John Guttag do MIT disponíveis em <http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00-introduction-to-computer-science-and-programming-fall-2008/>. Estas vídeo-aulas são destinadas a estudantes com pouca ou nenhuma experiência em programação. Elas proporcionam aos alunos uma compreensão do papel que a computação pode desempenhar na resolução de problemas. Elas também têm o objetivo de ajudar os alunos, independentemente de sua formação, a se sentirem confiantes em sua capacidade de escrever pequenos programas que lhes permitam atingir objetivos úteis.

### Listas de discussão sobre Python

Existe também uma lista de discussão (<http://mail.python.org/mailman/listinfo/tutor>) onde iniciantes são bem-vindos para fazer perguntas sobre Python. Tanto usar os arquivos quanto postar suas próprias questões (o que, de fato, ajuda outros também) podem ajudar você a entender a linguagem. Use a etiqueta padrão da lista de discussão (por exemplo, seja educado, conciso, etc.). Você pode ter interesse em ler <http://www.catb.org/esr/faqs/smart-questions.html> para obter algumas orientações sobre como fazer perguntas em listas de discussão.

## Versões do Python

Existem duas versões de Python por aí: Python 2.x and Python 3.x. Elas são levemente diferentes — as mudanças na Python 3.x foram introduzidas para corrigir algumas deficiências no projeto da linguagem identificados desde o seu início. Uma decisão que foi tomada assumiu que alguma incompatibilidade deveria ser aceita para se atingir o objetivo maior de uma linguagem melhor para o futuro.

Para computação científica, é crucial fazer uso de bibliotecas numéricas tais como [NumPy](http://numpy.scipy.org/), [SciPy](http://www.scipy.org) e o pacote de plotagem [Matplotlib](http://matplotlib.sourceforge.net/).

Todos eles estão disponíveis para Python 3, versão que usaremos aqui. No entanto, há muito código ainda em uso que foi escrito para Python 2. Para tanto, é útil saber das diferenças. O exemplo mais proeminente é que em Python 2.x, o comando `print` é especial, ao passo que em Python 3 é uma função ordinária. Por exemplo, em Python 2.7, podemos escrever:

```python
print "Hello World"
```

ao passo que, em Python 3, isto causaria um erro de sintaxe. A maneira correta de usar `print` em Python 3 seria como uma função, i.e.

print("Hello World")

Felizmente, a notação de função (i.e. com os parênteses) também é permitida em Python 2.7. Assim, nossos exemplos devem funcionar tanto em Python 2.x, quanto em Python 3.x. (Existem outras diferenças não mencionadas aqui.)

## Estes documentos

Este material foi convertido do `LaTex` para um conjunto de `Jupyter Notebooks`, tornando os exemplos nele contidos interativos. Você pode executar qualquer bloco de código iniciado por `In [ ]:` clicando na respectiva célula e pressionando `shift-enter`, ou clicando no botão <i class="fa fa-step-forward"></i> da barra de ferramentas.

## Seu *feedback*

Seu *feedback* é desejado. Caso você encontre algum erro neste texto, ou tiver sugestões sobre como alterá-lo ou estendê-lo, fique à vontade para entrar em contato com o Hans pelo e-mail `fangohr@soton.ac.uk`.

Se você encontrar uma URL que não está funcionando (ou apontando para o material errado), informe ao Hans também. Como o conteúdo da internet muda rapidamente, é difícil acompanhar essas mudanças sem um *feedback*.