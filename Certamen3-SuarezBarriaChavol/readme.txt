Certamen 3 Lenguajes de Programación

Grupo Integrantes:
Graciela Suárez
Romily Barría
Camilo Chavol

Enlace al Repositorio Git:
https://github.com/CamiloChavol/Certamen3.git

-----------------------------------------------------------------
  Descripción del Proyecto
-----------------------------------------------------------------
Este proyecto implementa un Motor de Búsqueda de texto completo utilizando
la estructura de datos de Índice Invertido. La solución es modular e integra
distintos paradigmas y lenguajes según lo solicitado:

1.  Indexación (AWK): Se utiliza AWK para procesar el dataset (CSV), normalizar
    el texto (minúsculas, sin puntuación) y generar pares (palabra, id_doc).
    
2.  Limpieza (Python + Recursividad): Se implementó una función recursiva
    ('filtrar_recursivo') que recorre el índice crudo y elimina las palabras
    definidas en 'stopwords.txt', imprimiendo en consola cada eliminación.
    
3.  Búsqueda (Python): Se carga el índice limpio en memoria y se realizan
    consultas utilizando intersección de conjuntos (lógica AND), tal como
    se especifica en las figuras del enunciado.

-----------------------------------------------------------------
  Archivos
-------------------------------------------------
- dataset.csv       : Archivo de datos fuente (Documentos).
- stopwords.txt     : Lista de palabras a excluir.
- indexador.awk     : Script de indexación (usado por el limpiador Python).
- limpiador.py      : Script principal. Realiza indexación, limpieza recursiva y genera el índice maestro.
- buscador.py       : Motor de búsqueda interactivo.
- Makefile          : Automatización del flujo de trabajo.

-----------------------------------------------------------------
  Instrucciones de Ejecución
-----------------------------------------------------------------
Para la ejecución, la herramienta 'make' no es obligatoria, pero el flujo es el siguiente:

1- Requisitos
- Tener instalado Python 3.
- Archivo 'gawk.exe' (o 'awk.exe') debe estar disponible en la carpeta o en el PATH.

2- Navegar a la Carpeta del Proyecto
Por ejemplo, en el caso de uno de nuestros integrantes del grupo :
cd C:\Users\faith\OneDrive\Desktop\Certamen3-SuarezBarriaChavol

3- Opción A: Ejecución Manual (Recomendada para depuración)
Se ejecutan los pasos directamente en la terminal.

1.  Indexar (AWK): Genera index_raw.txt :
    .\gawk.exe -f indexador.awk dataset.csv > index_raw.txt
    

2.  Limpiar/Procesar (Python Recursivo): Genera index_master.txt :
    python limpiador.py
    

3.  Buscar: Inicia el motor de búsqueda interactivo:
    python buscador.py
    

  Opción B: Ejecución Automática (Si 'make' está instalado)
El Makefile automatiza los 3 pasos anteriores.

1.  Abrir terminal en la carpeta del proyecto.
2.  Ejecutar :
    make run
    

 4. Pruebas de Funcionamiento
Una vez que el buscador esté activo, ingrese las siguientes consultas (sin comillas):

| Consulta              | Documentos Encontrados | Lógica                               |
------------------------------------------------------------------------------------------------------------------
| perro                    | 1, 3, 5                              | Término simple.                |
| perro casa            | 1, 5                                  | Intersección (AND Lógico). |
| gato casa arbol    | 2                                      | Triple Intersección.             |

| salir                     | Cierra el programa.           |                                          |
