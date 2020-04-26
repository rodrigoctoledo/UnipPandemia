'''
Rodrigo de Camargo Toledo D26EB3-6 CCP13 
Algoritmo Pandemia
Desenvolvedor: Rodrigo Toledo
Baseado no Enunciado do Professor Dirceu,
As Vezes é necessario interagir com o programa, apertando Enter para obter resultados ou inserindo informações

Após apertar, o enter, pode demorar um pouco, pois coloquei o elemento temporal

Durante o codigo Tem os meus Codigos e referencias as questoes do Professor e com as questões as respostas
'''
import random
from random import randint
import os
import time
print("Bem Vindo ao Fim do Mundo de Pandemia")
doenca = input('Entre com o nome da Doença: ')
#Referencia da Probalidade: https://www.the-hospitalist.org/hospitalist/article/218769/coronavirus-updates/covid-19-update-transmission-5-or-less-among-close
probalidade = int(randint(1,5))

# Parte do Codigo para Limpeza de Tela, mas como funciona apenas no CMD do Windows, Resolvi deixar comentado
'''  matriz[l][c] = int(randint(0,200))



textoNaTela = "\ncomo limpar a tela do terminal cmd"

print(10 * textoNaTela)
print("\nLimparei a tela em 5 segundos!")


os.system("cls")

'''
'''
a) Implemente um software que contenha uma área (uma matriz quadrada, escolha o tamanho),
que pode ser ocupada por pontos (escolha a quantidade),
chamado de elementos (pessoas)
'''
elementos = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
elementos1 = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
elementos2 = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]


for l in range(0,3):
    for c in range(0,6):
        elementos[l][c] = 'Saudavel'
        elementos1[l][c] = 'Saudavel'
        elementos2[l][c] = 'Saudavel'
print('-='*30)


for l in range(0,3):
    for c in range(0,6):
        if l == 0 and c == 0:

            elementos[l][c] ='Contaminado'
            '''A.1) Cada pessoa se movimentará dentro desta área'''
            print('Essa é o Esquema simples que representa o primeiro contaminado')
            for l in range(0, 3):
             #   l1 += 1
            #    print("L1:"+str(l1))
                for c in range(0, 6):
                 #   l2 += 1
                 #   print("L2:" + str(l2))

                    print(f'[{elementos[l][c]:^5}]', end='')
                print()



            input("Pressione ENTER para continuar:")

'''A.2) A cada ciclo (unidade temporal), cada pessoa se movimentará dentro desta área.'''

print('-='*60)
contflag = 0
contpassa =0
conttempo1 =0
flag = False
# A.3) Em uma velocidade aleatória
while(contflag < 17):

    time.sleep(randint(1, 1))
    conttempo1 += 1

    for l in range(0,3):
        for c in range(0,6):



            if elementos[l][c] =='Saudavel':

                # ao entrar em contato com outros elementos.
                # Ao final de cada ciclo, se uma pessoa estiver próxima de outra pessoa,
                # ela pode transmitir a doença para os elementos que estão em volta de si
                # (considere o posicionamento dentro da matriz, mais a probabilidade de transmissão da doença para este cálculo).
                #No caso, utilizei um Random, para possibilidade, e a Matriz se a pessoa está saudavel, no if acima
               prabalidade = randint(0, probalidade)
              # print(prabalidade)
               contpassa += 1


               if prabalidade <=30:

                   contflag += 1
                   #print("ContFlag:"+str(contflag))


                   elementos[l][c] ='Contaminado'


for l in range(0, 3):
             #   l1 += 1
            #    print("L1:"+str(l1))
                for c in range(0, 6):
                 #   l2 += 1
                 #   print("L2:" + str(l2))

                    print(f'[{elementos[l][c]:^5}]', end='')
                print()
#b) Calcule quantos ciclos são necessários para se contaminar todos os elementos do grupo.
print("Quantidade de ciclos para infectar todos:" + str(contpassa))
print("Tempo de passagem: "+str(conttempo1)+" Segundos")
input("Pressione ENTER para continuar:")

#c) Qual é a influencia da quantidade de pessoas que estão circulando pelas ruas,
# na velocidade de contaminação das pessoas?
# R: Quanto Mais pessoas nas Ruas, menos tempo ou ciclos acontece a infeccção de todos

#Não consegui achar um numero para probalidade
# https://saude.abril.com.br/medicina/coronavirus-novos-dados-sobre-grupos-de-risco/
# Peguei desse Site a Idade, para estipular o grupo de Risco
#https://g1.globo.com/ciencia-e-saude/noticia/2019/09/16/estudo-confirma-recorde-de-longevidade-da-francesa-jeanne-calment-que-morreu-aos-122-anos.ghtml
print('-='*60)
contflag = 0
contpassa =0
i =int(0)
flag = False
conttempo2 =0

