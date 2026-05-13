# 📐 Exercici: Recordem l’expressió d’una recta

## 🎯 Objectiu
Recordar com s’escriu i interpreta l’equació d’una **recta**:

$$
y = m x + b
$$

on:
- $m$ → **pendent** (slope): quant canvia `y` quan `x` augmenta una unitat.  
- $b$ → **intercept** o **ordenada a l’origen**: el valor de `y` quan `x = 0`.  

---

## ✳️ 1️⃣ Interpreta l’equació
Dona’t la recta següent:

$$
y = 2x + 1
$$

1. Quina és la pendent?  
2. Quina és l’ordenada a l’origen?  
3. Si $x = 0$, quant val $y$?  
4. Si $x = 3$, quant val $y$?  

🧮 *Fes els càlculs a mà i comprova que la recta passa pels punts (0, 1) i (3, 7).*

---

## 📈 2️⃣ Dibuixa-la
Dibuixa la recta amb els punts anteriors (a mà o amb una eina digital).

| x | y |
|---|---|
| 0 | 1 |
| 1 | 3 |
| 2 | 5 |
| 3 | 7 |

🔹 Què indica la pendent sobre la inclinació de la recta?  
🔹 Què passaria si canviéssim `m` o `b`?

---

## 🔄 3️⃣ Experimenta amb altres valors
Completa aquesta taula de valors per diferents pendents i intercepts:

| Equació | Pendent (m) | Intercept (b) | Punt (0, b) | Punt (1, m + b) | Observació |
|----------|--------------|----------------|---------------|------------------|-------------|
| y = x + 1 | 1 | 1 | | | |
| y = 2x | 2 | 0 | | | |
| y = -x + 3 | -1 | 3 | | | |
| y = 0.5x + 2 | 0.5 | 2 | | | |

💬 Com canvia la inclinació segons el signe i el valor de `m`?

---

## 🧠 4️⃣ Càlcul invers
Si tens un punt $(x, y) = (2, 7)$ i saps que $b = 3$, troba la pendent `m`.

$$
m = \frac{y - b}{x} = \frac{7 - 3}{2} = 2
$$

Comprova que la recta és $y = 2x + 3$.

---

## 🔍 5️⃣ Connecta amb Machine Learning
- En regressió lineal, el model té la mateixa forma:  

$$
\hat{y} = w x + b
$$

on `w` és la **pendent** (paràmetre del model) i `b` és el **bias** o intercept.  
- L’algorisme d’aprenentatge “aprèn” els valors de `w` i `b` que minimitzen l’error (MSE).  
