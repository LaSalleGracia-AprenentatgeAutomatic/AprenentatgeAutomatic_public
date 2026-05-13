
# Bloc 5 — Aprenentatge No Supervisat  
## Sessió 3 — Reducció de dimensionalitat amb PCA


---

# 1. Punt de partida: per què necessitem PCA?

A la sessió anterior hem agrupat dades amb **K-means**.

Però hi ha un problema habitual:

- a vegades les dades no tenen 2 variables
- poden tenir 5, 10, 20 o 100 variables
- llavors no les podem visualitzar fàcilment
- també pot haver-hi variables redundants o sorolloses

Pregunta inicial per a classe:

> Si un dataset té 12 variables, com el podem “veure”?

Idea que ha de quedar clara:

> Quan tenim moltes variables, ens interessa **resumir** la informació sense perdre l’essencial.

---

# 2. Exemple simple: dades que ja “apunten” en una direcció

## Situació

Imaginem que tenim dades d’alumnes amb dues variables:

- hores d’estudi
- nota final

Taula simplificada:

| Alumne | Hores estudi | Nota |
|---|---:|---:|
| A | 6 | 8 |
| B | 3 | 5 |
| C | 2 | 4 |
| D | 5 | 7 |
| E | 4 | 6 |

Si dibuixem aquests punts, veurem que:

- no estan repartits a l’atzar
- segueixen una direcció dominant
- hi ha una estructura clara

Pregunta:

> Si haguéssim de resumir aquests punts en una sola direcció, quina triaríem?

Resposta intuïtiva:

> La direcció que segueix millor el núvol de punts.

Aquesta és la primera intuïció de PCA.

---

# 3. Primera intuïció geomètrica

PCA busca:

> les direccions en què les dades varien més

No busca la direcció “més bonica”, ni la que separa classes, ni la que prediu una etiqueta.

Busca:

> **la direcció amb més informació estructural**, entesa com la direcció amb més variabilitat.

---

## Idea visual

Si els punts formen un núvol allargat:

- hi ha una direcció principal, la de màxima extensió
- i una segona direcció perpendicular, amb menys variació

Aquestes direccions seran:

- **primer component principal**
- **segon component principal**

---

# 4. Matemàtiques just in time (1): la variància

Abans de parlar de PCA, necessitem una idea:

> **variància = com de disperses estan les dades**

Exemple simple:

Conjunt A:  
`5, 5, 5, 4, 5`

Conjunt B:  
`1, 3, 5, 7, 9`

Tots dos poden tenir una mitjana semblant, però:

- al conjunt A gairebé no hi ha variació
- al conjunt B hi ha molta variació

Idea clau:

> PCA busca eixos on la variància sigui gran.

Per què?

> perquè on hi ha variació acostuma a haver-hi més informació útil sobre l’estructura de les dades.

---

# 5. Matemàtiques just in time (2): projecció

Ara imaginem un conjunt de punts en 2D.

Si projectem els punts sobre una recta:

- obtenim una versió simplificada del dataset
- cada punt queda representat per una sola coordenada sobre aquella recta

Pregunta:

> quina recta ens convé més?

Resposta:

> la recta sobre la qual les projeccions conservin la màxima variabilitat.

Això és exactament la idea del **primer component principal**.

---

# 6. Activitat guiada sense paquets

## Exercici 1 — Triar la millor direcció visualment

3 possibles rectes sobre un núvol de punts:

- una recta horitzontal
- una vertical
- una diagonal

Decidim:

1. quina recta recull millor la forma del núvol
2. quina conservaria més informació si projectéssim els punts
3. quina sembla la pitjor opció

Conclusió esperada:

> la millor direcció és la que segueix l’allargament principal del núvol de punts.

---

# 7. Del cas de 2D al cas real

Fins aquí ho hem vist en 2 dimensions perquè és fàcil de visualitzar.

Però en realitat:

- les dades poden tenir moltes variables
- PCA generalitza aquesta mateixa idea
- en lloc de buscar una recta en 2D, busca direccions òptimes en espais de més dimensions

Resultat:

- podem passar de 10 variables a 2 components
- podem passar de 50 variables a 3 components
- podem conservar una part important de la informació

---

# 8. Què és exactament PCA?

PCA vol dir:

> **Principal Component Analysis**

És una tècnica que transforma les variables originals en noves variables anomenades:

> **components principals**

Aquestes noves variables:

- són combinacions lineals de les originals
- estan ordenades de més a menys informació
- no estan correlacionades entre elles

---

## Idea clau dels components

