from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from PIL import Image, ImageTk
from ventas import Ventas
from inventario import Inventario
from informacion import Informacion

class Container(tk.Frame):
    def __init__(self, padre, controlador):
        super().__init__(padre)
        self.controlador = controlador
        self.pack()
        self.place(x=0, y=0, width=800, height=400)
        self.config(bg="#C6D9E3")
        self.widgets()

    def show_frames(self, container):
        top_level = tk.Toplevel(self)
        frame = container(top_level)
        frame.config(bg="#C6D9E3")
        frame.pack(fill="both", expand=True)
        top_level.geometry("1100x650+120+20")
        top_level.resizable(False, False)

    def ventas(self):
        self.show_frames(Ventas)

    def inventario(self):
        self.show_frames(Inventario)
        
    def informacion(self):
        self.show_frames(Informacion)

    def widgets(self):  
        
#==============Frame superior=======================================================================================================#
        frame1 = tk.Frame(self, bg="#C6D9E3",highlightbackground="gray", highlightthickness=1)
        frame1.pack()
        frame1.place(x=0, y=0, width=800, height=400)
        
        #Boton 1
        
        btnventas = Button(frame1, bg="#f4b400", fg="white", text="Ir a ventas", font="sans 18 bold", command=self.ventas)
        btnventas.place(x=500, y=30, width=240, height=60)
        
        #Boton 2
        
        btninventario = Button(frame1, bg="#c62e26", fg="white", text="Ir a inventario", font="sans 18 bold",command=self.inventario)
        btninventario.place(x=500, y=130, width=240, height=60)
        
        #Boton 3
        
        btninformacion = Button(frame1, bg="#4287f9", fg="white", text="About Us", font="sans 18 bold",command=self.informacion)
        btninformacion.place(x=500, y=230, width=240, height=60)
        
        self.logo_image = Image.open("imagenes/registradora.png")
        self.logo_image = self.logo_image.resize((280, 280))
        self.logo_image = ImageTk.PhotoImage(self.logo_image)
        self.logo_label = tk.Label(frame1, image=self.logo_image, bg="#C6D9E3")
        self.logo_label.place(x=100, y=30)

        copyright_label = tk.Label(frame1, text="© 2024 InnovaSoft Code. Todos los derechos reservados.", font=("Arial", 12), bg="#C6D9E3", fg="gray")
        copyright_label.place(x=180, y=350)
        
       