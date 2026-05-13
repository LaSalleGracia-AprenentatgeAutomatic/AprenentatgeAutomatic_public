# Bloc 6 · Sessió 1  
## Fonaments de les Xarxes Neuronals

---

## Objectiu de la sessió

En aquesta sessió faràs el salt del Machine Learning clàssic al **Deep Learning**. Aprendràs en què s'inspiren les xarxes neuronals i en comprendràs la peça fonamental: **la neurona artificial (o perceptró)**.

Al final de la sessió hauries de ser capaç de:
- entendre la diferència principal entre els models vistos anteriorment i el Deep Learning,
- identificar els components d'una neurona artificial: entrades, pesos (weights), biaixos (biases) i sortida,
- calcular matemàticament el resultat (forward pass) d'una neurona simple a mà,
- conèixer les funcions d'activació bàsiques (Esglaó, ReLU, Sigmoide) i per què serveixen,
- implementar una neurona artificial pas a pas utilitzant només Python i Numpy.

---

## 1. Machine Learning vs Deep Learning

Fins ara hem treballat amb models on, d'alguna manera, l'enginyer havia d'ajudar l'algoritme (fent neteja de dades, creant columnes noves o donant un pes especial a certa informació). Això es diu *Feature Engineering*.

Les **Xarxes Neuronals** o (Deep Learning) tenen un enfocament diferent:
- S'inspiren en l'estructura del **cervell humà**.
- Són capaces d'extreure les característiques rellevants pel seu compte si tenen prou dades.
- Destaquen especialment en dades complexes o no estructurades (imatges, àudio, text sencer).

### Pregunta clau

> Com podem simular el comportament del cervell amb codi per resoldre problemes?

---

## 2. La Neurona Artificial (El Perceptró)

