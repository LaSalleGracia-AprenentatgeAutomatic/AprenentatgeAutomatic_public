🎓 GUIA DOCENT — Sessió 3: Normalització, Correlació i EDA
🎯 Objectiu docent de la sessió

Explicar quan i per què normalitzem dades.
Comprendre les relacions entre variables amb la correlació.
Interpretar gràfics d’exploració per detectar patrons, problemes i oportunitats.

🧱 1. Normalització i estandardització — Per què són imprescindibles?
🔥 Explicació conceptual (amb metàfora potent)
🎢 Metàfora del parc d’atraccions

Imagina que tens tres atraccions amb files d’alçada totalment diferents:
Atracció A → 0–2 metres
Atracció B → 0–120 metres
Atracció C → 0–500 metres

Si les vols comparar tal qual, la tercera atracció dominarà totes les mesures, perquè és molt més gran.
En ML passa EXACTAMENT això: les variables amb valors més grans “aplasten” les altres.

Normalitzar és posar totes les atraccions en una escala comuna, com si convertíssim totes les altures en un percentatge del 0 al 100.

📏 1.1. Normalització (Min-Max Scaling)
Fa que les dades quedin entre 0 i 1.
Visualment:
Distància original:     50m —— 200m —— 500m —— 1000m  
Distància normalitzada: 0.05 — 0.20 — 0.50 — 1.00

Exemple visual potent

Mostra dues gràfiques:
Dades originals
Escala completament descompensada: les variables petites “desapareixen”.

Dades normalitzades
Tot entre 0 i 1 → totes igual de rellevants.

❄️ 1.2. Estandardització (Z-Score Scaling)
Fa que la variable tingui:
Mitjana = 0
Desviació estàndard = 1

👉 És com posar totes les variables dins una distribució “normal” comparable.
Exemple visual
Mostra un histograma abans i després:
Abans: desplaçat cap a la dreta
Després: centrat a 0

Quan usar cadascun?
Situació	                    Normalització	Estandardització
Dades amb rang limitat	            ✔️	                ❌
Algoritmes geomètrics (KNN, SVM)	✔️	                ✔️
Models lineals	                    ❌	               ✔️
Xarxes neuronals	                ✔️	                ✔️



🔗 2. Correlació — Com identifiquem relacions amagades?
💥 Introducció amb un exemple impactant

Exemple real i cridaner:
"El consum de gelats correlaciona amb els ofegaments a l’estiu."

👉 Això NO vol dir que els gelats causin ofegaments.
Correlació ≠ causalitat.

Imatges recomanades
Un gràfic amb dues línies: temperatura i consum de gelats.
Una tercera línia amb “ofegaments”.
Totes tres pugen a l’estiu → correlació espúria.

💡 Explicació simple
Correlació de Pearson

Mesura si dues variables pugen o baixen juntes.

+1 → van juntes perfectament

-1 → quan una puja, l’altra baixa

0 → cap relació lineal

🎯 Exemple visual potent amb dades del curs
Exemple: altura vs pes

Mostra un scatterplot:

Núvol de punts inclinat cap amunt → correlació positiva clara.

Exemple: edat vs ingressos

Tot i que és sintètic, la relació és bastant visible.

Exemple: ingressos vs target (benestar)

Matriu de correlació: colors intensos per captar l’atenció.

📊 Heatmap cridaner

El heatmap és la manera més impactant d’ensenyar correlacions:

Colors blau profund per valors negatius

Colors vermell intens per valors positius

Visualment espectacular i fàcil d’interpretar:

👉 "On veieu vermell, hi ha relació forta.
On veieu blau, relació inversa.
On hi ha blanc, no hi ha res."

🔍 3. Exploració visual de dades (EDA)
🎨 Objectiu

Aquesta part és on l’alumnat veu “la bellesa” de les dades.

🔹 3.1. Histogrames — Veure la forma de la distribució

Exemple interessant: ingressos

Molt asimètric

Molts valors baixos, pocs de molt alts

Pot requerir transformació logarítmica
(efecte visual espectacular si es mostra abans/després)

Impacte visual

Abans (skewed, cap a la dreta)

Després de log() (molt més equilibrat)

🔹 3.2. Scatter plots — Relacions entre dues variables
Exemples visuals cridaners:

altura vs pes
Perfecte per mostrar una relació lineal marcada.

edat vs target
Més dispers → explica la debilitat de la correlació.

🔹 3.3. Boxplots — Detectar outliers en un instant
Exemple impactant:

ingressos
Alguns punts molt separats → outliers.

Reflexió cridanera:

“Aquests punts representen persones estranyes o errors?
Si no ho sabem, no podem fer ciència.”

🔹 3.4. Pairplot — La “radiografia completa” del dataset

Aquest gràfic és un wow moment visual:

Permet veure totes les relacions de cop

Ideal per concloure la sessió

🎤 4. Moment docent clau: interpretació guiada

Proposa preguntes impactants per fer pensar:

1. Si només poguéssim triar 2 variables per predir el benestar (target), quines serien? Per què?
2. Quina variable eliminaries del model?
3. Quin gràfic us ha revelat una informació que no esperàveu?
4. Alguna correlació us sembla sospitosa o massa perfecta?

Aquestes preguntes provoquen participació i crítica.

🧩 5. Conclusió memorable

Tanca amb una frase que resumeixi la sessió:

“Els models d’IA no són més intel·ligents que les dades que els alimenten.
La qualitat de les dades és la qualitat del model.”