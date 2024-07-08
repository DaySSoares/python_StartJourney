# O input é uma função entre as varias que existem no python, a partir dessa função podemos criar dentro do sistema uma entrada de dados via teclado. Podemos ter inputs de nome, telefone, cpf, assim por diante... Veja abaixo como funciona o uso do input:
# %%
nome = input("Insira um nome para usuário: \n")
print("Bem-vindo(a) de volta usuario", nome)

# %%
#calculadora com python
print("Calculadora de soma")
a = input("Insira um valor: ")
a= int(a)

b = int(input("Insira mais um valor: "))


soma = a + b
print("A soma de", a, "e" ,b , "sera de:", soma)
# %%
# o inout sempre lera um dado recebido por um usuario em formato de string!!!! SEMPRE SEMPRE SEMPRE SEMPRE. Para resolver esse problema basta fazer a conversão de tipo de dado
