# Literature Review

Para guardar aqui as referencias e anotações

## Emotion Recognition from Physiological Signal Analysis: A Review

[Emotion Recognition from Physiological Signal Analysis: A Review](https://www.sciencedirect.com/science/article/pii/S157106611930009X)

Nesse estudo eles citam o uso do FACS em um método de reconhecimento de emoções através de câmeras no tópico 3.2

> The Affectiva Emotion SDK (Affectiva, Massachusetts, U.S.A.) [53] offers a six-month trial for students and is able to identify 20 expressions and seven emotions based on the Facial Action Coding System (FACS) by Ekman [26], with a broad support for operating systems (iOS, Android, Web, Windows, Linux, macOS, Unity, Raspberry Pi).

## Facial emotion recognition in major depressive disorder: A meta-analytic review

[Facial emotion recognition in major depressive disorder: A meta-analytic review ](https://www.sciencedirect.com/science/article/abs/pii/S016503272100639X)

Nesse eles não falam sobre o que queremos, eles abordam como as pessoas com depressão reconhecem expressões. O que queremos e o inverso

> Studies examining facial emotion recognition in participants with MDD have produced discrepant findings. Specifically, some studies have suggested that symptoms of depression are associated with a general deficit in facial emotion recognition

> The purpose of the current study is to better understand the process of facial emotion recognition in MDD and address the inconsistencies associated with previous studies in this area. Specifically, we examined whether dysthymic participants show a consistent deficit in their ability to identify facial expression of emotion or whether they evidence difficulties in the recognition of specific emotions.

## Automated Facial Action Coding System for dynamic analysis of facial expressions in neuropsychiatric disorders

[Automated Facial Action Coding System for dynamic analysis of facial expressions in neuropsychiatric disorders](https://www.sciencedirect.com/science/article/abs/pii/S016502701100358X)

Esse artigo apresenta uma solução interessante para analisar a diferença entre a forma na qual as expressões faciais são construídas entre pessoas com e sem doenças mentais, contudo, o método de FACS necessita ser feito em vídeo, pois boa parte da análise é feita na transição entre uma Action Unit estar ausente até estar presente.
Entretanto, o artigo apresenta alguns problemas, tais como uma população de estudo baixíssima (6 pessoas, 3 saudáveis e 3 com esquizofrenia) e o foco em tentar diferenciar as expressões de neurotípicos e de esquizofrênicos em específico. O resultado que chegaram é que esquizofrênicos tem expressões mais ambíguas.

Em alguns pontos a estratégia deles se assemelha à nossa (No caso de comparar com a expressão neutra):

> To extract geometric features of a test face, we first align the face to the template by similarity transformations to suppress within-subject head pose variations and inter-subject geometric differences. Next, we use differences of edge lengths between each face and a neutral face of the same person, formed into a 436-dimensional vector of geometric features, thereby further emphasizing the change due to facial expressions and suppressing irrelevant changes

E uma coisa que achei interessante é que eles fizeram um método para identificar emoções "erradas", por exemplo em uma expressão de medo não deveria existir ativação dos músculos de alegra (Esse foi um exemplo que inventei, não chequei a tabela de AUs desqualificadoras pra fazer esse exemplo)

> To define “inappropriate” frames, we used the statistical study of Kohler et al. (2004), which analyzed which AUs are involved in expressing theuniversal emotions ofhappiness, sadness, anger, and fear. Specifically, they identified AUs that are uniquely present or absent in each emotion. AUs that are uniquely present in a certain emotion were called “qualifying” AUs of the emotion, and AUs that are uniquely absent were called “disqualifying” AUs ofthe emotion, as shown in Table 2. Based on this, we defined an image frame from an intended emotion as inappropriate if it contained one or more disqualifying AUs of that emotion or one or more qualifying AUs of the other emotions. This decision rule was applied to all frames in a video to derive the inappropriateness measure automatically.

## What is the relationship between the recognition of emotions and core beliefs: Associations between the recognition of emotions in facial expressions and the maladaptive schemas in depressed patients

[What is the relationship between the recognition of emotions and core beliefs: Associations between the recognition of emotions in facial expressions and the maladaptive schemas in depressed patients](https://www.sciencedirect.com/science/article/abs/pii/S0005791610000807)

Eles não falam do que queremos, novamente eles avaliam a habilidades das pessoas com depressão de identificar emoções
