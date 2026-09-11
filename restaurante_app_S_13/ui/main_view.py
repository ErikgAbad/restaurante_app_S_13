import tkinter as tk

class MainView(tk.Frame):
    def __init__(self, master, servicio, callback_logout):
        super().__init__(master)
        self.servicio = servicio
        self.callback_logout = callback_logout
        self.pack(fill="both", expand=True, padx=20, pady=20)
        self._crear_widgets()

    def _crear_widgets(self):
        tk.Label(self, text="Panel Principal del Restaurante", font=("Arial", 14, "bold")).pack(pady=10)

        frame_botones = tk.Frame(self)
        frame_botones.pack(pady=5)

        tk.Button(frame_botones, text="Ver Productos", command=self._mostrar_productos).pack(side="left", padx=5)
        tk.Button(frame_botones, text="Ver Usuarios", command=self._mostrar_usuarios).pack(side="left", padx=5)
        tk.Button(frame_botones, text="Ventas (Pendiente)", command=self._mostrar_ventas).pack(side="left", padx=5)

        self.txt_contenido = tk.Text(self, width=40, height=8)
        self.txt_contenido.pack(pady=10)

        tk.Button(self, text="Cerrar Sesión", bg="#f44336", fg="white", command=self.callback_logout).pack(pady=5)

    def _limpiar_texto(self):
        self.txt_contenido.delete("1.0", tk.END)

    def _mostrar_productos(self):
        self._limpiar_texto()
        productos = self.servicio.obtener_productos()
        for p in productos:
            self.txt_contenido.insert(tk.END, f"{p}\n")

    def _mostrar_usuarios(self):
        self._limpiar_texto()
        usuarios = self.servicio.obtener_usuarios()
        for u in usuarios:
            self.txt_contenido.insert(tk.END, f"{u}\n")

    def _mostrar_ventas(self):
        self._limpiar_texto()
        self.txt_contenido.insert(
            tk.END, 
            "Función Pendiente:\n\nLa funcionalidad de Ventas será implementada en las siguientes semanas."
        )