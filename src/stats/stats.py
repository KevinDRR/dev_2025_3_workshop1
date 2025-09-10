import math

class Stats:
    def promedio(self, numeros):
        if not numeros:
            return 0
        return sum(numeros) / len(numeros)

    def mediana(self, numeros):
        if not numeros:
            return 0
        
        numeros_ordenados = sorted(numeros)
        n = len(numeros_ordenados)
        indice_medio = n // 2
        
        if n % 2 == 1:
            return float(numeros_ordenados[indice_medio])
        else:
            return (numeros_ordenados[indice_medio - 1] + numeros_ordenados[indice_medio]) / 2.0

    def moda(self, numeros):
        if not numeros:
            return None
        
        return max(set(numeros), key=numeros.count)

    def desviacion_estandar(self, numeros):
        if len(numeros) < 1:
            return 0.0
        
        media = self.promedio(numeros)
        varianza = sum((x - media) ** 2 for x in numeros) / len(numeros)
        return math.sqrt(varianza)

    def varianza(self, numeros):
        if len(numeros) < 1:
            return 0.0
            
        media = self.promedio(numeros)
        return sum((x - media) ** 2 for x in numeros) / len(numeros)

    def rango(self, numeros):
        if not numeros:
            return 0
        return max(numeros) - min(numeros)