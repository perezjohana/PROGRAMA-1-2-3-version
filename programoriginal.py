import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

datos_guardados = []#el nombre del arreglo

def mensaje_bienvenida():#el nombre de la funcion es el nombre de bienvenida
    area_dinamica_limpia()
    tk.Label(area_dinamica, text="Bienvenido", font=("Arial", 14)).pack(pady=10)
    tk.Button(area_dinamica, text="Hola", command=lambda: messagebox.showinfo("Selecciona en la barra de inicio que necesitas realizar")).pack()#se cambio el mensaje de bienvenida
    
def ingreso_datos():#el nombre de la funcion es el ingresar datos
    area_dinamica_limpia()
    tk.Label(area_dinamica, text="Datos del alumno", font=("Arial", 14)).pack(pady=10)

    tk.Label(area_dinamica, text="Ingresa el nombre del alumno:").pack()#se cambio el campo a por el ombre del alumno
    campo_texto_uno = tk.Entry(area_dinamica)
    campo_texto_uno.pack(pady=5)

    tk.Label(area_dinamica, text="Turno:").pack()
    opcion_elegida = tk.StringVar(value="Matutino")
    tk.Radiobutton(area_dinamica, text="Matutino", variable=opcion_elegida, value="Opción 1").pack()
    tk.Radiobutton(area_dinamica, text="vespertino", variable=opcion_elegida, value="Opción 2").pack()

    tk.Label(area_dinamica, text="Grado:").pack()
    combo = ttk.Combobox(area_dinamica, values=["primero", "segundo", "tercero"])
    combo.pack()
    combo.current(0)
    
    
    etiqueta_datos = tk.Label(area_dinamica, text="", font=("Arial", 12), fg="black")
    etiqueta_datos.pack(pady=10)

    def accion_guardar():
        valor = campo_texto_uno.get()
        seleccion = opcion_elegida.get()
        lista = combo.get()
        
        # Guardamos los datos en la lista
        datos_guardados.append(f"Nombre: {valor}, Selección: {seleccion}, Lista: {lista}")
        
        # Actualizar la visualización de los datos en el área dinámica
        etiqueta_datos.config(text="\n".join(datos_guardados))

    tk.Button(area_dinamica, text="Guardar Datos", command=accion_guardar).pack(pady=5)


def color_ventana():#te da la opcion de cambiar el color de la ventana
    area_dinamica_limpia()
    tk.Label(area_dinamica, text="Configuraciones temporales", font=("Arial", 14)).pack(pady=10)

    colores = ["lightblue", "lightgreen", "lightyellow", "lightgray"]
    tk.Label(area_dinamica, text="Color de la impresion").pack()

    def cambiar_color(c):
        ventana_principal.config(bg=c)
        menu_lateral.config(bg=c)
        area_dinamica.config(bg=c)

    for c in colores:
        tk.Button(area_dinamica, text=c, bg=c, width=20, command=lambda col=c: cambiar_color(col)).pack(pady=2)

def interfaz_preguntas():#te da texto donde menciona algunas preguntas sobre el codigo
    area_dinamica_limpia()
    tk.Label(area_dinamica, text="Preguntas del programa", font=("Arial", 14)).pack(pady=10)#cambiamos el titulo de la ventana por lo que es
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
ventana_principal.geometry("600x400")#se cambio el tamaño para poder apreciar mejor las cosas
ventana_principal.config(bg="lightblue")

menu_lateral = tk.Frame(ventana_principal, bg="lightblue", width=120)
menu_lateral.pack(side="left", fill="y")

area_dinamica = tk.Frame(ventana_principal, bg="white")
area_dinamica.pack(side="right", expand=True, fill="both")

tk.Button(menu_lateral, text="Inicio", command=mensaje_bienvenida, width=15).pack(pady=10)
tk.Button(menu_lateral, text="Ingreso de datos", command=ingreso_datos, width=15).pack(pady=10)
tk.Button(menu_lateral, text="color de la impresion", command=color_ventana, width=15).pack(pady=10)#se le cambio el nombre del boton dependiendo de que hace cada cosa
tk.Button(menu_lateral, text="Dudas del programa", command=interfaz_preguntas, width=15).pack(pady=10)
tk.Button(menu_lateral, text="Regresar", command=ventana_principal.destroy, width=15).pack(pady=30)

mensaje_bienvenida()
ventana_principal.mainloop()
