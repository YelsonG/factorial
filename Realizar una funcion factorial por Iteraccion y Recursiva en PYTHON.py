Python 3.10.10 (tags/v3.10.10:aad5f6a, Feb  7 2023, 17:20:36) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import tkinter as tk
from tkinter import messagebox

def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

... def factorial_recursive(n):
...     if n == 0:
...         return 1
...     else:
...         return n * factorial_recursive(n - 1)
... 
... def calculate_factorial():
...     try:
...         num = int(entry.get())
...         if num < 0:
...             messagebox.showerror("Error", "El número debe ser no negativo.")
...         else:
...             iterative_result = factorial_iterative(num)
...             recursive_result = factorial_recursive(num)
...             result_label.config(text=f"Factorial Iterativo: {iterative_result}\nFactorial Recursivo: {recursive_result}")
...     except ValueError:
...         messagebox.showerror("Error", "Ingresa un número entero válido.")
... 
... # Configuración de la interfaz gráfica
... root = tk.Tk()
... root.title("Factorial Calculator")
... 
... frame = tk.Frame(root)
... frame.pack(padx=20, pady=20)
... 
... label = tk.Label(frame, text="Ingresa un número entero:")
... label.pack()
... 
... entry = tk.Entry(frame)
... entry.pack()
... 
... calculate_button = tk.Button(frame, text="Calcular Factorial", command=calculate_factorial)
... calculate_button.pack()
... 
... result_label = tk.Label(frame, text="")
... result_label.pack()
... 
