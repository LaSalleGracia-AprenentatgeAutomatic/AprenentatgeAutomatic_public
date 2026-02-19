# Bloc 4 · Sessió 1  
## Classificació: entendre abans d’automatitzar (K-NN)

---

## Objectiu de la sessió

En aquesta sessió aprendràs **què és un problema de classificació** i com es pot resoldre **entenent realment què fa l’algoritme**, abans d’utilitzar llibreries automàtiques.

Al final de la sessió hauries de ser capaç de:
- explicar què vol dir classificar dades,
- entendre què és una classe o etiqueta,
- representar dades en un espai de característiques,
- calcular distàncies entre dades,
- aplicar l’algoritme K-NN a mà,
- entendre el paper del valor *k*,
- comprendre per què la normalització és clau en models basats en distàncies.

---

## 1. Classificació vs regressió

En blocs anteriors has treballat **regressió**, on l’objectiu era predir un valor numèric continu (per exemple, un preu o una temperatura).

En **classificació**, l’objectiu és diferent:
- no prediem un número,
- assignem una **categoria o classe**.

### Exemples de classificació
- correu brossa / no correu brossa  
- risc alt / risc baix  
- esportista / no esportista  

Aquestes categories s’anomenen **classes** o **etiquetes**.

---

## 2. Espai de característiques

Cada dada es descriu mitjançant **variables** (també anomenades característiques o *features*).

Exemple:
- hores d’activitat física setmanal
- IMC

Cada variable correspon a una **dimensió** de l’espai.

- 1 variable → línia  
- 2 variables → pla  
- 3 variables → espai  

Cada persona o objecte es pot representar com **un punt** en aquest espai.

> Un algoritme no veu persones ni objectes: veu punts en un espai de números.

---

## 3. Píndola matemàtica — Distància

Per decidir si dues dades són semblants, necessitem una mesura de **distància**.

La més habitual és la **distància euclidiana**:

$`d = \sqrt((x1 - x2)^2 + (y1 - y2)^2)`$


Idea clau:
- com més petita és la distància, més semblants són els punts,
- com més gran és la distància, menys s’assemblen.

### Exemple
Punt A: (2, 3)  
Punt B: (4, 6)

Calculant la distància podem saber quin punt està més a prop d’un tercer.

---

## 4. Algoritme K-NN (K Nearest Neighbors)

K-NN vol dir **K veïns més propers**.

És un algoritme molt intuïtiu:
1. busquem quins punts estan més a prop del punt nou,
2. seleccionem els *k* més propers,
3. assignem la classe majoritària.

### Conceptes clau
- **veí**: una dada propera en l’espai de característiques  
- **k**: nombre de veïns que tenim en compte  
- **votació**: cada veí aporta la seva classe  

---

## 5. K-NN a mà: entendre l’algoritme

Abans d’automatitzar, aplicarem K-NN **manualment** per entendre què està passant.

### Dataset
| Persona | Activitat (h/setmana) | IMC | Classe |
|--------|-----------------------|-----|--------|
| A | 6 | 22 | saludable |
| B | 1 | 31 | risc |
| C | 4 | 25 | saludable |
| D | 0 | 34 | risc |
| E | 5 | 23 | saludable |

Nou punt:
- Activitat = 3  
- IMC = 28  

### Passos
1. Calcular la distància del nou punt a cada persona
2. Ordenar les distàncies de menor a major
3. Classificar amb diferents valors de *k* (1, 3, 5)
4. Comparar resultats

Aquest exercici mostra que **el resultat pot canviar segons *k***.

---

## 6. El paper del valor k

El valor de *k* controla el comportament del model:

- *k* petit:
  - decisions molt locals,
  - molt sensible al soroll i als outliers.
- *k* gran:
  - decisions més estables,
  - pot perdre detall local.

No existeix un valor de *k* universalment correcte.  
Depèn del problema i de les dades.

---

## 7. Normalització de les variables (clau en K-NN)

K-NN decideix **només a partir de distàncies**.  
Això fa que l’**escala de les variables** sigui molt important.

Si una variable té valors molt més grans que una altra, pot dominar completament el càlcul de la distància.

### Exemple
- Activitat física: 0–10  
- IMC: 18–40  

Sense normalització:
- l’IMC pesa molt més que l’activitat física,
- el model pren decisions esbiaixades.

> Sense normalització, no totes les variables tenen la mateixa importància.

---

### Píndola matemàtica — Normalització Min–Max

La normalització Min–Max transforma totes les variables a l’interval [0, 1]:

$`x' = (x - min(x)) / (max(x) - min(x))`$


Aquesta transformació:
- no canvia la informació,
- només canvia l’escala,
- fa que totes les variables contribueixin de manera equilibrada.

---

## 8. K-NN amb Python (sense llibreries)

Ara implementarem K-NN amb Python bàsic, **sense utilitzar scikit-learn**.

L’objectiu és entendre l’algoritme, no fer-lo automàtic.

### Pseudocodi del procés K-NN

entrada:

X_train: dades d'entrenament (n mostres, m variables)

y_train: classes associades

x_new: nou punt

k: nombre de veïns

1. per a cada mostra i de X_train:
calcular la distància entre x_new i X_train[i]

2. ordenar les mostres per distància creixent

3. seleccionar els k veïns més propers

4. obtenir les seves classes

5. fer una votació

6. retornar la classe majoritària


---

## 9. Idees clau de la sessió

- Classificar és prendre decisions amb dades
- Les dades es representen com punts en un espai
- La distància mesura semblança
- K-NN decideix segons els veïns
- El valor de *k* és fonamental
- La normalització és imprescindible en models basats en distàncies

A la següent sessió veurem com **automatitzar aquests models** i com **avaluar si funcionen bé**.
