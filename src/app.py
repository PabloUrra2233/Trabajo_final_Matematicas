"""
Aplicación principal con CustomTkinter.

Ejecutar desde la raíz del proyecto con:
python src/app.py
"""

from pathlib import Path
import tkinter.messagebox as messagebox

import customtkinter as ctk

from config import PERFILES_VEHICULO, PRECIOS_COMBUSTIBLE_CLP
from converters import formatear_clp, kilometros_a_metros, kilometros_a_millas
from graph_manager import (
    cargar_grafo,
    obtener_ciudades,
    obtener_resumen_grafo,
    validar_requisitos_basicos,
)
from shortest_path import dijkstra
from transport_modes import estimar_auto, estimar_caminata
from visualization import dibujar_grafo

RUTA_BASE = Path(__file__).resolve().parent.parent
RUTA_CIUDADES = RUTA_BASE / "data" / "ciudades.csv"
RUTA_CONEXIONES = RUTA_BASE / "data" / "conexiones.csv"

class AplicacionRutas(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Ruta óptima entre ciudades")
        self.geometry("860x620")

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.grafo = cargar_grafo(RUTA_CIUDADES, RUTA_CONEXIONES)
        self.ciudades = obtener_ciudades(self.grafo)

        self.crear_interfaz()
        self.mostrar_resumen_inicial()

    def crear_interfaz(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)

        titulo = ctk.CTkLabel(
            self,
            text="Ruta óptima entre ciudades",
            font=ctk.CTkFont(size=24, weight="bold"),
        )
        titulo.grid(row=0, column=0, columnspan=2, padx=20, pady=(20, 10), sticky="ew")

        panel_controles = ctk.CTkFrame(self)
        panel_controles.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")

        panel_resultado = ctk.CTkFrame(self)
        panel_resultado.grid(row=1, column=1, padx=20, pady=20, sticky="nsew")
        panel_resultado.grid_rowconfigure(0, weight=1)
        panel_resultado.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(panel_controles, text="Ciudad de origen").pack(pady=(15, 5))
        self.combo_origen = ctk.CTkComboBox(panel_controles, values=self.ciudades)
        self.combo_origen.pack(padx=15, pady=5, fill="x")

        ctk.CTkLabel(panel_controles, text="Ciudad de destino").pack(pady=(15, 5))
        self.combo_destino = ctk.CTkComboBox(panel_controles, values=self.ciudades)
        self.combo_destino.pack(padx=15, pady=5, fill="x")

        ctk.CTkLabel(panel_controles, text="Modo de transporte").pack(pady=(15, 5))
        self.combo_modo = ctk.CTkComboBox(
            panel_controles,
            values=["Vehículo", "Caminando"],
            command=self.actualizar_estado_controles,
        )
        self.combo_modo.set("Vehículo")
        self.combo_modo.pack(padx=15, pady=5, fill="x")

        ctk.CTkLabel(panel_controles, text="Perfil de vehículo").pack(pady=(15, 5))
        self.combo_vehiculo = ctk.CTkComboBox(
            panel_controles,
            values=list(PERFILES_VEHICULO.keys()),
        )
        self.combo_vehiculo.set("Sedán")
        self.combo_vehiculo.pack(padx=15, pady=5, fill="x")

        ctk.CTkLabel(panel_controles, text="Octanaje").pack(pady=(15, 5))
        self.combo_octanaje = ctk.CTkComboBox(
            panel_controles,
            values=list(PRECIOS_COMBUSTIBLE_CLP.keys()),
        )
        self.combo_octanaje.set("95")
        self.combo_octanaje.pack(padx=15, pady=5, fill="x")

        boton_calcular = ctk.CTkButton(
            panel_controles,
            text="Calcular ruta óptima",
            command=self.calcular,
        )
        boton_calcular.pack(padx=15, pady=(25, 10), fill="x")

        boton_grafo = ctk.CTkButton(
            panel_controles,
            text="Ver grafo completo",
            command=lambda: dibujar_grafo(self.grafo),
        )
        boton_grafo.pack(padx=15, pady=10, fill="x")

        self.texto_resultado = ctk.CTkTextbox(panel_resultado, font=ctk.CTkFont(size=14))
        self.texto_resultado.grid(row=0, column=0, padx=15, pady=15, sticky="nsew")

    def actualizar_estado_controles(self, _valor=None):
        modo = self.combo_modo.get()

        if modo == "Caminando":
            self.combo_vehiculo.configure(state="disabled")
            self.combo_octanaje.configure(state="disabled")
        else:
            self.combo_vehiculo.configure(state="normal")
            self.combo_octanaje.configure(state="normal")

    def mostrar_resumen_inicial(self):
        resumen = obtener_resumen_grafo(self.grafo)
        errores = validar_requisitos_basicos(self.grafo)

        texto = "Resumen inicial del grafo\n"
        texto += "========================\n"
        texto += f"Ciudades: {resumen['cantidad_ciudades']}\n"
        texto += f"Conexiones: {resumen['cantidad_conexiones']}\n"
        texto += f"¿Es conexo?: {'Sí' if resumen['es_conexo'] else 'No'}\n\n"

        if errores:
            texto += "Advertencias:\n"
            for error in errores:
                texto += f"- {error}\n"
        else:
            texto += "El grafo cumple los requisitos básicos del proyecto.\n"

        self.escribir_resultado(texto)

    def calcular(self):
        origen = self.combo_origen.get()
        destino = self.combo_destino.get()

        if not origen or not destino:
            messagebox.showwarning("Datos incompletos", "Debes seleccionar origen y destino.")
            return

        if origen == destino:
            messagebox.showwarning("Selección inválida", "El origen y el destino deben ser distintos.")
            return

        try:
            ruta, distancia_km = dijkstra(self.grafo, origen, destino)
        except Exception as error:
            messagebox.showerror("Error", str(error))
            return

        texto = self.construir_texto_resultado(ruta, distancia_km)
        self.escribir_resultado(texto)
        dibujar_grafo(self.grafo, ruta)

    def construir_texto_resultado(self, ruta: list[str], distancia_km: float) -> str:
        modo = self.combo_modo.get()

        texto = "Ruta óptima encontrada\n"
        texto += "======================\n"
        texto += " → ".join(ruta) + "\n\n"

        texto += "Distancia base\n"
        texto += "--------------\n"
        texto += f"{distancia_km:.2f} km\n"
        texto += f"{kilometros_a_metros(distancia_km):.0f} metros\n"
        texto += f"{kilometros_a_millas(distancia_km):.2f} millas\n\n"

        if modo == "Vehículo":
            perfil = self.combo_vehiculo.get()
            octanaje = self.combo_octanaje.get()
            rendimiento = PERFILES_VEHICULO[perfil]["rendimiento_km_l"]

            estimacion = estimar_auto(distancia_km, rendimiento, octanaje)

            texto += "Estimación en vehículo\n"
            texto += "----------------------\n"
            texto += f"Perfil: {perfil}\n"
            texto += f"Rendimiento estimado: {rendimiento} km/L\n"
            texto += f"Octanaje: {octanaje}\n"
            texto += f"Precio estimado por litro: {formatear_clp(estimacion['precio_litro'])}\n"
            texto += f"Litros estimados: {estimacion['litros']:.2f} L\n"
            texto += f"Costo estimado: {formatear_clp(estimacion['costo'])}\n"
        else:
            estimacion = estimar_caminata(distancia_km)

            texto += "Estimación caminando\n"
            texto += "--------------------\n"
            texto += f"Tiempo estimado: {estimacion['horas']:.2f} horas\n"
            texto += f"Calorías estimadas: {estimacion['calorias']:.0f} kcal\n"

        texto += "\nNota: la ruta óptima se calcula solo con kilómetros. "
        texto += "Las conversiones son valores derivados para presentar el resultado."

        return texto

    def escribir_resultado(self, texto: str):
        self.texto_resultado.delete("1.0", "end")
        self.texto_resultado.insert("1.0", texto)


if __name__ == "__main__":
    app = AplicacionRutas()
    app.mainloop()
