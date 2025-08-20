class Calculadora:
    numero1 = 0
    numero2 = 0
   
    def __init__(self, numero1, numero2):
        self._numero1 = numero1
        self._numero2 = numero2
        self._historial = []
        
    """----------setter and getter------------"""
    @property
    def numero1(self):
        return self._numero1
    
    @numero1.setter
    def numero1(self, nuevo_numero1):
        if type(nuevo_numero1) in (int, float):
            self._numero1 = nuevo_numero1
        else:
            raise ValueError("Debe ser un número")
    @property
    def numero2(self):
        return self._numero2

    @numero2.setter
    def numero2(self, nuevo_numero2):
        if type(nuevo_numero2) in (int, float):
            self._numero2 = nuevo_numero2
        else:
            raise ValueError("Debe ser un número")
   

    def sumar(self):
        resultado = self._numero1 + self._numero2
        self._registrar_operacion('+', resultado)
        return resultado

    def restar(self):
        resultado = self._numero1 - self._numero2
        self._registrar_operacion('-', resultado)
        return resultado

    def multiplicar(self):
        resultado = self._numero1 * self._numero2
        self._registrar_operacion('*', resultado)
        return resultado

    def dividir(self):
        if self._numero2 == 0:
            raise ValueError("No se puede dividir entre cero")
        resultado = self._numero1 / self._numero2
        self._registrar_operacion('/', resultado)
        return resultado

    def _registrar_operacion(self, operador, resultado):
        """Método privado para registrar operaciones en el historial"""
        self._historial.append({
            'operacion': f"{self._numero1} {operador} {self._numero2}",
            'resultado': resultado
        })

    def ver_historial(self):
        """Muestra el historial de operaciones"""
        print("\n--- Historial de Operaciones ---")
        for i, op in enumerate(self._historial, 1):
            print(f"{i}. {op['operacion']} = {op['resultado']}")




def interpretar_expresion(expresion):
    """Interpreta la expresión matemática ingresada"""
    for operador in ['+', '-', '*', '/']:
        if operador in expresion:
            partes = expresion.split(operador)
            if len(partes) == 2:
                num1 = float(partes[0].strip())
                num2 = float(partes[1].strip())
                return num1, num2, operador
               

def main():
    calc = Calculadora(0,0)
    print("Calculadora Básica. Escribe 'salir' para terminar o 'historial' para ver operaciones.\n")
    
    while True:
        entrada = input("Ingresa la operación (ejemplo: 5 + 5): ")
        
        if entrada.strip().lower() == "salir":
            print("¡Hasta pronto!")
            break
        
        if entrada.strip().lower() == "historial":
            calc.ver_historial()
            continue
        
        resultado = interpretar_expresion(entrada)
        if not resultado:
            print("Expresión no válida. Usa el formato: número operador número (ej. 5 + 5)\n")
            continue
        num1, num2, operador = resultado
        calc.numero1 = num1
        calc.numero2 = num2
        if operador == '+':
            print("Resultado:", calc.sumar())
        elif operador == '-':
            print("Resultado:", calc.restar())
        elif operador == '*':
            print("Resultado:", calc.multiplicar())
        elif operador == '/':
            print("Resultado:", calc.dividir())
                



main()
