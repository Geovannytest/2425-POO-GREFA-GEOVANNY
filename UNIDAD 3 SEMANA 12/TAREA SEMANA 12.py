class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.detalles = (titulo, autor)  # Tupla para título y autor (inmutables)
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"{self.detalles[0]} de {self.detalles[1]} (Categoría: {self.categoria}, ISBN: {self.isbn})"


class Usuario:
    def __init__(self, nombre, usuario_id):
        self.nombre = nombre
        self.usuario_id = usuario_id
        self.libros_prestados = []  # Lista para gestionar los libros prestados

    def __str__(self):
        return f"Usuario: {self.nombre} (ID: {self.usuario_id})"


class Biblioteca:
    def __init__(self):
        self.libros_disponibles = {}  # Diccionario con ISBN como clave
        self.usuarios_registrados = set()  # Conjunto para IDs únicos
        self.historial_prestamos = {}  # Diccionario para registrar préstamos

    def agregar_libro(self, libro):
        self.libros_disponibles[libro.isbn] = libro
        print(f"Libro agregado: {libro}")

    def quitar_libro(self, isbn):
        if isbn in self.libros_disponibles:
            del self.libros_disponibles[isbn]
            print(f"Libro con ISBN {isbn} eliminado.")
        else:
            print("El libro no existe en la biblioteca.")

    def registrar_usuario(self, usuario):
        if usuario.usuario_id not in self.usuarios_registrados:
            self.usuarios_registrados.add(usuario.usuario_id)
            self.historial_prestamos[usuario.usuario_id] = []
            print(f"Usuario registrado: {usuario}")
        else:
            print("El ID de usuario ya está registrado.")

    def dar_baja_usuario(self, usuario_id):
        if usuario_id in self.usuarios_registrados:
            self.usuarios_registrados.remove(usuario_id)
            del self.historial_prestamos[usuario_id]
            print(f"Usuario con ID {usuario_id} dado de baja.")
        else:
            print("El usuario no está registrado.")

    def prestar_libro(self, usuario, isbn):
        if usuario.usuario_id not in self.usuarios_registrados:
            print("El usuario no está registrado.")
            return
        if isbn in self.libros_disponibles:
            libro = self.libros_disponibles.pop(isbn)
            usuario.libros_prestados.append(libro)
            self.historial_prestamos[usuario.usuario_id].append(libro)
            print(f"Libro prestado: {libro} a {usuario.nombre}")
        else:
            print("Libro no disponible.")

    def devolver_libro(self, usuario, isbn):
        for libro in usuario.libros_prestados:
            if libro.isbn == isbn:
                usuario.libros_prestados.remove(libro)
                self.libros_disponibles[isbn] = libro
                print(f"Libro devuelto: {libro}")
                return
        print("El usuario no tiene este libro prestado.")

    def buscar_libro(self, criterio, valor):
        resultados = [libro for libro in self.libros_disponibles.values() if getattr(libro, criterio) == valor]
        if resultados:
            print("Resultados de búsqueda:")
            for libro in resultados:
                print(libro)
        else:
            print("No se encontraron libros con ese criterio.")

    def listar_prestamos(self, usuario):
        if usuario.libros_prestados:
            print(f"Libros prestados a {usuario.nombre}:")
            for libro in usuario.libros_prestados:
                print(libro)
        else:
            print("El usuario no tiene libros prestados.")


# Pruebas del sistema
biblioteca = Biblioteca()

libro1 = Libro("1984", "George Orwell", "Ficción", "123456")
libro2 = Libro("El Principito", "Antoine de Saint-Exupéry", "Infantil", "789101")
usuario1 = Usuario("Ana Pérez", "U001")

biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.registrar_usuario(usuario1)

biblioteca.prestar_libro(usuario1, "123456")
biblioteca.listar_prestamos(usuario1)

biblioteca.devolver_libro(usuario1, "123456")
biblioteca.listar_prestamos(usuario1)

biblioteca.buscar_libro("categoria", "Infantil")