# Bloc 6 · Sessió 2  
## Entrenament i Arquitectures Bàsiques (MLP)

> **MLP** (*Multi-Layer Perceptron*, Perceptró Multicapa) és el nom tècnic del tipus de xarxa neuronal que construirem avui: diverses capes de neurones totalment connectades encadenades en seqüència. És l'arquitectura base del Deep Learning, i la que amaga darrere el terme `Dense` de Keras.

---

## Objectiu de la sessió

A la sessió anterior hem construït una neurona aïllada i hem vist com fa la **propagació cap endavant** (*forward pass*). Avui donem el salt definitiu: aprendrem com una xarxa sencera **s'equivoca i es corregeix sola**.

Al final de la sessió hauries de ser capaç de:
- entendre el cicle complet d'entrenament d'una xarxa neuronal,
- saber per a què serveix la funció de pèrdua (*loss function*) i com es calcula,
- tenir una intuïció del **Descens del Gradient** i la **Backpropagation**,
- construir, compilar i entrenar el teu primer model real amb **Keras / TensorFlow**,
- avaluar el model i representar les corbes d'entrenament.

---

## 1. La pregunta clau de la sessió

> Si una xarxa té milers de pesos, com sap quins ha d'ajustar i en quina direcció quan s'equivoca?

A la sessió anterior vam veure que la xarxa genera una predicció a partir de multiplicar entrades per pesos (*forward pass*). Però aquesta predicció serà dolenta si els pesos s'han inicialitzat aleatòriament. La clau és mesurar **quant de malament ho fa** i després **propagar l'error cap enrere** per ajustar cada pes.

---

## 2. La Funció de Pèrdua (*Loss Function*)

La **funció de pèrdua** mesura la diferència entre la predicció del model i el valor real. Com més gran és, pitjor ho ha fet el model. L'objectiu de l'entrenament és **minimitzar** aquest valor.

Depenent del tipus de problema:

| Problema | Funció de pèrdua habitual | Intuïció |
|---|---|---|
| **Regressió** | MSE — *Mean Squared Error* | Distància quadràtica entre predicció i real |
| **Classificació binària** | Binary Cross-Entropy | Penalitza prediccions molt segures però errònies |
| **Classificació multiclasse** | Categorical Cross-Entropy | Igual però per a $N$ classes |

### MSE (Fàcil per entendre-ho a mà)

$$\text{MSE} = \frac{1}{n} \sum_{i=1}^{n} (\hat{y}_i - y_i)^2$$

On $\hat{y}_i$ és la predicció i $y_i$ és el valor real.

---

## 3. Píndola matemàtica — La derivada com a brúixola

