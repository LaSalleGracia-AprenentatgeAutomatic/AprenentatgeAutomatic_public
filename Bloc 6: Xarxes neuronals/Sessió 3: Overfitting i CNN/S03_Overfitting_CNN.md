# Bloc 6 · Sessió 3  
## Overfitting i Xarxes Convolucionals (CNN)

> Aquesta sessió té dues parts encadenades. Primer diagnosticarem el problema més comú en Deep Learning (*overfitting*) i aprendrem dues eines per combatre'l. Després saltarem directament a la pràctica: construir el nostre primer classificador d'imatges amb una **Xarxa Convolucional (CNN)**.

---

## Objectiu de la sessió

A la Sessió 2 vas entrenar un MLP i vas veure que la `loss` baixava cada epoch. Però sovint el model aprèn massa bé les dades d'entrenament i deixa de funcionar amb dades noves: això és *l'overfitting*. Avui aprendràs a detectar-lo, mitigar-lo i, sobretot, construir el primer model pensat específicament per a imatges.

Al final de la sessió hauries de ser capaç de:
- identificar l'**overfitting** i l'**underfitting** a partir de les corbes d'entrenament,
- aplicar **`Dropout`** i **`EarlyStopping`** per millorar la generalització,
- entendre per què un MLP no escala bé per a imatges,
- comprendre els conceptes de **convolució** i **pooling**,
- construir i entrenar una **CNN** sobre el dataset Fashion MNIST.

---

## 1. El problema: memoritzar no és aprendre

A la Sessió 2 vas veure que la `loss` baixava cada epoch sobre el dataset de vins amb les 142 mostres netes. Ara reprenem **exactament el mateix model** (`Dense(64) → Dense(32) → Dense(1)`), però l'entrenem sobre només **50 mostres amb un 15% d'etiquetes invertides** (soroll). Aquest és el patró que veuràs al BLOC 0 del notebook:

```
train loss  ──────────────────────╲ (continua baixant fins a 0)
val loss    ──────────╲ (arriba a un mínim i torna a pujar)
```

Quan les dues línies es separen d'aquesta manera —això és el que anomenem la **"tisora"**— el model ha entrat en **overfitting**: ha memoritzat les dades d'entrenament (fins als sorolls i les excepcions) i ha perdut la capacitat de generalitzar a dades noves.

L'analogia: un estudiant que memoritza les respostes exactes dels exàmens passats però no entén el concepte. En un examen nou, falla.

| Situació | `train loss` | `val loss` | Diagnòstic |
|---|---|---|---|
| Model massa simple | Alta | Alta | **Underfitting** — cal més capacitat |
| Equilibri | Baixa | Baixa (similar) | **Bon model** |
| Model massa complex | Molt baixa | Puja | **Overfitting** — cal regularitzar |

---

Al **BLOC A** del notebook, afegim `Dropout` al mateix model i el deixem entrenar els mateixos 200 epochs: la tisora es redueix. Al **BLOC B** afegim a sobre `EarlyStopping`, que para l'entrenament automàticament quan ja no millora.

---

## 2. Solució 1 — Dropout

**`Dropout(p)`** apaga aleatòriament una fracció `p` de neurones durant cada pas d'entrenament. A cada batch, un subconjunt diferent de neurones s'apaga.

Per què funciona? El model no pot dependre de cap neurona concreta per memoritzar un patró. S'obliga a aprendre representacions més robustes i distribuïdes.

```python
keras.layers.Dense(64, activation='relu'),
keras.layers.Dropout(0.3),   # apaga el 30% de les neurones aleatòriament
keras.layers.Dense(32, activation='relu'),
```

> Durant la **inferència** (predicció), el Dropout s'apaga automàticament: totes les neurones participen. Keras ho gestiona sol.

Valors habituals: entre `0.2` i `0.5`. Un Dropout massa alt perjudica l'aprenentatge.

---

## 3. Solució 2 — EarlyStopping

