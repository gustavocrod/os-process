# -*- coding: utf-8 -*-
class Scheduler:
    """ Classe para o escalonador de processos."""

    def __init__(self, processes):
        """ Description
        Método construtor da classe Scheduler

        :param processos: lista com os dados de todos os processos
        """
        self.processes = processes  # lista de processos
        self.clock = 0  # representacao do tempo no algoritmo
        self.idle_time = 0  # tempo ocioso do processador, caso não haja processos executando ou na fila de espera

        for process in self.processes:
            process.init_process()

    def show_results(self, name):
        print()
        print("=======================================================================================")
        print(name)
        for p in self.processes:
            p.show_process()
        print("=======================================================================================")
        print()

    def first_come_first_served(self):
        """ Description
            Método que simula o algoritmo de escalonamento First Come First Served - FIFO
        """

        # coleta os proecessos que chegaram na CPU no tempo zero
        waiting_queue = [process for process in self.processes if process.arrival_time == 0]
        finished_queue = []

        while len(finished_queue) < len(self.processes):
            # enquanto a fila de terminados é menor que a de todos processos

            while len(waiting_queue) == 0:  # caso a fila de espera esteja vazia
                '''mostra os simbolos correspondentes para cada processo, caso um processo
                saia de bloqueado, vai para a fila de espera'''

                self.verify_process(waiting_queue)

                self.clock += 1

                # coleta os processos que chegaram na CPU naquele clock
                waiting_queue += [process for process in self.processes if process.arrival_time == self.clock]

            process = waiting_queue.pop(0)  # pega o primeiro para executar (o que chegou primeiro)

            if process.elapsed_time == 0:
                process.start_time = self.clock  # define o tempo que o processo começou a executar

            while not process.is_finished:
                # permanece executando o processo até finalizar

                # avança um ciclo de execucao
                process.execute()

                ''' adiciona o simbolo correspondente para cada processo
                 se um processo saia do bloqueio ele volta para a fila de espera (pronto)'''
                self.verify_process(waiting_queue, process)

                self.clock += 1  # incrementa o tempo

                # pega os processos que chegaram a CPU no clock atual
                waiting_queue += [process for process in self.processes if process.arrival_time == self.clock]

            if process.is_finished:
                process.end_time = self.clock    # seta o tempo que o processo terminou a sua execução
                finished_queue.append(process)  # poe na fila de processos terminados

        self.show_results("First Come, First Served --> FCFS")

        return

    def shortest_job_first(self):
        """ Description
            Método que simula o algoritmo de escalonamento SJF
            é preciso ordenar a fila de espera para que o processo com menor de ciclo de CPU possa executar previamente

        """

        # processos que chegaram no tempo 0
        waiting_queue = [process for process in self.processes if process.arrival_time == 0]
        finished_queue = []

        while len(finished_queue) < len(self.processes):
            # enquanto nao executou todos os processos

            while len(waiting_queue) == 0:
                self.verify_process(waiting_queue)
                self.clock += 1
                # pega os processos que chegaram naquel clock
                waiting_queue += [process for process in self.processes if process.arrival_time == self.clock]

            # ordena pelo tamanho
            waiting_queue.sort(key=lambda x: x.size)

            process = waiting_queue.pop(0)  # pega o primeiro pra executar
            if process.elapsed_time == 0:  # se o tempo decorrido for zero, significa que começou ali
                process.start_time = self.clock

            while not process.is_finished:
                # permanece executando o processo até finalizar
                process.execute()

                self.verify_process(waiting_queue, process)

                self.clock += 1  # incrementa o tempo

                # pega os processos que chegaram naquele tempo na cpu
                waiting_queue += [process for process in self.processes if process.arrival_time == self.clock]

            if process.is_finished:
                process.end_time = self.clock
                finished_queue.append(process)

        self.show_results("Shortest Job First --> SJF")
        return

    def round_robin(self, quantum):
        """Description
            Método que simula o algoritmo de escalonamento Round Robin

            O processo para de executar quando o executa pela quantidade de quantum definida,
            assim da espaço para que outro processo possa executar

        :param quantum: Tempo máximo que um processo pode executar em sequência

        """
        waiting_queue = [process for process in self.processes if process.arrival_time == 0]
        finished_queue = []

        if quantum > 0:

            while len(finished_queue) < len(self.processes):

                while len(waiting_queue) == 0:
                    self.clock += 1
                    self.verify_process(waiting_queue)
                    waiting_queue += [process for process in self.processes if process.arrival_time == self.clock]

                process = waiting_queue.pop(0)
                process.execution_time = 0  # deixando o tempo em 0 inicial
                if process.elapsed_time == 0:
                    process.start_time = self.clock

                ## enquanto nao finalizou
                while not process.is_finished:

                    # caso atingiu o tempo maximo em execucao - quantum
                    if process.execution_time == quantum:
                        process.execution_time = 0  # reseta o tempo em execucao
                        waiting_queue.append(process)
                        break

                    process.execute()

                    self.clock += 1
                    self.verify_process(waiting_queue, process)
                    waiting_queue += [process for process in self.processes if process.arrival_time == self.clock]

                if process.is_finished:
                    process.end_time = self.clock
                    finished_queue.append(process)

            self.show_results("Round Robin --> RR")

        return

    def priority(self):
        """ Description
        Método que simula o algoritmo de escalonamento de Prioridade

        Os processos não mais executam mais que um ciclo por vez, assim a verificação de prioridade é feita a
        cada ciclo de clock

        A fila de espera é ordenado com base na prioridade dos processos.
        """

        waiting_queue = [process for process in self.processes if process.arrival_time == 0]
        finished_queue = []

        while len(finished_queue) < len(self.processes):

            while len(waiting_queue) == 0:
                # enquanto nao chegou ninguem como pronto
                self.verify_process(waiting_queue)
                self.clock += 1
                # fica pegando os processos até um ficar pronto
                waiting_queue += [process for process in self.processes if process.arrival_time == self.clock]

            # ordena pela prioridade :: quanto maior = mais prioridade
            waiting_queue.sort(key=lambda x: x.priority * -1)

            process = waiting_queue.pop(0)  # pega o de maior prioridade
            if process.elapsed_time == 0:  # se ele ainda nao havia começado, entao esse e o start time
                process.start_time = self.clock

            # executa o processo
            process.execute()

            self.verify_process(waiting_queue, process)
            self.clock += 1  # avanca no tempo

            # adiciona alguem que chegou a mais naquele clock
            waiting_queue += [process for process in self.processes if process.arrival_time == self.clock]

            # se o processo atual terminou
            if process.is_finished:
                process.end_time = self.clock
                finished_queue.append(process)
            else:
                waiting_queue.insert(0, process)

        self.show_results("Prioridade --> P")
        return

    def verify_process(self, waiting_queue, process=None):
        """ Description
        Método que percorre os processos do escalonador verificando se é o processo que está em execução ou não.
        Se for o processo em execução, o "buffer" do vetor é marcado com um 'x'
        Caso contrário será marcado com o respectivo estado do processo. Símbolos que representam os estados dos processos:
        Processo em espera: '_'
        Processo terminado: 'V'


        :param waiting_queue: Fila de processos em espera
        :param processo: Processo em execução no momento da chamada da função

        :rtype: None
        """
        for proc in self.processes:  # percorre toda a lista de processos existentes
            if proc != process:  # caso não seja o processo que esteja executando no momento
                # insere o simbolo correspondente ao estado do processo
                if proc.is_finished:
                    proc.append('.')  # terminado
                elif proc in waiting_queue:
                    proc.append('_')  ## em espera (pronto)
                else:
                    proc.append(' ')  # caso não esteja esperando/bloqueado/executando
            else:
                proc.append('x')  # simbolo referente a uma execução do processo