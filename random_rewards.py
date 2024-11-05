import random
import os
from colorama import Fore

my_list_rewards = ['Respirar','Jogar','Assistir  algo', 'Assistir  youtube', 'Journal','Ioga','Ligar  para alguem', 'Escutar  musica alta']
my_list_wake_up = ['Assistir algo',
  'Jogar',
  'Pegar no meu telefone',
  'Ler']
clear = lambda: os.system('clear')

while True:
    answer = input('Qual tipo de recompensa?\n 1- De manha \n 2- Recompensas\n 0- Sair\n')
    print('resposta', answer, '\n')
    if answer == '1':
        clear()
        print(Fore.BLUE + random.choice(my_list_wake_up));
        print(Fore.RESET)
    elif answer == '2':
        clear()
        print(Fore.GREEN + random.choice(my_list_rewards));
        print(Fore.RESET)
    elif answer == '0':
        clear()
        print(Fore.CYAN + 'Bye!');
        print(Fore.RESET)
        break
    else:
        clear()
        print(Fore.RED + 'Resposta invalida, por favor comece de novo\n')
        print(Fore.RESET)
