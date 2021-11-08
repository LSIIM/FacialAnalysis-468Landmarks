# FacialAnalysis-468Landmarks

Este é um novo repositório para aplicar as tecnicas de analise usadas anteriormente pelo Tobias, contudo, desta vez utilizando o novo modelo facil da MediPipe com 468 landmarks.

# Correlação com os músculos da face

Na pasta /MuscleCorrelation estão os algoritimos utilizados para identificar os musculos da face e relacioná-los com os pontos fornecidos pelo modelo.
Este é um exemplo do resultado (Abra a imagem em uma nova guia, ela é ridiculamente gigante)

<p align="center">
<img src="./MuscleCorrelation/human-muscles-landmarks-colored.jpg" height="600px" width="auto"/>
</p>

# Experimentos

## Experimento 1 - Analisar os rostos com o mediapipe e salvar os dados das posições dos Landmarks

O objetivo é coletar os dados para que possam ser analisados e correlacionados posteriormente. O experimento esta descrito na pasta `01-face_points_exp`

## Experimento 2 - Analisar os dados obtidos no Exp1 para encontrar algum padrão

O objetivo é calcular a distancia de cada ponto para cada ponto da mascara de cada expressão e calcular a distancia entre cada ponto com sua contraparte na expressão neutra e salvar essas proporções em um csv

# Dados

Os dados serão salvos na pasta processed. Um resumo de seu conteudo é o que segue

/processed </br>
|- db.sqlite (Banco de dados com todos os dados processados e agregados) </br>
| </br>
|-/face_points </br>
| | </br>
| |-/[id_expressão] </br>
| | </br>
| | |-/[id_pessoa] </br>
| | | | </br>
| | | |- positions.csv </br>
| | | |- [id_pessoa]-[id_expressão]\mask-line_1.png </br>
| | | |- [id_pessoa]-[id_expressão]\mask-line_2.png </br>
| | | |- [id_pessoa]-[id_expressão]\mask-line_2.png </br>
| | | |- [id_pessoa]-[id_expressão]\mask-triangles_1.png </br>
| | | |- [id_pessoa]-[id_expressão]\mask-triangles_2.png </br>
| | | |- [id_pessoa]-[id_expressão]\mask-triangles_2.png </br>
| | | |- [id_pessoa]-[id_expressão]\mask-line_mean.png </br>
| | | |- [id_pessoa]-[id_expressão]\mask-triangles_mean.png </br>
| </br>
|-/pattern_analysis </br>
| | </br>
| |-/[id_pessoa] </br>
| | </br>
| | |- 0-x.csv </br>
| | |- 1-x.csv </br>
| | |- 2-x.csv </br>
| | |- 3-x.csv </br>
| | |- 4-x.csv </br>
| | |- 5-x.csv </br>
| | |- 6-x.csv </br>
| | |- 7-x.csv </br>
| | |- 0-x.png </br>
| | |- 1-x.png </br>
| | |- 2-x.png </br>
| | |- 3-x.png </br>
| | |- 4-x.png </br>
| | |- 5-x.png </br>
| | |- 6-x.png </br>
| | |- 7-x.png </br>
