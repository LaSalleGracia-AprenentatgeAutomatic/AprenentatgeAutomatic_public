# Pràctica — Part 1: Desenvolupament tècnic (codi)

**Treball en grups:** 2 persones  
**Format:** Notebook (`.ipynb`)

## Objectiu
Construir, avaluar i comparar models de classificació, explicant i interpretant cada pas del procés.

---

## Tasques a realitzar

### 1. Dataset
- El tutor proposarà diversos datasets de classificació.
- Cada grup n’ha de triar **un**.
- El dataset ha de tenir una variable objectiu clara i diverses variables d’entrada.

---

### 2. Exploració de dades (EDA)
Cal analitzar i explicar:
- mida del dataset
- tipus de variables
- distribució de la variable objectiu
- possible desbalanceig de classes

Incloeu gràfics senzills i una interpretació breu de cada un.

---

### 3. Preparació de dades
- Separar variables d’entrada (`X`) i variable objectiu (`y`).
- Dividir les dades en entrenament i test.
- Explicar per què aquesta separació és necessària.

---

### 4. Models
Construïu **dos models diferents**:
- Regressió logística
- Arbre de decisió

No cal optimitzar hiperparàmetres de manera exhaustiva.

---

### 5. Avaluació
Per a cada model:
- Prediccions en train i test
- Matriu de confusió
- Almenys **una mètrica principal** (accuracy, precision o recall), justificada

---

### 6. Cross-validation
- Aplicar cross-validation a cada model.
- Analitzar el resultat mitjà.
- Comparar-lo amb el resultat del test únic.

---

### 7. Interpretació
Cal interpretar:
- diferències entre train, test i cross-validation
- possibles indicis de sobreajustament
- quines variables són més rellevants

---

## Requisit final
El notebook ha d’explicar **què feu, per què ho feu i què indiquen els resultats**.
