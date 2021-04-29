# -*- coding: utf-8 -*-
#!/usr/bin/env python3
from process import Process
from scheduler import Scheduler
from random import randrange


def make_processes(n=5):
    """
        Funcao para gerar processos para teste
    :param num: quantidade de processos
    :return:
    """
    dados = []
    for p in range(n):
        process = dict()
        process['pid'] = p + 1  # id do processo
        process['size'] = randrange(1, 15)  # tamanho
        process['priority'] = int(randrange(1, 20))  # prioridade
        process['arrival_time'] = int(randrange(0, 9))  # tempo de chegada
        dados.append(process)
    return dados


if __name__ == "__main__":
    quantum = 4
    dados = make_processes()

    # Printa os simbolos dos estados dos processos
    print(" ===>> LEGENDA  <<===")
    print("Processo em espera: _ ")
    print("Processo em execução: x")
    print("Processo terminado: .")

    processes = []
    for dado in dados:
        # criando os dados
        p = Process(dado)

        processes.append(Process(dado))

    # Chamada dos métodos dos algoritmos de escalonamento

    sche = Scheduler(processes)
    sche.first_come_first_served()

    sche = Scheduler(processes)
    sche.shortest_job_first()

    sche = Scheduler(processes)
    sche.round_robin(quantum)

    sche = Scheduler(processes)
    sche.priority()
