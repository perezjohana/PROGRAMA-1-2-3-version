import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def interfaz_uno():
    area_dinamica_limpia()
    tk.Label(area_dinamica, text="Bienvenido", font=("Arial", 14)).pack(pady=10)
    tk.Button(area_dinamica, text="Confirmar", command=lambda: messagebox.showinfo("Hola", "Selecciona en la barra de inicio que deseas hacer")).pack()

def interfaz_dos():
    area_dinamica_limpia()
    tk.Label(area_dinamica, text="Datos del alumno", font=("Arial", 14)).pack(pady=10)

    tk.Label(area_dinamica, text="Nombre del alumno:").pack()
    campo_texto_uno = tk.Entry(area_dinamica)
    campo_texto_uno.pack(pady=5)

    tk.Label(area_dinamica, text="Turno:").pack()
    opcion_elegida = tk.StringVar(value="Matutino")
    tk.Radiobutton(area_dinamica, text="Matutino", variable=opcion_elegida, value="Opción 1").pack()
    tk.Radiobutton(area_dinamica, text="Vespertino", variable=opcion_elegida, value="Opción 2").pack()

    tk.Label(area_dinamica, text="Lista desplegable:").pack()
    combo = ttk.Combobox(area_dinamica, values=["Prmero", "Segundo", "Tercero"])
    combo.pack()
    combo.current(0)

    def accion_guardar():
        valor = campo_texto_uno.get()
        messagebox.showinfo("Revisión", f"Texto: {valor}\nSelección: {opcion_elegida.get()}\nLista: {combo.get()}")

    tk.Button(area_dinamica, text="Botón 2", command=accion_guardar).pack(pady=10)

def interfaz_tres():
    area_dinamica_limpia()
    tk.Label(area_dinamica, text="Configuraciones temporales", font=("Arial", 14)).pack(pady=10)

    colores = ["lightblue", "lightgreen", "lightyellow", "lightgray"]
    tk.Label(area_dinamica, text="Cambiar fondo:").pack()

    def cambiar_color(c):
        ventana_principal.config(bg=c)
        menu_lateral.config(bg=c)
        area_dinamica.config(bg=c)

    for c in colores:
        tk.Button(area_dinamica, text=c, bg=c, width=20, command=lambda col=c: cambiar_color(col)).pack(pady=2)

def interfaz_cuatro():
    area_dinamica_limpia()
    tk.Label(area_dinamica, text="Preguntas del programa", font=("Arial", 14)).pack(pady=10)
    contenido = (
        "Explica con tus palabras:\n\n"
        "- ¿Qué hace cada botón?\n"
        "- ¿Qué cambias si modificas un texto?\n"
        "- ¿Cómo cambias un color?\n"
        "- ¿Qué debes renombrar?"
    )
    tk.Label(area_dinamica, text=contenido, justify="left").pack(pady=10)

def area_dinamica_limpia():
    for widget in area_dinamica.winfo_children():
        widget.destroy()

ventana_principal = tk.Tk()
ventana_principal.title("Interfaz para prácticas")
ventana_principal.geometry("500x400")
ventana_principal.config(bg="lightblue")

menu_lateral = tk.Frame(ventana_principal, bg="lightblue", width=120)
menu_lateral.pack(side="left", fill="y")

area_dinamica = tk.Frame(ventana_principal, bg="white")
area_dinamica.pack(side="right", expand=True, fill="both")

tk.Button(menu_lateral, text="Inicio", command=interfaz_uno, width=15).pack(pady=10)
tk.Button(menu_lateral, text="Datos generales", command=interfaz_dos, width=15).pack(pady=10)
tk.Button(menu_lateral, text="Color de la impresión", command=interfaz_tres, width=15).pack(pady=10)
tk.Button(menu_lateral, text="Dudas del progra", command=interfaz_cuatro, width=15).pack(pady=10)
tk.Button(menu_lateral, text="Preguntas del programa", command=interfaz_cuatro, width=15).pack(pady=10)
tk.Button(menu_lateral, text="Regresar", command=ventana_principal.destroy, width=15).pack(pady=30)

interfaz_uno()
ventana_principal.mainloop()
