class Conversion:
    def celsius_a_fahrenheit(self, celsius):
        return (celsius * 9/5) + 32
    
    def fahrenheit_a_celsius(self, fahrenheit):
        return (fahrenheit - 32) * 5/9
    
    def metros_a_pies(self, metros):
        return metros * 3.28084
    
    def pies_a_metros(self, pies):
        return pies * 0.3048

    def decimal_a_binario(self, decimal):
        if decimal == 0:
            return "0"
        return bin(decimal)[2:]
    
    def binario_a_decimal(self, binario):
        return int(binario, 2)
    
    def decimal_a_romano(self, numero):
        if not 0 < numero < 4000:
            return "Número fuera de rango (debe ser entre 1 y 3999)"
        
        valores_map = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"),
            (1, "I")
        ]
        
        resultado = ""
        for valor, simbolo in valores_map:
            while numero >= valor:
                resultado += simbolo
                numero -= valor
        return resultado
    
    def romano_a_decimal(self, romano):
        romano_map = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        
        resultado = 0
        i = 0
        while i < len(romano):
            valor_actual = romano_map[romano[i]]
            if i + 1 < len(romano) and romano_map[romano[i+1]] > valor_actual:
                resultado += romano_map[romano[i+1]] - valor_actual
                i += 2
            else:
                resultado += valor_actual
                i += 1
        return resultado

    def texto_a_morse(self, texto):
        morse_dict = {
            'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
            'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
            'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
            'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
            'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
            '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
            '9': '----.', '0': '-----', ' ': '/'
        }
        
        resultado = []
        for char in texto.upper():
            if char in morse_dict:
                resultado.append(morse_dict[char])
        return " ".join(resultado)
    
    def morse_a_texto(self, morse):
        morse_dict_inv = {
            '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F',
            '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
            '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R',
            '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
            '-.--': 'Y', '--..': 'Z', '.----': '1', '..---': '2', '...--': '3',
            '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8',
            '----.': '9', '-----': '0', '/': ' '
        }
        
        palabras_morse = morse.split('   ')
        texto_final = []
        for palabra_morse in palabras_morse:
            letras_morse = palabra_morse.split(' ')
            palabra_decodificada = ""
            for letra in letras_morse:
                if letra in morse_dict_inv:
                    palabra_decodificada += morse_dict_inv[letra]
            texto_final.append(palabra_decodificada)
            
        return " ".join(texto_final)