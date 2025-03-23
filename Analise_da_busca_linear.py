import random


testes = [497624, 282062, 689410, 554834, 698783, 366777, 149528, 400180, 11388, 392959, 505979, 287361, 674663, 849712, 482574]


def GeradorDados(tamanho, limite, seed):
    dados = []
    random.seed(seed)
    for i in range(tamanho):
        dados.append(random.randint(1, limite))

    return dados

N   = 1000000    # Quantidade de números no vetor
LIM = 1000000   # Limite para geração do número aleatório
S   = 2         # Seed: para manter sempre uma mesma sequência




dados = GeradorDados(N, LIM, S)
dadosTestes = GeradorDados(1000, LIM, S)
print("\n\n\n")

print(" Tamanho da lista: " + str(len(dados)))
print(" Lista: ")
print(dados[0:20])
print("\n\n\n")


def PesquisaLinear1(lista, chave):

  achou   = False
  pos     = -1
  tam     = len(lista)
  i       = 0
  while (i < tam ) and (not(achou)):
      if (lista[i] == chave):
        achou = True
        pos = i
      i+=1

  resultado = [chave, achou, pos, 0, 0]

  return resultado


print("\n\n\n")

print("valor dos testes pesquisa linear 1")

for i in range(0, len(testes)):
    posicao = testes[i]
    chave = dados[posicao]
    print(" Valor e posição: " + str(chave) + " - " + str(posicao))
    result  = PesquisaLinear1(dados, chave)
    print("\033[32m" + str(result) + "\033[m")  





import time

# instrs é uma variável que vai contar quantas "instruções"
# t é uma variável que vai recuperar o tempo de execução
def PesquisaLinear2(lista, chave):

  instrs = 4            # Cada instrução neste bloco de abaixo
  t      = time.time()  # recuperando instante atual

  achou = False
  pos = -1
  tam = len(lista)
  i = 0

  while (i < tam ) and (not(achou)):
      if (lista[i] == chave):
        achou = True
        pos = i
        instrs+=2      # 2 instruções acima
      i+=1
      instrs+=4        # While, IF e increm i

  t = time.time() - t      # diferença em relação ao instante
  resultado = [chave, achou, pos, t, instrs]

  return resultado


print("\n\n\n")

print("valor dos testes pesquisa linear 2")

for i in range(0, len(testes)): #fazendo o gráfico de acordo com os números de cada grupo
    posicao = testes[i]
    chave = dados[posicao]
    print(" Valor e posição: " + str(chave) + " - " + str(posicao))
    result  = PesquisaLinear2(dados, chave)
    print("\033[32m" + str(result) + "\033[m")  

print("\n\n\n")
print("Testando chave que não existe")	
chave = -1 # chave que não existe
result = PesquisaLinear2(dadosTestes, chave)
print(result)
print("\n\n\n")

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Gerando resultados para análise
lstresults = []
for posicao in range(0, len(testes)):  # Amostragem de posições
    chave = dados[testes[posicao]]
    result = PesquisaLinear2(dados, chave)
    lstresults.append(result)

# Criando um DataFrame para análise
df = pd.DataFrame(lstresults, columns=['Chave', 'Existe', 'Posicao', 'Tempo', 'Instrucoes'])

# Criando o ambiente dos gráficos
sns.set_style("white")
fig, axes = plt.subplots(2, 1, figsize=(10, 12))  # Criando 2 subgráficos (2 linhas, 1 coluna)

# Gráfico superior: Número de Instruções vs. Posição da Chave
sns.lineplot(ax=axes[0], data=df, x="Posicao", y="Instrucoes",
             color="red", marker="*", markersize=10)
axes[0].set_title('Número de Instruções vs. Posição da Chave')
axes[0].set_xlabel('Posição da Chave\n')
axes[0].set_ylabel('Número de Instruções')


# Gráfico inferior: Tempo de Execução vs. Posição da Chave
sns.lineplot(ax=axes[1], data=df, x="Posicao", y="Tempo",
             color="blue", marker="o", markersize=8)
axes[1].set_title('Tempo de Execução vs. Posição da Chave')
axes[1].set_xlabel('Posição da Chave\n')
axes[1].set_ylabel('Tempo de Execução (s)')

# Ajustando layout para melhor visualização
plt.tight_layout()
plt.show()




# Conclusão Baseada nos Experimentos:
# Para um vetor de 1000 números desorganizados, qual o esforço para "encontrar" (perceber que ela não existe) uma chave que não está no vetor?
# No pior caso, onde o vetor não estar organizado, tornando impossível criar um algoritmo de parada para a busca linear, o esforço será de 1000 verificações (o(n)) 4004 instruções.


# Qual o melhor caso, situação em que haveria o menor número de instruções? Onde ele estaria no gráfico?
# O melhor caso ocorre quando a chave está na primeira posição, exigindo apenas 8 instruções. No gráfico, isso estaria no ponto mais baixo a esqueda, próximo da origem.


# E qual o pior caso e onde estaria no gráfico?
# O pior caso ocorre quando a chave está na última posição ou não existe. Isso levaria ao maior número de instruções, e no gráfico apareceria como o ponto mais alto a direita, oposto ao melhor caso.


# Qual o formato (grau) da função de complexidade do algoritmo? Quais parâmetros no gráfico caracterizam essa função?
# A função de complexidade é linear, O(n). Isso significa que o número de instruções cresce proporcionalmente ao tamanho da lista. No gráfico, essa relação é representada por uma reta crescente.


# valor dos testes pesquisa linear 2

# chave  | achou | pos | tempo | instruções
# -------------------------------------------
# [731821, True, 497624, 0.03370809555053711, 1990506]
# [806405, True, 26664, 0.002403736114501953, 106666]
# [140007, True, 458088, 0.029071569442749023, 1832362]
# [597361, True, 504037, 0.033954620361328125, 2016158]
# [759676, True, 102106, 0.008008003234863281, 408434]
# [173878, True, 366777, 0.024781227111816406, 1467118]
# [248386, True, 149528, 0.010831594467163086, 598122]
# [104662, True, 285557, 0.017258167266845703, 1142238]
# [656223, True, 11388, 0.0008547306060791016, 45562]
# [218850, True, 392959, 0.025435209274291992, 1571846]
# [837538, True, 505979, 0.033501386642456055, 2023926]
# [942437, True, 88801, 0.005477190017700195, 355214]
# [357223, True, 183631, 0.012547731399536133, 734534]
# [645388, True, 849712, 0.05525994300842285, 3398858]
# [83138, True, 482574, 0.030319929122924805, 1930306]