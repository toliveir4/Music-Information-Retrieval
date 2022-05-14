# Music Information Retrieval

## Report

__Done by:__

- Marco Pais - Nº 2019218
- Tiago Oliveira - Nº 2019219068
- Emílio Hurtado - Nº 2021169693

<br>

### 1. Preparação

- 1.1. Ganhar familiaridade com um sistema de recomendação real, e.g., Jango.com, Spotify, Last.fm, Torch ou outro.

- 1.2. Descarregar a base de dados a utilizar (4Q audio emotion dataset) do seguinte URL: <http://mir.dei.uc.pt/downloads.html>.

- 1.3. Analisar a base de dados.

  - 1.3.1. Excertos áudio: ficheiros mp3 (em particular as 4 queries).

  - 1.3.2. Metadados: ficheiro panda_dataset_taffc_metadata.csv, colunas Song, Artist, Quadrant, MoodsStrSplit e GenresStr.

  - 1.3.3. Features: ficheiros top100_features.csv (features extraídas) e features.csv (descrição das features).

- 1.4. Estudar a framework de processamento áudio librosa

  - 1.4.1. Instalar a framework a partir do seguinte URL: <https://librosa.org/>. Será também necessário instalar a framework ffmpeg para leitura de ficheiros .mp3: <https://ffmpeg.org/>.

  - 1.4.2. Analisar o código fonte de base fornecido no InforEstudante (ficheiro mrs.py).

  - 1.4.3. Estudar a documentação da framework: <https://librosa.org/doc/>.

<br>

### 2. Extracção de Features

- 2.1. Processar as features do ficheiro top100_features.csv.

  - 2.1.1. Ler o ficheiro e criar um array numpy com as features disponibilizadas.

  - 2.1.2. Normalizar as features no intervalo [0, 1].

  - 2.1.3. Criar e gravar em ficheiro um array numpy com as features extraídas (linhas = músicas; colunas = valores das features).

  - 2.2. Extrair features da framework librosa.

  - 2.2.1. Para os 900 ficheiros da BD, extrair as seguintes features (sugestão: guardar todas as músicas na mesma pasta):

    - Features Espectrais: mfcc, spectral centroid, spectral bandwidth, spectral
        contrast, spectral flatness e spectral rolloff.

    - Features Temporais: F0, rms e zero crossing rate.

    - Outras features: tempo.

    - Utilize os parâmetros por omissão do librosa (sr = 22050 Hz, mono, window
        length = frame length = 92.88 ms e hop length = 23.22 ms).

    - Guarde as features num array numpy 2D, com __número de linhas = número de
        músicas e número de colunas = número de feartures__

  - 2.2.2. Calcular as 7 estatísticas típicas sobre as features anteriores: média, desvio padrão, assimetria (skewness), curtose (kurtosis), mediana, máximo e mínimo. Para o efeito, utilizar a biblioteca scipy.stats (e.g., scipy.stats.skew).

  - 2.2.3. Normalizar as features no intervalo [0, 1].

  - 2.2.4. Criar e gravar em ficheiro o array numpy com as features extraídas.

- 2.3. __Alínea com bonificação de 10% na nota final! (Sugestão: desenvolver nas semanas 5 e 6).__ Implementar features de raiz. Neste ponto, não é permitido utilizar o librosa nem
qualquer outra biblioteca, à excepção do scipy e numpy, e.g., scipy.fftpack.

  - 2.3.1. Desenvolver o código Python/numpy para extrair as features anteriores (à
    excepção de spectral contrast, F0 e tempo), usando a mesma parametrização.     Comparar os resultados obtidos com os resultados do librosa.

  - 2.3.2. Criar e gravar em ficheiro um array numpy com as features extraídas (i.e, as estatísticas correspondentes, com normalização).

<br>

### 3. Implementação de métricas de similaridade

- 3.1. Desenvolver o código Python/numpy para calcular as seguintes métricas de
similaridade:
  
  - 3.1.1. Distância Euclidiana
  
  - 3.1.2. Distância de Manhattan
  
  - 3.1.3. Distância do Coseno
  
  - 3.2. Criar e gravar em ficheiro 6 (ou 9, se bonificação) matrizes de similaridade (900x900), uma para cada conjunto de features e métrica de distância utilizada.

