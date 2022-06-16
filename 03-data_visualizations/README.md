# Experimento 3 - Visualização dos dados

## Gráficos de pseudo-cluster

    Os dados gerados na primeira abordagem do experimento 2 foram plotados em relação às respostas dos questionários. Não foi possível extrair nenhuma informação desta analise

## Analise da distribuição das distancias da segunda abordagem

Para cada tipo de expressão foi gerado um histograma das médias de cada usuário, para analisar a distribuição dos dados. Todos caem em uma distribuição normal

## Cluster K-Means

Como foram selecionados 77 pontos, houve uma sobrecarga de dados para fazer a analise. Então foi utilizada esta técnica de clusterização para reduzir a quantidade de dados.
Os 77 pontos foram dividos em 6 grupos, mostrados na imagem abaixo
![image](https://user-images.githubusercontent.com/42501669/167314346-cbb2a811-d579-4a31-a8af-918f1d3f09b8.png)
A relação ponto-grupo esta salvo no arquivo `points_above_average.csv`
Para a execução dos testes na secção 04 será utilizada a média de cada de distância de cada ponto

### Expansão dos grupos
Dois novos grupos serão adicionados para analise arbitrariamente para ser feita uma visualização da relação do tamanho do sorriso com a contração dos olhos, para verificar se o sorriso é, de fato verdadeiro. Esta nova relação de grupos está no arquivo `points_above_average_expanded.csv`

## Remoções do Dataset

- 02935: Não respondeu aos questionários
