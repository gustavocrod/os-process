# :closed_book: PROCESSOS


*Task: Implemente uma representação de processo (do ponto de vista do sistema operacional)*

- Crie uma estrutura de dados que represente o processo.
- Implemente um gerenciador de processos, que "simule" os possíveis estados de um processo.
- Implemente diferentes políticas de escalonamento de processos. Considere que para cada processo existem informações pertinentes associadas (Prioridades do processo 1 até 20 e mecanismos de incremento e decremento de prioridades).
Cada processo em execução pode ser interrompido por preempção ou por chamada de sistema (escolha isso aleatoriamente). Decremente a prioridade se o processo for interrompido por preempção e incremente a prioridade em caso contrário.

[Clicke aqui](https://github.com/gustavocrod/os-process/blob/main/src/README.md) para saber como executar.

## :arrow_forward: Definição de Processo
Um processo é caracterizado por um **programa em execução**.

*Nada mais do que um programa que é posto em execução.*

#### Diferença entre processo e programa?

Um processo é uma instância de um progrma e possui dados de entrada, dados de saída e um estado: **executando, bloqueado ou pronto**;

Um programa pode ter várias instâncias em execução (em diferentes processos), mas um processo é único.
O processo é a forma pela qual o SO vê um programa e possibilita sua execução.

Existem dois tipos de processos: 
#### 1. Processo em Primeiro Plano
Interage com o usuário. (Específico)

Ex.:
- ler um arquivo
- iniciar um browser

#### 2. Processo em Segundo Plano (background)
Processos com funções específicas que independem de usuários - _daemons_ (Genérico)

Ex.:
- Recepção e envio de email
- Serviços de impressão

## Componentes de um Processo
 - Conjunto de instruções
 - Espaço de endereçamento (espaço reservado para que o processo possa ler e escrever -- 0 até max [relativo])
 - Contexto de hardware (valores nos registradores, como PC, ponteiro de pilha e reg. de propósito geral)
 - Contexto de software (atributos em geral, como lista de arquivos abertos e variáveis)

#### Tabela de Processos
 - Também chamada de BCP (Bloco Controle de Processo)
 - Contém informações de contexto de cada processo (ex. ponteiros de arquivos abertos, posição do pŕoximo byte a ser lido em cada arquivo, etc.)
 - Contém informações necessárias para trazer o processo de volta, caso o SO tenha que tirá-lo de execução.
 - Contém estados de um processo em um determinado tempo

## Estados de um processo

![estados-processo](https://github.com/gustavocrod/os-process/blob/main/images/estados-processos.png)
 - em execução
 - à espera(para usar um recurso de um recurso usado por outro processo no momento)
 - pronto pra executar

## Características de Processo
Um processo pode ser I/O Bound e CPU Bound:
 - Um processo de I/O Bound utiliza majoritariamente de tarefas de entrada e saída.
 - Um processo CPU Bound utiliza majoritariamente de tarefas realizadas na Central única de Processamento.
---

## :twisted_rightwards_arrows: Escalonamento
O Escalonamento consiste na tarefa de organizar/escolher/agendar qual processo deverá ir para a CPU. 
Seu objetivo é definir a prioridade de execução, e, para além disso, garantir que a UCP não fique ociosa por algum tempo significativo.
Existem diferentes algoritmos

#### 1. objetivos gerais do escalonamento: 
* Justiça (processos devem ser tratados igualmente);
* Minimizar overhead: recursos não devem ser disperdiçados(embora algum investimento momentâneo em um processo permita maior eficiência);
* Balancear o uso de recursos;

O maior problema para a implementação de um algoritmo de escalonamento é a natureza imprevisível do comportamento de um processo: não se sabe se um processo x usará intensamente processador, entrada/saída, memória ou quaisquer outros recursos computacionais.

#### 2. Algoritmos de escalonamento implementados nesse trabalho:
Algoritmos de escalonamento podem ser **preemptivos** ou **não preemptivos**;

##### Algoritmos não preemptivos 

**não permitem troca de contexto**. Isto é, quando um processo entra em execução, ele será executado até o fim.

* First Come, Frist Served - FCFS (*FIFO*);
* Shortest job first - SJF (sem preempção)
  
    Menor processo primeiro, não preemptivo. Pode-se dizer que é um algoritmo guloso. Devido ao seu comportmento, é grande a probabilidade de *starvation*(postergação indefinida) para os processos maiores.
    **Originalmente é executado sem preempção, porém esta pode ser implementada**. (NÃO IMPLEMENTADO)

##### Algoritmos preemptivos:

Os algoritmos preemptivos salvam o contexto do processo a ser interrompido. Esse contexto é salvo nos registradores e na memória responsável pela execução do processo em questão. Isso permite a **troca de contexto** dos processos, trocando em miúdos: trocar um processo não terminado por outro que está para ser executado agora(devido ao algoritmo de escalonamento);

* Round-Robin:
   
  Este algoritmo atribui ao escalonador a definição de um **quantum (*timeslice*)** para cada processo. Após o encerramento da fatia, o processo sofre uma interrupção voluntária.
  Mantém-se uma lista circular de processos prontos(ready);
  
* Escalonamento por prioridade:
    
    Prioridades são decididas e atribuídas aos processos. Desempate entre processos de mesma prioridade pode ocorrer usando de outros algoritmos, como o FIFO. A atribuição das prioridades pode ser ascendente ou descedente.
    **Um processo de baixa prioridade está sujeito a *starvation***.
    **Para tratar disso, utiliza-se do conceitos de *aging*(envelhecimento) o qual consiste no aumento da prioridade em razão do tempo decorrido na espera** (NÃO IMPLEMENTADO)
    


  
