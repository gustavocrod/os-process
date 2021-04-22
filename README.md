# PROCESSOS

*Task: Implemente uma representação de processo (do ponto de vista do sistema operacional)*

- Crie uma estrutura de dados que represente o processo.
- Implemente um gerenciador de processos, que "simule" os possíveis estados de um processo.
- Implemente diferentes políticas de escalonamento de processos. Considere que para cada processo existem informações pertinentes associadas (Prioridades do processo 1 até 20 e mecanismos de incremento e decremento de prioridades).
Cada processo em execução pode ser interrompido por preempção ou por chamada de sistema (escolha isso aleatoriamente). Decremente a prioridade se o processo for interrompido por preempção e incremente a prioridade em caso contrário.

## Definição de Processo
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
 - Espaço de endereçamento (espaço reservado para que o processo possa ler e escrever -- 0 até max)
 - Contexto de hardware (valores nos registradores, como PC, ponteiro de pilha e reg. de propósito geral)
 - Contexto de software (atributos em geral, como lista de arquivos abertos e variáveis)
