# Bloc 5 · Sessió 1  
## Descobrint patrons a les dades — Clustering i K-Means

---

## Objectiu de la sessió

En aquesta sessió descobriràs com podem trobar **estructura i patrons en dades sense etiquetes**, i aprendràs com funciona l'algoritme de clustering més popular: **K-Means**.

Al final de la sessió hauries de ser capaç de:
- explicar la diferència entre aprenentatge supervisat i no supervisat,
- entendre el concepte de **clustering** i **similitud**,
- calcular la distància euclidiana entre dos punts,
- calcular la mitjana d'un conjunt de vectors,
- aplicar K-Means a mà per entendre com funciona l'algoritme,
- implementar K-Means amb Python i visualitzar els resultats.

---

## 1. Aprenentatge supervisat vs no supervisat

Fins ara hem treballat amb **aprenentatge supervisat**: sabíem la resposta correcta per a cada exemple d'entrenament (una etiqueta, un valor numèric).

En **aprenentatge no supervisat**:
- no tenim etiquetes,
- no hi ha una resposta correcta,
- l'objectiu és **descobrir estructura o patrons** en les dades.

### Pregunta clau

> Si tenim dades però **no tenim etiquetes**, què podem fer?

### Exemples reals d'aprenentatge no supervisat

| Problema | Dades | Resultat esperat |
|----------|-------|-----------------|
| Segmentació de clients | Historial de compres | Grups de clients similars |
| Agrupació de notícies | Text d'articles | Temes recurrents |
| Anàlisi genètica | Perfils d'expressió gènica | Grups de gens relacionats |
| Sistemes de recomanació | Patrons d'escolta o visualització | Perfils similars d'usuari |

---

## 2. Clustering: la idea principal

**Clustering** és el procés d'agrupar dades de tal manera que:
- les dades del **mateix grup (cluster) siguin similars entre si**,
- les dades de **grups diferents siguin poc similars**.

### Conceptes clau

- **patró**: regularitat o tendència que es repeteix en les dades
- **similitud**: mesura de com s'assemblen dues dades
- **distància**: mesura de com de lluny estan dues dades
- **cluster**: grup de dades similars

> El clustering no és únic. Depèn de com mesurem la similitud i de quants grups volem trobar.

---

## 3. Píndola matemàtica — Distància euclidiana

Per decidir si dues dades s'assemblen, necessitem una **mesura de distància**.

La més habitual és la **distància euclidiana**, que és simplement la distància en línia recta entre dos punts.

### En 2 dimensions

Donats dos punts $A = (x_1, y_1)$ i $B = (x_2, y_2)$:

$$d(A, B) = \sqrt{(x_1 - x_2)^2 + (y_1 - y_2)^2}$$

### En n dimensions

Per a vectors de qualsevol dimensió:

$$d(\mathbf{a}, \mathbf{b}) = \sqrt{\sum_{i=1}^{n} (a_i - b_i)^2}$$

### Interpretació

- distància **petita** → punts **semblants**
- distància **gran** → punts **diferents**

### Exemple resolt

Punt A: (1, 2)  
Punt B: (4, 6)

$$d(A, B) = \sqrt{(1-4)^2 + (2-6)^2} = \sqrt{9 + 16} = \sqrt{25} = 5$$

---

## 4. Píndola matemàtica — Mitjana de vectors (centroide)

K-Means treballa amb **centroides**, que són els centres de cada cluster.

El centroide d'un conjunt de punts és simplement la seva **mitjana**:

$$\mathbf{c} = \frac{1}{N} \sum_{i=1}^{N} \mathbf{x}_i$$

On $N$ és el nombre de punts i $\mathbf{x}_i$ és cada punt.

### Exemple resolt

Donat el conjunt de punts: (1, 2), (3, 4), (5, 6)

$$c_x = \frac{1 + 3 + 5}{3} = 3 \qquad c_y = \frac{2 + 4 + 6}{3} = 4$$

$$\mathbf{c} = (3, 4)$$

> El centroide és el "punt central" del grup. K-Means el fa servir per representar cada cluster.

---

## 5. L'algoritme K-Means

**K-Means** és l'algoritme de clustering més senzill i popular.

### Idea fonamental

> K-Means assigna cada punt al seu centre més proper i actualitza els centres fins que tot s'estabilitza.

### Passos de l'algoritme

1. **Triar k**: decidir quants clusters volem.
2. **Inicialitzar centres**: col·locar k centres de manera aleatòria.
3. **Assignar punts**: assignar cada punt al centre més proper (mínima distància euclidiana).
4. **Recalcular centres**: el nou centre de cada cluster és la mitjana de tots els seus punts.
5. **Repetir** els passos 3 i 4 fins que els centres no canvien (convergència).

