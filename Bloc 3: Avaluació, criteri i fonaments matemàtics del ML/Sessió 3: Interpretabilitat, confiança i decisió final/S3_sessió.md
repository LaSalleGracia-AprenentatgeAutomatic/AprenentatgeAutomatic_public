# Bloc 3 · Sessió 3  
## Interpretabilitat, confiança i decisió final

## 1. Connexió amb les sessions anteriors
### Pregunta inicial
> Si dos models tenen errors semblants, com decidim quin és millor?



## 2. Interpretabilitat: entendre què fa el model

### Idea clau
Un model és més fiable si podem explicar, encara que sigui de manera aproximada, com pren decisions.

---

### Exemple 1 — Regressió lineal

y = 2.1·X1 − 0.5·X2 + 0.1·X3

#### Preguntes guiades
- Quina variable té més impacte?
- Hi ha variables poc rellevants?
- Podríem explicar aquest model amb paraules?


---

### Exemple 2 — Arbre de decisió
X1: 65%
X2: 25%
X3: 10%


#### Preguntes guiades
- Aquest model és interpretable?
- És tan explicable com el model lineal?

---

## 3. Confiança: quan un error baix no és suficient

### Idea clau
Un error baix no garanteix que el model sigui fiable.

---

### Cas 1 — Mateix error puntual, diferent estabilitat

| Model | MAE test  | MAE CV |
|------ |---------- |--------|
| A     | 20        | 35     |
| B     | 22        | 23     |

#### Preguntes guiades
- Quin model sembla millor segons el test?
- Quin és més estable?
- Quin confiaries per a un ús real?

---

### Cas 2 — Error molt baix en entrenament

| Model | MAE train | MAE test |
|------ |-----------|----------|
| C     |  3        | 40       |

#### Preguntes guiades
- Aquest model és bo?
- Què està passant?

---

## 4. Decisió final: criteri i context

### Idea clau
La decisió final sobre un model depèn del context, no només de la mètrica.

---

### Escenari proposat
- Model A: millor rendiment, difícil d’explicar  
- Model B: rendiment una mica pitjor, molt interpretable  

#### Preguntes guiades
- Quin model triaries per una empresa?
- I per una administració pública?
- I per un sistema crític?


---

## 5. Part pràctica curta

### Activitat proposada

| Model | MAE train | MAE test | MAE CV | Interpretabilitat |
|------ |-----------|----------|--------|------------------ |
| Lineal| 18        | 22       | 21     | Alta              |
| Arbre |  6        | 35       | 33     | Mitjana           |

### Tasques
1. Identificar quin model està sobreajustat  
2. Decidir quin model triarien  
3. Justificar la decisió en 4–5 línies  

---

## 6. Tancament del Bloc 3
> Un bon model no és només el que s’equivoca poc, sinó el que entenem i en què podem confiar.
