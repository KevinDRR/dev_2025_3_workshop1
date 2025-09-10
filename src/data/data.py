import collections

class Data:
    def invertir_lista(self, lista):
        lista_invertida = []
        for i in range(len(lista) - 1, -1, -1):
            lista_invertida.append(lista[i])
        return lista_invertida
    
    def buscar_elemento(self, lista, elemento):
        for i, valor in enumerate(lista):
            if valor == elemento:
                return i
        return -1
    
    def eliminar_duplicados(self, lista):
        sin_duplicados = []
        for elemento_actual in lista:
            encontrado = False
            for item_unico in sin_duplicados:
                if item_unico == elemento_actual and type(item_unico) is type(elemento_actual):
                    encontrado = True
                    break
            if not encontrado:
                sin_duplicados.append(elemento_actual)
        return sin_duplicados
    
    def merge_ordenado(self, lista1, lista2):
        resultado = []
        i, j = 0, 0
        
        while i < len(lista1) and j < len(lista2):
            if lista1[i] < lista2[j]:
                resultado.append(lista1[i])
                i += 1
            else:
                resultado.append(lista2[j])
                j += 1
        
        resultado.extend(lista1[i:])
        resultado.extend(lista2[j:])
        return resultado
    
    def rotar_lista(self, lista, k):
        if not lista:
            return []
        
        k_efectivo = k % len(lista)
        
        return lista[-k_efectivo:] + lista[:-k_efectivo]
    
    def encuentra_numero_faltante(self, lista):
        n = len(lista) + 1
        suma_esperada = n * (n + 1) // 2
        suma_real = sum(lista)
        
        return suma_esperada - suma_real
    
    def es_subconjunto(self, conjunto1, conjunto2):
        for elemento in conjunto1:
            if elemento not in conjunto2:
                return False
        return True
    
    def implementar_pila(self):
        pila = []
        return {
            "push": lambda elemento: pila.append(elemento),
            "pop": lambda: pila.pop() if pila else None,
            "peek": lambda: pila[-1] if pila else None,
            "is_empty": lambda: len(pila) == 0,
            "show": lambda: pila
        }
    
    def implementar_cola(self):
        cola = collections.deque()
        return {
            "enqueue": lambda elemento: cola.append(elemento),
            "dequeue": lambda: cola.popleft() if cola else None,
            "peek": lambda: cola[0] if cola else None,
            "is_empty": lambda: len(cola) == 0,
            "show": lambda: list(cola)
        }
    
    def matriz_transpuesta(self, matriz):
        if not matriz or not matriz[0]:
            return []
            
        filas = len(matriz)
        columnas = len(matriz[0])
        
        transpuesta = [[matriz[j][i] for j in range(filas)] for i in range(columnas)]
        return transpuesta