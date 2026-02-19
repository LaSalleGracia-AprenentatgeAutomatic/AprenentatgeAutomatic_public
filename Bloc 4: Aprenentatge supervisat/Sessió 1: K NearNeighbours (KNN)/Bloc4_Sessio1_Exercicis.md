# Bloc 4 · Sessió 1  
## Exercicis — Classificació i K-NN

Aquests exercicis estan pensats per fer **durant la sessió** i acabar-los, si cal, com a treball personal.  
L’objectiu no és només obtenir un resultat, sinó **entendre i justificar cada decisió**.

---

## Exercici 1 — Classificar a mà amb K-NN

### Context
Volem classificar persones segons el seu perfil de salut.

### Dataset
| Persona | Activitat (h/setmana) | IMC | Classe |
|--------|-----------------------|-----|--------|
| A | 6 | 22 | saludable |
| B | 1 | 31 | risc |
| C | 4 | 25 | saludable |
| D | 0 | 34 | risc |
| E | 5 | 23 | saludable |

### Nou punt a classificar
- Activitat = 3  
- IMC = 28  

### Tasques
1. Calcula la distància euclidiana entre el nou punt i cada persona.
2. Ordena les distàncies de menor a major.
3. Assigna una classe utilitzant:
   - k = 1
   - k = 3
   - k = 5
4. Respon:
   - Canvia la classe segons el valor de k?
   - Quin valor de k et sembla més raonable? Per què?

---

## Exercici 2 — Impacte d’un outlier

### Nou escenari
Afegim una nova persona al dataset:

| Persona | Activitat (h/setmana) | IMC | Classe |
|--------|-----------------------|-----|--------|
| F | 10 | 40 | saludable |

### Tasques
1. Torna a classificar el punt nou amb k = 3 i k = 5.
2. Analitza:
   - Aquest punt sembla coherent amb la seva classe?
   - Com afecta el resultat final?
3. Explica amb paraules què és un **outlier** en aquest context.

---

## Exercici 3 — Implementar K-NN amb Python (sense llibreries)

### Objectiu
Implementar manualment l’algoritme K-NN amb Python bàsic.

### Requisits
- Pots utilitzar `numpy`
- No està permès utilitzar `scikit-learn`

### Tasques
1. Guarda el dataset en estructures de dades adequades.
2. Escriu una funció que:
   - calculi la distància euclidiana,
   - ordeni els punts segons distància,
   - retorni la classe majoritària per un valor de k donat.
3. Comprova que el resultat coincideix amb el càlcul fet a mà.

---

## Exercici 4 — Reflexió i interpretació

Respon de manera raonada:

1. És correcte dir que K-NN "aprèn"?
2. Quin tipus de problemes pot tenir K-NN amb datasets grans?
3. En quin cas creus que K-NN no seria una bona elecció?

---

## Criteris d’avaluació (orientatius)

- Correcció dels càlculs de distància
- Justificació del valor de k
- Claredat en les explicacions
- Capacitat d’interpretar errors i limitacions

Aquest document forma part del treball de la Sessió 1 del Bloc 4.
