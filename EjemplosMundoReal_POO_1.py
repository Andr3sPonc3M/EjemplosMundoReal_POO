# Tarea semana 4 Ejemplos del mundo real 1.

class Television:
    # Representa una televisión.

    def __init__(self, marca, tamaño):
        # Inicializa una nueva televisión con marca y tamaño.
        self.marca = marca  # Atributo marca de la televisión
        self.tamaño = tamaño  # Atributo tamaño de la televisión
        self.encendida = False  # Atributo que indica si la TV está encendida
        self.canal = 1  # Atributo canal actual de la televisión
        self.volumen = 10  # Atributo volumen actual de la televisión

    def encender(self):
        # Enciende la televisión.
        self.encendida = True
        print(f"La TV {self.marca} está encendida.")

    def apagar(self):
        # Apaga la televisión.
        self.encendida = False
        print(f"La TV {self.marca} está apagada.")

    def cambiar_canal(self, nuevo_canal):
        # Cambia el canal de la televisión.
        if self.encendida:
            self.canal = nuevo_canal
            print(f"Canal cambiado a {self.canal}.")
        else:
            print("La TV está apagada. No se puede cambiar el canal.")

    def ajustar_volumen(self, nuevo_volumen):
        # Ajusta el volumen de la televisión.
        if self.encendida:
            self.volumen = nuevo_volumen
            print(f"Volumen ajustado a {self.volumen}.")
        else:
            print("La TV está apagada. No se puede ajustar el volumen.")

    def __str__(self):
        # Devuelve una representación en cadena de la televisión.
        estado = "encendida" if self.encendida else "apagada"
        return f"Televisión {self.marca} de {self.tamaño} pulgadas, actualmente {estado}"

    # Fin del programa.