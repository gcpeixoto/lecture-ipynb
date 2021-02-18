*Shells* para Python
=============

IDLE
----

O **IDLE** vem com toda distribuição Python e é uma ferramenta útil para a programação diária. Seu editor fornece destaque de sintaxe.

Existem duas razões pelas quais você poderia optar por outro *shell* para Python, por exemplo:

- Ao trabalhar com o *prompt* do Python, se você desejar preenchimento automático de nomes de variáveis, nomes de arquivos e comandos. Nesse caso, *IPython* é a sua ferramenta de escolha (veja abaixo). O IPython não fornece um editor, mas você pode continuar usando o editor IDLE ou qualquer outro que você quiser para editar seus arquivos.

O IPython fornece uma série de recursos agradáveis para o programador Python mais experiente, incluindo um perfil conveniente de código (veja <http://ipython.scipy.org>).

Recentemente, algumas características interessantes foram adicionadas ao IDLE também (e.g. pressionar a tecla `tab` depois de ter digitado as primeiras letras de nomes de objetos e palavras-chave para preenchimento automático).

Python (linha de comando)
---------------------

Esta é a face mais básica de um *shell* para Python. É muito semelhante ao *prompt* do Python no IDLE, mas não há menus para clicar e nenhuma instalação para editar arquivos.

Python Interativo (IPython)
----------------------------

### Console IPython

O IPython é uma versão melhorada da linha de comando do Python. É uma ferramenta valiosa e vale a pena explorar suas capacidades (veja <http://ipython.org/ipython-doc/stable/interactive/qtconsole.html>)

Você encontrará os seguintes recursos muito úteis:

- Preenchimento automático: Suponha que você digite <span>`a = range(10)`</span>. Em vez de digitar todas as letras, basta digitar <span>`a = ra`</span> e pressionar a tecla `tab`. O IPython mostrará todos os comandos possíveis (e nomes de variáveis) que começam com <span>`ra`</span>. Se você digitar uma terceira letra, aqui <span>`n`</span> e pressionar `Tab` novamente, o IPython completará e adicionará <span>`ge`</span> automaticamente. Isso também funciona para nomes de variáveis e de módulos.

- Para obter ajuda sobre um comando, podemos usar o comando de ajuda do Python. Por exemplo: <span>`help(range)`</span>. O IPython fornece um atalho. Para alcançar o mesmo, basta digitar o comando seguido de um ponto de interrogação: <span>`range?`</span>

- Você pode navegar facilmente por diretórios no seu computador. Por exemplo,

    - <span>`!dir`</span> lista o conteúdo do diretório atual (mesmo que <span>`ls`</span>)

    - <span>`pwd`</span> mostra o diretório de trabalho atual

    - <span>`cd`</span> permite alterar diretórios

- Em geral, ao usar um ponto de exclamação antes do comando, você passa o comando para o `shell` (e não para o interpretador do Python).

- Você pode executar programas Python a partir do IPython usando `%run`. Suponha que você tenha um arquivo `hello.py` no diretório atual. Você pode então executá-lo digitando: `%run hello`. Observe que isto difere da execução de um programa Python no IDLE: o IDLE reinicia a sessão do interpretador do Python e, assim, deleta todos os objetos existentes antes de a execução começar. Este não é o caso com o comando <span>`run`</span> no IPython (nem ao executar partes de código Python no Emacs usando o modo Python). Em particular, isso pode ser muito útil se for necessário configurar alguns objetos para testar o código em que se está trabalhando. Usar o comando <span>`run`</span> do IPython, ou o Emacs em vez do IDLE permite-nos manter esses objetos na sessão do interpretador e atualizar apenas a função, classe, etc. que está sendo desenvolvida.

- permite a edição de várias linhas do histórico de comandos

- fornece destaque de sintaxe *on-the-fly*

- exibe *docstrings* *on-the-fly*

- pode incluir figuras via Matplotlib (ativar modo `inline` com o comando `%matplotlib inline`)

- `% load` carrega o arquivo do disco ou de alguma URL para edição

- `% timeit` mede o tempo de execução para uma determinada declaração

- ...e muito mais.

- Leia mais em <http://ipython.org/ipython-doc/dev/interactive/qtconsole.html>

Se você tiver acesso a esse *shell*, você talvez o considerará como seu *prompt* padrão do Python.


### Jupyter Notebook

O Jupyter Notebook (anteriormente IPython Notebook) permite que você execute, armazene, carregue e reexecute uma sequencia de comandos Python, além de incluir texto explicativo, imagens e outras mídias. É um desenvolvimento recente e excitante que tem o potencial de se desdobrar em uma ferramenta de grande significado, por exemplo, para

-   documentar cálculos e processamento de dados

-   dar suporte ao ensino e aprendizagem

    -   do Python em si

    -   de métodos estatísticos

    -   do pós-processamento geral de dados

    -   ...

-   documentação de novos códigos

-   testes de regressão automática pela reexecucação de *IPython notebooks* para fins de comparação entre dados de saída e dados armazenados.

**Leitura complementar**

-   Jupyter Notebook (<http://jupyter-notebook.readthedocs.io/en/latest/>).

-   IPython (<http://ipython.org>).

Spyder
------

Spyder é o *Scientific PYthon Development EnviRonment*: um ambiente de desenvolvimento interativo poderoso para a linguagem Python com recursos avançados de edição, teste interativo, depuração, introspecção e computação numérica, graças ao suporte do IPython e bibliotecas populares, tais como NumPy (linear algebra), SciPy (signal and image processing) ou Matplotlib (plotagem interativa 2D/3D). Veja mais em <http://pythonhosted.org/spyder/>.

Algumas características do Spyder:

- Dentro do Spyder, o console IPython é o interpretador Python padrão, e

- o código no editor pode ser executado total ou parcialmente neste buffer.

- O editor suporta a verificação automática de erros usando `pyflakes` e

- o editor avisa (se desejado) se a formatação do código se desviar do guia de estilo PEP8.

- O Depurador Ipython pode ser ativado e

- um analisador de desempenho (*profiler*) é fornecido.

- Um explorador de objetos mostra documentação para funções, métodos, etc, *on-the-fly* e um

- explorador de variáveis exibe nomes, tamanho e valores para variáveis numéricas.

O Spyder está atualmente (a partir de 2014) no caminho para se tornar um ambiente integrado multi-plataforma poderoso e robusto para desenvolvimento em Python, com especial ênfase em computação científica e engenharia.

Editores
-------

Todos os principais editores que são usados para programação fornecem suporte a Python (e.g. Emacs, Vim, Sublime Text), alguns *Integrated Development Enviroments* (IDEs) vêm com seu próprio editor (Spyder, Eclipse). Qual é o melhor é, em parte, uma questão de escolha.

Para iniciantes, o Spyder parece uma escolha sensata, pois fornece um IDE, permite a execução de porções de código em uma sessão de interpretação e é fácil de aprender.