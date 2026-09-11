from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.archivo_servicio import ArchivoServicio

class RestauranteServicio:
    def __init__(self):
        self.usuarios = []
        self.productos = []
        self._cargar_datos()

    def _cargar_datos(self):
        datos_usuarios = ArchivoServicio.cargar_json('datos/usuarios.json')
        for u in datos_usuarios:
            self.usuarios.append(Usuario(u['username'], u['password'], u['nombre']))

        datos_productos = ArchivoServicio.cargar_json('datos/productos.json')
        for p in datos_productos:
            self.productos.append(Producto(p['id'], p['nombre'], p['precio'], p['categoria']))

    def validar_acceso(self, username, password):
        if not username or not password:
            return False, "Por favor complete todos los campos."
        
        for usuario in self.usuarios:
            if usuario.username == username and usuario.password == password:
                return True, f"Bienvenido, {usuario.nombre}"
        
        return False, "Usuario o contraseña incorrectos."

    def obtener_productos(self):
        return self.productos

    def obtener_usuarios(self):
        return self.usuarios