### Conceptes importants

- **k**: nombre de clusters (cal especificar-lo nosaltres)
- **inèrcia**: suma de les distàncies quadràtiques de cada punt al seu centroide (volem minimitzar-la)
- **convergència**: l'algoritme s'atura quan els centres deixen de moure's

---

## 6. K-Means a mà: entendre l'algoritme

Aplicarem K-Means manualment per entendre els passos.

### Dataset

| Punt | X | Y |
|------|---|---|
| A | 1 | 1 |
| B | 1 | 2 |
| C | 2 | 1 |
| D | 8 | 8 |
| E | 8 | 9 |
| F | 9 | 8 |

### Pas 1: Triar k = 2 i inicialitzar centres

Suposem que els centres inicials son:

- $C_1 = (1, 1)$ — el punt A
- $C_2 = (8, 8)$ — el punt D

### Pas 2: Assignar cada punt al centre més proper

Calculem la distància de cada punt als dos centres:

| Punt | d(punt, C₁) | d(punt, C₂) | Cluster assignat |
|------|-------------|-------------|-----------------|
| A (1,1) | 0.0 | 9.90 | C₁ |
| B (1,2) | 1.0 | 9.22 | C₁ |
| C (2,1) | 1.0 | 9.22 | C₁ |
| D (8,8) | 9.90 | 0.00 | C₂ |
| E (8,9) | 10.63 | 1.00 | C₂ |
| F (9,8) | 10.63 | 1.00 | C₂ |

### Pas 3: Recalcular els centres

Cluster 1 conté: A(1,1), B(1,2), C(2,1)

$$C_1 = \left(\frac{1+1+2}{3}, \frac{1+2+1}{3}\right) = \left(\frac{4}{3}, \frac{4}{3}\right) \approx (1.33, 1.33)$$

Cluster 2 conté: D(8,8), E(8,9), F(9,8)

$$C_2 = \left(\frac{8+8+9}{3}, \frac{8+9+8}{3}\right) = \left(\frac{25}{3}, \frac{25}{3}\right) \approx (8.33, 8.33)$$

### Pas 4: Repetir

Tornant a assignar amb els nous centres, l'assignació no canvia → **convergència**.

> En dades ben separades com aquestes, K-Means converge ràpidament.

---

## 7. Exercicis a mà

### Exercici 1 — Calcular distàncies

Donats els punts:
- P1 = (3, 4)
- P2 = (6, 8)
- P3 = (1, 1)

**Tasques:**
1. Calcula la distància euclidiana entre P1 i P2.
2. Calcula la distància euclidiana entre P1 i P3.
3. Quin dels dos punts (P2 o P3) és més proper a P1?

---

### Exercici 2 — Centroide

Donats tres punts:
- A = (2, 4)
- B = (6, 2)
- C = (4, 8)

**Tasques:**
1. Calcula el centroide del conjunt de punts.
2. Dibuixa els tres punts i el centroide en un eix de coordenades.

---

### Exercici 3 — K-Means a mà (k = 2)

Donat el dataset:

| Punt | X | Y |
|------|---|---|
| A | 2 | 3 |
| B | 3 | 3 |
| C | 4 | 3 |
| D | 10 | 8 |
| E | 11 | 8 |
| F | 12 | 9 |

**Centres inicials:** $C_1 = (2, 3)$ i $C_2 = (12, 9)$

**Tasques:**
1. Assigna cada punt al centre més proper calculant les distàncies.
2. Recalcula els nous centroides de cada cluster.
3. Comprova si els punts canvien d'assignació amb els nous centres.
4. Quants punts té cada cluster al final?

---

### Exercici 4 — Reflexió conceptual

Respon raonant breument:

1. Si tenim dades d'alumnes (hores d'estudi, nota del curs), podries aplicar clustering? Quins grups podrien aparèixer?
2. Quin problema pot tenir K-Means si triem un valor de k molt gran?
3. Per quina raó l'escala de les variables pot afectar el resultat del clustering?

---

## 8. Exercicis amb Python

### Exercici 5 — Visualitzar clusters sintètics amb `make_blobs`

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs

# Generar dades sintètiques amb 3 clusters
X, y_real = make_blobs(n_samples=150, centers=3, cluster_std=0.8, random_state=42)

# Visualitzar
plt.figure(figsize=(6, 5))
plt.scatter(X[:, 0], X[:, 1], alpha=0.6, edgecolors='k', s=60)
plt.title("Dataset sintètic (sense etiquetes)")
plt.xlabel("Variable 1")
plt.ylabel("Variable 2")
plt.tight_layout()
plt.show()
```

**Tasques:**
1. Executa el codi i observa el scatter plot.
2. A ull, quants grups distincts veus?
3. Prova a canviar `centers=3` per `centers=4` o `centers=2`. Quin canvi observes?

---

### Exercici 6 — Aplicar K-Means amb scikit-learn

```python
from sklearn.cluster import KMeans

