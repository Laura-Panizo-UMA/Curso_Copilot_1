#!/usr/local/bin/python3
import numpy as np

def estimar_pi(num_puntos):
    x = np.random.uniform(-1, 1, num_puntos)
    y = np.random.uniform(-1, 1, num_puntos)
    dentro_circulo = np.sum(x**2 + y**2 <= 1)
    pi_estimado = 4 * dentro_circulo / num_puntos
    return pi_estimado

# Ejemplo de uso
if __name__ == "__main__":
    puntos = 1000000
    print(f"Estimación de Pi con {puntos} puntos: {estimar_pi(puntos)}")