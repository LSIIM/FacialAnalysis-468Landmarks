# Experimento 2 - Analisar os dados obtidos no Exp1 para encontrar algum padrão

## Parte 1
Para cada uma das máscaras de um usuário, obter as distâncias de cada ponto desta máscara para sua mascára neutra não supervisionada (00/00). Com esses dados, também gerar distâncias médias para a neutra NS de todos os usuários

## Parte 2
A partir dos dados gerados na parte 1, que são MUITOS, reduzílos a alguns números que, em teoria, representam a mascara daquela pessoa. Os resultados que serão coletados são os que seguem:

- Média de diferença entre a distancia de cada distancia de uma máscara para a máscara média
- Média de diferença entre a distancia de cada distancia de uma máscara para a máscara média, agrupado por músculos (Ver [MuscleCorrelation](https://github.com/MIGMA-Team/FacialAnalysis-468Landmarks/tree/main/MuscleCorrelation))
- Média de diferença entre a distancia de cada distancia de uma máscara para a máscara média, agrupado por GRUPOS musculares

Todos os dados citados acima serão salvos em .cvs's, de acordo com a relação dos arquivos gerados


## Arquivos gerados

```
.
├── /processed
|
│   ├── /pattern_analysis
│   |   |
│   |   ├── /[id_pessoa]
│   |   |   |
│   |   |   ├── exp-tp_00-00.csv (A diferença entre cada ponto das expressões para o neutro NS)

```

## Remoções do dataset

- Usuário 06644: Não fez todas as capturas
