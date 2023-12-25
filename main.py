'''
Desafio 8 - Acessando e modificando Lista

Para este desafio, vamos começar ultilizando a lista "Frutas" do desafio
anterior.

Modificações:
- Teremos que encontrar o index de "banana" e alterar para "morango".
- Adicionar no final da lista o "abacaxi".

Ao final deveremos imprimir o a lista "frutas".

'''

#Lista

frutas = ['maça', 'banana', 'manga','uva']

#Acessando para encontrar o index banana.
posicao = frutas.index('banana')
frutas[posicao] = 'morango'

#Adicionando o item "Abacaxi"
frutas.append('abacaxi')


#saida
print(frutas)
