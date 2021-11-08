# Experimento 1 - Analisar os rostos com o mediapipe e salvar os dados das posições dos Landmarks

Será analisada cada imagem de cada pessoa em cada uma das expressões e o resultado será salvo na pasta processed da seguinte forma:

```
.
├── /processed </br>
| </br>
│   ├── /face_points </br>
│   |   |   </br>
│   |   ├── /[id_expressão] </br>
│   |   |   |</br>
│   |   |   ├──/[id_pessoa] </br>
│   |   |   |   | </br>
│   |   |   |   ├── positions.csv (vai conter as posições xy dos landmarks das 3 fotos e uma média) </br>
│   |   |   |   ├── [id_pessoa]-[id_expressão]\mask-line_1.png (Foto da pessoa, mas com uma linha em cima de uma mascara simples ligando alguns pontos) </br>
│   |   |   |   ├── [id_pessoa]-[id_expressão]\mask-line_2.png (Foto da pessoa, mas com uma linha em cima de uma mascara simples ligando alguns pontos) </br>
│   |   |   |   ├── [id_pessoa]-[id_expressão]\mask-line_2.png (Foto da pessoa, mas com uma linha em cima de uma mascara simples ligando alguns pontos) </br>
│   |   |   |   ├── [id_pessoa]-[id_expressão]\mask-triangles_1.png (Foto da pessoa, mas com uma linha em cima de uma mascara complexa com triangulos ligando todos os pontos) </br>
│   |   |   |   ├── [id_pessoa]-[id_expressão]\mask-triangles_2.png (Foto da pessoa, mas com uma linha em cima de uma mascara complexa com triangulos ligando todos os pontos) </br>
│   |   |   |   ├── [id_pessoa]-[id_expressão]\mask-triangles_2.png (Foto da pessoa, mas com uma linha em cima de uma mascara complexa com triangulos ligando todos os pontos) </br>
│   |   |   |   ├── [id_pessoa]-[id_expressão]\mask-line_mean.png (somente a mascara simples com uma linha preta e fundo branco) </br>
│   |   |   |   ├── [id_pessoa]-[id_expressão]\mask-triangles_mean.png (somente a mascara complexa de triangulos com uma linha preta e fundo branco) </br>
```

## Procedimentos

Para melhor analisar as imagens posteriormente um padrão será adotado, e ele será o seguinte:

- Todas as imagens serão rotacionadas para que os olhos fiquem sempre na mesma linha
- As imagens serão recortadas em um quadrado, deixando apenas o rosto centralizado. com os pontos XXX (Queixo) e XXX (Testa) sempre no mesmo pixel para termos o mesmo alinhamento em todas as imagens
- A imagem será redimensionada para possuir 500px x 500px
- somente então será salva com os dados relativos a imagem no fim deste processo.
