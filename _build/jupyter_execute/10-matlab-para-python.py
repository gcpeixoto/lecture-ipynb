Do Matlab para Python
=====================

Comandos importantes
------------------

### O laço `for`

Matlab:

```octave
for i = 1:10
    disp(i)
end
```

No Matlab, a palavra-chave `end` é necessária para finalizar o bloco do laço `for`.

No Python:

for i in range(1,11):
    print(i)

Em Python, é necessário adicionar dois-pontos (":") no final da linha do `for`. (Isto é importante e frequentemente esquecido, principalmente, para quem já programou em Matlab antes.) Além disso, os comandos a serem executados dentro do laço `for` devem ser indentados. 

### A declaração condicional `if-then`

Matlab:

```octave
if a==0
    disp('a é zero')
elseif a<0
    disp('a é negativo')
elseif a==42
    disp('a é 42')
else
    disp('a é positivo')
end
```

Em Matlab, a palavra-chave `end` é necessária na parte final do bloco.

Python:

a = -5

if a==0:
    print('a é zero')
elif a<0:
    print('a é negativo')
elif a==42:
    print('a é 42')
else:
    print('a é positivo')

Em Python, é necessário adicionar dois-pontos (":") após cada condição (i.e., nas linhas começando com `if`, `elif`, `else`). Além disso, os comandos a serem executados dentro de cada parte do escopo `if-then-else` devem ser indentados.

### Indexação

No Matlab, a indexação de matrizes e vetores começa em 1 (similarmente ao Fortran), ao passo que no Python, ela começa em 0 (similarmente ao C).

### Matrizes

Em Matlab, todo objeto é uma matriz. Em Python, há uma biblioteca especializada chamada NumPy que fornece o objeto `array`, o qual, por sua vez, possui todas as funcionalidades correspondentes. Similarmente ao Matlab, o NumPy é baseado em bibliotecas cuja execução é bastante rápida. 

Há um documento introdutório dedicado ao NumPy para usuários do Matlab disponível em <https://docs.scipy.org/doc/numpy-dev/user/numpy-for-matlab-users.html>.