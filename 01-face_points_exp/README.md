# Experimento 1 - Analisar os rostos com o mediapipe e salvar os dados das posições dos Landmarks

Será analisada cada imagem de cada pessoa em cada uma das expressões e o resultado será salvo na pasta processed da seguinte forma:

```
.
├── /processed
|   |
|   ├── [id_expressão]
|   |   |
|   |   ├── mean_[id_expressão].png (Mascara com triangulos fantas da expressão com fundo branco)
|   |   ├── [id_supervisionado]
|   |   |   ├── [id_pessoa]
|   |   |   |   |
|   |   |   |   ├── [id_foto].csv (vai conter as posições xy dos landmarks da foto)
|   |   |   |   ├── [id_foto].jpg (Mascara de triangulos da pessoa com fundo preto pra cada foto)
|   |   |   |   ├── mean_[id_pessoa].jpg (Mascara de triangulos fantasma da pessoa com fundo branco)

```

## Descrição dos arquivos

Os scrips desta pasta devem ser rodados em um shell do pipenv. para instalá-lo, basta executar `$ pip install pipenv` e para iniciar o ambiente virtual: `$ pipenv shell`

#### `analyser.py`

Anda de pasta em pasta do dataset e salva os .csv em processed na pasta raiz do projeto

#### `draw_triangles.py`

Anda pelas pastas de processed e, a partir dos csv, gera as mascaras e as salva em .jpg no mesmo diretório

#### `error_verifier.py`

Verifica e exclui as inconsistencias encontradas no dataset, como pastas com numeros equivocados de imagens, e casos nos quais faces não foram reconhecidas

#### `face_mesh.py`

Uma classe para extrair os pontos da face

#### `face_adjustments.py`

Faz as transformações na imagem a partir dos pontos extraidos, de acordo com as definições abaixo

## Procedimentos

Para melhor analisar as imagens posteriormente um padrão será adotado, e ele será o seguinte:

- Todas as imagens serão rotacionadas para que os olhos fiquem sempre na mesma linha (alignEyes)
- O ponto 10 é deixado sempre na altura 25 e no centro da imagem, com a distancia entre o ponto 10 e o ponto 152 sendo de 320px (alignFace)
- A imagem será recortada em um retangulo, deixando apenas o rosto centralizado, com margem de 25px.
- A imagem será deixada com 600px X 600px sem redimensionar, apenas colocando bordas pretas nas laterais e em baixo para completar o tamanho
- somente então será salva com os dados relativos a imagem no fim deste processo.

![image](https://user-images.githubusercontent.com/42501669/140919974-db400ddb-41a4-4c7f-bd41-c7ad0ad03ba6.png)

## Remoções do Dataset

### Número incorreto de fotos em uma pasta do usuário

nos casos em que foi detectado que uma das pastas do usuário continha um numero diferente de 3 fotos, todas as pastas dele foram removidas da analise.
Os usuários que esta regra foi aplicada são os que seguem, com as seguintes observações:

- 00541 - 4 imagens em 00/00
- 02069 - 11 imagens em 00/00
- 05669 - 7 imagens em 00/00
- 06644 - 2 imagens em 00/00

## Exemplo de Máscara gerada com os Landmarks obtidos

<p align="center">
<img src="./results/05/00/04435/data-lms-2019-06-07 10_59_12.jpg" height="auto" width="350px"/>
</p>

## Resultado das médias de cada expressão

|                                                                                                 |                                                                                                 |                                                                                                 |                                                                                                 |
| ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| <img src="./results/00/mean_00.jpg" height="auto" width="250px"/></br> <p align="center">00</p> | <img src="./results/01/mean_01.jpg" height="auto" width="250px"/></br> <p align="center">01</p> | <img src="./results/02/mean_02.jpg" height="auto" width="250px"/></br> <p align="center">02</p> | <img src="./results/03/mean_03.jpg" height="auto" width="250px"/></br> <p align="center">03</p> |
| <img src="./results/04/mean_04.jpg" height="auto" width="250px"/></br> <p align="center">04</p> | <img src="./results/05/mean_05.jpg" height="auto" width="250px"/></br> <p align="center">05</p> | <img src="./results/06/mean_06.jpg" height="auto" width="250px"/></br> <p align="center">06</p> | <img src="./results/07/mean_07.jpg" height="auto" width="250px"/></br> <p align="center">07</p> |

### Comparação entre supervisionado e não supervisionado

|                                                                                                       |                                                                                                       |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| <img src="./results/00/mean_00-00.jpg" height="auto" width="250px"/></br> <p align="center">00/00</p> | <img src="./results/00/mean_00-01.jpg" height="auto" width="250px"/></br> <p align="center">00/01</p> |
| <img src="./results/01/mean_01-00.jpg" height="auto" width="250px"/></br> <p align="center">01/00</p> | <img src="./results/01/mean_01-01.jpg" height="auto" width="250px"/></br> <p align="center">01/01</p> |
| <img src="./results/02/mean_02-00.jpg" height="auto" width="250px"/></br> <p align="center">02/00</p> | <img src="./results/02/mean_02-01.jpg" height="auto" width="250px"/></br> <p align="center">02/01</p> |
| <img src="./results/03/mean_03-00.jpg" height="auto" width="250px"/></br> <p align="center">03/00</p> | <img src="./results/03/mean_03-01.jpg" height="auto" width="250px"/></br> <p align="center">03/01</p> |
| <img src="./results/04/mean_04-00.jpg" height="auto" width="250px"/></br> <p align="center">04/00</p> | <img src="./results/04/mean_04-01.jpg" height="auto" width="250px"/></br> <p align="center">04/01</p> |
| <img src="./results/05/mean_05-00.jpg" height="auto" width="250px"/></br> <p align="center">05/00</p> | <img src="./results/05/mean_05-01.jpg" height="auto" width="250px"/></br> <p align="center">05/01</p> |
| <img src="./results/06/mean_06-00.jpg" height="auto" width="250px"/></br> <p align="center">06/00</p> | <img src="./results/06/mean_06-01.jpg" height="auto" width="250px"/></br> <p align="center">06/01</p> |
| <img src="./results/07/mean_07-00.jpg" height="auto" width="250px"/></br> <p align="center">07/00</p> | <img src="./results/07/mean_07-01.jpg" height="auto" width="250px"/></br> <p align="center">07/01</p> |