# Aplicar K-Means amb k=3
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X)

# Etiquetes assignades a cada punt
etiquetes = kmeans.labels_

# Centres dels clusters
centres = kmeans.cluster_centers_

# Visualitzar
plt.figure(figsize=(6, 5))
plt.scatter(X[:, 0], X[:, 1], c=etiquetes, cmap='viridis', alpha=0.6, edgecolors='k', s=60)
plt.scatter(centres[:, 0], centres[:, 1], c='red', marker='X', s=200, label='Centroides')
plt.title("K-Means amb k=3")
plt.xlabel("Variable 1")
plt.ylabel("Variable 2")
plt.legend()
plt.tight_layout()
plt.show()
```

**Tasques:**
1. Executa el codi. Els clusters que ha trobat K-Means coincideixen amb els que havies identificat visualment?
2. Modifica el codi per provar amb `n_clusters=2` i `n_clusters=4`. Quin valor de k sembla millor per a aquestes dades?
3. Consulta el valor de la inèrcia amb `kmeans.inertia_`. Quin valor obteràs amb k=2, k=3 i k=4?

---

### Exercici 7 — Implementar K-Means sense scikit-learn

L'objectiu és implementar K-Means pas a pas per entendre com funciona per dins.

```python
import numpy as np

def distancia_euclidiana(a, b):
    """Calcula la distància euclidiana entre dos vectors."""
    return np.sqrt(np.sum((a - b) ** 2))

def assignar_clusters(X, centres):
    """Assigna cada punt al centre més proper."""
    etiquetes = []
    for punt in X:
        distancies = [distancia_euclidiana(punt, c) for c in centres]
        etiquetes.append(np.argmin(distancies))
    return np.array(etiquetes)

def recalcular_centres(X, etiquetes, k):
    """Calcula el nou centroide de cada cluster."""
    nous_centres = []
    for i in range(k):
        punts_cluster = X[etiquetes == i]
        nous_centres.append(punts_cluster.mean(axis=0))
    return np.array(nous_centres)

def kmeans_manual(X, k, max_iter=100, random_state=42):
    """Implementació manual de K-Means."""
    np.random.seed(random_state)
    # Inicialitzar centres aleatòriament
    idx = np.random.choice(len(X), k, replace=False)
    centres = X[idx]

    for iteracio in range(max_iter):
        etiquetes = assignar_clusters(X, centres)
        nous_centres = recalcular_centres(X, etiquetes, k)

        # Comprovar convergència
        if np.allclose(centres, nous_centres):
            print(f"Convergència assolida a la iteració {iteracio + 1}")
            break
        centres = nous_centres

    return etiquetes, centres

# Provar amb les dades sintètiques
etiquetes_manual, centres_manual = kmeans_manual(X, k=3)

# Visualitzar
plt.figure(figsize=(6, 5))
plt.scatter(X[:, 0], X[:, 1], c=etiquetes_manual, cmap='plasma', alpha=0.6, edgecolors='k', s=60)
plt.scatter(centres_manual[:, 0], centres_manual[:, 1], c='red', marker='X', s=200, label='Centroides')
plt.title("K-Means manual amb k=3")
plt.xlabel("Variable 1")
plt.ylabel("Variable 2")
plt.legend()
plt.tight_layout()
plt.show()
```

**Tasques:**
1. Executa el codi i comprova que el resultat és similar al de scikit-learn.
2. Modifica la funció `distancia_euclidiana` per imprimir el valor calculat a cada crida. Quantes vegades es calcula durant la primera iteració?
3. Afegeix un `print` per mostrar els centres en cada iteració i observa com convergeixen.

---

## 9. Idees clau de la sessió

- L'aprenentatge **no supervisat** troba patrons en dades sense etiquetes.
- El **clustering** agrupa dades similars; la **distància** mesura la similitud.
- La **distància euclidiana** és la mesura de similitud més habitual.
- El **centroide** és el punt central d'un cluster, calculat com la mitjana dels seus punts.
- **K-Means** assigna cada punt al centre més proper i recalcula els centres iterativament.
- Cal especificar **k** (el nombre de clusters) a priori.
- L'**escala de les variables** importa: sense normalització, variables amb rangs grans poden dominar la distància.

A la sessió 2 aprendrem a **escollir el valor de k** amb el mètode del colze i a **avaluar la qualitat** dels clusters amb el Silhouette Score.
