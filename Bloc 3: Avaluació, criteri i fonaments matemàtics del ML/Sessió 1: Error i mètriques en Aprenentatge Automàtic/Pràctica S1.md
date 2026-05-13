# Pràctica — Regressió, error i avaluació amb train/test

En aquesta pràctica treballaràs amb un **problema general de regressió** i realitzaràs el procés bàsic complet d’avaluació d’un model d’aprenentatge automàtic:

- separar dades d’entrenament i de test
- entrenar un model de regressió
- fer prediccions
- avaluar el model amb una mètrica d’error
- interpretar els resultats

La pràctica és **independent del tipus concret de dades**. El focus està en el **procés**, no en la temàtica del dataset.

---

## Dataset
Se’t proporciona un dataset de regressió ja preparat, amb:
- diverses variables d’entrada (X)
- una variable de sortida (y)

https://archive.ics.uci.edu/dataset/2/adult

Feu un EDA per estudiar el dataset.

---

## Codi base 

### 1. Separació de dades en train i test (70% / 30%)

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)
```


### 2. Creació, entrenament i predicció del Model, 
```python
from sklearn.linear_model import LinearRegression

model = LinearRegression()

model.fit(X_train, y_train)

y_pred_train = model.predict(X_train)
y_pred_test = model.predict(X_test)

```

### 3. Extreure la Confusion Matrix i les mètriques. Decidir quina mètrica és més adequada


### 4. Provar de repetir el procés nous models, proveu canviant paràmetres del LinearRegression i després amb un altre model de regressió diferent al lineal. Després comparar mètriques
