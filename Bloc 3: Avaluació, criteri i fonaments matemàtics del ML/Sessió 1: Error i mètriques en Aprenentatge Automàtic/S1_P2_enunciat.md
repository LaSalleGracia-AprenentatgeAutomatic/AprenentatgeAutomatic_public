# Pràctica 2 — Tipus d’error, matriu de confusió i mètriques

## Context
En la pràctica anterior has après a calcular l’error global d’un model. Ara veurem que, en problemes de **classificació**, no tots els errors tenen el mateix impacte i que cal distingir **tipus d’error**.

L’objectiu d’aquesta pràctica és entendre:
- com es classifiquen els errors d’un model
- com es construeix una matriu de confusió
- com es calculen i s’interpreten les mètriques bàsiques


---

## Part 1 — Treball a mà
### Problema
Sistema de detecció de correu brossa.

- Positiu: el correu és *spam*
- Negatiu: el correu *no* és spam

### Dades

| Correu | Realitat | Predicció |
|-------|----------|-----------|
| 1 | Spam | Spam |
| 2 | No spam | Spam |
| 3 | Spam | No spam |
| 4 | No spam | No spam |

---

### Tasques

#### 1. Classificació dels errors
Per a cada correu, indica si el resultat és:
- TP (veritable positiu)
- FP (fals positiu)
- FN (fals negatiu)
- TN (veritable negatiu)

---

#### 2. Matriu de confusió
Construeix la matriu de confusió corresponent en format 2×2.

---

#### 3. Càlcul de mètriques
Calcula manualment les mètriques següents:
# Taula comparativa de mètriques de classificació
# Taula comparativa de mètriques de classificació

| Mètrica   | Càlcul | Què mesura | Error que controla | Quan és important |
|----------|--------|------------|--------------------|-------------------|
| Accuracy | (TP + TN) / Total | Percentatge total de prediccions correctes | Errors en general | Quan les classes estan equilibrades i tots els errors tenen un impacte similar |
| Precision | TP / (TP + FP) | De tots els positius predits, quants són realment positius | Falsos positius (FP) | Quan és important no marcar com a positiu allò que no ho és (ex.: correu spam, bloqueig de clients legítims) |
| Recall | TP / (TP + FN) | De tots els positius reals, quants són detectats pel model | Falsos negatius (FN) | Quan és important no deixar escapar positius reals (ex.: detecció de frau, diagnòstic mèdic) |

---

### Pregunta de reflexió
Quin tipus d’error consideres més greu en aquest problema? Per què?

---

## Part 2 — Treball amb Python i sklearn

### Problema
Sistema de detecció de frau bancari.

- Positiu: operació fraudulenta
- Negatiu: operació legítima

### Dades

```python
y_true = [1, 0, 1, 0, 1, 0, 0, 1, 0, 0]
y_pred = [1, 0, 0, 0, 1, 1, 0, 1, 0, 0]
```

Tasques
1. Matriu de confusió amb sklearn

Utilitza la funció confusion_matrix per calcular la matriu de confusió.

```python 
from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_true, y_pred)
print(cm)
```

Identifica quina cel·la correspon a TP, FP, FN i TN.

2. Càlcul de mètriques amb sklearn

Calcula les mètriques següents utilitzant sklearn:

```python 
from sklearn.metrics import accuracy_score, precision_score, recall_score

accuracy = accuracy_score(y_true, y_pred)
precision = precision_score(y_true, y_pred)
recall = recall_score(y_true, y_pred)

print(accuracy, precision, recall)
```

3. Interpretació dels resultats

Quina mètrica és més rellevant en aquest problema?

Quin tipus d’error és més greu?

Consideraries acceptable aquest model en un entorn real?