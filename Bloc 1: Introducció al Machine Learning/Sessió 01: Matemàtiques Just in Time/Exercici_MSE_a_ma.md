# 🧮 Exercici: Calcula el MSE a mà

## ✳️ Situació
Tenim un model que intenta predir el **pes (kg)** de quatre persones a partir de la seva alçada.  
Les prediccions no són perfectes: a vegades encerta i a vegades s’equivoca una mica.

| Persona | Pes real (y) | Predicció (ŷ) |
|----------|--------------|---------------|
| 1 | 60 | 58 |
| 2 | 65 | 67 |
| 3 | 72 | 70 |
| 4 | 80 | 85 |

---

## 🧩 1️⃣ Calcula l’error individual
L’error és la diferència entre el valor real i el predit:

$$
e_i = y_i - \hat{y_i}
$$

| Persona | y | ŷ | $e_i = y - \hat{y}$ |
|----------|----|----|--------------------|
| 1 | 60 | 58 | 2 |
| 2 | 65 | 67 | -2 |
| 3 | 72 | 70 | 2 |
| 4 | 80 | 85 | -5 |

---

## 🧮 2️⃣ Eleva cada error al quadrat

$$
e_i^2 = (y_i - \hat{y_i})^2
$$

| Persona | $e_i$ | $e_i^2$ |
|----------|-----------|-------------|
| 1 | 2 | 4 |
| 2 | -2 | 4 |
| 3 | 2 | 4 |
| 4 | -5 | 25 |

---

## 📏 3️⃣ Fes la mitjana dels errors quadràtics

$$
MSE = \frac{1}{n} \sum e_i^2
$$

$$
MSE = \frac{4 + 4 + 4 + 25}{4} = \frac{37}{4} = 9.25
$$

---

## ✅ Resultat final
**MSE = 9.25**

---

## 💬 Interpretació
- Si el MSE fos **0**, voldria dir que el model encerta exactament tots els valors.  
- Com que és **9.25**, vol dir que els errors mitjans són petits però significatius (al voltant de 3 kg en error absolut).  
- L’elevació al quadrat fa que **un error gran (com el -5)** pesi molt més que els petits.

---

## 🧠 Preguntes per reflexionar
1. Quin dels quatre punts fa pujar més el MSE?  
2. Si eliminéssim el valor amb més error, què passaria amb el MSE?  
3. Per què creus que els errors es quadren abans de fer la mitjana?
