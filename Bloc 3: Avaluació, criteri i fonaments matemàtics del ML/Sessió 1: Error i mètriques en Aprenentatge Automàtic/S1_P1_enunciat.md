# Activitat 1 — Càlcul bàsic de l’error d’un model

## Context
Un model d’aprenentatge automàtic fa prediccions numèriques. Aquestes prediccions no sempre coincideixen amb la realitat, i per això diem que el model comet **errors**.

En aquesta activitat aprendràs a **calcular i resumir aquests errors** de manera senzilla.

---

## Dades

El model intenta predir el **consum elèctric diari (en kWh)** d’un habitatge.

| Dia | Valor real (y) | Predicció del model A (ŷ_A) | Predicció del model B (ŷ_B)
|----|----------------|------------------------------|----------------------------|
| 1 | 20 | 18 | 15 |
| 2 | 22 | 23 | 22 |
| 3 | 19 | 20 | 23 |

---

## Tasques

### 1. Error de predicció
Calcula l’error de cada dia utilitzant la fórmula:

\[
\text{Error}_i = y_i - \hat{y}_i
\]

Completa una taula amb els errors obtinguts.

---

### 2. Error absolut
Calcula el **valor absolut** de cada error:

\[
|\text{Error}_i| = |y_i - \hat{y}_i|
\]

---

### 3. Error global (cost del model)
Calcula el **cost del model**, definit com la mitjana dels errors absoluts:

\[
\text{Cost} = \frac{1}{n} \sum |y_i - \hat{y}_i|
\]

---

## Pregunta final
> **Què representa aquest valor de cost sobre el comportament del model?**