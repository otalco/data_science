# Data_Science

## Sobre o repositório:
Trata-se de um repositório de estudo para a disciplina de ciência de dados do curso de Análise e Desenvolvimento de Sistemas da Unifil.

## Sobre as análises
### water_quality.py
Análise desenvolvida no contexto da seguinte atividade avaliativa:

>Você foi contratado por uma companhia de distribuição de água para criar um modelo que auxilie na análise de qualidade de água. Os dados (disponível em: https://www.kaggle.com/mssmartypants/water-quality. Acesso em: 22 ago. 2022) estão em um arquivo CSV que descreve a quantidade mensurada de 20 compostos presentes em amostras de água, como alumínio, amônia, cobre e outros. O link do dataset fornece uma referência sobre a quantidade aceitável de cada composto e contém uma coluna adicional (is_safe) que descreve se a amostra é segura (valor 1) ou não é segura (valor 0). Assim sendo, siga o roteiro a seguir para realizar a tarefa: 

>Carregue o arquivo CSV como um dataframe Pandas;
>Faça uma análise prévia sobre o formato dos dados (os recursos head, tail e dtypes podem ser úteis);
>As colunas “ammonia” e “is_safe” possuem alguns dados com erros de leitura que devem ser removidos do conjunto. Identifique os registros com problema, remova-os do dataframe e resolva possíveis problemas de tipagem das colunas (a função pandas.to_numeric pode ser útil);
>Verifique e resolva um possível problema de desbalanceamento dos dados (checar o final deste texto para instruções);
>Faça uma análise exploratória de dados para entende-los melhor;
>Separe os dados em conjuntos de treinamento (70%) e teste (30%);
>Aplique os classificadores Gaussian Naive Bayes, K Nearest Neighbours (n_neighbors=3 e metric='euclidean') e Decision Tree;
>Aplique o classification report para analisar a performance dos modelos e identifique o estimador com os melhores resultados.```

>Dica: para tornar os resultados comparáveis, utilize random_state=1.

>OBS.: o problema de desbalanceamento consiste em uma situação onde a quantidade de amostras pertencentes a uma determinada classe é muito superior às amostras das demais classes. Uma forma simples de tratar o problema de desbalanceamento é realizar uma reamostragem dos dados conforme os passos a seguir:

>Verificar o problema de desbalanceamento:
>print(df.is_safe.value_counts())

>Reamostragem:
>c_0 = df[df.is_safe == 0].sample(n = 912, random_state=1)

>c_1 = df[df.is_safe == 1]

>df = pd.concat([c_0, c_1])

>df = df.reset_index(drop=True)

>Verificar o resultado obtido:
>print(df.is_safe.value_counts())```

### O data-set para essa atividade pode ser encontrado [aqui](https://www.kaggle.com/datasets/mssmartypants/water-quality)

### dehli_climate_2013_2017.py
Análise desenvolvida no contexto da seguinte atividade avaliativa:


##### Descrição do conjunto de dados

et- Tipos de variáveis: Descrever os tipos de dados presentes em cada coluna (e.g., numérico, categórico).
al- Número de linhas e colunas: Informar a quantidade total de registros e colunas no dataset.
ha
### Estatísticas descritivas
nt- Média, mediana, desvio padrão: Calcular e apresentar as principais estatísticas descritivas para as variáveis numéricas.
o 
### Análise de dados faltantes
s - Identificação de dados faltantes: Verificar a presença de valores ausentes no dataset.
An- Estratégias para lidar com dados faltantes: Descrever possíveis abordagens para tratar os valores ausentes, como remoção de registros, imputação de valores, etc.
ál
is### Visualização de dados
es- Distribuição de variáveis: Criar gráficos para explorar a distribuição das variáveis (e.g., histogramas, boxplots).

- - Presença de outliers: Identificar e visualizar possíveis outliers no dataset.
Co
rrelações entre variáveis: Utilizar heatmaps ou scatter plots para identificar correlações entre as variáveis.



### O data-set para essa atividade pode ser encontrado [aqui](https://www.kaggle.com/sumanthvrao/daily-climate-time-series-data)
