import tkinter as tk
from tkinter import messagebox

def agregar_item():
    item = entrada_texto.get()
    if item:
        lista.insert(tk.END, item)
        entrada_texto.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "El campo de texto está vacío")

def limpiar_lista():
    lista.delete(0, tk.END)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Aplicación GUI Básica")
ventana.geometry("400x300")

# Etiqueta
etiqueta = tk.Label(ventana, text="Ingrese un ítem:")
etiqueta.pack(pady=5)

# Campo de texto
entrada_texto = tk.Entry(ventana)
entrada_texto.pack(pady=5)

# Botón Agregar
boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_item)
boton_agregar.pack(pady=5)

# Lista para mostrar los ítems
lista = tk.Listbox(ventana)
lista.pack(pady=5, fill=tk.BOTH, expand=True)

# Botón Limpiar
boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_lista)
boton_limpiar.pack(pady=5)

# Iniciar la aplicación
ventana.mainloop()
