# PARA O TERMINAL:
# Dois parâmetros:
# 1 - Nome do arquivo; 2- Modo que iremos trabalhar o arquivo -> "w" para escrita sobrescrevendo (caso exista)
# "r" para leitura e "a" para adicionar

arquivo = open("palavras.txt", "w")

arquivo.write("banana")
arquivo.write("melancia")

arquivo.close()

print(arquivo)
