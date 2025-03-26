import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry


class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")
        self.root.geometry("500x400")

        # Frame de entrada de datos
        self.frame_input = tk.Frame(root)
        self.frame_input.pack(pady=10)

        tk.Label(self.frame_input, text="Fecha:").grid(row=0, column=0, padx=5, pady=5)
        self.date_entry = DateEntry(self.frame_input, width=12, background='darkblue', foreground='white',
                                    borderwidth=2)
        self.date_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.frame_input, text="Hora:").grid(row=1, column=0, padx=5, pady=5)
        self.time_entry = tk.Entry(self.frame_input, width=15)
        self.time_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.frame_input, text="Descripción:").grid(row=2, column=0, padx=5, pady=5)
        self.desc_entry = tk.Entry(self.frame_input, width=30)
        self.desc_entry.grid(row=2, column=1, padx=5, pady=5)

        # Frame para la tabla
        self.frame_table = tk.Frame(root)
        self.frame_table.pack(pady=10)

        self.tree = ttk.Treeview(self.frame_table, columns=("Fecha", "Hora", "Descripción"), show='headings')
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.pack()

        # Frame para botones
        self.frame_buttons = tk.Frame(root)
        self.frame_buttons.pack(pady=10)

        self.add_button = tk.Button(self.frame_buttons, text="Agregar Evento", command=self.add_event)
        self.add_button.grid(row=0, column=0, padx=5)

        self.delete_button = tk.Button(self.frame_buttons, text="Eliminar Evento", command=self.delete_event)
        self.delete_button.grid(row=0, column=1, padx=5)

        self.exit_button = tk.Button(self.frame_buttons, text="Salir", command=root.quit)
        self.exit_button.grid(row=0, column=2, padx=5)

    def add_event(self):
        date = self.date_entry.get()
        time = self.time_entry.get()
        desc = self.desc_entry.get()

        if date and time and desc:
            self.tree.insert("", "end", values=(date, time, desc))
            self.time_entry.delete(0, tk.END)
            self.desc_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Todos los campos deben estar llenos")

    def delete_event(self):
        selected_item = self.tree.selection()
        if selected_item:
            confirm = messagebox.askyesno("Confirmar", "¿Estás seguro de eliminar el evento seleccionado?")
            if confirm:
                self.tree.delete(selected_item)
        else:
            messagebox.showwarning("Advertencia", "Selecciona un evento para eliminar")


if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()
