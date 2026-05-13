# Exercici — Recomanador de pel·lícules basat en gèneres (K-NN)

## Context

Disposem d’un dataset de pel·lícules amb diferents característiques:
- gèneres
- director
- durada
- altres camps opcionals

L’objectiu és construir un **sistema de recomanació**:  
donada una pel·lícula nova, volem **recomanar una llista de pel·lícules similars**.

En aquest exercici començarem **només amb els gèneres**, i progressivament afegirem més informació.

---

## 1. Dataset inicial

| Títol | Gèneres |
|------|---------|
| Film A | Acció, Aventura |
| Film B | Comèdia, Romàntic |
| Film C | Acció, Ciència-ficció |
| Film D | Drama |
| Film E | Comèdia |
| Film F | Acció, Thriller |
| Film G | Drama, Romàntic |

---

## 2. Preparació de dades — Separar els gèneres

### Tasca 1
1. Extreu la llista de tots els gèneres únics del dataset.
2. Aquesta llista definirà les dimensions de l’espai de característiques.

---

## 3. Vectorització de gèneres (CountVectorizer)

Cada gènere correspon a una dimensió del vector:
- 1 si la pel·lícula té el gènere
- 0 si no el té

### Tasca 2
Vectoritza totes les pel·lícules del dataset.

---

## 4. Nova pel·lícula a recomanar

Nova pel·lícula:
- Gèneres: Acció, Aventura

Construeix el vector corresponent.

---

## 5. Recomanació amb K-NN (manual)

### Tasca 3
1. Calcula la distància entre la nova pel·lícula i totes les altres.
2. Ordena-les de més similars a menys.
3. Tria un valor de k i retorna les k pel·lícules recomanades.

---

## 6. Reflexió sobre el valor de k

Respon:
1. Què passa amb k=1?
2. Què passa amb un k molt gran?
3. Quin k et sembla més adequat i per què?

---

## 7. Extensió — Afegir nous camps

Afegeix:
- director
- durada

Repeteix la recomanació. Prova amb varies pel·lícules inserides manualment (que no hi siguin al dataset) 

---

## 8. Comparació final

1. Canvien les recomanacions?
2. Quins camps influeixen més?
3. Cal normalitzar? Per què?