- 3.3. Criar os 6 (ou 9) rankings de similaridade (para as 4 queries fornecidos). Considere apenas recomendações de 20 músicas.

- __3.4. Apresentar, comparar e discutir os resultados.__

## __Euclidiana: top100__

### __MT0000202045__
|||||||||||
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| MT0014878397 | MT0011821215 | MT0011380622 | MT0005129157 | MT0033415296 | MT0040033011 | MT0005091539 | MT0012534566 | MT0006001707 | MT0029874624 |
| MT0011413068 | MT0004896738 | MT0032235381 | MT0000011975 | MT0013313448 | MT0009016829 | MT0004958762 | MT0009010830 | MT0003311798 | MT0008733057 |

### __MT0000379144__
|||||||||||
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| MT0006742179 | MT0010482550 | MT0005029328 | MT0003462877 | MT0003442366 | MT0000729701 | MT0008222676 | MT0011376343 | MT0007067293 | MT0011369407 |
| MT0003968586 | MT0012116237 | MT0001870847 | MT0007627521 | MT0008530072 | MT0029772184 | MT0015005100 | MT0027002641 | MT0005515169 | MT0006367176 |

### __MT0000414517__
|||||||||||
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| MT0026776967 | MT0028335228 | MT0033159895 | MT0003402538 |  'MT0009117202 | MT0007443823 | MT0002915967 | MT0034005433 | MT0009437817 | MT0006640857 |
| MT0001942272 | MT0000540286 | MT0011440705 | MT0006397809 | MT0027835071 | MT0027159893 | MT0006919273 | MT0007087238 | MT0011032905 | MT0000922312 |

### __MT0000956340__
|||||||||||
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| MT0006552038 | MT0005331755 | MT0012914763 | MT0005478759 | MT0004085907 | MT0007535042 | MT0014838459 | MT0028345470 | MT0011960348 | MT0029065626 |
| MT0004715422 | MT0034403951 | MT0001340713 | MT0010617945 | MT0006352493 | MT0006862088 | MT0007812490 | MT0005751512 | MT0011999773 | MT0003248394 |
<br>

### 4. Avaliação

- 4.1. Avaliação objectiva.

  - 4.1.1. Para cada uma das 4 queries, obter o ranking das 20 músicas recomendadas com base na correspondência com os __metadados__ seguintes: artista, género, quadrante e emoção. Por cada item coincidente, adicionar um ponto à qualidade da música alvo, e.g., se tanto a música de referência como o alvo tiverem género = jazz e emoção = happy, a qualidade do alvo será 2.

  - 4.1.2. Criar e gravar a matriz de similaridade baseada em contexto (i.e., nos metadados).
  
  - 4.1.3. Para cada um dos rankings determinados em 3.3, calcular a métrica precision, assumindo como relevantes as músicas devolvidas em 4.1.1 (metadados).
  
  - __4.1.4. Apresentar, comparar e discutir os resultados.__

- 4.2. Avaliação subjectiva.

  - 4.2.1. Para cada uma das 4 queries, conjunto de 100 features e distância do coseno, avaliar a qualidade de cada uma das 20 recomendações, com base na seguinte escala de Likert ": 1 – Muito Má; 2 – Má; 3 – Aceitável; 4 – Boa; 5 – Muito Boa(para as 4 queries). Cada elemento do grupo deverá efectuar individualmente a avaliação da recomendação.

    __a)__ Calcular a média e o desvio-padrão de todos os membros por query, assim como a média e o desvio-padrão global para as 4 queries.

    __b)__ Definindo um score mínimo de 2.5 para “recomendação relevante”, calcular a
precision resultante.
  
  - 4.2.2. Para cada uma das 4 queries e similaridade com base nos metadados, avaliar a qualidade de cada uma das 20 recomendações, com base na escala de Likert anterior. Cada elemento do grupo deverá efectuar individualmente a avaliação da recomendação.
  
    __a)__ Calcular a média e o desvio-padrão de todos os membros por query, assim
como a média e o desvio-padrão global para as 4 queries.

    __b)__ Definindo um score mínimo de 2.5 para “recomendação relevante”, calcular a
precision resultante e actualizar o valor da F-measure.

  - __4.2.3. Apresentar, comparar e discutir os resultados.__

<br>
