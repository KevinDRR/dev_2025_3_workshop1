import math

class Magic:
    def fibonacci(self, n):
        if n < 0:
            return None
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a

    def secuencia_fibonacci(self, n):
        if n <= 0:
            return []
        resultado = []
        a, b = 0, 1
        for _ in range(n):
            resultado.append(a)
            a, b = b, a + b
        return resultado

    def es_primo(self, n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def generar_primos(self, n):
        if n < 2:
            return []
        primos = [True] * (n + 1)
        primos[0] = primos[1] = False
        for i in range(2, math.isqrt(n) + 1):
            if primos[i]:
                for multiplo in range(i * i, n + 1, i):
                    primos[multiplo] = False
        return [i for i, es_primo in enumerate(primos) if es_primo]

    def es_numero_perfecto(self, n):
        if n <= 1:
            return False
        suma_divisores = 1
        for i in range(2, math.isqrt(n) + 1):
            if n % i == 0:
                suma_divisores += i
                if i * i != n:
                    suma_divisores += n // i
        return suma_divisores == n

    def triangulo_pascal(self, filas):
        if filas <= 0:
            return []
        triangulo = [[1]]
        for i in range(1, filas):
            fila_anterior = triangulo[-1]
            nueva_fila = [1]
            for j in range(len(fila_anterior) - 1):
                nueva_fila.append(fila_anterior[j] + fila_anterior[j + 1])
            nueva_fila.append(1)
            triangulo.append(nueva_fila)
        return triangulo

    def factorial(self, n):
        if n < 0:
            return None
        if n == 0:
            return 1
        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
        return resultado

    def mcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def mcm(self, a, b):
        if a == 0 or b == 0:
            return 0
        return abs(a * b) // self.mcd(a, b)

    def suma_digitos(self, n):
        suma = 0
        num = abs(n)
        while num > 0:
            suma += num % 10
            num //= 10
        return suma

    def es_numero_armstrong(self, n):
        if n < 0:
            return False
        s_n = str(n)
        potencia = len(s_n)
        suma = sum(int(digito) ** potencia for digito in s_n)
        return suma == n

    def es_cuadrado_magico(self, matriz):
        if not matriz or not all(len(fila) == len(matriz) for fila in matriz):
            return False
        
        tamano = len(matriz)
        suma_objetivo = sum(matriz[0])

        for fila in matriz:
            if sum(fila) != suma_objetivo:
                return False

        for j in range(tamano):
            if sum(matriz[i][j] for i in range(tamano)) != suma_objetivo:
                return False

        if sum(matriz[i][i] for i in range(tamano)) != suma_objetivo:
            return False

        if sum(matriz[i][tamano - 1 - i] for i in range(tamano)) != suma_objetivo:
            return False

        return True