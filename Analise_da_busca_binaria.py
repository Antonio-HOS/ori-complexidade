import random

random.seed(0)
for i in range(5):
    print(random.randint(1, 1000000))

# Criando um vetor (lista) com
#     - N elementos (tamanho),
#     - dentro de uma faixa de valores (limite) e
#     - sempre com uma mesma sequência (seed)
# Questão: No Python existe o conceito de vetor? Como ele trata este recurso?
import random

def GeradorDados(tamanho, limite, seed):
    dados = []
    random.seed(seed)
    for i in range(tamanho):
        dados.append(random.randint(1, limite))

    return dados


# Gerando e manipulando os dados
N   = 1000000    # Quantidade de números no vetor
LIM = 1000000   # Limite para geração do número aleatório
S   = 2         # Seed: para manter sempre uma mesma sequência

dados = GeradorDados(N, LIM, S)

print(" Tamanho da lista: " + str(len(dados)))
print(" Lista: ")
print(dados[0:20])


dados_ord = sorted(dados)
print(dados_ord[1:100])


import time

def PesquisaBinaria(lista, chave):

  instrs = 4            # Cada instrução abaixo
  t      = time.time()  # recuperando instante atual

  esquerda, direita = 0, len(lista) - 1
  achou = False
  pos = -1  # Posição padrão caso não encontre

  while esquerda <= direita:
      instrs += 3  # Comparação e cálculo do meio
      meio = (esquerda + direita) // 2

      if lista[meio] == chave:
          instrs += 1
          achou = True
          pos = meio
          break  # Sai do loop pois encontrou a chave
      elif lista[meio] < chave:
          instrs += 1
          esquerda = meio + 1
      else:
          instrs += 1
          direita = meio - 1

  t = time.time() - t      # diferença em relação ao instante
  resultado = [chave, achou, pos, t, instrs]

  return resultado

# Testando a função de Pesquisa Binária
testes = [497624, 282062, 689410, 554834, 698783, 366777, 149528, 400180, 11388, 392959, 505979, 287361, 674663, 849712, 482574]
testes2 = [1000, 10000, 100000, 500000]
for i in range(0, len(testes)):
    posicao = testes[i]
    chave = dados[posicao]
    print(" Valor e posição: " + str(chave) + " - " + str(posicao))
    result  = PesquisaBinaria(dados_ord, chave)
    print("\033[32m" + str(result) + "\033[m")
    print("\n")


# Os resultados da execução acima devem ser copiados para esta lista
lstresults = [[731821, True, 731643, 0.0, 84],
[806405, True, 806307, 0.0, 80],
[140007, True, 139799, 0.0, 64],
[597361, True, 597127, 0.0, 72],
[759676, True, 759786, 0.0, 72],
[173878, True, 173866, 0.0, 80],
[248386, True, 247666, 0.0, 76],
[104662, True, 104447, 0.0, 76],
[656223, True, 656095, 0.0, 64],
[218850, True, 218393, 0.0, 76],
[837538, True, 837549, 0.0, 84],
[942437, True, 942582, 0.0, 76],
[357223, True, 356698, 0.0, 76],
[645388, True, 645157, 0.0, 84],
[83138, True, 83149, 0.0, 84]]

# Resultados das posições de teste 1000, 10000, 100000 e 500000
'''
lstresults = [[26152, True, 26093, 0.0, 76],
[662666, True, 662614, 0.0, 76],
[807285, True, 807155, 0.0, 80],
[53778, True, 53552, 0.0, 76]]
'''

# Questão: Verifique de o Pandas e o Dataframe são muito usados em ciência de dados?
#          Imagine como seria um gráfico (Tempo vs Posição da Chave) e (Número de Instruções vs Posição)
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Gerando o DataFrame a partir da lista de resultados
df = pd.DataFrame(lstresults, columns=['Chave', 'Existe', 'Posicao', 'Tempo', 'Instrucoes'])

# Configurações para melhorar a estética do gráfico
sns.set_style("white")
plt.figure(figsize=(12, 12))

# Gráfico Tempo vs Posição da Chave
plt.subplot(3, 1, 1)  # 3 linhas, 1 coluna, primeiro gráfico
graf_linha_tempo = sns.lineplot(data=df, x="Posicao", y="Tempo", color="blue", marker="o", markersize=5, label="Tempo de Execução")
plt.title("Tempo vs Posição da Chave")
plt.xlabel("Posição da Chave\n\n")
plt.ylabel("Tempo (segundos)")
plt.grid(True)

