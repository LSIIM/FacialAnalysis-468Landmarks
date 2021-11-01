# Muscle Correlation

Aqui é onde fiz as analises da face para identificar os músculos.

## Sobre os arquivos aqui contidos

O arquivo `muscles_identification.py` é onde é escrito manualmente a relação entre o "Músculo A" e os pontos que o representam, e atribui uma cor para identificá-lo na imagem gerada no `mani.py`. Para criar uma nova identificação de músculo pasta adicionar um item à lista `muscle_list`, do tipo Muscle, que recebe como parâmetro (Nome_do_musculo,lista_de_pontos,cor_RGB)

O arquivo `FaceMeshModule.py` é onde está a classe que analisa o rosto. Rela retorna uma nova imagem, caso alguma modificação seja feita lá dentro e uma lista de Faces (Ela pode detectar mais de um rosto). Para cada face ela retorna um par (x,y) que é a coordenada do ponto. O mediapipe analisa a imagem de maneira tridimensional, contudo, como a coordenada Z é irrelevante para esta analise, eu a ignorei.

O arquivo `main.py` utiliza o módulo e a lista de músculos para identificar cada ponto na imagem, gerando um arquivo png com uma legenda, no canto superior esquerdo, dos musculos
