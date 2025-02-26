🏨 ETL de Datos de Hoteles y Eventos en Madrid

📖 Descripción

Nuestra empresa se dedica al sector hotelero en Madrid. Se nos ha proporcionado un archivo en formato Parquet que contiene información sobre reservas de hoteles, incluyendo datos de hoteles propios y de la competencia. Nuestro objetivo es extraer, transformar y cargar (ETL) estos datos para generar insights relevantes.

Este proyecto analiza los datos históricos de la ejecución de ingresos entre 2013 y 2021 con los siguientes objetivos:

    Identificar patrones
    Detectar áreas problemáticas donde la recaudación ha sido consistentemente menor a lo previsto.
    Proponer recomendaciones basadas en los datos que ayuden a mejorar la precisión de las previsiones y la eficiencia de la recaudación.

📁 Estructura del Proyecto

    ├── datos/               
        |──data_raw          # Datos crudos
        |──data_clean        # Datos procesados
    ├── notebooks/           # Jupyter notebooks con el código limpio  
    |── notebooks pruebas    # Jupyter notebooks con pruebas    
    ├── src/                 # Archivo con funciones de soporte
    ├── Creacion BBDD/       # Script para la creación de la base de datos
    ├── README.md            # Descripción del proyecto

🛠️ Instalación y Requisitos

- Python: Versión 3.13.0
- Jupyter Notebook (ejecutado a través de VSCode)
- postgres mediante DBeaver
- Librerías: 
    - pandas 
    - numpy 
    - seaborn 
    - matplotlib
    - requests
    - selenium
    - time
    - webdriver-manager
    - psycopg2

Para más detalles puedes consultar el archivo requirements.txt

📊 Resultados y Conclusiones
      - Los hoteles de la competencia son más baratos y tienen mayor valoración que los hoteles de nuestra marca. Se debería analizar las causas de la baja valoración.
      - Los días 4 y 6 de febrero se produjeron altos picos de demanda en las reservas, mientras que el día 8 fue el día de menor demanda. Dado que no hay demasiados     datos temporales no se detecta relación entre días de la semana y demanda.


🔄 Próximos Pasos

    Generar archivos .py con el código organizado en funciones.

🤝 Contribuciones

Las contribuciones son bienvenidas. Si deseas mejorar el proyecto, por favor abre un pull request o una issue. 

✒️ Autores y Agradecimientos

Marta María Llordén Alonso - @MartaM1206