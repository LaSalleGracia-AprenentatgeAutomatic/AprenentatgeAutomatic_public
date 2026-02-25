# 🧩 Bloc 2 — Sessió 1: Comprendre i explorar les dades

## 🕒 Durada
3 hores

## 🎯 Objectius específics
- Comprendre què és un **dataset** i com s’estructura.
- Descriure dades amb **Pandas**.
- Detectar **valors nuls**, **tipus de variables** i **inconsistències**.
- Aplicar conceptes bàsics d’**estadística descriptiva**.

---

## 🧠 Conceptes clau

| Tema | Contingut |
|------|------------|
| Estructura de dades | DataFrame, columnes, files, índex |
| Tipus de dades | Numèriques, categòriques, booleans, datetimes |
| Exploració inicial | `.head()`, `.info()`, `.describe()`, `.value_counts()` |
| Qualitat de dades | Detecció de valors nuls, duplicats, formats incorrectes |
| Estadística descriptiva | Mitjana, mediana, moda, desviació estàndard |

---

## 📘 Matemàtiques Just In Time

| Concepte | Fórmula | Explicació |
|-----------|----------|------------|
| Mitjana | \( \bar{x} = \frac{1}{n}\sum x_i \) | Valor promig d’un conjunt |
| Mediana | — | Valor central d’un conjunt ordenat |
| Desviació estàndard | \( \sigma = \sqrt{\frac{1}{n}\sum (x_i - \bar{x})^2} \) | Mideix la dispersió de les dades |
| Variància | \( \sigma^2 \) | Quadrat de la desviació estàndard |

---

## 🧩 Activitat pràctica: Exploració d’un dataset real

**Dataset recomanat:**  
[Students Performance in Exams (Kaggle)](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams)

### Objectiu
Explorar i comprendre un dataset mitjançant eines de Python i estadística descriptiva.

### Instruccions
1. Carrega el dataset (`students_performance.csv`) amb `pd.read_csv()`.
2. Mostra les 5 primeres files (`.head()`).
3. Consulta informació general (`.info()`) i resum estadístic (`.describe()`).
4. Identifica:
   - Nombre de files i columnes.
   - Columnes amb valors nuls.
   - Columnes categòriques i numèriques.
5. Calcula:
   - Mitjana, mediana i desviació estàndard de les notes.
6. Escriu un breu **comentari interpretatiu**:
   - Quines variables semblen tenir relació?
   - Hi ha diferències de rendiment per gènere?

---

## Sessió 1 — Tipus de dades i neteja bàsica (2 h)

Objectiu: Comprendre les tipologies de dades i preparar-les per al tractament automàtic.

RAs: RA2, RA6

Continguts
- Tipus de dades (numèriques, categòriques, temporals, mixtes)
- Valors nuls (NaN, None)
- Estratègies de substitució: mitjana, moda, valors per defecte
- Introducció a Pandas i als DataFrame

Matemàtiques just in time
- Mitjana aritmètica
- Moda
- Percentatge de valors nuls

Activitat pràctica
- Carregar un dataset real.
- Comptar i substituir valors nuls amb pandas.
- Discussió sobre l’impacte de la neteja en la qualitat del model.

## Sessió 2 — Detecció d’outliers i codificació de variables (2 h)

Objectiu: Detectar valors atípics i transformar variables categòriques a formats numèrics.

RAs: RA2, RA6

Continguts
- Detecció d’outliers amb boxplots i z-score
- Codificació: Label Encoding i One-Hot Encoding
- Escalat de dades: StandardScaler i MinMaxScaler

Matemàtiques just in time
- Desviació estàndard
- Z-score

Activitat pràctica
- Detecció d’outliers amb gràfics i estadístiques.
- Codificació de columnes categòriques.
- Escalat de les dades per als models de ML.

## Sessió 3 — Normalització, correlació i visualització exploratòria (2 h 30 min)

Objectiu: Normalitzar dades i analitzar relacions entre variables.

RAs: RA2, RA6

Continguts
- Normalització vs estandardització
- Matriu de correlació i heatmap
- EDA: distribucions, histogrames, scatter plots

Matemàtiques just in time
- Fòrmula de normalització (min-max)
- Fòrmula de z-score
- Coeficient de correlació de Pearson

Activitat pràctica
- Calcular i visualitzar correlacions.
- Detectar variables redundants.
- Crear gràfics exploratoris amb Seaborn.

## Sessió 4 — Divisió de conjunts i validació de qualitat (2 h 30 min)

Objectiu: Preparar un conjunt de dades per entrenar un model de ML assegurant-ne la coherència.

RAs: RA2, RA6

Continguts
- train_test_split i percentatges (80/20, 70/15/15…)
- Aleatorietat i random state
- Balanç de classes i estratificació
- Validació de qualitat del dataset

Matemàtiques just in time
- Proporcions i percentatges
- Conceptes bàsics de mostreig

Activitat pràctica
- Divisió del dataset amb train_test_split.
- Comparació de distribucions entre train i test.
- Guardar i documentar el dataset final per al Bloc 3.

🧮 Resum del Bloc 2
Sessió	Continguts principals	RA	Matemàtiques	Activitat
1	Tipus de dades i valors nuls	RA2, RA6	Mitjana, moda	Neteja bàsica amb Pandas
2	Outliers i codificació	RA2, RA6	Desviació estàndard, z-score	Outliers i encoding
3	Normalització i correlació	RA2, RA6	Min-max, Pearson	EDA i heatmaps
4	Divisió i validació	RA2, RA6	Percentatges, mostreig	Preparació dataset final