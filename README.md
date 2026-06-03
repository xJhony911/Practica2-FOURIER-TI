# Analizador de Series de Fourier y Procesamiento de Señales 📊🌀

Este repositorio contiene la solución computacional y el informe teórico-práctico correspondientes a la **Práctica de Laboratorio Nº 2: Series de Fourier**. El proyecto implementa algoritmos en Python para el cálculo, análisis espectral y visualización interactiva de señales canónicas, análisis de convergencia y transformadas discretas.

---

## 🚀 Ejecución en Google Colab

Para facilitar la revisión del código y observar las gráficas interactivas en tiempo real sin necesidad de realizar una instalación local, puedes ejecutar el entorno interactivo directamente en Google Colab haciendo clic en el siguiente botón:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/14Q3X64nWOoJtYCWXPdEMMdH1G0kSIdtV?usp=sharing)
---

## 🏫 Información Institucional

* **Institución:** Escuela Superior Politécnica de Chimborazo (ESPOCH).
* **Facultad:** Facultad de Informática y Electrónica.
* **Carrera:** Tecnologías de la Información.
* **Asignatura:** Matemáticas Avanzadas / Procesamiento de Señales.
* **Docente:** Lic. Miriam Avila P. Mg..
* **Periodo Académico:** 2 de marzo - 15 de julio de 2026.

### 👥 Integrantes (Grupo 1)
* Jonathan Steven Acosta Aldaz
* Kevin Andres Morales Abril
* Kevin Gabriel Chinlle Yunga

---

## 📝 Descripción del Proyecto

El proyecto combina deducciones analíticas matemáticas con simulaciones computacionales robustas escritas en Python. El programa principal está dotado de un menú interactivo en consola que permite ejecutar de forma independiente cuatro grandes bloques temáticos de análisis de señales:

### 🔍 Contenido y Actividades Desarrolladas

1. **Actividad 1: Cálculo y Visualización de Series de Fourier de Señales Canónicas 📐**
   * Reconstrucción matemática y gráfica de 4 señales fundamentales: Onda Cuadrada, Onda Triangular, Diente de Sierra y Onda de Seno Rectificado (`|sin(t)|`).
   * Evaluación de la convergencia visual utilizando diferentes números de armónicos ($N = 1, 3, 5, 11, 51$).
   * Simulación y estudio detallado del **Fenómeno de Gibbs**, verificando la sobreoscilación del $\approx 8.9\%$ en los puntos de discontinuidad.

2. **Actividad 2: Espectro de Amplitud y Fase - Análisis Espectral 📈**
   * Obtención y mapeo de los coeficientes en su Forma Exponencial Compleja ($c_n$).
   * Generación de espectros de amplitud bilateral ($|c_n|$) y espectros de fase ($\angle c_n$) en el intervalo de armónicos $n \in [-15, 15]$.
   * Verificación numérica de la **Identidad de Parseval** para la conservación de la energía, comprobando analíticamente que el error relativo disminuye por debajo del umbral del $1\%$ para $N \ge 20$.

3. **Actividad 3: Función Impulso Unitario y Aproximación Gaussiana ⚡**
   * Estudio del comportamiento del impulso de Dirac ($\delta(x)$) mediante el uso de funciones gaussianas paramétricas estrechas ($f_\epsilon(x)$) cuando $\epsilon \to 0$.
   * Demostración computacional y gráfica de la convergencia hacia un **Espectro de Amplitud Plano** ($1/\pi$), donde todas las frecuencias poseen la misma densidad espectral de energía.

4. **Actividad 4: Forma Compleja, Simetrías Especiales y DFT 🔄**
   * Identificación algebraico-gráfica de la "Simetría Escondida" tras remover componentes continuas (DC) en funciones compuestas.
   * Implementación de la **Transformada Discreta de Fourier (DFT)** de 8 puntos para una señal cuadrada discreta utilizando la librería optimizada `numpy.fft`.
   * Análisis comparativo de los resultados del dominio discreto frente a los coeficientes de la serie continua tradicional.

---

## 🛠️ Tecnologías y Librerías Utilizadas

El entorno de desarrollo está basado puramente en Python 3 y hace uso de herramientas científicas estándar de la industria:
* **NumPy:** Para la manipulación eficiente de matrices numéricas, operaciones trigonométricas integradas y transformadas rápidas (`np.fft`).
* **Matplotlib (PyPlot):** Para el renderizado de figuras científicas multipanel, subgráficas de convergencia y diagramas de espectro discreto (`stem`).

---

## 📁 Estructura del Repositorio

* `Grupo_1.py`: Script ejecutable que contiene el núcleo algorítmico, las funciones de las señales canónicas, las rutinas de graficación y la interfaz del menú interactivo por consola.
* `Grupo_1_práctica_2.pdf`: Informe formal de laboratorio que documenta en detalle el marco teórico, los desarrollos de las ecuaciones analíticas paso a paso, los diagramas de flujo y las conclusiones obtenidas.

---

## 💻 Instalación y Ejecución Local

Si deseas clonar el repositorio y correr el proyecto en tu máquina local de forma nativa, sigue estos pasos:

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/xJhony911/Practica2-FOURIER-T
   cd TU_REPOSITORIO
