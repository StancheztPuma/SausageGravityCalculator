# Función para calcular la gravedad en base a la anchura de la salchicha, peso y altura
def calcular_gravedad(anchura, peso, altura):
    # Fórmula inventada para este ejemplo
    gravedad_aparente = (anchura * peso) / (altura + 1)
    
    return gravedad_aparente

# Pedir al usuario la anchura de la salchicha, el peso y la altura desde la que fue lanzada
anchura = float(input("Introduce la anchura de la salchicha en cm: "))
peso = float(input("Introduce el peso de la salchicha en gramos: "))
altura = float(input("Introduce la altura desde la que fue lanzada en metros: "))

# Calcular la gravedad
gravedad_aparente = calcular_gravedad(anchura, peso, altura)

# Mostrar el resultado
print(f"La gravedad 'aparente' calculada es: {gravedad_aparente:.2f} unidades imaginarias")
