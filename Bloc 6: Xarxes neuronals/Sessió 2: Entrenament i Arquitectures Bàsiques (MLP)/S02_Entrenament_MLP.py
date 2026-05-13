# =============================================================================
# Bloc 6 · Sessió 2 — Entrenament i Arquitectures Bàsiques (MLP)
# =============================================================================
# Executa les seccions en ordre. Cada bloc correspon als exercicis del material.

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import keras

print(f"Keras {keras.__version__}  (backend: {keras.backend.backend()})")

# =============================================================================
# EXERCICI 3 — Primer model Keras: classificació de varietats de vi
# =============================================================================

# --- 1. Carreguem les dades ---
data = load_wine()
X = data.data
# Binaritzem: vinya A (classe 0) → y=1 | vinyes B/C (classes 1 i 2) → y=0
y = (data.target == 0).astype(int)

# --- 2. Dividim en train/test ---
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# --- 3. Normalitzem ---
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test  = scaler.transform(X_test)

print(f"Mida train: {X_train.shape}")
print(f"Mida test:  {X_test.shape}")
print(f"Nombre de característiques: {X_train.shape[1]}")

# --- 4. Definim l'arquitectura ---
model = keras.Sequential([
    keras.layers.Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    keras.layers.Dense(32, activation='relu'),
    keras.layers.Dense(1, activation='sigmoid')
])

model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

model.summary()

# Tasca 4: paràmetres de la primera capa
# params = (entrades × neurones) + neurones(biaixos)
# = (13 × 64) + 64 = 832 + 64 = 896
print(f"\nParàmetres capa 1 (manual): {X_train.shape[1] * 64 + 64}")

# =============================================================================
# EXERCICI 4 — Entrenem, avaluem i visualitzem
# =============================================================================

# --- 5. Entrenem ---
history = model.fit(
    X_train, y_train,
    epochs=50,
    batch_size=32,
    validation_split=0.2,
    verbose=1
)

# --- 6. Avaluació final ---
loss, accuracy = model.evaluate(X_test, y_test, verbose=0)
print(f"\nAccuracy en test: {accuracy:.4f}")
print(f"Loss en test:     {loss:.4f}")

# --- 7. Corbes d'entrenament ---
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
fig.suptitle("S02 — MLP sobre Wine dataset", fontweight='bold')

ax1.plot(history.history['loss'],     label='train loss')
ax1.plot(history.history['val_loss'], label='val loss')
ax1.set_title('Funció de Pèrdua per Epoch')
ax1.set_xlabel('Epoch')
ax1.set_ylabel('Loss')
ax1.legend()

ax2.plot(history.history['accuracy'],     label='train accuracy')
ax2.plot(history.history['val_accuracy'], label='val accuracy')
ax2.set_title('Accuracy per Epoch')
ax2.set_xlabel('Epoch')
ax2.set_ylabel('Accuracy')
ax2.legend()

plt.tight_layout()
plt.savefig('S02_corbes_entrenament.png', dpi=120)
plt.show()
print("Gràfic guardat com S02_corbes_entrenament.png")

# =============================================================================
# EXERCICI 4 · Repte opcional — Tercera capa oculta
# =============================================================================

model_deeper = keras.Sequential([
    keras.layers.Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    keras.layers.Dense(32, activation='relu'),
    keras.layers.Dense(16, activation='relu'),
    keras.layers.Dense(1,  activation='sigmoid')
])
model_deeper.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
history_deeper = model_deeper.fit(
    X_train, y_train, epochs=50, batch_size=32, validation_split=0.2, verbose=0
)
loss_d, acc_d = model_deeper.evaluate(X_test, y_test, verbose=0)
print(f"\nModel amb 3 capes ocultes — Accuracy: {acc_d:.4f}")
print("Diferència respecte al model de 2 capes:", round(acc_d - accuracy, 4))
