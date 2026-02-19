# Decisió i generalització en Aprenentatge Automàtic

En aquest notebook estudiarem com avaluar correctament un model
i per què **generalitzar** és més important que ajustar-se perfectament
a les dades d'entrenament.

Treballarem amb:
- un model senzill d'arbre de decisió
- dades separades en train i test
- la mètrica MAE (Mean Absolute Error)

Finalment, introduirem el concepte de **cross-validation**.

# Repàs ràpid
## R² (regressió)
- **Què mesura:** proporció de variabilitat de `y` explicada pel model (comparat amb predir la mitjana).
- **Càlcul (idea):** 1 − (error del model / error de predir la mitjana)
- **Interpretació habitual:**
  - 1: ajust perfecte
  - 0: igual que predir la mitjana
  - < 0: pitjor que predir la mitjana
- **Limitació típica:** pot ser difícil d’interpretar en alguns contextos i no dona l’error en unitats reals.

---

## MAE (regressió)
- **Què mesura:** error mitjà en valor absolut (en les mateixes unitats que `y`).
- **Càlcul:** (1/n) · Σ |y − ŷ|
- **Avantatge clau:** molt interpretable (“ens equivoquem de mitjana X unitats”).
- **Limitació típica:** no penalitza especialment els errors molt grans.

---

## MSE (regressió)
- **Què mesura:** error mitjà quadràtic (penalitza més els errors grans).
- **Càlcul:** (1/n) · Σ (y − ŷ)²
- **Avantatge clau:** castiga fortament els errors grans (útil si els outliers són crítics).
- **Limitació típica:** unitats quadrades (menys intuïtiva) i molt sensible a valors extrems.



## Generalització

Un model **generalitza bé** quan és capaç de fer bones prediccions
sobre dades que **no ha vist durant l'entrenament**.

Avaluar un model només amb les dades d'entrenament no és correcte,
perquè pot haver après patrons molt específics que no es repeteixen
en dades noves.


## Overfitting (sobreajustament)

Parlem d’**overfitting** quan un model:
- té un error molt baix en entrenament
- però un error molt més alt en dades de test

Això indica que el model ha après massa bé les dades d'entrenament,
incloent soroll o detalls poc rellevants, i **no generalitza bé**.


## DEMO

Observa els resultats:
- Quin model té l'error més baix en entrenament?
- Quin model té l'error més baix en test?
- Quin model mostra una diferència gran entre train i test?

Un model amb MAE molt baix en train però alt en test
és un exemple clar d’**overfitting**.


## Cross-validation

La **cross-validation** és una tècnica per avaluar un model de manera
més fiable.

En lloc de fer una sola separació train/test:
- repetim l'experiment diverses vegades
- cada vegada amb una partició diferent
- i fem la mitjana dels errors obtinguts

Això permet mesurar:
- el rendiment mitjà del model
- la seva estabilitat
