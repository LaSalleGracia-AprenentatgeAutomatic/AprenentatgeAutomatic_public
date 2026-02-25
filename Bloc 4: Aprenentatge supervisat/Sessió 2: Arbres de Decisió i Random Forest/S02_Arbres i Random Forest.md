# Bloc 4 · Sessió 2  
## Arbres de decisió i Random Forest (de regles a sklearn)

---

# Objectius de la sessió

En aquesta sessió aprendràs a:

- Entendre com funciona un **arbre de decisió** com a conjunt de regles
- Construir i aplicar un arbre **a mà** sobre un dataset petit
- Identificar i explicar **overfitting** en arbres
- Conèixer els **paràmetres principals** de `DecisionTreeClassifier` i `RandomForestClassifier`
- Entrenar arbres i random forests amb `scikit-learn`
- Comparar models (arbre vs random forest) amb mètriques ja conegudes

---

# 0. Recordatori (connexió amb la sessió 1)

A la sessió 1 hem vist K-NN:
- basa la decisió en distàncies
- normalització sovint és necessària

Ara veurem una família totalment diferent:
- **arbres de decisió**: decideixen amb **regles** (if/else)
- normalització **no és necessària** (en general) perquè no calcula distàncies

---

# 1. Què és un arbre de decisió?

Un arbre de decisió és un model que:
- tria una variable
- aplica una pregunta del tipus: *és més gran que un llindar?*
- separa les dades en dos grups
- repeteix el procés fins arribar a una decisió final (fulla)

A la pràctica, un arbre és un conjunt de regles:

- Si (X1 <= 2.5) i (X2 > 7.0) → classe A  
- Si (X1 > 2.5) → classe B  

---

# 2. Píndola conceptual: impuresa i criteri de divisió

Un arbre intenta dividir les dades perquè cada grup resultant sigui el més “pur” possible.

Dos criteris típics:

- **Gini** (impuresa de Gini)
- **Entropia** (information gain)

No entrarem en la fórmula. Ens quedem amb la idea:

> Un bon tall separa les classes el màxim possible.

---

# 3. Exercici a mà 1 — Construir regles senzilles

## Dataset (petit i visual)

Classificarem si una persona és “esportista” o “no esportista” amb dues variables:

| Persona | Activitat (h/setmana) | FC repòs | Classe |
|--------|------------------------|----------|--------|
| A | 6 | 55 | esportista |
| B | 5 | 60 | esportista |
| C | 4 | 62 | esportista |
| D | 2 | 78 | no esportista |
| E | 1 | 82 | no esportista |
| F | 0 | 88 | no esportista |
| G | 3 | 70 | no esportista |

## Tasques

1. Proposa una regla simple amb una sola variable (ex: Activitat > ?).
2. Prova diferents llindars (per exemple 2.5, 3.5, 4.5).
3. Tria el llindar que separi millor les classes.
4. Dibuixa l'arbre a paper

## Preguntes de reflexió

- Quina variable separa millor: Activitat o FC repòs?
- Quin tipus d’errors comets amb aquesta regla?

---

# 4. Exercici a mà 2 — Esbós d’un arbre de profunditat 2

## Objectiu
Construir un arbre molt petit (2 decisions màxim).

## Dades
 Persona | Activitat (h/setmana) | FC repòs | Classe |
|----------|------------------------|----------|------------|
| A | 6.0 | 55 | esportista |
| B | 5.0 | 60 | esportista |
| C | 4.0 | 68 | esportista |
| K | 5.0 | 69 | esportista |
| H | 4.5 | 72 | no esportista |
| G | 3.0 | 70 | no esportista |
| D | 2.0 | 78 | no esportista |
| E | 1.0 | 82 | no esportista |
| F | 0.0 | 88 | no esportista |
| J | 2.0 | 60 | no esportista |

## Tasques

1. Primera divisió: escull la variable i el llindar principal.
2. Segona divisió: per a un dels costats, afegeix una segona regla.
3. Dibuixa l’arbre (amb nodes i fulles) o escriu les regles.

## Preguntes de reflexió

- Quin avantatge té tenir dues decisions en lloc d’una?
- Pots crear un arbre que classifiqui perfectament el dataset?
- Si classifica perfectament, què pot passar quan arribin dades noves?

---

# 5. Overfitting en arbres (idea clau)

Els arbres poden sobreajustar fàcilment perquè:
- poden memoritzar dades si els deixem créixer massa
- creen fulles amb molt pocs exemples

Símptoma típic:
- accuracy train molt alta
- accuracy test més baixa

---

# 6. Arbres amb sklearn (DecisionTreeClassifier)

