# Tarea semana 4 Ejemplos del mundo real 2.

class Usuario:
    # Representa un usuario en una red social.

    def __init__(self, nombre, email):
        # Inicializa un nuevo usuario con nombre y email.
        self.nombre = nombre  # Atributo nombre del usuario
        self.email = email  # Atributo email del usuario
        self.publicaciones = []  # Lista para almacenar publicaciones del usuario

    def hacer_publicacion(self, contenido):
        # Crea una nueva publicación y la agrega a la lista de publicaciones del usuario.
        publicacion = Publicacion(contenido, self.nombre)
        self.publicaciones.append(publicacion)
        print(f"{self.nombre} ha hecho una nueva publicación.")

    def mostrar_publicaciones(self):
        # Muestra todas las publicaciones del usuario.
        for publicacion in self.publicaciones:
            print(publicacion)

    def __str__(self):
        # Devuelve una representación en cadena del usuario.
        return f"Usuario: {self.nombre}, Email: {self.email}"


class Publicacion:
    # Representa una publicación en la red social.

    def __init__(self, contenido, autor):
        # Inicializa una nueva publicación con contenido y autor.
        self.contenido = contenido  # Atributo contenido de la publicación
        self.autor = autor  # Atributo autor de la publicación

    def __str__(self):
        # Devuelve una representación en cadena de la publicación.
        return f"Publicación de {self.autor}: {self.contenido}"

    # Fin del programa.