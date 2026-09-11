import tkinter as tk
from tkinter import messagebox

class LoginView(tk.Frame):
    def __init__(self, parent, restaurante_servicio, on_login_success):
        super().__init__(parent)
        self.servicio = restaurante_servicio
        self.on_login_success = on_login_success
        self._crear_componentes()

    def _crear_componentes(self):
        tk.Label(self, text="Inicio de Sesión - Restaurante", font=("Arial", 14, "bold")).pack(pady=15)

        tk.Label(self, text="Usuario:").pack(pady=2)
        self.entry_user = tk.Entry(self)
        self.entry_user.pack(pady=2)

        tk.Label(self, text="Contraseña:").pack(pady=2)
        self.entry_pass = tk.Entry(self, show="*")
        self.entry_pass.pack(pady=2)

        tk.Button(self, text="Ingresar", command=self._intentar_login).pack(pady=15)

    def _intentar_login(self):
        user = self.entry_user.get().strip()
        pas = self.entry_pass.get().strip()

        exito, mensaje = self.servicio.validar_acceso(user, pas)

        if exito:
            messagebox.showinfo("Éxito", mensaje)
            self._limpiar_campos()
            self.on_login_success()
        else:
            messagebox.showerror("Error de Autenticación", mensaje)

    def _limpiar_campos(self):
        self.entry_user.delete(0, tk.END)
        self.entry_pass.delete(0, tk.END)