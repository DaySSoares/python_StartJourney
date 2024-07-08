
# %%
#Regra das booleanas:
# ou = soma
# e = multiplicação

# operações com e
print(True * True) # = true
print(True * False) # = false
print(False * False) # = false
print(False * True) # = false
print(bool(1 * 1)) # = true
print(bool(1 * 0)) # = false
print(bool(0 * 0)) # = false
print(bool(0 * 1)) # = false

# operações com ou 
print(True * True) # = true
print(True + False) # = true
print(False + False) # = false
print(False + True) # = true
print(bool(1 * 1)) # = true
print(bool(1 + 0)) # = true
print(bool(0 + 0)) # = false
print(bool(0 + 1)) # = true
# %%
# Exercicio de tabela verdade:
idade = int(input("Insira sua idade: "))
cnh = input("Você já possui CNH? ")

if idade >= 18 and cnh == "sim":
    print("Prosseguir com cadastramento...")
elif idade >= 18 and cnh == "nao":
    print("É preciso ter cnh para prosseguir com o cadastro no site!")
else:
    print("Não é permitido o cadastro de menores de idade!")
# %%
