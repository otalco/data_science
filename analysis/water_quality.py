import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report

'''DataSet download Link: https://www.kaggle.com/datasets/mssmartypants/water-quality'''

# Carregar o arquivo CSV como um dataframe Pandas
df = pd.read_csv('data_sets\\waterQuality1.csv')

# Análise prévia sobre o formato dos dados
print(df.head())
print(df.tail())
print(df.dtypes)
print(df.columns)  # Check the column names to ensure 'ammonia' is present

# Ensure 'ammonia' column exists
if 'ammonia' not in df.columns:
	raise KeyError("'ammonia' column is missing from the dataset")

# Identificar e remover registros com problemas nas colunas "ammonia" e "is_safe"
df = df[pd.to_numeric(df['ammonia'], errors='coerce').notnull()]
df = df[pd.to_numeric(df['is_safe'], errors='coerce').notnull()]
df['ammonia'] = pd.to_numeric(df['ammonia'])
df['is_safe'] = pd.to_numeric(df['is_safe'])

# Verificar o problema de desbalanceamento
print(df['is_safe'].value_counts())

# Reamostragem para tratar o desbalanceamento
c_0 = df[df['is_safe'] == 0].sample(n=912, random_state=1)
c_1 = df[df['is_safe'] == 1]
df = pd.concat([c_0, c_1])
df = df.reset_index(drop=True)

# Verificar o resultado obtido
print(df['is_safe'].value_counts())

# Separar os dados em conjuntos de treinamento (70%) e teste (30%)
X = df.drop('is_safe', axis=1)
y = df['is_safe']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

# Aplicar os classificadores
# Gaussian Naive Bayes
gnb = GaussianNB()
gnb.fit(X_train, y_train)
y_pred_gnb = gnb.predict(X_test)
print("Gaussian Naive Bayes Classification Report:")
print(classification_report(y_test, y_pred_gnb))

# K Nearest Neighbours
knn = KNeighborsClassifier(n_neighbors=3, metric='euclidean')
knn.fit(X_train, y_train)
y_pred_knn = knn.predict(X_test)
print("K Nearest Neighbours Classification Report:")
print(classification_report(y_test, y_pred_knn))

# Decision Tree
dt = DecisionTreeClassifier(random_state=1)
dt.fit(X_train, y_train)
y_pred_dt = dt.predict(X_test)
print("Decision Tree Classification Report:")
print(classification_report(y_test, y_pred_dt))