# Gráfico Número de Instruções vs Posição da Chave
plt.subplot(3, 1, 2)  # 3 linhas, 1 coluna, segundo gráfico
graf_linha_instrucoes = sns.lineplot(data=df, x="Posicao", y="Instrucoes", color="green", marker="*", markersize=8, label="Número de Instruções")
plt.title("Número de Instruções vs Posição da Chave")
plt.xlabel("Posição da Chave\n\n")
plt.ylabel("Número de Instruções")
plt.grid(True)

# Gráfico de Dispersão (Número de Instruções vs Chave)
plt.subplot(3, 1, 3)  # 3 linhas, 1 coluna, terceiro gráfico
graf_linha_disp = sns.scatterplot(data=df, x="Posicao", y="Instrucoes", color="red", marker="*", s=100, label="Instruções por Posição")
plt.title("Dispersão de Instruções")
plt.xlabel("Posição da Chave\n\n")
plt.ylabel("Número de Instruções")
plt.grid(True)

# Ajustando o layout para que os gráficos não se sobreponham
plt.tight_layout()

# Exibindo os gráficos
plt.show()


"""
CONCLUSÕES:
1 - Para concluir a atividade, acrescente a seguir os resultados (Istresults e gráfico) do laboratório de Busca Linear e deste laboratório de Busca Binária

Busca Binária: 

chave  | achou | pos | tempo | instruções
-------------------------------------------
[[731821, True, 731643, 0.0, 84],
[806405, True, 806307, 0.0, 80],
[140007, True, 139799, 0.0, 64],
[597361, True, 597127, 0.0, 72],
[759676, True, 759786, 0.0, 72],
[173878, True, 173866, 0.0, 80],
[248386, True, 247666, 0.0, 76],
[104662, True, 104447, 0.0, 76],
[656223, True, 656095, 0.0, 64],
[218850, True, 218393, 0.0, 76],
[837538, True, 837549, 0.0, 84],
[942437, True, 942582, 0.0, 76],
[357223, True, 356698, 0.0, 76],
[645388, True, 645157, 0.0, 84],
[83138, True, 83149, 0.0, 84]]

Busca Linear: 
chave  | achou | pos | tempo | instruções
-------------------------------------------
[731821, True, 497624, 0.03370809555053711, 1990506]
[806405, True, 26664, 0.002403736114501953, 106666]
[140007, True, 458088, 0.029071569442749023, 1832362]
[597361, True, 504037, 0.033954620361328125, 2016158]
[759676, True, 102106, 0.008008003234863281, 408434]
[173878, True, 366777, 0.024781227111816406, 1467118]
[248386, True, 149528, 0.010831594467163086, 598122]
[104662, True, 285557, 0.017258167266845703, 1142238]
[656223, True, 11388, 0.0008547306060791016, 45562]
[218850, True, 392959, 0.025435209274291992, 1571846]
[837538, True, 505979, 0.033501386642456055, 2023926]
[942437, True, 88801, 0.005477190017700195, 355214]
[357223, True, 183631, 0.012547731399536133, 734534]
[645388, True, 849712, 0.05525994300842285, 3398858]
[83138, True, 482574, 0.030319929122924805, 1930306]

Para melhores comparações, vá no arquivo Grafico_BinariaXLinear.py, lá mostra os gráficos comparativos entre os dois algoritmos.

2 - Para cada um dos valores de posição a seguir, leia no gráfico qual o número de instruções (esforço) para realizar a busca
o Poisições: 1000, 10000, 100000, 500000

Posição 1000: 76 instruções
Posição 10000: 76 instruções
Posição 100000: 80 instruções
Posição 500000: 76 instruções

chave  | achou | pos | tempo | instruções
-------------------------------------------
[26152, True, 26093, 0.0, 76],
[662666, True, 662614, 0.0, 76],
[807285, True, 807155, 0.0, 80],
[53778, True, 53552, 0.0, 76]

3 - Para cada busca, apresente qual o "formato" da função de complexidade
O formato da função de complexidade é logarítmica, pois o número de instruções cresce de forma logarítmica em relação ao tamanho da lista.
    T(n)=O(logn)
"""
