import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")
        self.root.geometry("400x500")
        self.root.resizable(False, False)

        self.tasks = []

        # Campo de entrada
        self.entry = tk.Entry(self.root, font=("Arial", 14))
        self.entry.pack(pady=10, padx=10, fill=tk.X)
        self.entry.focus()

        # Botones
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=5)

        self.add_button = tk.Button(button_frame, text="Añadir Tarea", command=self.add_task)
        self.add_button.grid(row=0, column=0, padx=5)

        self.complete_button = tk.Button(button_frame, text="Marcar Completada", command=self.complete_task)
        self.complete_button.grid(row=0, column=1, padx=5)

        self.delete_button = tk.Button(button_frame, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.grid(row=0, column=2, padx=5)

        # Lista de tareas
        self.task_listbox = tk.Listbox(self.root, font=("Arial", 12), selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        # Asociar atajos de teclado
        self.root.bind('<Return>', lambda event: self.add_task())
        self.root.bind('<c>', lambda event: self.complete_task())
        self.root.bind('<C>', lambda event: self.complete_task())
        self.root.bind('<d>', lambda event: self.delete_task())
        self.root.bind('<D>', lambda event: self.delete_task())
        self.root.bind('<Delete>', lambda event: self.delete_task())
        self.root.bind('<Escape>', lambda event: self.root.quit())

    def add_task(self):
        task_text = self.entry.get().strip()
        if task_text:
            self.tasks.append({'text': task_text, 'completed': False})
            self.update_task_list()
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Campo vacío", "Por favor ingresa una tarea.")

    def complete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            idx = selected_index[0]
            self.tasks[idx]['completed'] = not self.tasks[idx]['completed']
            self.update_task_list()
        else:
            messagebox.showwarning("Sin selección", "Por favor selecciona una tarea.")

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            idx = selected_index[0]
            del self.tasks[idx]
            self.update_task_list()
        else:
            messagebox.showwarning("Sin selección", "Por favor selecciona una tarea.")

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            text = task['text']
            if task['completed']:
                text += " (Completada)"
            self.task_listbox.insert(tk.END, text)
            # Dar feedback visual: tareas completadas en gris
            if task['completed']:
                self.task_listbox.itemconfig(tk.END, fg="gray")
            else:
                self.task_listbox.itemconfig(tk.END, fg="black")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
