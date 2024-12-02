# Amazon Recommender System Project


## **Introducción**

### **Caso de estudio**
El análisis de reviews de usuarios en plataformas e-commerce, como Amazon, permite a las empresas comprender mejor la percepción de sus productos y servicios. Por lo que, este estudio se centra en clasificar las reviews de Gift Cards de Amazon del año 2023 como positivas o negativas, utilizando técnicas NLP y machine learning. Asimismo, el objetivo es implementar un modelo que ayude a identificar patrones y tendencias en los comentarios de los usuarios, facilitando la toma de decisiones estratégicas para los vendedores.

### **Justificación**
La clasificación automática de reviews de Gift Cards de Amazon es vital, ya que las opiniones de los usuarios son determinantes para la percepción de los productos y servicios. Ante esto, el presente trabajo permite a las empresas identificar patrones y tendencias, de tal manera que puedan tomar las mejores decisiones empresariales para sus productos. Además, proporciona a los consumidores una forma estructurada y accesible de evaluar la calidad de los productos. Finalmente, el uso de tecnicas de NLP y Machine Learning, garantizan un alto grado de aprovechamiento de un dataset actualizado, de esta forma se podra ofrecer una solución escalable y automatizada.

## **Dataset**
### Amazon Reviews'23

### **Descripción**

El dataset Amazon Reviews 2023 es un recurso de gran escala que contiene reseñas de productos de Amazon junto con información extensa en metadatos y enlaces entre usuarios y productos. Este fue diseñado para la investigación en sistemas de recomendación e interpretación del lenguaje natural.

### **Origen**

Este dataset fue recopilado por McAuley Lab y cubre interacciones desde mayo de 1996 hasta septiembre de 2023, siendo una versión ampliada y mejorada de ediciones anteriores.

**Versiones anteriores**

|Año|#Review|#User|#Item|#R_Token|#M_Token|#Domain|Timespan|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
2013|34.69M|6.64M|2.44M|5.91B|–|28|Jun’96 - Mar’13
2014|82.83M|21.13M|9.86M|9.16B|4.14B|24|May’96 - Jul’14
2018|233.10M|43.53M|15.17M|15.73B|7.99B|29|May’96 - Oct’18
2023|571.54M|54.51M|48.19M|30.14B|30.78B|33|May’96 - Sep’23

<sub><sup>Tablero extraído de Amazon Reviews'23</sup></sub>

### **Tamaño**

**Para el dataset de Gift_Cards**

**Reviews**

- Tamaño aproximado por línea: 233 B.
- Cantidad de líneas: 152,410.
- Peso total estimado: ~35.5 MB.

**Metadata**
- Tamaño aproximado por línea: 2.33 KB.
- Cantidad de líneas: 1137.
- Peso total estimado: ~2.65 MB.

## **Dificultades técnicas**
Dificultades técnicas que tuvimos fue:
* La limpieza de los datos del campo "text". Estos tenian mucho ruido, como los espacios, emojis, negritas, etiquetas HTML, etc.
* Desbalanceo del dataset, estos tienen mas reviews positivas que negativas, lo cual puede afectar en la etapa de entrenamiento del modelo, por lo que es vital filtrarlo de manera adecuada y equitativa
* Manejo de lenguaje, ya que el dataset contiene variados textos en diferentes idiomas, lo cual podria afectar el etiquetado de nuestro modelo a traves de la LLM.
* Implementacion del modelo LLM para el etiquetado de nuestro dataset, tanto en Pandas como Dask.

## **Herramientas empleadas**
- MongoDB
- Datalake
- Dask y Pandas
- LLM y Random Forest
- Seguimiento de experimentos (W&B)

## **Cómo ejecutar el proyecto**
1. Tener instalado Python 3.12 
2. Instalar las dependencias a traves del requirements.txt (revisar archivo ''notebook.ipynb'')
3. Crear una base de datos local en MongoDB Compass
4. Crear el diccionario ''gift-cards''
5. Crear el diccionario ''meta-gift-cards''
6. Correr todo el archivo ''notebook.ipynb''

## **Arquitectura del proyecto**

### **Diagrama**

### **Descripción**

## **Proceso ETL**

### **Extracción**
La extraccion de los datos se llevo a cabo de manera automatizada a traves de un link de descarga en la que se obtiene un archivo ''gz'', posteriormente lo descomprimimos y guardamos en la carpeta ''data''. Asimismo, para la eleccion de un correcto grupo de datos del dataset, se realizo un filtrado a traves de una consulta en MongoDB en la cual garantizamos que las reviews no contengan anomalias o data atipica.

### **Transformación**
La transformacion de los datos se lleva a cabo en la limpieza de estos para su posterior carga, en este apartado nos encargamos de eliminar el ruido en el atributo "text", estos contenian etiquetas HTML, emojis, negritas, espacios, exceso de caracteres especiales.

### **Cargado**
El cargado de nuestro dataset se lleva a cabo utilizando MongoDB, herramienta que nos facilito el filtrado para escoger el grupo de datos que llevaremos a cabo durante todo el estudio y posterior entrenamiento de nuestro modelo.

## **Resultados obtenidos**

### **Análisis**

## **Dificultades**

## **Conclusiones**

### **Posibles mejoras**


