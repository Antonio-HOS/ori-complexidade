# Os resultados da execução acima devem ser copiados para esta lista
lstresults_binaria = [[731821, True, 731643, 0.0, 84],
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

lstresults_linear = [
[731821, True, 497624, 0.0, 1990506],
[806405, True, 26664, 0.0, 106666],
[140007, True, 458088, 0.0, 1832362],
[597361, True, 504037, 0.0, 2016158],
[759676, True, 102106, 0.0, 408434],
[173878, True, 366777, 0.0, 1467118],
[248386, True, 149528, 0.0, 598122],
[104662, True, 285557, 0.0, 1142238],
[656223, True, 11388, 0.0, 45562],
[218850, True, 392959, 0.0, 1571846],
[837538, True, 505979, 0.0, 2023926],
[942437, True, 88801, 0.0, 355214],
[357223, True, 183631, 0.0, 734534],
[645388, True, 849712, 0.0, 3398858],
[83138, True, 482574, 0.0, 1930306]]



# Questão: Verifique de o Pandas e o Dataframe são muito usados em ciência de dados?
#          Imagine como seria um gráfico (Tempo vs Posição da Chave) e (Número de Instruções vs Posição)
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# Analisando graficamente

# Gerando um Dataframe, isso ajudará na produção dos gráficos
# Veremos mais sobre Dataframes e Gráficos em próximos capítulos
df = pd.DataFrame(lstresults_binaria, columns =['Chave', 'Existe', 'Posicao', 'Tempo', 'Instrucoes'])
df2 = pd.DataFrame(lstresults_linear, columns =['Chave', 'Existe', 'Posicao', 'Tempo', 'Instrucoes'])

# Criando o ambiente do gráfico
sns.set_style("white")
plt.figure(figsize=(10, 6))

# Gráfico de Dispersão para busca binária
sns.lineplot(data=df, x="Posicao", y="Instrucoes",
             color="green", marker="*", markersize=10, label="Busca Binária")

# Gráfico de Dispersão para busca linear
sns.lineplot(data=df2, x="Posicao", y="Instrucoes",
             color="red", marker="*", markersize=10, label="Busca Linear")

# Adicionando título e legendas
plt.title('Comparação entre Busca Binária e Linear')
plt.xlabel('Posição da Chave')
plt.ylabel('Número de Instruções')
plt.legend()

plt.show()