En biologia, una neurona rep senyals (a través de les dendrites). Si la combinació d'aquests senyals és prou forta, la neurona s'activa i despren impuls elèctric (per l'axó).

La **neurona artificial** simula exactament això:
1. **Entrades ($x$)**: Les dades que rep.
2. **Pesos ($w$)**: Cada entrada té un pes que indica "quanta importància" se li ha de donar a aquella informació en concret.
3. **Suma ponderada**: Multiplica cada entrada pel seu pes i ho suma tot. 
4. **Biaix ($b$)**: Un valor extra (bias) que ajusta la sensibilitat de la neurona. Ens permet moure el resultat amunt o avall.
5. **Funció d'activació**: Decideix si el número fruit de la suma és suficient per "activar" la neurona (si treu un $1$, un $0$, etc.).

Fórmula bàsica (abans de l'activació):
$$ z = (x_1 \cdot w_1) + (x_2 \cdot w_2) + ... + (x_n \cdot w_n) + b $$

---

## 3. Píndola matemàtica — Producte Escalar (Dot Product)

Escriure la fórmula anterior variable a variable és molt pesat si en tenim moltes. Ho podem escriure en forma de matrius (o vectors).

L'operació $$(x_1 \cdot w_1) + (x_2 \cdot w_2)$$ s'anomena **Producte Escalar** entre dos vectors (el vector d'entrades $X$ i el vector de pesos $W$).

$$ X = [1, 3] $$
$$ W = [2, -1] $$

El producte escalar és: $X \cdot W = (1 \times 2) + (3 \times -1) = 2 - 3 = -1$.

> Utilitzar vectors i productes escalars permet que els ordinadors (i en especial les targetes gràfiques, GPUs) formin les operacions molt ràpidament.

---

## 4. Píndola matemàtica — Funcions d'activació

La suma ponderada $+ b$ genera un número (p. ex. $z = -1$, o $z = 45$).
Un model que només fa sumes i multiplicacions sempre serà una **línia recta**. Com que el món és complex (les dades fan ondulacions i corbes), ens cal introduir **no-linealitat**. Això ho fa la funció d'activació.

Les 3 més conegudes per començar:
1. **Step (Funció Esglaó)**: Si $z > 0$, treu $1$. Si $z \leq 0$, treu $0$. (Bona per decisions binaries fàcils, avui dia poc usada per entrenar).
2. **Sigmoid**: Aixafa qualsevol número perquè quedi entre $0$ i $1$. (Bona per a probabilitats).
3. **ReLU (Rectified Linear Unit)**: Si $z$ és negatiu, treu $0$. Si és positiu, treu $z$. (És la més popular a les capes internes perquè és súper ràpida).

---

## 5. Exercicis a mà

### Exercici 1 — Càlcul d'una neurona simple
Imagina que estem avaluant si concedir un crèdit. 
Tenim els següents factors (Entrades $X$):
- $x_1$: Nombre de deutes vigents (Valor = $2$)
- $x_2$: Historial de pagaments correcte? (Valor = $1$ si Sí, $0$ si No. Posem $1$)

Pesos (importància, $W$):
- $w_1 = -3$ (tenir deutes castiga la nota final)
- $w_2 = 4$ (bon historial suma punts)
- Biaix $b = 1$

**Tasques:**
1. Calcula la suma ponderada neta ($z$).
2. Si la neurona empra una funció d'activació **esglaó** (Step), quin serà el resultat final? El crèdit es concedeix (treu $1$) o es denega (treu $0$)?

---

### Exercici 2 — Màgia amb ReLU
Observa la mateixa neurona, però ara els valors d'entrada canvien:
- $X = [0, 1]$ (Cap deute, bon historial).
- Els pesos són els mateixos $W = [-3, 4]$, i el biaix $b = -2$.

**Tasques:**
1. Calcula l'operació $z = X \cdot W + b$.
2. Si apliquem l'activació **ReLU**, quin és l'output de la neurona?
3. Si apliquem l'activació **Sigmoid** (a ull), serà més proper a 0 o a 1?

---

## 6. Exercicis d'ordinador

### Exercici 3 — Joc i visualització amb TensorFlow Playground

El Playground et permet "tocar" una xarxa neuronal de forma visual sense programar.
1. Obre: https://playground.tensorflow.org/
2. En la pestanya "Data" (menú de l'esquerra) tria el primer dataset (grups blau i taronja, dades linials).
3. Treu totes les capes ocultes ('Hidden Layers: 0'). Dóna-li al botó "Play" d'entrenament. Es resol el problema ràpid?
4. Canvia el dataset per al segon (Cercle blau tancat dins l'anell taronja).
5. Deixa "Hidden Layers: 0" i "Play". Què passa? Funciona amb una sola neurona?
6. Ara, afegeix una 'Hidden Layer' (Capa oculta) amb 3 neurones. Canvia l'activació (més amunt) de 'Linear' a 'ReLU'. Prem "Play".
   **Reflexió:** Què permet agrupar el cercle central? Quina diferència fa tenir la capa oculta acompanyada de ReLU contra la Linear?

---

### Exercici 4 — Construir la neurona artificial pas a pas amb NumPy

Implementarem artificialment, exactament el que has fet a mà a l'Exercici 1. Ho realitzarem sense utilitzar llibreries complexes, tan sols operacions vectoritzades amb Numpy.

```python
import numpy as np

# Definim entrades i pesos (com a vectors Numpy)
X = np.array([2, 1])   # deutes=2, bon historial=1
W = np.array([-3, 4])  # pesos assignats (-3 i 4)
b = 1                  # biaix

# 1. Producte escalar
# Mètode de numpy per evitar bucles sumatoris
z = np.dot(X, W) + b

print(f"Suma ponderada (z): {z}")

# 2. Definim funcions d'activació
def step_function(z):
    return 1 if z > 0 else 0

def relu_function(z):
    return max(0, z)

# 3. Aplicar activació
output_step = step_function(z)
output_relu = relu_function(z)

print(f"Resultat amb Step: {output_step}")
print(f"Resultat amb ReLU: {output_relu}")
```

**Tasques:**
1. Copia i enganxa l'exercici a un Notebook o intèrpret local. Concideixen els resultats amb el que havies calculat a mà?
2. Afegeix un $X2 = [0, 1]$. Ajusta la programació per realitzar els dos individus de cop utilitzant una matriu per $X$. Pots fer l'$np.dot$ amb una matriu vs un vector? (Investiga la funció de *broadcasting* d'aprenentatges anteriors amb Numpy).

---

## 7. Idees clau de la sessió

- Tota la "màgia" del Deep Learning comença amb una entitat minúscula coneguda com a **neurona o perceptró**, que realitza una senzilla combinació lineal (*sumatori_ponderat + biaix*).
- Les **funcions d'activació** són crítiques, sense una eina com la ReLU o la *Sigmoid*, les xarxes neuronals només aprendrien línies rectes i l'aprenentatge patiria un límit sever.
- Agrupar neurones en una mateixa ubicació forma les famoses **capes (layers)**. A les pròximes sessions veurem com interrelacionar diverses capes per donar pas al veritable *Multi-Layer*(Perceptron).
