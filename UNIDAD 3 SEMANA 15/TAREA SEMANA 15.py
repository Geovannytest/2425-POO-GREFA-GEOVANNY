import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")
        self.root.geometry("400x400")

        # Lista de tareas
        self.task_list = []

        # Entrada de texto
        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack(pady=10)
        self.task_entry.bind("<Return>", self.add_task)  # Presionar Enter para añadir

        # Botones
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=5)

        self.add_button = tk.Button(btn_frame, text="Añadir Tarea", command=self.add_task)
        self.add_button.pack(side=tk.LEFT, padx=5)

        self.complete_button = tk.Button(btn_frame, text="Marcar Completada", command=self.complete_task)
        self.complete_button.pack(side=tk.LEFT, padx=5)

        self.delete_button = tk.Button(btn_frame, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.pack(side=tk.LEFT, padx=5)

        # Lista de tareas (Listbox)
        self.task_listbox = tk.Listbox(root, width=50, height=15)
        self.task_listbox.pack(pady=10)
        self.task_listbox.bind("<Double-Button-1>", self.complete_task)  # Doble clic para completar

    def add_task(self, event=None):
        """Añade una nueva tarea a la lista."""
        task = self.task_entry.get().strip()
        if task:
            self.task_list.append((task, False))  # False indica que no está completada
            self.update_listbox()
            self.task_entry.delete(0, tk.END)  # Limpiar campo de entrada
        else:
            messagebox.showwarning("Advertencia", "No puedes añadir una tarea vacía.")

    def complete_task(self, event=None):
        """Marca una tarea como completada cambiando su estado."""
        try:
            index = self.task_listbox.curselection()[0]
            task, completed = self.task_list[index]
            self.task_list[index] = (task, not completed)  # Cambia el estado de la tarea
            self.update_listbox()
        except IndexError:
            messagebox.showwarning("Advertencia", "Selecciona una tarea para marcar como completada.")

    def delete_task(self):
        """Elimina la tarea seleccionada de la lista."""
        try:
            index = self.task_listbox.curselection()[0]
            del self.task_list[index]
            self.update_listbox()
        except IndexError:
            messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminar.")

    def update_listbox(self):
        """Actualiza la Listbox con las tareas actuales."""
        self.task_listbox.delete(0, tk.END)
        for task, completed in self.task_list:
            display_text = f"[✔] {task}" if completed else f"[ ] {task}"
            self.task_listbox.insert(tk.END, display_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
