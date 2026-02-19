---
layout: default
title: FAQ
permalink: /faq/
nav_order: 8
---

# Preguntes Freqüents (FAQ)

## Sobre el Curs

### Quin es el nivell del curs?

Intermedi-avançat. Requerim coneixements bàsics de programació en Python i estadística.

### Hi ha prerequisits?

Sí:
- Python bàsic (variables, funcions, bàsic de libreries)
- Estadística bàsica (mitjana, variància, distribucions)
- Àlgebra lineal elemental (matrius, vectors)

---

## Sobre les Pràctiques

### Puc fer la pràctica en grup?
Consultar al professor depenent de la pràctica.

### Quin format han de tenir els lliuraments?

- **Notebook Jupyter** (.ipynb) o **Script Python** (.py)
- **Informe opcional** en format PDF
- Codi comentat i ben estructurat

### Puc lliurar tard?

No sense justificació. Es penalitzarà si no es té un motiu de pes

---

## Sobre les Mètriques i Avaluació

### Quin és el millor model sempre?

No n'hi ha. Depèn del problema. Per això comparem models amb mètriques apropriades.

### Per què Accuracy no és suficient en classificació?

Perquè és dolent en datasets desbalancejats. Per exemple, si el 95% és d'una classe, accuracy és 95% però el model pot no encertar cap d'altres classes.

### Quan uso Precision vs Recall?

- **Precision**: Quan volem pocs falsos positius (ex: diagnòstics mèdics)
- **Recall**: Quan volem pocs falsos negatius (ex: detecció de fraude)
- **F1-Score**: Quan volem balanç entre tots dos

---

## Sobre Python i Libreries

### Com instal·lo scikit-learn?

```bash
pip install scikit-learn
```

O si uses Anaconda:

```bash
conda install scikit-learn
```

### Puc usar altres libreries com TensorFlow?

Sí, però el curs es centra en scikit-learn. Altres libreries són bonus.

### Quina versió de Python necesito?

Python 3.8 o superior. Recomanem 3.10+.

---

## Sobre Dubtes Tècnics

### On puc preguntar dubtes?

1. Consulta els materials i FAQ
2. Pregunta a classe
3. Envia email al professor

### Com contacto amb el professor?

Email: jcortes@lasalle.cat

---

## Sobre Recursos Computacionals

### Necesito GPU?

No. Tot funciona amb CPU. GPU es opcional per models més complexes.

### Puc usar Google Colab?

Sí, és gratuït i té suficients recursos per aquest curs.

### Puc usar la meva màquina?

Sí. Anaconda + Jupyter és gratuït i funciona bé en Windows/Mac/Linux.