Imagina que estàs en una muntanya amb els ulls tancats i vols arribar al punt més baix (el mínim de l'error). Com ho fas?

Toques el terra amb el peu i notes si puja o baixa. Si puja cap a la dreta → t'has de moure cap a l'esquerra. Exactament això és la **derivada** aplicada a una funció d'error.

La **derivada** d'una funció en un punt ens diu:
- **El signe** → en quina direcció decreix la funció.
- **El valor absolut** → quant de pronunciada és la pendent (si és plana o molt inclinada).

Formalment, si la funció d'error és $L(w)$ respecte a un pes $w$:

$$\frac{\partial L}{\partial w} \approx \text{"si incremento } w \text{, l'error puja o baixa?"}$$

> **Regla pràctica:** Si la derivada és positiva → el pes és massa gran, l'hem de fer baixar. Si és negativa → l'hem de fer pujar.

---

## 4. Descens del Gradient (*Gradient Descent*)

L'algoritme que usa la derivada per actualitzar els pesos es diu **Descens del Gradient**. Actualitza cada pes amb la fórmula:

$$w_{\text{nou}} = w_{\text{antic}} - \eta \cdot \frac{\partial L}{\partial w}$$

On $\eta$ (eta) és la **taxa d'aprenentatge** (*learning rate*): un hiperparàmetre que controla la mida del "pas" que fem cuesta avall.

- **$\eta$ massa gran →** el model pot saltar per sobre del mínim i no convergir mai.
- **$\eta$ massa petit →** l'entrenament és molt lent i pot quedar-se en un mínim local.

L'optimitzador **Adam** (que farem servir avui) és una versió adaptativa d'aquest algoritme que ajusta la taxa d'aprenentatge automàticament per a cada pes.

---

## 5. Backpropagation — Com es propaga l'error

La **Backpropagation** (*Propagació cap enrere*) és l'algoritme que calcula $\frac{\partial L}{\partial w}$ per a **cada pes de la xarxa** de manera eficient.

Funciona en dues fases en cada pas d'entrenament:

1. **Forward pass:** Passa les dades de l'entrada fins a la sortida i calcula la predicció $\hat{y}$ i l'error $L$.
2. **Backward pass:** Desplaça l'error de la sortida cap a l'entrada. Gràcies a la **Regla de la cadena** (*chain rule*) del càlcul, Keras calcula la derivada de l'error respecte a cada pes de la xarxa automàticament.

Frameworks com Keras i PyTorch implementen la *Backpropagation* de forma completament automàtica. Tu **no has de derivar res a mà**.

---

## 6. El cicle complet d'entrenament: Epochs i Batch size

Cada vegada que el model veu **totes les dades d'entrenament** una vegada es diu una **Epoch**.

Però les xarxes no processen totes les dades d'una sola vegada (seria molt lent). En comptes d'això, divideixen les dades en **lots** (*batches*) i fan un pas de gradient per cada lot.

```
Per cada Epoch:
    Per cada Batch de dades:
        1. Forward pass: calcula prediccions i error (Loss)
        2. Backward pass: calcula els gradients (Backprop)
        3. Actualitza els pesos (Gradient Descent / Adam)
    Registra l'error mig de l'epoch
```

| Concepte | Definició | Exemple típic |
|---|---|---|
| **Epoch** | Una passada completa per tot el dataset | 50, 100 epochs |
| **Batch size** | Nombre de mostres per actualitzar pesos | 32, 64, 128 |

> Més epochs → el model aprèn més (fins que no pot millorar). Però massa epochs pot conduir a *overfitting* (tema de la Sessió 3).

---

## 7. Exercicis a mà

### Exercici 1 — Calcula l'error (MSE) manualment

Un model de regressió ha fet les següents prediccions:

| Mostra | Valor real ($y$) | Predicció ($\hat{y}$) |
|---|---|---|
| 1 | 10 | 12 |
| 2 | 20 | 18 |
| 3 | 30 | 31 |

**Tasques:**
1. Calcula l'error individual per a cada mostra: $(\hat{y}_i - y_i)^2$.
2. Calcula el MSE total (la mitjana dels tres).
3. Si un quart model hagués predit exactament $y_4 = 25$ quan el valor real és $25$, quant contribueix al MSE? Té sentit intuïtivament?

---

### Exercici 2 — Intuïció del Descens del Gradient

Un model té un sol pes $w = 3.0$ i la taxa d'aprenentatge és $\eta = 0.1$. En el pas d'entrenament actual, el càlcul de la backpropagation diu que la derivada de la pèrdua respecte al pes és $\frac{\partial L}{\partial w} = 5.0$.

**Tasques:**
1. Aplica la fórmula de l'actualització del pes: $w_\text{nou} = w_\text{antic} - \eta \cdot \frac{\partial L}{\partial w}$.
2. El nou pes ha pujat o ha baixat? Té sentit si la derivada és positiva (l'error puja quan $w$ puja)?
3. Repeteix el càlcul fent servir $\eta = 1.5$ (taxa massa gran). Quin és el valor de $w$ que obtens? Indica un potencial problema.

---

## 8. Exercicis d'ordinador

### Exercici 3 — El primer model Keras: classificació de varietats de vi

Usarem el dataset **Wine** de `sklearn`: 178 mostres de vi analitzades químicament amb 13 característiques (contingut d'alcohol, d'àcid màlic, de magnesi, de flavonoids, etc.), procedents de tres vinyes italianes. **Binaritzem** el problema: volem predir si el vi és de la **vinya A** (classe 0, considerada la de més prestigi) o de les **vinyes B/C** (classes 1 i 2 agrupades). Em recorda a classificadors que ja hem vist al Bloc 4!

**Configuració inicial (copia i executa-ho):**

```python
import numpy as np
import pandas as pd
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

import tensorflow as tf
from tensorflow import keras

# --- 1. Carreguem les dades ---
data = load_wine()
X = data.data
# Binaritzem: vinya A (classe 0) → y=1 | vinyes B/C (classes 1 i 2) → y=0
y = (data.target == 0).astype(int)

# --- 2. Dividim en train/test ---
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# --- 3. Normalitzem (molt important per a xarxes neuronals!) ---
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

print(f"Mida train: {X_train.shape}")
print(f"Mida test:  {X_test.shape}")
print(f"Nombre de característiques: {X_train.shape[1]}")
```

**Tasques:**
1. Executa el bloc anterior. Quantes mostres i característiques tenim per entrenar?
2. Per a quina raó és especialment important normalitzar les dades per a les xarxes neuronals? (Pensa en el que saps de la Sessió 1 sobre els pesos i la suma ponderada.)
3. Construeix el model seqüencial amb Keras seguint l'arquitectura indicada:

```python
# --- 4. Definim l'arquitectura del model ---
model = keras.Sequential([
    # Capa d'entrada + primera capa oculta
    keras.layers.Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    # Segona capa oculta
    keras.layers.Dense(32, activation='relu'),
    # Capa de sortida: 1 neurona + sigmoid = probabilitat binària
    keras.layers.Dense(1, activation='sigmoid')
])

# --- 5. Compilem el model (triem l'optimitzador i la funció de pèrdua) ---
model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

# Resum de l'arquitectura
model.summary()
```

4. Llegeix el resum que imprimeix `model.summary()`. Quants **paràmetres entrenables** (pesos i biaixos) té la primera capa densa? Comprova-ho a mà a partir del nombre d'entrades i neurones: $\text{params} = (\text{entrades} \times \text{neurones}) + \text{neurones}$ (els biaixos). Atenció: quantes entrades tenim en aquest dataset?

---

### Exercici 4 — Entrenem, avaluem i visualitzem

```python
import matplotlib.pyplot as plt

# --- 6. Entrenem ---
history = model.fit(
    X_train, y_train,
    epochs=50,
    batch_size=32,
    validation_split=0.2,   # 20% del train per validació
    verbose=1
)

# --- 7. Avaluació final sobre test ---
loss, accuracy = model.evaluate(X_test, y_test, verbose=0)
print(f"\nAccuracy en test: {accuracy:.4f}")
print(f"Loss en test:     {loss:.4f}")
```

**Tasques:**
1. Nota com l'accuracy puja i la loss baixa a mesura que avancen les epochs. En quin moment comença a estabilitzar-se?
2. Compara l'accuracy final del teu model neuronal amb els models del Bloc 4 (KNN, Decision Tree, Logistic Regression). El resultat et sorprèn, donades les dades que tenim?
3. Representa les corbes d'entrenament amb el codi següent i interpreta el gràfic:

```python
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))

# Corba de Loss
ax1.plot(history.history['loss'], label='train loss')
ax1.plot(history.history['val_loss'], label='val loss')
ax1.set_title('Funció de Pèrdua per Epoch')
ax1.set_xlabel('Epoch')
ax1.set_ylabel('Loss')
ax1.legend()

# Corba d'Accuracy
ax2.plot(history.history['accuracy'], label='train accuracy')
ax2.plot(history.history['val_accuracy'], label='val accuracy')
ax2.set_title('Accuracy per Epoch')
ax2.set_xlabel('Epoch')
ax2.set_ylabel('Accuracy')
ax2.legend()

plt.tight_layout()
plt.show()
```

4. **(Repte opcional)** Modifica l'arquitectura per afegir una tercera capa oculta de 16 neurones. Millora l'accuracy? Per què creus que hi ha o no hi ha diferència?

---

## 9. Idees clau de la sessió

- Una xarxa neuronal aprèn calculant **quant s'equivoca** (*loss function*) i ajustant els pesos en la direcció que minimitza l'error (*gradient descent*).
- La **Backpropagation** usa la regla de la cadena per calcular el gradient de l'error respecte a cada pes de forma eficient. Keras ho fa automàticament.
- L'**epoch** és una iteració sobre tot el dataset; el **batch size** controla quantes mostres es processen abans de cada actualització de pesos.
- Per construir un model a Keras: `Sequential` → afegir capes `Dense` → `compile` amb optimitzador i loss → `fit`.
- La **normalització** de les dades és clau: si les entrades estan en escales molt diferents, el gradient descent no convergeix bé.
- A la sessió 3 veurem com interpretar i diagnosticar les corbes d'entrenament per detectar *overfitting*.
