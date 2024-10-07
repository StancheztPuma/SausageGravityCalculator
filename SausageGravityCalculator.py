# SausageGravityCalculator.py

def calcular_gravedad(anchura, peso, altura):
    """
    Función que calcula la gravedad en base a la anchura, peso y altura.
    Parámetros:
    - anchura (float): La anchura de la salchicha en cm.
    - peso (float): El peso de la salchicha en gramos.
    - altura (float): La altura desde la que se lanza en metros.
    
    Retorna:
    - float: Gravedad 'aparente' calculada.
    """
    gravedad_aparente = (anchura * peso) / (altura +  1)
    return gravedad_aparente
