BEGIN {
    # Configuración de separadores
    FS = ",";       # Entrada separada por comas (CSV)
    OFS = "|";     # Salida separada por tabulaciones
}

{
    # $1 = ID del Documento
    # $2 = Texto del contenido
    
    # 1. Limpiar cualquier espacio o retorno de carro en el ID del documento ($1)
    gsub(/[[:space:]\r\n]/, "", $1);
    
    # 2. Convertir todo el texto a minúsculas
    texto = tolower($2);
    
    # 3. Eliminar signos de puntuación
    gsub(/[.,:;!?]/, "", texto);
    
    # 4. Dividir el texto en un array llamado 'palabras'
    n = split(texto, palabras, " ");
    
    # 5. FIX FINAL: Imprimir la palabra solo después de limpiarla
    for (i = 1; i <= n; i++) {
        # Copiamos la palabra del array
        palabra = palabras[i];
        
        # ELIMINAR ESPACIOS AL PRINCIPIO Y AL FINAL DE LA PALABRA
        gsub(/^[[:space:]]+|[[:space:]]+$/, "", palabra); 
        
        # Si la palabra ya limpia no está vacía, la imprimimos
        if (palabra != "") {
            print palabra, $1;
        }
    }
}