- **PC1**: direcció amb màxima variància
- **PC2**: segona direcció amb màxima variància, perpendicular a la primera
- **PC3**: tercera direcció, i així successivament

Si ens quedem amb els primers components:

> reduïm dimensions mantenint molta informació.

---

# 9. Matemàtiques just in time (3): combinació lineal

Sense entrar en càlcul matricial profund, podem dir:

Si tenim variables com:

- ingressos
- despesa
- estalvi

un component principal podria ser una combinació com:

$$
PC1 = 0.6 \cdot ingressos + 0.5 \cdot despesa - 0.2 \cdot estalvi
$$

Important entendre que:

> cada component és una barreja intel·ligent de les variables originals.

---

# 10. Exemple continuat: perfil de clients

Ara fem el salt a un exemple més realista.

Suposem un dataset amb clients i variables com:

- edat
- ingressos anuals
- despesa mensual
- freqüència de compra

Quin problema tenim?

- són 4 variables
- no ho podem veure tot bé en un sol gràfic
- hi pot haver variables relacionades entre elles

Objectiu:

> reduir aquestes 4 variables a 2 components i representar els clients en un pla.

Això ens permetrà:

- veure grups
- detectar patrons
- preparar millor un clustering

---

# 11. Idea important: abans de PCA, escalar

Aquí cal insistir molt.

Si una variable està en valors grans i una altra en valors petits:

- la variable gran dominarà el resultat
- PCA quedarà distorsionat

Exemple:

- ingressos: entre 20.000 i 80.000
- freqüència de compra: entre 1 i 10

Si no escalem, ingressos pesarà molt més.

Per això, abans de PCA, normalment fem:

> **estandardització**

és a dir:

- mitjana 0
- desviació estàndard 1

---

# 12. Aplicació amb Python: primer contacte

Ara sí, passem a paquets.

## Dataset suggerit: wine

## Pas 1 — Carregar dades

```python
from sklearn.datasets import load_wine
import pandas as pd

data = load_wine()
X = pd.DataFrame(data.data, columns=data.feature_names)

X.head()
```

Pregunta a classe:

- quantes variables tenim?
- les podríem visualitzar totes alhora?

---

## Pas 2 — Escalar dades

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```

IMPORTANT!!!

> PCA quasi sempre s’ha d’aplicar sobre dades escalades.

---

## Pas 3 — Aplicar PCA a 2 components

```python
from sklearn.decomposition import PCA

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)
```

Interpretació:

- abans teníem moltes variables
- ara cada observació queda resumida en 2 components

---

## Pas 4 — Visualitzar

```python
import matplotlib.pyplot as plt

plt.scatter(X_pca[:, 0], X_pca[:, 1])
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.title("Projecció PCA en 2 dimensions")
plt.show()
```

Preguntes:

- es veuen agrupacions?
- els punts ocupen tot l’espai o segueixen una estructura?
- sembla una representació útil?

---

# 13. Variància explicada

Aquest és un concepte molt important.

```python
pca.explained_variance_ratio_
```

Això ens diu:

> quina proporció d’informació conserva cada component

Per exemple, si surt una cosa semblant a:

```python
[0.36, 0.19]
```

vol dir:

- PC1 conserva un 36% de la variància
- PC2 conserva un 19%
- entre tots dos conserven un 55%

Pregunta clau:

> amb 2 components en tenim prou o estem perdent massa informació?

---

## Extensió

També podem mirar la variància acumulada:

```python
import numpy as np

np.cumsum(pca.explained_variance_ratio_)
```

Això ajuda a decidir quants components ens convé conservar.

---

# 14. PCA i interpretació

Cal advertir una limitació important.

PCA és molt útil per:

- resumir dades
- visualitzar
- eliminar redundància
- preparar altres models

Però també té un cost:

- els nous eixos no són variables originals
- la interpretació és menys directa

Exemple:

- “edat” és fàcil d’entendre
- “PC1” ja no és una variable natural, és una combinació

---

# 15. PCA + clustering

Aquí connectem amb la sessió 2.

Idea:

> si reduïm dimensions, pot ser més fàcil veure patrons i aplicar clustering

Exemple:

```python
from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=3, random_state=42)
labels = kmeans.fit_predict(X_pca)

plt.scatter(X_pca[:, 0], X_pca[:, 1], c=labels)
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.title("KMeans sobre dades transformades amb PCA")
plt.show()
```

Pregunta:

- PCA ha ajudat a veure millor els possibles grups?

Missatge important:

> PCA no fa clustering, però pot ajudar-nos a preparar i visualitzar les dades.

