import sys
import csv
import re

# Aumentamos el límite de recursión por seguridad
sys.setrecursionlimit(20000)

def cargar_stopwords(ruta):
    """Carga las stopwords."""
    try:
        with open(ruta, 'r', encoding='utf-8') as f:
            return set(linea.strip() for linea in f)
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo de stopwords en la ruta especificada.")
        sys.exit(1)

def tokenizar_y_limpiar(texto_crudo):
    """Limpia el texto, elimina puntuación y tokeniza."""
    texto = texto_crudo.lower()
    # Eliminar puntuación
    texto = re.sub(r'[.,:;!?]', '', texto)
    # Devolver lista de palabras (eliminando espacios extra)
    return texto.split()

def procesar_y_filtrar_recursivo(lineas_csv, stopwords, index=0, indice_filtrado=[]):
    """
    FUNCIÓN RECURSIVA (Requerimiento 4)
    Procesa las líneas del CSV, tokeniza, y filtra stopwords.
    """
    # Caso Base
    if index == len(lineas_csv):
        return indice_filtrado

    try:
        doc_id = lineas_csv[index][0].strip()
        texto = lineas_csv[index][1]
        
        palabras = tokenizar_y_limpiar(texto)
        
        for palabra in palabras:
            if not palabra: continue

            if palabra in stopwords:
                print(f"[Stopword Eliminada] '{palabra}' del documento {doc_id}")
            else:
                # Agregamos la palabra limpia y el ID usando el separador '|'
                indice_filtrado.append(f"{palabra}|{doc_id}")
        
    except IndexError:
        pass # Ignoramos líneas mal formadas

    # Llamada recursiva al siguiente índice
    return procesar_y_filtrar_recursivo(lineas_csv, stopwords, index + 1, indice_filtrado)


def main():
    entrada_csv = "dataset.csv"
    salida_indice = "index_master.txt"
    
    print(" Iniciando Indexación y Limpieza Recursiva (Solo Python)")
    stopwords = cargar_stopwords("stopwords.txt")
    
    try:
        # Usamos 'r' y 'utf-8-sig' para leer el CSV de forma segura
        with open(entrada_csv, 'r', encoding='utf-8-sig') as f:
            # Usamos el módulo CSV de Python para un parseo seguro
            lector = csv.reader(f)
            lineas_csv = list(lector)
            
        # Iniciamos el proceso recursivo en el contenido del CSV
        lineas_limpias_para_archivo = procesar_y_filtrar_recursivo(lineas_csv, stopwords)
        
        with open(salida_indice, 'w', encoding='utf-8') as f:
            for linea in lineas_limpias_para_archivo:
                f.write(linea + "\n")
                
        print(f"--- Proceso finalizado. Índice limpio guardado en '{salida_indice}' ---\n")
        
    except FileNotFoundError:
        print(f"Error: No se encontró {entrada_csv}.")
        sys.exit(1)

if __name__ == "__main__":
    main()