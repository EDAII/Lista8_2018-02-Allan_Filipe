## Lista 8 - Grafos
### Geração de Grafos com Aplicação de Métricas

##### Alunos

| Matrícula | Nome | GitHub |
|--|--|--|
| 15/0029624 | Allan Jefrey Pereira Nobre | @AllanNobre |
| 15/0059213 | Filipe Coelho Hilário Barcelos | @FilipeKN4 |

##### Para executar
O ambiente deve ser configurado para a utilização do framework Django na versão 2.1. Após a configuração, deve-se executar o comando abaixo: 

```sh
$ python3 manage.py runserver
```

Após a execução abra o link do servidor em http://127.0.0.1:8000/.

##### Descrição

O programa irá executar um código de geração de grafos e aplicação de métricas de acoplamento entre nós de acordo com a leitura de um arquivo ".csv" que deve possuir em cada linha o nó de partida(primeiro elemento) e todos os nós com que ele se liga. O código é relacionado aos "Directed Graphs", que são grafos direcionados onde existem nós de partida que se ligam a outros nós de chegada.

##### Visualização

Para a visualização dos resultados foi utilizado o Framework Django da linguagem de programação Python, de modo que foi possível criar uma interface Web estilizada por meio do framework Bootstrap.  

##### Directed Graphs - Geração de Métricas

São indicados na tela o tempo de execução da geração do grafo, tempo de acesso aos nós, tempo de acesso as arestas e tempo de acesso aos graus, além de três tabelas para visualização. A primeira tabela se refere a quantidade de nós, a segunda se refere a quantidade de arestas e a última tabela mostra os graus de entrada, saída e total dos nós. 

##### Observações

Segue um ".csv" de exemplo de entrada para a geração de um grafo direcionado e aplicação das métricas de acoplamento de nós sugeridas.