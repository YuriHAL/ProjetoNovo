import random
lista = ['r' ,'p', 's'] 

def sorteio():
          logica()
maquina = random.choice(lista)
jogador = input('digite sua opcao: ') 
print("sua opcao eh ",jogador.lower()) #trasnforma letra maiuscula para minuscula porem nao entra no if
def logica():
    if (maquina == 'r'):
        if jogador == 'r':
            print("Empate entra jogador e a maquina")
        elif jogador == 'p':
            print("Papel embola pedra\\ Jogador VENCEU")
        elif jogador == 's':
            print('Pedra quebra tesoura\\ Computador Venceu')    
    elif maquina== 'p':
        if jogador == 'p':
            print("Empate entra jogador e a maquina")
        elif jogador == 'r':
            print("papel embola pedra\\ COMPUTADOR VENCEU")
        elif jogador == 's':
            print('Tesoura corta papel\\ Jogador Venceu')  
    elif maquina == 's':
        if jogador == 'p':
            print("Eetsoura corta papel\\Computador venceu")
        elif jogador == 'r':
            print('pedra quebra tesoura\\JOGADOR VENCEU')
        elif jogador == 's':
            print('Empate') 

def  main(): #funcao e mostra os resultados
        print("Jogo do Pedra,Papel,tesoura")
        print('r= Pedra')
        print("p= Papel")
        print("s= Tesoura") 
        logica()
print('O elemento sorteado foi:', maquina)

 