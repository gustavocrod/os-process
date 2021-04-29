# -*- coding: utf-8 -*-
class Process:
    def __init__(self, data):
        """ Description
        Método construtor da classe Process

        :type self: Process (class)
        :type data: dict
        :param data: Estrutura contendo todas as informações coletadas na main.py do arquivo.
        """
        self.pid = data['pid']    # id
        self.size = data['size']    # tamanho do processo
        self.priority = data['priority']    # prioritdade do processo (1-20)
        self.arrival_time = data['arrival_time']    # hora de chegada

        self.elapsed_time = None  # tempo executado
        self.start_time = None  # tempo de inicio
        self.end_time = None  # tempo do fim
        self.waiting_time = None  # tempo em espera
        self.is_finished = None
        self.execution_time = None  # tempo em execucao
        self.pico_index = None
        self.pretty_print = None

    def init_process(self):
        self.elapsed_time = 0  # tempo executado
        self.start_time = 0  # tempo de inicio
        self.end_time = 0  # tempo do fim
        self.waiting_time = 0  # tempo em espera
        self.is_finished = False
        self.execution_time = 0  # tempo em execucao
        self.pico_index = 0
        self.pretty_print = ''

    def append(self, data):
        self.pretty_print += data

    def execute(self):
        """ Description
        Método que faz a execução em si do processo, incrementando seu tempo executado e o tempo em execução.
        E faz a comparação do tempo executado com seu tamanho, quando a condição é verdadeiro o processo tem
        seu estado mudado para Finished.

        """
        self.elapsed_time += 1
        self.execution_time += 1

        if self.elapsed_time == self.size:
            self.is_finished = True

        return

    def show_process(self):
        """ Description
            Método que printa o id e as informações relativas dos estados dos respectivos processos.

        """
        print(f"Process[{self.pid}] | {self.pretty_print} | Total Size[{self.size}] | Priority[{self.priority}] "
              f"| Arrival time[{self.arrival_time}]")
        return
