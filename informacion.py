import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class Informacion(tk.Frame):
    db_name = "database.db"

    def __init__(self, parent):
        super().__init__(parent)
        self.widgets()

    def widgets(self):
        
        #==============Frame superior=======================================================================================================#
        frame1 = tk.Frame(self, bg="#dddddd",highlightbackground="gray", highlightthickness=1)
        frame1.pack()
        frame1.place(x=0, y=0, width=1100, height=100)
        
        titulo = tk.Label(frame1, text="ABOUT US", font="sans 30 bold", bg="#dddddd", anchor="center")
        titulo.pack() 
        titulo.place(x=5, y=0, width=1090, height=90)
        
        #============Frame inferior=======================================================================================================#
        
        frame2 = tk.Frame(self, bg="#C6D9E3",highlightbackground="gray", highlightthickness=1)
        frame2.place(x=0, y=100, width=1100, height=550)

        self.logo_image1 = Image.open("imagenes/innova1.png")
        self.logo_image1 = self.logo_image1.resize((680, 180))
        self.logo_image1 = ImageTk.PhotoImage(self.logo_image1)
        self.logo_label1 = ttk.Label(frame2, image=self.logo_image1, background="#C6D9E3")
        self.logo_label1.place(x=220, y=40)
        
        # Texto de información sobre nosotros
        texto_informacion = """
        Somos una empresa comprometida con brindar soluciones tecnológicas innovadoras. 
        Nuestro equipo está dedicado a proporcionar productos y servicios de alta calidad 
        que satisfagan las necesidades de nuestros clientes. ¡Gracias por elegirnos!
        
        Proyecto: Caja registradora
        Version: 1.00
        Ultima actualizacion: 15/05/2024
        
        Soporte: kevineao@hotmail.com
        Celular: +57 300 2385798
        InnovaSoft Code
        
        Copyright © 2024 Todos los derechos reservados
        """
        label_info = tk.Label(frame2, text=texto_informacion, font="sans 16", bg="#C6D9E3", justify="center")
        label_info.place(x=100, y=180)