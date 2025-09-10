class Strings:
    def es_palindromo(self, texto):
        cadena_limpia = ''.join(filter(str.isalnum, texto)).lower()
        return cadena_limpia == cadena_limpia[::-1]

    def invertir_cadena(self, texto):
        cadena_invertida = ""
        for char in texto:
            cadena_invertida = char + cadena_invertida
        return cadena_invertida

    def contar_vocales(self, texto):
        vocales = "aeiou"
        contador = 0
        for char in texto.lower():
            if char in vocales:
                contador += 1
        return contador

    def contar_consonantes(self, texto):
        contador = 0
        for char in texto.lower():
            if char.isalpha() and char not in "aeiou":
                contador += 1
        return contador

    def es_anagrama(self, texto1, texto2):
        cadena1_limpia = "".join(sorted(texto1.lower().replace(" ", "")))
        cadena2_limpia = "".join(sorted(texto2.lower().replace(" ", "")))
        return cadena1_limpia == cadena2_limpia

    def contar_palabras(self, texto):
        return len(texto.split())

    def palabras_mayus(self, texto):
        return texto.title()

    def eliminar_espacios_duplicados(self, texto):
        if not texto:
            return ""
        resultado = []
        for i, char in enumerate(texto):
            if char == ' ' and i > 0 and texto[i-1] == ' ':
                continue
            else:
                resultado.append(char)
        return "".join(resultado)

    def es_numero_entero(self, texto):
        if not texto:
            return False
        texto = texto.strip()
        if texto.startswith('-') or texto.startswith('+'):
            return texto[1:].isdigit()
        return texto.isdigit()

    def cifrar_cesar(self, texto, desplazamiento):
        resultado = ""
        for char in texto:
            if char.isalpha():
                base = ord('a') if char.islower() else ord('A')
                codigo_actual = ord(char) - base
                nuevo_codigo = (codigo_actual + desplazamiento) % 26
                resultado += chr(base + nuevo_codigo)
            else:
                resultado += char
        return resultado

    def descifrar_cesar(self, texto, desplazamiento):
        return self.cifrar_cesar(texto, -desplazamiento)

    def encontrar_subcadena(self, texto, subcadena):
        posiciones = []
        len_texto = len(texto)
        len_sub = len(subcadena)
        if len_sub == 0:
            return []
        for i in range(len_texto - len_sub + 1):
            if texto[i:i+len_sub] == subcadena:
                posiciones.append(i)
        return posiciones