**`EarlyStopping`** és un *callback*: un mecanisme que monitoritza una mètrica durant l'entrenament i para automàticament quan deixa de millorar.

```python
from keras.callbacks import EarlyStopping

early_stop = EarlyStopping(
    monitor='val_loss',          # observa la pèrdua de validació
    patience=5,                  # espera 5 epochs sense millora abans de parar
    restore_best_weights=True    # recupera els pesos del millor epoch
)

model.fit(
    X_train, y_train,
    epochs=200,                  # màxim teòric alt — EarlyStopping pararà abans
    callbacks=[early_stop]
)
```

`patience=5` vol dir: "si en 5 epochs consecutives la `val_loss` no millora, para i recupera els pesos del millor moment."

---

## 4. Exercicis a mà

### Exercici 1 — Diagnosticar tres models a partir de les corbes

Tens tres models entrenats sobre el mateix dataset. Les corbes finals són aproximadament així (valors al final de l'entrenament, després de 50 epochs):

| Model | `train loss` | `val loss` | Arquitectura |
|---|---|---|---|
| **A** | 0.85 | 0.88 | `Dense(8) → Dense(1)` |
| **B** | 0.12 | 0.18 | `Dense(64) → Dense(32) → Dense(1)` |
| **C** | 0.01 | 0.95 | `Dense(512) → Dense(256) → Dense(128) → Dense(64) → Dense(1)` |

**Tasques:**
1. Diagnostica cada model: **underfitting**, **bon equilibri** o **overfitting**. Justifica-ho mirant la relació entre `train loss` i `val loss`.
2. Dibuixa (a mà, en paper o tauleta) com creus que serien les dues corbes (`train loss` i `val loss` al llarg de les epochs) per al model **C**. Marca el punt on l'`EarlyStopping` amb `patience=5` hauria parat l'entrenament.
3. El model **C** té massa capacitat per a aquest problema. Proposa **dues modificacions** concretes per evitar l'overfitting sense canviar l'optimitzador ni la `loss`. (Pista: una de les dues hauria de ser un `Dropout`.)

---

## 5. Per què un MLP no serveix per a imatges?

Una imatge en escala de grisos de 28×28 píxels, aplanada, dona $28 \times 28 = 784$ entrades. Manejable. Però una imatge de resolució normal, per exemple 224×224 en color (RGB), té:

$$224 \times 224 \times 3 = 150.528 \text{ entrades}$$

Amb una sola capa `Dense(512)` això generaria $150.528 \times 512 = 77.070.336$ paràmetres. Impossible d'entrenar de manera eficient.

A més, **aplanar una imatge destrueix la informació espacial**: un píxel té una relació directa amb els seus veïns (formen vores, textures, formes). Un MLP no sap que el píxel a la posició 100 és veí del 101.

---

## 6. La convolució: detectar patrons locals

Un **filtre** (o *kernel*) és una petita matriu numèrica, per exemple de 3×3, que llisca per tota la imatge. En cada posició, multiplica element a element i suma el resultat: això és la **convolució**.

```
Imatge (fragment):    Filtre (detecta vores):    Resultat:
 1  0  1              -1 -1 -1
 0  1  0      →        0  0  0       →    valor alt = "hi ha vora aquí"
 1  0  1               1  1  1
```

Cada filtre aprèn a detectar un tipus de patró: vores horitzontals, vores verticals, textures, colors, etc. Les primeres capes detecten patrons simples; les capes més profundes combinen patrons simples en formes complexes.

**La clau:** el mateix filtre (matriu de 9 pesos) s'aplica a tota la imatge. Molt menys paràmetres que un MLP.

---

## 7. MaxPooling: reduir sense perdre el que importa

Després de detectar patrons amb una `Conv2D`, la **`MaxPooling2D`** redueix la resolució espacial conservant el patró més fort de cada zona.

```
Zona de 2×2:    MaxPool(2×2):
 3   1              
 2   4      →      4    (el valor màxim)
```

Efectes:
- Redueix la mida de les capes → menys paràmetres.
- Dóna cert grau d'invariança a la traducció (el patró es detecta si es desplaça lleugerament).

---

## 8. Arquitectura CNN bàsica

El patró típic és: **Extracció de característiques** (Conv + Pool repetit) seguida de **Classificació** (MLP dens al final).

```
Input: imatge 28×28×1 (escala de grisos)
  ↓
Conv2D(32 filtres, 3×3) + ReLU   → 32 mapes de característiques 26×26
  ↓
MaxPooling2D(2×2)                → 32 mapes 13×13
  ↓
Conv2D(64 filtres, 3×3) + ReLU   → 64 mapes 11×11
  ↓
MaxPooling2D(2×2)                → 64 mapes 5×5
  ↓
Flatten                          → vector de 64×5×5 = 1600 valors
  ↓
Dense(64) + ReLU                 → MLP final (classificació)
  ↓
Dense(10) + Softmax              → probabilitats de 10 classes
```

La capa `Softmax` és l'equivalent multiclasse de la `Sigmoid`: retorna 10 probabilitats que sumen 1, una per a cada classe.

---

## 9. Exercicis d'ordinador

Treballarem amb el dataset **Fashion MNIST**: 70.000 imatges en escala de grisos de 28×28, cadascuna etiquetada amb una de 10 categories de roba.

| Etiqueta | Categoria | Etiqueta | Categoria |
|---|---|---|---|
| 0 | T-shirt/top | 5 | Sandàlia |
| 1 | Pantalons | 6 | Camisa |
| 2 | Jersei | 7 | Sabatilla |
| 3 | Vestit | 8 | Bossa |
| 4 | Abric | 9 | Botí |

### Exercici 2 — Càrrega i exploració del dataset

```python
import numpy as np
import matplotlib.pyplot as plt
import keras
from keras import layers
from keras.callbacks import EarlyStopping

# --- 1. Carreguem el dataset ---
(X_train, y_train), (X_test, y_test) = keras.datasets.fashion_mnist.load_data()

print(f"Train: {X_train.shape}  |  Test: {X_test.shape}")

# --- 2. Visualitzem algunes mostres ---
fig, axes = plt.subplots(2, 5, figsize=(12, 5))
class_names = ['T-shirt', 'Pantalons', 'Jersei', 'Vestit', 'Abric',
               'Sandàlia', 'Camisa', 'Sabatilla', 'Bossa', 'Botí']
for i, ax in enumerate(axes.flat):
    ax.imshow(X_train[i], cmap='gray')
    ax.set_title(class_names[y_train[i]])
    ax.axis('off')
plt.tight_layout()
plt.show()
```

**Tasques:**
1. Executa el bloc. Quina forma (`shape`) tenen les imatges? Quantes mostres té el conjunt d'entrenament i quantes el de test?
2. Per quina raó **no** normalitzem amb `StandardScaler` com a la S2, sinó dividint per `255.0`? (Pensa en el rang de valors d'un píxel.)
3. Mira les 10 mostres visualitzades. Quines categories creus que seran més fàcils de confondre per a un model? Per què?

---

### Exercici 3 — Construir i entrenar la CNN

```python
# --- 3. Normalitzem els píxels a [0, 1] ---
X_train = X_train / 255.0
X_test  = X_test  / 255.0

# --- 4. Afegim la dimensió del canal (escala de grisos = 1) ---
X_train = X_train.reshape(-1, 28, 28, 1)
X_test  = X_test.reshape(-1, 28, 28, 1)

# --- 5. Construïm la CNN ---
model = keras.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    layers.MaxPooling2D((2, 2)),
    layers.Dropout(0.25),

    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Dropout(0.25),

    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dropout(0.5),
    layers.Dense(10, activation='softmax')
])

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

model.summary()

# --- 6. EarlyStopping ---
early_stop = EarlyStopping(
    monitor='val_loss',
    patience=5,
    restore_best_weights=True
)

# --- 7. Entrenem ---
history = model.fit(
    X_train, y_train,
    epochs=30,
    batch_size=64,
    validation_split=0.1,
    callbacks=[early_stop],
    verbose=1
)

# --- 8. Avaluem ---
loss, accuracy = model.evaluate(X_test, y_test, verbose=0)
print(f"\nAccuracy en test: {accuracy:.4f}")
```

**Tasques:**
1. Mira el `model.summary()`. Compara el nombre total de paràmetres entrenables amb el que tindria un MLP equivalent (per exemple `Dense(64) → Dense(64) → Dense(10)` aplicat sobre l'entrada aplanada de 784 valors). Quina arquitectura té més paràmetres?
2. En quina epoch ha parat l'`EarlyStopping`? Coincideix amb el punt on les corbes s'estabilitzen?
3. Quina accuracy obtens al test? Quina creus que seria una baseline raonable (predicció aleatòria sobre 10 classes)?

---

### Exercici 4 — Diagnosticar el resultat

```python
# --- 9. Corbes d'entrenament ---
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))

ax1.plot(history.history['loss'], label='train loss')
ax1.plot(history.history['val_loss'], label='val loss')
ax1.set_title('Funció de Pèrdua per Epoch')
ax1.set_xlabel('Epoch'); ax1.set_ylabel('Loss'); ax1.legend()

ax2.plot(history.history['accuracy'], label='train accuracy')
ax2.plot(history.history['val_accuracy'], label='val accuracy')
ax2.set_title('Accuracy per Epoch')
ax2.set_xlabel('Epoch'); ax2.set_ylabel('Accuracy'); ax2.legend()

plt.tight_layout()
plt.show()

# --- 10. Prediccions visuals ---
predictions = model.predict(X_test[:10])
predicted_labels = np.argmax(predictions, axis=1)

fig, axes = plt.subplots(2, 5, figsize=(12, 5))
for i, ax in enumerate(axes.flat):
    ax.imshow(X_test[i].reshape(28, 28), cmap='gray')
    color = 'green' if predicted_labels[i] == y_test[i] else 'red'
    ax.set_title(f"Pred: {class_names[predicted_labels[i]]}\nReal: {class_names[y_test[i]]}", color=color)
    ax.axis('off')
plt.tight_layout()
plt.show()
```

**Tasques:**
1. Analitza les corbes. Les línies de `train` i `val` estan juntes o separades? Hi ha signes d'overfitting? Recorda el diagnòstic que vas fer a l'Exercici 1.
2. Mira les 10 prediccions visuals. Quines categories ha confós el model? Es corresponen amb les que vas predir a l'Exercici 2 · Tasca 3?
3. **(Repte opcional)** Elimina **totes** les capes `Dropout` del model i torna a entrenar amb 30 epochs sense `EarlyStopping`. Compara les corbes amb les anteriors. Veus ara la separació entre `train` i `val loss`?

---

## 10. Idees clau de la sessió

- **Overfitting** = la `val_loss` puja mentre la `train_loss` segueix baixant. El model ha memoritzat en comptes d'aprendre.
- **`Dropout`** apaga neurones aleatòriament durant l'entrenament, obligant la xarxa a aprendre representacions robustes.
- **`EarlyStopping`** para l'entrenament quan la validació deixa de millorar, recuperant automàticament el millor model.
- Les **CNN** resolen els dos problemes del MLP per a imatges: eficiència de paràmetres (filtres reutilitzables) i preservació de l'estructura espacial.
- Patró CNN: `Conv2D` + `MaxPooling2D` repetit → `Flatten` → `Dense` → sortida.
- **`sparse_categorical_crossentropy`** s'usa quan les etiquetes són enters (0–9); **`categorical_crossentropy`** quan estan en format *one-hot*.
