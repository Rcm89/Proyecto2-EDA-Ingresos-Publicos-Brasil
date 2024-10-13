
# Análisis exploratorio sobre datos de ingresos públicos de Brasil del 2013 al 2021.
![Descripción de la imagen](imagenes/Rio_de_Janeiro.jpg)

Este proyecto consiste en la realización de un análisis exploratorio de datos (EDA) sobre un conjunto de datos de ingresos gubernamentales de Brasil que contiene información de diferentes categorías económicas, organizaciones y años entre 2013 y 2021. El objetivo principal es identificar tendencias en los ingresos, su evolución a lo largo del tiempo y las diferencias entre los valores previstos y recaudados.

## Objetivos del Proyecto

Los objetivos principales del proyecto son:

1. **Limpieza de datos**: Se parte de nueve archivos de tipo `csv` distintos cuya cosistencia hay que comprobar para despues concatenerlos y generar el archivo principal sobre el cual trabajaremos.

2. **Análisis Exploratorio de Datos (EDA)**: Examinar la relación entre diferentes variables clave, centrando la atencion en las categorías económicas para tratar de patrones o discrepancias significativas. En este análisis se incluye generar visualizaciones que ayuden a encontrar y mostrar los patrones y tendencias presentes en el Análisis

3. **Conclusiones y Recomendaciones**: Extraer de los datos una serie de conclusiones concretasque idenetifiquen las tendencias y discrepancias encontradas en el análisis y en base a estas conclusioens hacer una serie de recomendaciones de mejora.


## Resumen del proyecto

-En primer lugar se cargaron los datos, se hizo una exploración de los mismos y se concatenaron en uno solo, que es el archivo principal sobre el que se ha basado nuestro análisis.

- El siguiente paso fue una limpieza del archivo de datos, traduciendo del portugues al español los nombres de las columnas, eliminando duplicados y tratando valores nulos categóricos (unos se pudieron rellenar a traves de las columnas de codigos y otros se eliminaron), mientras que los numéricos se rellenaron con la mediana en profundidad de los valores nulos.

- El análisis se centró en tres puntos principales: distribución de ingresos por categoría económica, evaluación de las tendencias a lo largo del tiempo e identificación de discrepancias. En esta etapa del análisis se integraron las visualizaciones con la doble finalidad de contribuir a la elaboración del analisis y de reperesentarlo de una forma visualmente accesible de cara a posibles lectores del mismo.

## Conclusiones y Recomendaciones

- Se elaboran una serie de conclusiones extraidas del analisis, particularmete de la distribuncion de ingresos por categoría económica, la evaluación de tendencias a lo largo del tiempo (tanto años, como meses) y en la identificación de discrepancias.

- Así mismo, en base a esas conclusiones se hacen una serie de recomendaciones de cara a optimizar la ejecución de ingresos en Brasil

- Invito al lector a entrar en el repositorio para leer el análisis y las conclusiones



## Estructura del Proyecto

El proyecto está organizado de la siguiente manera:

- **datos/**: Carpeta que contiene los archivos `.csv` de ingresos de cada año, así como el archivo principal de nuestro análisis ftuo de la concatenación de los csv de cada año tras haber sido limpiado. Se encuentra bajo el nombre de "concatenado_limpio."csv

- **notebooks/**: Carpeta que contiene los archivos `.ipynb` sobre los cuales hemos trabajado los datos en el siguiente orden:
  - `1-notebook_limpieza_de_datos.ipynb`. En el que se cargan los csv, se concatenan y se hace la limpieza de datos
    
  - `2-notebook_EDA.ipynb`. En el que se lleva acabo el Analisis EDA, incluidas las visualizaciones, y se extraen las conclusiones y recomendaciones.

- **src/**: Carpeta que contiene los archivos `.py` externos usados para definir las funciones que se llaman desde los notebooks.
  - `support.py`


## Instalación y Requisitos
Este proyecto usa Python 3.12 y requiere importar las siguientes librerías:
- numpy
- pandas
- matplotlib.pyplot
- seaborn

Para visualizar el proyecto en tu ordenador, sigue estos pasos:

1. **Clona el repositorio**:
   ```bash
   git clone [URL del repositorio]
   
2. **Navega a la carpeta del proyecto**:
   ```bash
   cd Proyecto2-EDA-Ingresos-Publicos-Brasil/notebooks

3. **Ejecutar los archivos**:
   Deberás ejecutar cada notebook en el orden definido para poder ir viendo el proceso de unión, limpiado y análisis de los datos.
