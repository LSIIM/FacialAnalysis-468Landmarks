# Experimento 2 - Analisar os dados obtidos no Exp1 para encontrar algum padrão

## Primeira abordagem - Todos os pontos (Não deu resultados, foi abandonado)

### Parte 1

Para cada uma das máscaras de um usuário, obter as distâncias de cada ponto desta máscara para sua mascára neutra não supervisionada (00/00). Com esses dados, também gerar distâncias médias para a neutra NS de todos os usuários

### Parte 2

A partir dos dados gerados na parte 1, que são MUITOS, reduzílos a alguns números que, em teoria, representam a mascara daquela pessoa. Os resultados que serão coletados são os que seguem:

- Média de diferença entre as distancias da máscara em análise para todas as distancias da máscara neutra NS média
- Média de diferença entre as distancias da máscara em análise para todas as distancias da máscara neutra NS média, agrupado por músculos (Ver [MuscleCorrelation](https://github.com/MIGMA-Team/FacialAnalysis-468Landmarks/tree/main/MuscleCorrelation))
- Média de diferença entre as distancias da máscara em análise para todas as distancias da máscara neutra NS média, agrupado por GRUPOS musculares
- Média de diferença entre as distancias da máscara em análise para todas as distancias, separado por músculo, da máscara neutra NS média, agrupado por músculos (Ver [MuscleCorrelation](https://github.com/MIGMA-Team/FacialAnalysis-468Landmarks/tree/main/MuscleCorrelation))
- Média de diferença entre as distancias da máscara em análise para todas as distancias, separado por grupo múscular da máscara neutra NS média, agrupado por GRUPOS musculares

Todos os dados citados acima serão salvos em .cvs's, de acordo com a relação dos arquivos gerados

### Arquivos gerados

```
.
├── /processed
|
│   ├── /pattern_analysis
│   |   |
│   |   ├── /[id_pessoa]
│   |   |   |
│   |   |   ├── exp-tp_00-00.csv (A diferença entre cada ponto das expressões para o neutro NS)
│   |   |   ├── mean-dists_allp-allp.csv (A media de distancia entre cada ponto das expressões para o neutro NS)
│   |   |   ├── mean-diff-dists_allp-allp.csv (A diferença entre cada ponto das expressões para o neutro NS média)
```

#### mean-dists_allp-allp.csv

Neste cvs estão os dados relativos às analises de todos os pontos para todos os pontos, de acordo com a segiunte tabela:
| |exp|tp|face|muscle1|muscle2|...|
|---|---|---|---|---|---|---|
| |Número da expressão|Supervisionado ou não|distância média de todos para todos da face inteira|distância média de todos para todos do músculo 1|distância média de todos para todos do músculo 2|...|

#### mean-diff-dists_allp-allp.csv

Neste cvs estão os dados relativos às analises de todos os pontos para todos os pontos, de acordo com a segiunte tabela:
| |exp|tp|face|muscle1|muscle2|...|
|---|---|---|---|---|---|---|
| |Número da expressão|Supervisionado ou não|diferença da distância média de todos os pontos para todos da face inteira para a mascara média|diferença da distância média de todos os pontos para todos do músculo 1 da mascara média|diferença da distância média de todos os pontos para todos do músculo 2 da mascara média|...|

## Segunda abordagem - Pontos com alta variação em relação à face neutra

Neste experimento apenas serão analisados os pontos e suas contrapartes na expressão neutra.
A primeira parte foi calcular a média de distancia de cada ponto de todas as 16 máscaras para a neutra e então selecionei todos os pontos que a distancia é superior a média da máscara em todas as máscaras. 77 pontos foram selecionados

![points_img](https://user-images.githubusercontent.com/42501669/154383045-156d83f9-3731-47cc-ba60-9f3e7fd51810.png)


Com estes 77 pontos em mão, para cada máscara foi calculada a média deles, criando o arquivo `masks_means_pav.csv`

> pav = points above average

## Remoções do dataset

- Usuário 06644: Não fez todas as capturas
