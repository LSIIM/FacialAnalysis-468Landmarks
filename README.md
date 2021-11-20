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
# Correlação com os músculos da face

Na pasta [`MuscleCorrelation`](https://github.com/MIGMA-Team/FacialAnalysis-468Landmarks/blob/main/MuscleCorrelation) estão os algoritimos utilizados para identificar os musculos da face e relacioná-los com os pontos fornecidos pelo modelo.

# Experimentos

## Experimento 1 - Analisar os rostos com o mediapipe e salvar os dados das posições dos Landmarks

O objetivo é coletar os dados para que possam ser analisados e correlacionados posteriormente. O experimento esta descrito na pasta [`01-face_points_exp`](https://github.com/MIGMA-Team/FacialAnalysis-468Landmarks/tree/main/01-face_points_exp)

## Experimento 2 - Analisar os dados obtidos no Exp1 para encontrar algum padrão

O objetivo é calcular a distancia de cada ponto para cada ponto da mascara de cada expressão e calcular a distancia entre cada ponto com sua contraparte na expressão neutra e salvar essas proporções em um csv. O experimento esta descrito na pasta [`02-pattern_analysis`](https://github.com/MIGMA-Team/FacialAnalysis-468Landmarks/tree/main/02-pattern_analysis_exp)

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
|

----- isso eu ainda não decidi ------------
│   ├── /pattern_analysis
│   |   |
│   |   ├── /[id_pessoa]
│   |   |   |
│   |   |   ├── 0-x.csv
│   |   |   ├── 1-x.csv
│   |   |   ├── 2-x.csv
│   |   |   ├── 3-x.csv
│   |   |   ├── 4-x.csv
│   |   |   ├── 5-x.csv
│   |   |   ├── 6-x.csv
│   |   |   ├── 7-x.csv
│   |   |   ├── 0-x.png
│   |   |   ├── 1-x.png
│   |   |   ├── 2-x.png
│   |   |   ├── 3-x.png
│   |   |   ├── 4-x.png
│   |   |   ├── 5-x.png
│   |   |   ├── 6-x.png
│   |   |   ├── 7-x.png
```
