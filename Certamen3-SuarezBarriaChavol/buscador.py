import sys

def cargar_indice_invertido(ruta):
    """
    Carga el índice invertido en un Diccionario de Python.
    Aplica limpieza defensiva al cargar las claves.
    """
    indice = {}
    try:
        # LECTURA: Usamos 'utf-8-sig' y el separador Pipe '|'
        with open(ruta, 'r', encoding='utf-8-sig') as f:
            for linea in f:
                partes = linea.strip().split('|') 
                if len(partes) < 2: continue
                
                palabra = partes[0].strip()
                doc_id = partes[1].strip()
                
                if palabra not in indice:
                    indice[palabra] = set()
                indice[palabra].add(doc_id)
        return indice
    except FileNotFoundError:
        print("Error crítico: No se encontró el índice maestro. Asegúrese de ejecutar los pasos 1 y 2.")
        sys.exit(1)

def buscar(consulta, indice):
    """
    Realiza la búsqueda intersectando listas de posteo (Lógica AND).
    """
    palabras_consulta = consulta.lower().strip().split() 

    if not palabras_consulta:
        return set()
    
    primera_palabra = palabras_consulta[0] 
    documentos_resultado = indice.get(primera_palabra, set())
    
    for palabra in palabras_consulta[1:]: 
        key_limpia = palabra.strip()
        docs_siguiente = indice.get(key_limpia, set())
        documentos_resultado = documentos_resultado.intersection(docs_siguiente)
        
    return documentos_resultado

def main():
    print(">>> MOTOR DE BÚSQUEDA (ÍNDICE INVERTIDO) <<<")
    indice = cargar_indice_invertido("index_master.txt")
    print(f"Índice cargado en memoria. {len(indice)} términos únicos.\n")
    
    while True:
        try:
            consulta = input("Ingrese su búsqueda (o 'salir'): ")
            if consulta.lower() == 'salir':
                break
            
            resultados = buscar(consulta, indice)
            
            if resultados:
                lista_res = sorted(list(resultados))
                print(f"RESULTADO: Documentos encontrados -> {', '.join(lista_res)}")
            else:
                print("RESULTADO: No se encontraron documentos con esos términos.")
                
            print("-" * 40)
            
        except KeyboardInterrupt:
            break
            
    print("\nFin del programa.")

if __name__ == "__main__":
    main()