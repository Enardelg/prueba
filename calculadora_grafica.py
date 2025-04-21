import tkinter as tk
from tkinter import messagebox

# === LÓGICA DE CÁLCULO ===
def calculadora_basica(*args, **kwargs):
    if len(args) != 2:
        return "Error: Debes proporcionar exactamente dos números."

    num1, num2 = args
    operacion = kwargs.get("operacion")

    def suma(a, b): return a + b
    def resta(a, b): return a - b
    def multiplicacion(a, b): return a * b
    def division(a, b):
        if b == 0:
            return "Error: División por cero."
        return a / b
    def potencia(base, exponente):
        if exponente == 0:
            return 1
        return base * potencia(base, exponente - 1)

    def crear_calculadora(operacion):
        return {
            "suma": suma,
            "resta": resta,
            "multiplicacion": multiplicacion,
            "division": division,
            "potencia": potencia
        }.get(operacion, None)

    operacion_func = crear_calculadora(operacion)
    if not operacion_func:
        return "Error: Operación no válida."
    return operacion_func(num1, num2)

# === INTERFAZ GRÁFICA ===
def realizar_operacion():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operacion = operacion_var.get()
        resultado = calculadora_basica(num1, num2, operacion=operacion)
        resultado_label.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Error", "Ingresa números válidos.")

# Crear ventana
ventana = tk.Tk()
ventana.title("Calculadora Básica")

# Campos de entrada
tk.Label(ventana, text="Número 1:").grid(row=0, column=0)
entry1 = tk.Entry(ventana)
entry1.grid(row=0, column=1)

tk.Label(ventana, text="Número 2:").grid(row=1, column=0)
entry2 = tk.Entry(ventana)
entry2.grid(row=1, column=1)

# Selección de operación
operacion_var = tk.StringVar(value="suma")
operaciones = ["suma", "resta", "multiplicacion", "division", "potencia"]
tk.Label(ventana, text="Operación:").grid(row=2, column=0)
tk.OptionMenu(ventana, operacion_var, *operaciones).grid(row=2, column=1)

# Botón de calcular
tk.Button(ventana, text="Calcular", command=realizar_operacion).grid(row=3, columnspan=2)

# Resultado
resultado_label = tk.Label(ventana, text="Resultado:")
resultado_label.grid(row=4, columnspan=2)

# Ejecutar la app
ventana.mainloop()
