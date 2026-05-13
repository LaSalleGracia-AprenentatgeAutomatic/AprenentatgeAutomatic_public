# Bloc 5 · Sessió 2
## K-Means en profunditat — Nombre de clusters i avaluació

---

## Objectiu de la sessió

En aquesta sessió aprendrem a aplicar **K-Means en problemes més complexos** i a resoldre un dels seus inconvenients principals: **com escollir el nombre de clusters (k)**. A més, introduirem mètriques per avaluar si una agrupació és bona o dolenta.

Al final de la sessió hauries de ser capaç de:
- aplicar **K-Means amb scikit-learn** en datasets reals en múltiples dimensions,
- escalar dades adequadament abans d'aplicar clustering,
- escollir el nombre òptim de clusters utilitzant el **mètode del colze (Elbow Method)**,
- interpretar la qualitat dels clusters amb el **Silhouette Score**.

---

## 1. Recordatori conceptual

Recordem els conceptes clau de la sessió anterior:
- **K-Means** assigna seqüencialment els punts al centroide més proper.
- Minimitza la distància dels punts al seu centre.
- **Requereix que fixem $k$**, el nombre de grups, per endavant.

### Pregunta clau

> Què passa si triem un **k incorrecte** (massa gran o massa petit)?

---

## 2. El problema del nombre de clusters: El Mètode del Colze (Elbow Method)

Atès que en aprenentatge no supervisat **no tenim la resposta correcta** (no hi ha etiquetes), no podem calcular un "accuracy" normal. 

Per escollir $k$, fem servir la **inèrcia (Inertia o WCSS - Within-Cluster Sum of Squares)**, també coneguda com a **Intra-cluster o Within-class distance**. Aquesta mètrica representa la suma de les distàncies al quadrat de cada punt al seu centroide. Volem que els punts dins d'un mateix cluster estiguin molt cohesionats (distància petita).

- Si $k$ augmenta, la inèrcia **sempre disminueix** (cada punt està més a prop del seu centre).
- Si $k = N$ (cada punt és un cluster), la inèrcia és 0. Això no és útil.

### El mètode del colze
Consisteix a calcular KMeans per a diferents valors de $k$ (ex: d'1 a 10), traçar la inèrcia en un gràfic, i buscar el **"colze"**: el punt on afegir més clusters deixa d'aportar una millora significativa.

---

## 3. Mètrica de qualitat: Silhouette Score

Mentre el mètode del colze usa només les distàncies internes del cluster, el **coeficient de Silhouette** incorpora els dos conceptes fonamentals per avaluar i validar qualsevol procés de clustering:
1. **Cohesió ($a$) o *Within-class distance***: distància mitjana d'un punt a la resta de punts del *mateix* cluster. (Ens diu com de compacte és el grup).
2. **Separació ($b$) o *Inter-class distance***: distància mitjana d'un punt als punts del *cluster més proper*. (Ens diu com d'aïllat està el grup respecte la resta).

$$S = \frac{b - a}{\max(a, b)}$$

### Interpretació

- Prop de **1 → clusters ben separats** i punts ben assignats.
- Prop de **0 → clusters solapats** (el punt està a la frontera entre dos clusters).
- **Negatiu → mala agrupació** (el punt estaria millor en l'altre cluster).

---

## 4. Pràctica guiada amb Python

Treballarem per agrupar fets i extreure diferents segments (clusters).

### Escalar les dades: imprescindible

En calcular distàncies (com l'Euclidiana), les variables amb valors grans dominaran completament sobre les variables amb valors petits. **Sempre hem d'escalar / normalitzar dades** abans d'aplicar KMeans.

```python
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Simulem dades per a l'exemple pràctic (Es pot usar 'mall_customers.csv')
from sklearn.datasets import make_blobs
X, y_true = make_blobs(n_samples=200, centers=4, cluster_std=1.0, random_state=42)

# 1. Escalar (Molt important!)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 2. Mètode del Colze
inercies = []
K_range = range(1, 11)

for k in K_range:
    km = KMeans(n_clusters=k, random_state=42)
    km.fit(X_scaled)
    inercies.append(km.inertia_)

# Visualització del colze
plt.figure(figsize=(8, 4))
plt.plot(K_range, inercies, marker='o')
plt.title('Mètode del Colze (Elbow Method)')
plt.xlabel('Nombre de clusters (k)')
plt.ylabel('Inèrcia')
plt.xticks(K_range)
plt.grid(True)
plt.show()
```

---

## 5. Exercicis a mà o de reflexió

### Exercici 1 — Escalat de dades (Conceptual)

Donat un client A amb Edat=30, Sou=30000 i un client B amb Edat=32, Sou=30050.  
Un client C té Edat=30, Sou=31000 i Edat=60, Sou=30000.  

1. Reflexiona: quina variable tindrà més pes al calcular la distància euclidiana si no s'escalen les dades? Com ho solucionarà el `StandardScaler`?

### Exercici 2 — Interpretació del Colze
1. Segons l'explicació de la "inèrcia", dibuixa a mà en un paper un gràfic de colze hipotètic on els valors d'inèrcia per a k=1..5 són, respectivament: [1000, 800, 300, 250, 240].
2. Quin seria el valor de $k$ òptim segons el teu gràfic? Raona-ho.

---

## 6. Exercicis amb ordinador

L'objectiu és aplicar l'explicació sobre dades reals o el dataset de pràctica de l'apartat anterior.

### Exercici 3 — Aplicar K-Means i Mètriques numèriques

**Tasques:**
1. Genera o carrega el teu dataset d'estudi amb `X_scaled`.
2. Fixa $k = 4$ basant-te en els gràfics del colze vists anteriorment.
3. Entrena un model `KMeans`.
4. Calcula l'índex de qualitat utilitzant `silhouette_score(X_scaled, kmeans.labels_)`. Imprimeix aquest valor.
5. Repeteix per $k = 2$ i $k = 5$. Quin dóna millor Silhouette Score i per tant millor agrupació matemàtica?

```python
# Escriu aquí el teu codi
# recorda importar: from sklearn.metrics import silhouette_score

```

---

## 7. Discussió i conclusions

- Les dades del món real (clients, cançons, etc.) gairebé mai formen clusters "perfectes" de manual.
- **El clustering descobreix estructures possibles, no veritats absolutes.** 
- El sentit de negoci sovint determina un $k$ més adequat (per exemple, si el departament de màrqueting necessita 3 perfils clau, forçarem $k=3$ encara que el Silhouette sigui millor per a $k=5$).