## Sintaxi base

```python
from sklearn.tree import DecisionTreeClassifier

tree = DecisionTreeClassifier(random_state=0)
tree.fit(X_train, y_train)
```

---

## 6.1 Paràmetres importants (i què signifiquen)

### `max_depth`
- limita profunditat de l’arbre
- menor profunditat → menys complexitat → menys overfitting

### `min_samples_leaf`
- mínim de mostres a cada fulla
- evita fulles amb 1 o 2 dades

### `min_samples_split`
- mínim de mostres per fer una divisió

### `criterion`
- 'gini' o 'entropy' (com decideix el millor tall)

---

# 7. Exercici amb sklearn 1 — Arbre sense restriccions vs arbre controlat

## Tasques

1. Entrena un arbre sense restriccions (per defecte).
2. Entrena un arbre amb:
   - max_depth = 3
3. Entrena un arbre amb:
   - max_depth = 5
4. Compara mètriques en test (accuracy i F1).
5. Observa diferències train vs test.

## Preguntes de reflexió

- Quin arbre generalitza millor?
- Quin arbre sembla sobreajustar?
- Quina profunditat et sembla més raonable i per què?

---

# 8. Exercici amb sklearn 2 — Dibuixar l’arbre amb llibreries

## Objectiu
Visualitzar un arbre entrenat i interpretar les seves decisions.

## Tasques

1. Fes servir el mateix dataset de l’exercici 7.
2. Entrena un `DecisionTreeClassifier` amb `max_depth=3`.
3. Dibuixa l’arbre amb `plot_tree` i mostra’l en un gràfic.
4. Escriu (o captura) les tres primeres regles que observes.
5. Opcional: genera el text de l’arbre amb `export_text`.

## Codi base (exemple)

```python
from sklearn.tree import DecisionTreeClassifier, plot_tree, export_text
import matplotlib.pyplot as plt

tree = DecisionTreeClassifier(max_depth=3, random_state=0)
tree.fit(X_train, y_train)

plt.figure(figsize=(12, 6))
plot_tree(tree, feature_names=feature_names, class_names=class_names, filled=True)
plt.show()

print(export_text(tree, feature_names=feature_names))
```

## Preguntes de reflexió

- Les primeres divisions tenen sentit amb el que esperaves?
- Quines variables apareixen més amunt de l’arbre?
- Com canvia la interpretabilitat si augmentes `max_depth`?

---

# 9. Random Forest (RandomForestClassifier)

## Què és?

Un Random Forest és:
- un conjunt de molts arbres
- cada arbre s’entrena amb una mostra aleatòria de dades (bootstrap)
- i cada divisió considera només un subconjunt de variables

La decisió final és per votació.

> Random Forest redueix la variància i acostuma a generalitzar millor que un sol arbre.

---

## 8.1 Paràmetres importants

```python
from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier(
    n_estimators=100,
    random_state=0
)
```

### `n_estimators`
Nombre d’arbres.
- més arbres → més estable (fins a un punt)

### `max_depth`
Controla complexitat dels arbres interns.

### `max_features`
Nombre de variables considerades a cada tall.
- valors típics: 'sqrt', 'log2' o un número

### `min_samples_leaf`
Evita fulles massa petites.

---

# 10. Exercici amb sklearn 3 — Comparar Arbre vs Random Forest

## Tasques

1. Entrena:
   - un DecisionTree
   - un RandomForest amb n_estimators=10
   - un RandomForest amb n_estimators=100
2. Compara accuracy i F1 en test.
3. Compara estabilitat (si canvies random_state, canvia molt el resultat?).

## Preguntes de reflexió

- Per què el Random Forest acostuma a millorar l’arbre?
- Augmentar n_estimators sempre millora?
- Quin model triaries si necessites explicar decisions?

---

# 11. Comparació final amb K-NN

Completa aquesta comparació:

| Aspecte | K-NN | Arbre | Random Forest |
|---|---|---|---|
| Basat en distància | | | |
| Necessita normalització | | | |
| Interpretabilitat | | | |
| Risc d’overfitting | | | |
| Escalabilitat | | | |

Preguntes:
- Quin model és millor per explicar una decisió?
- Quin model esperes que funcioni millor en dades no lineals?

---

# 12. Idees clau de la sessió

- Un arbre és un conjunt de regles (if/else).
- Els arbres poden sobreajustar fàcilment si creixen massa.
- Podem controlar la complexitat amb paràmetres com `max_depth` i `min_samples_leaf`.
- Random Forest combina molts arbres i sol generalitzar millor.
- Els paràmetres de sklearn canvien el comportament del model.
