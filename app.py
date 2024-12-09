import tkinter as tk
from tkinter import messagebox

# Función para validar una cadena según las reglas corregidas
def validate_chain(chain):
    count_a = chain.count('a')
    count_b = chain.count('b')
    # Reglas: `a` no puede ser mayor que `b` y `b` debe ser mayor que `a`
    if count_a <= count_b:
        return "Accept"
    return "Reject"

# Función para validar las cadenas en la tabla
def validate_all():
    for i in range(5):  # 5 filas
        chain = entries[i].get()
        if not chain.isalpha():
            results[i].set("Invalid input")
        else:
            results[i].set(validate_chain(chain))

# Crear la ventana principal
root = tk.Tk()
root.title("Validador de Cadenas")

# Crear la tabla
entries = []
results = []

tk.Label(root, text="Cadenas").grid(row=0, column=0, padx=10, pady=10)
tk.Label(root, text="Resultado").grid(row=0, column=1, padx=10, pady=10)

for i in range(5):
    # Crear campo de entrada para la cadena
    entry = tk.Entry(root, width=20)
    entry.grid(row=i+1, column=0, padx=10, pady=5)
    entries.append(entry)
    
    # Crear campo para el resultado
    result = tk.StringVar()
    result_label = tk.Label(root, textvariable=result, width=20)
    result_label.grid(row=i+1, column=1, padx=10, pady=5)
    results.append(result)

# Botón para validar cadenas
validate_button = tk.Button(root, text="Validar", command=validate_all)
validate_button.grid(row=6, column=0, columnspan=2, pady=10)

# Ejecutar la aplicación
root.mainloop()