# C.1) e calcule, quanto isso influencia na velocidade de contaminação dos elementos.
while(contflag <= 17):
    time.sleep(randint(1, 1))
    conttempo2 += 1

    idade = int(randint(0, 122))
    i+=1
    # C.1) Faça exercícios de limitando a movimentação dos elementos na matriz,
    # Pessoas Com mais de 60 ou com alguma outra doença que entre no grupo, representado, por resto da divisão 1, não se movimentam
    if idade >=60 and idade % 2 == 0:
        print("Pessoa no Grupo de Risco, não pode sair")

    else:
        for l in range(0,3):
            for c in range(0,6):


              if elementos1[l][c] =='Saudavel':

                 # ao entrar em contato com outros elementos.
                 # Ao final de cada ciclo, se uma pessoa estiver próxima de outra pessoa,
                 # ela pode transmitir a doença para os elementos que estão em volta de si
                 # (considere o posicionamento dentro da matriz, mais a probabilidade de transmissão da doença para este cálculo).
                 #No caso, utilizei um Random, para possibilidade, e a Matriz se a pessoa está saudavel, no if acima
                 prabalidade = randint(0, probalidade)
                 # print(prabalidade)
                 contpassa += 1

                 if prabalidade <=30:

                    contflag += 1
                   # print("ContFlag:"+str(contflag))


                    elementos1[l][c] ='Contaminado'


for l in range(0, 3):
             #   l1 += 1
            #    print("L1:"+str(l1))
                for c in range(0, 6):
                 #   l2 += 1
                 #   print("L2:" + str(l2))

                    print(f'[{elementos1[l][c]:^5}]', end='')
                print()

print("Quantidade de ciclos para infectar todos:" + str(contpassa))
print("Tempo de passagem: "+str(conttempo2)+" Segundos")
#C.3) Qual é a diferença entre o tempo que demora para contaminar todos os elementos no b, e com a limitação da movimentação.
print("Dirença de Tempo para o ciclo com e sem limitação: "+str(conttempo1-conttempo2)+" Segundos")
input("Pressione ENTER para continuar:")

#d) No protocolo de epidemia, estudado em classe, nem todos os elementos do sistema podem receber as informações mais atualizadas, isto acontece neste caso? Demonstre.
#Vou mandar Via Email
#e) Adicione o componente temporal,



print('-='*60)
contflag = 0
contpassa =0
mortes=0
curados=0


while(contflag <= 17):
    time.sleep(randint(1, 1))
    conttempo2 += 1

    for l in range(0,3):
            for c in range(0,6):


              if elementos2[l][c] =='Saudavel':

                 # ao entrar em contato com outros elementos.
                 # Ao final de cada ciclo, se uma pessoa estiver próxima de outra pessoa,
                 # ela pode transmitir a doença para os elementos que estão em volta de si
                 # (considere o posicionamento dentro da matriz, mais a probabilidade de transmissão da doença para este cálculo).
                 #No caso, utilizei um Random, para possibilidade, e a Matriz se a pessoa está saudavel, no if acima
                 prabalidade = randint(0, probalidade)
                 # print(prabalidade)
                 contpassa += 1

                 if prabalidade <=30:

                    contflag += 1
                   # print("ContFlag:"+str(contflag))


                    elementos2[l][c] ='Contaminado'
                   # As Mortes São bem Variaveis, segundo esse site:
                    #Coloque de 1 a 30% possibilidade
                    #https://www.abrasco.org.br/site/outras-noticias/saude-da-populacao/estimativas-do-impacto-da-covid-19-na-mortalidade-no-brasil/46151/

                    Morte = int(randint(1, 100))
                    Vivos = int(randint(1, 100))
                         #E.1) e comece a considerar que as pessoas se curam, depois de algum tempo,
                    if  Vivos >=90:
                        elementos2[l][c] = 'Saudavel'
                    # E.2)e que algumas morrem. O que muda neste cenário?
                    # Quantos ciclos demora pras pessoas serem contaminadas,
                    if Morte <= 30:
                        elementos2[l][c] = 'Morto'
                        mortes +=1






for l in range(0, 3):
             #   l1 += 1
            #    print("L1:"+str(l1))
                for c in range(0, 6):
                 #   l2 += 1
                 #   print("L2:" + str(l2))

                    print(f'[{elementos2[l][c]:^5}]', end='')
                print()

print("Quantidade de ciclos para infectar todos:" + str(contpassa))

#E.3) quantas pessoas morrem?
print("Quantidade de Mortos:" + str(mortes))
print(doenca+" Ferrou o Mundo :( ")

#f) Como comparar o espalhamento de um vírus, com a consistência de um banco de dados?
#R: Em questão de Replicação de Dados ou Pessoas contamidas que replicam os virus para outros pelo contato, a Consistência eventual, 
#como apresenta alguns problemas de Replicação, assosio com as pessoas evitando contando e assim quebrando a replica do Virus

#e) Como você compara cada indivíduo deste exercício, com processos e threads em um sistema distribuído?
#R: Um Local fechado, seria o processador, e as pessoas são Theads e processos, o virus é o Recurso, se as Theads(Pessoas)
#no Processador(Local), pararem de compartilhar recursos(Virus), vai ocorrer o Deadlock e as pessoas vão parar de compartilhar o virus
#
