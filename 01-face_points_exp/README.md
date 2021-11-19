# Experimento 1 - Analisar os rostos com o mediapipe e salvar os dados das posições dos Landmarks

Será analisada cada imagem de cada pessoa em cada uma das expressões e o resultado será salvo na pasta processed da seguinte forma:

```
.
├── /processed
|
│   ├── /face_points
│   |   |
│   |   ├── /[id_expressão]
│   |   |   |
│   |   |   ├──/[id_pessoa]
│   |   |   |   |
│   |   |   |   ├── positions.csv (vai conter as posições xy dos landmarks das 3 fotos e uma média)
│   |   |   |   ├── [id_pessoa]-[id_expressão]\mask-line_1.png (Foto da pessoa, mas com uma linha em cima de uma mascara simples ligando alguns pontos)
│   |   |   |   ├── [id_pessoa]-[id_expressão]\mask-line_2.png (Foto da pessoa, mas com uma linha em cima de uma mascara simples ligando alguns pontos)
│   |   |   |   ├── [id_pessoa]-[id_expressão]\mask-line_2.png (Foto da pessoa, mas com uma linha em cima de uma mascara simples ligando alguns pontos)
│   |   |   |   ├── [id_pessoa]-[id_expressão]\mask-triangles_1.png (Foto da pessoa, mas com uma linha em cima de uma mascara complexa com triangulos ligando todos os pontos)
│   |   |   |   ├── [id_pessoa]-[id_expressão]\mask-triangles_2.png (Foto da pessoa, mas com uma linha em cima de uma mascara complexa com triangulos ligando todos os pontos)
│   |   |   |   ├── [id_pessoa]-[id_expressão]\mask-triangles_2.png (Foto da pessoa, mas com uma linha em cima de uma mascara complexa com triangulos ligando todos os pontos)
│   |   |   |   ├── [id_pessoa]-[id_expressão]\mask-line_mean.png (somente a mascara simples com uma linha preta e fundo branco)
│   |   |   |   ├── [id_pessoa]-[id_expressão]\mask-triangles_mean.png (somente a mascara complexa de triangulos com uma linha preta e fundo branco)
```

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
