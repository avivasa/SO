import os
import time

def filho():
    while(True):
        print("Sou o Filho: PID {}. Meu Pai é {} \n".format(os.getpid(),os.getppid()))
        time.sleep(1)

def pai():
    while(True):
        print("Sou o Pai: PID {}. Meu Pai é {}\n".format(os.getpid(),os.getppid()))
        time.sleep(5)

## início do programa
print("Executando o Processo Pai - PID: {} \n".format(os.getpid()))

## cria o processo filho
retorno = os.fork()

## a partir deste ponto teremos processos pai e filho rodando
## Temos então que definir qual código cada um irá rodar
## isso é feito através deste if obtido pela variável retorno
if retorno > 0:
    pai()

else:
    filho()
