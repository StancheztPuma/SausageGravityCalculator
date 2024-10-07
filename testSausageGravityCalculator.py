# test_sausage_gravity.py

import unittest
from SausageGravityCalculator import calcular_gravedad  # Importar la función desde el otro archivo

# Clase de prueba unitaria
class TestCalcularGravedad(unittest.TestCase):
    
    def test_gravedad_aparente(self):
        # Valores de prueba
        anchura = 5.0  # cm
        peso = 100.0   # gramos
        altura = 10.0  # metros
        
        # Gravedad esperada
        resultado_esperado = 500 / 11  # ≈ 45.45
        
        # Llamar la función y comparar con el valor esperado
        self.assertAlmostEqual(calcular_gravedad(anchura, peso, altura), resultado_esperado, places=2)

# Ejecutar las pruebas
if __name__ == '__main__':
    unittest.main()

