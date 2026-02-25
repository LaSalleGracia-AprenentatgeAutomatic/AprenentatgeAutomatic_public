# 🔍 Activitat: Outlier-Hunters


## 🧩 Tasca

En grups de 2 o 3:

### **1. Busca un dataset públic amb valors numèrics**
Pots fer servir:
- Kaggle (recomanat): https://www.kaggle.com/datasets  
- UCI Machine Learning Repository  
- OpenML  
- Google Dataset Search  

---

### **2. Escolliu UNA variable numèrica**
Per exemple:
- alçada  
- pes  
- temperatura  
- ingressos  
- edats  
- temps de trajecte  
- nombre de vendes  
- preus d’habitatges  

---

### **3. Detecteu outliers**
Utilitzeu eines bàsiques:
- Boxplot  
- Z-score  
- Min/Max  
- Scatter (opcional)

Identifiqueu **quins valors s’allunyen clarament del patró**.

---

## 📝 4. Responeu aquestes preguntes a l’informe

### **A) Identificació**
1. Quin dataset heu triat? (Nom + enllaç)
2. Quina variable numèrica heu analitzat?
3. Quins outliers heu detectat? (llista o captura)

---

### **B) Interpretació d’outliers**
Per cada valor outlier detectat:

1. **Pot ser un cas real extrem?**  
   - Justifiqueu amb lògica (p. ex. "Una persona pot fer 2,20 m, encara que és molt poc freqüent").
2. **Té sentit en el context del dataset?**  
   - Té la unitat correcta?  
   - És coherent amb la resta de valors?  
3. **Podria ser un error de recollida de dades?**  
   - Un “0 kg”?  
   - Una edat “250”?  
   - Una temperatura “-300”?  
4. **El consideraríeu vàlid, invàlid o dubtós?**  
   - Expliqueu el motiu.

---

### **C) Decisions de preprocesat**
1. Què faríeu amb cada outlier?
   - 🔧 Eliminar-lo  
   - 🔄 Corregir-lo  
   - 🧮 Imputar-lo  
   - ✔️ Mantenir-lo  
2. Quina justificació té aquesta decisió?  
3. Com podria afectar aquesta decisió a un futur model de Machine Learning?
