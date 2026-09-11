class Usuario:
    def __init__(self, username, password, nombre):
        self.username = username
        self.password = password
        self.nombre = nombre

    def __str__(self):
        return f"{self.nombre} (@{self.username})"