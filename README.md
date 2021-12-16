# FacialAnalysis-468Landmarks

Este é um novo repositório para aplicar as tecnicas de analise usadas anteriormente pelo Tobias, contudo, desta vez utilizando o novo modelo facil da MediPipe com 468 landmarks.

# Lista de emoções

- 0: Neutra
- 1: Raiva
- 2: Desprezo (Contempt)
- 3: Nojo
- 4: Medo
- 5: Alegria
- 6: Tristeza
- 7: Surpresa

## Questionários Psiquiatricos

- **dbi_score** : Beck Depression Inventory
- **bai_score** : Beck Anxiety Inventory
- **asrsa_score** : Adult Self-Report Scale (Defict de Atenção)
- **asrsb_score** : Adult Self-Report Scale (Hiperatividade)
- **oci_score** : Obsessive-Compulsive Inventory
- **sqr_score** : ?

# Correlação com os músculos da face

Na pasta [`MuscleCorrelation`](https://github.com/MIGMA-Team/FacialAnalysis-468Landmarks/blob/main/MuscleCorrelation) estão os algoritimos utilizados para identificar os musculos da face e relacioná-los com os pontos fornecidos pelo modelo.

# Experimentos

## Experimento 1 - Analisar os rostos com o mediapipe e salvar os dados das posições dos Landmarks

O objetivo é coletar os dados para que possam ser analisados e correlacionados posteriormente. O experimento esta descrito na pasta [`01-face_points_exp`](https://github.com/MIGMA-Team/FacialAnalysis-468Landmarks/tree/main/01-face_points_exp)

## Experimento 2 - Processamento dos dados obtidos no Exp1

O objetivo é calcular a distancia entre cada ponto para cada ponto na expressão neutra não supervisionada e salvar essas proporções em um csv. O experimento esta descrito na pasta [`02-pattern_analysis`](https://github.com/MIGMA-Team/FacialAnalysis-468Landmarks/tree/main/02-pattern_analysis_exp)

## Experimento 3 - Criação dos gráficos de pseudo-cluster e clusterization

O obejtivo é renderizar gráficos bidimensionais para avaliar gráficamente a correlação entre as distâncias, e diferenças de distancias, com os resultados dos questionários psiquiatricos.
Os gráficos serão dividos em n partes

- Gráficos da parte 1: Todos para todos da Face inteira
- Gráficos da parte 2: Todos para todos do agrupamento por músculo
- Gráficos da parte 3: Todos para todos do agrupamento por grupo muscular
- Gráficos da parte 4: Todos para todos, por músculo, do agrupamento por músculo
- Gráficos da parte 5: Todos para todos, por grupo múscular, do agrupamento por grupo muscular
  > talves plotar de distancia para distancia, em vez de Score X Distância, de algum resultado positivo (se der o quote do exp 4 pode ser feito tb)
  > Como eu identifico se algo está bem clusterizado?

## Experimento 4 - Calculo de correlações

O experimento 3 foi útil para diminuir os candidatos à esta analise, pois caso contrário, o número de calculos de correlação feitos aqui seria astronômico. As correlações seão feitas com os dados nos quais foi possivel observar algum padrão de agrupamento nos gráficos da Experimento 3.

Para as correlações, primeiro será analisado o tipo de distribuição de cada variavel e então, feito os cálculos classicos de correlação, considerando o X cada um dos resultados do questionário e o Y cada uma das distâncias (Já deu para entender o por que de ser necessário a redução do conjunto de análise)

> Também pensei em fazer de Y para Y, mas ai eu já não sei se vale a pena

## Experimento 5 - Testes de hipóteses

### Hipótese 1 - pessoa com score mais alto em depressão tende a ter uma media maior das distancias da face neutra pra neutra media dos participantes

### Hipótese 2 -

# Dados

Os dados serão salvos na pasta processed. Um resumo de seu conteudo é o que segue

```

.
├── database
|   |
|   ├── db.sqlite (Banco de dados com todos os dados processados e agregados)
|
├── /processed
|   |
|   ├── [id_expressão]
|   |   |
|   |   ├── mean_[id_expressão].png
|   |   ├── [id_supervisionado]
|   |   |   ├── [id_pessoa]
|   |   |   |   |
|   |   |   |   ├── [id_foto].csv
|   |   |   |   ├── [id_foto].jpg
|   |   |   |   ├── mean_[id_pessoa].jpg
|   |
│   ├── /pattern_analysis
│   |   |
│   |   ├── /[id_pessoa]
│   |   |   |
│   |   |   ├── exp-tp_00-00.csv
│   |   |   ├── mean-dists_allp-allp.csv
│   |   |   ├── mean-diff-dists_allp-allp.csv
```
