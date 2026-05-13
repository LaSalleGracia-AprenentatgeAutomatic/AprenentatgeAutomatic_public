# Bloc 4 · Sessió 3  
## Regressió Logística i la idea bàsica de descens del gradient

---

# Objectius de la sessió

En aquesta sessió aprendràs a:

- Entendre què és un model lineal
- Comprendre el funcionament de la regressió logística
- Interpretar coeficients d’un model lineal
- Entendre què vol dir convergir
- Comprendre la idea bàsica de descens del gradient (sense matemàtica avançada)
- Relacionar iteracions, pendent i millora de l’error
- Utilitzar `LogisticRegression` amb sklearn i interpretar els seus paràmetres

---

# 0. Recordatori del mapa de models

Fins ara hem vist:

| Model | Idea principal |
|--------|----------------|
| KNN | Classificació per distància |
| Decision Tree | Classificació per regles |
| Random Forest | Ensemble d’arbres |

Ara afegim una nova família:

| Model | Idea principal |
|--------|----------------|
| Logistic Regression | Model lineal probabilístic |

---

# 1. Què és la regressió logística?

És un model lineal que:

1. Combina les variables de forma lineal.
2. Transforma el resultat en probabilitat.
3. Classifica segons un llindar.

---

## Model matemàtic (just-in-time)

Part lineal:

$$
z = w_1 x_1 + w_2 x_2 + b
$$

Transformació sigmoide:

$
\sigma(z) = {1}/{(1 + e^{-z})}
$

Classificació:

- Si $\sigma(z) > 0.5$ → classe 1  
- Si no → classe 0  

---

# 2. Exercici a mà — Interpretar un model

Suposem el model:

$$
z = 0.8 \cdot Activitat - 0.1 \cdot FC\_repòs + 2.4
$$

## Tasques

1. Calcula \( z \) per:
   - Activitat = 5
   - FC_repòs = 60
2. Calcula la probabilitat amb la sigmoide.
3. Classifica amb llindar 0.5.

## Preguntes de reflexió

- Què indica que el coeficient d’Activitat sigui positiu?
- Què indica que el coeficient de FC_repòs sigui negatiu?
- Si augmenta Activitat, què passa amb la probabilitat?

---

# 3. Pregunta clau

D’on surten aquests coeficients?

La resposta és important:

> La regressió logística no calcula la solució directament.  
> La busca iterativament.

---

# 4. Buscar la millor solució

El model:

1. Comença amb uns pesos inicials.
2. Calcula l’error.
3. Ajusta una mica els pesos.
4. Torna a calcular l’error.
5. Repeteix fins que l’error ja no millora gaire.

Això s’anomena **convergència**.

---

# 5. Convergència — Explicació visual

Imagina que la funció d’error és una vall.

- Si estem a dalt, l’error és alt.
- Baixem seguint la pendent.
- Cada pas redueix l’error.
- Quan la pendent és gairebé zero, hem arribat al mínim.

> El gradient ens indica la direcció de major descens.

No cal fer càlcul diferencial per entendre aquesta idea.

---

## Exemple d’iteracions

| Iteració | Error |
|----------|--------|
| 1 | 0.69 |
| 20 | 0.48 |
| 50 | 0.42 |
| 100 | 0.401 |
| 200 | 0.4009 |

Preguntes:

- Quan diries que ja ha convergit?
- Per què la millora és cada vegada més petita?

---

# 6. LogisticRegression amb sklearn

## Sintaxi base

```python
from sklearn.linear_model import LogisticRegression

model = LogisticRegression(
    C=1.0,
    max_iter=100,
    solver="lbfgs"
)

model.fit(X_train, y_train)
```

---

# 7. Paràmetres importants

## max_iter
Nombre màxim de passos que pot fer el model per trobar la solució.

Si és massa petit, pot aparèixer:

ConvergenceWarning

Traducció:

> Hem aturat el model abans que acabés de baixar la vall.

Podem consultar:

```python
model.n_iter_
```

---

## C (regularització)

Controla la mida dels coeficients.

- C petit → més regularització → model més estable
- C gran → menys regularització → model més flexible

Visualment:

> La regularització fa la vall més suau i evita pesos excessius.

---

# 8. Situacions especials

## Separació perfecta

Si les dades són perfectament separables:

- Els pesos poden créixer molt.
- Pot costar més convergir.
- La regularització ajuda a estabilitzar la solució.

---

# 9. Comparació conceptual amb altres models

| Aspecte | Logística | Arbre | KNN |
|----------|------------|--------|------|
| Lineal | Sí | No | No |
| Iteratiu | Sí | No | No |
| Basat en optimització | Sí | No | No |
| Necessita normalització | Sí | No | Sí |

---

# 10. Reflexió final

1. Per què la regressió logística necessita iteracions i un arbre no?
2. Què vol dir que un model no ha convergit?
3. Si augmentem molt max_iter, sempre millorarà?
4. En quin tipus de dades pot fallar un model lineal?

---

# 11. Idees clau de la sessió

- La regressió logística és un model lineal probabilístic.
- Els coeficients no es calculen directament: es busquen iterativament.
- Convergir significa arribar a un punt on l’error ja no millora gaire.
- El gradient indica la direcció de millora.
- Aquest mecanisme serà fonamental quan estudiem xarxes neuronals.
