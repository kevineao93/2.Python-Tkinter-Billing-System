import sqlite3
from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox

class Inventario(tk.Frame):
    db_name = "database.db"
    
    def __init__(self, padre):
        super().__init__(padre)
        self.pack()
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        self.widgets()
        
    def widgets(self):
        # Frame superior
        frame1 = tk.Frame(self, bg="#dddddd", highlightbackground="gray", highlightthickness=1)
        frame1.pack()
        frame1.place(x=0, y=0, width=1100, height=100)
                
        titulo = tk.Label(self, text="INVENTARIOS", font="sans 30 bold", bg="#dddddd", anchor="center")
        titulo.pack()  
        titulo.place(x=5, y=0, width=1090, height=90)
 
        # Frame inferior
        frame2 = tk.Frame(self, bg="#C6D9E3", highlightbackground="gray", highlightthickness=1)
        frame2.place(x=0, y=100, width=1100, height=550)
        
        # LabelFrame Izquierdo
        labelframe = LabelFrame(frame2, text="Productos", font="sans 22 bold", bg="#C6D9E3")
        labelframe.place(x=20, y=30, width=400, height=500)
        
        lblnombre = Label(labelframe, text="Nombre: ", font="sans 14 bold", bg="#C6D9E3")
        lblnombre.place(x=10, y=20)
        self.nombre = ttk.Entry(labelframe, font="sans 14 bold")
        self.nombre.place(x=140, y=20, width=240, height=40)
        
        lblproveedor = Label(labelframe, text="Proveedor: ", font="sans 14 bold", bg="#C6D9E3")
        lblproveedor.place(x=10, y=80)
        self.proveedor = ttk.Entry(labelframe, font="sans 14 bold")
        self.proveedor.place(x=140, y=80, width=240, height=40)

        lblprecio = Label(labelframe, text="Precio: ", font="sans 14 bold", bg="#C6D9E3")
        lblprecio.place(x=10, y=140)
        self.precio = ttk.Entry(labelframe, font="sans 14 bold")
        self.precio.place(x=140, y=140, width=240, height=40)
        
        lblcosto = Label(labelframe, text="Costo: ", font="sans 14 bold", bg="#C6D9E3")
        lblcosto.place(x=10, y=200)
        self.costo = ttk.Entry(labelframe, font="sans 14 bold")
        self.costo.place(x=140, y=200, width=240, height=40)
        
        lblstock = Label(labelframe, text="Stock: ", font="sans 14 bold", bg="#C6D9E3")
        lblstock.place(x=10, y=260)
        self.stock = ttk.Entry(labelframe, font="sans 14 bold")
        self.stock.place(x=140, y=260, width=240, height=40)
        
        boton_agregar = tk.Button(labelframe, text="Ingresar", font="sans 14 bold", bg="#dddddd", command=self.registrar)
        boton_agregar.place(x=80, y=340, width=240, height=40)
        
        boton_editar = tk.Button(labelframe, text="Editar producto", font="sans 14 bold", bg="#dddddd", command=self.editar_producto)
        boton_editar.place(x=80, y=400, width=240, height=40)

        # TreeView Tabla
        treFrame = Frame(frame2, bg="white")
        treFrame.place(x=440, y=50, width=620, height=400)

        # Barra de desplazamiento vertical
        scrol_y = ttk.Scrollbar(treFrame)
        scrol_y.pack(side=RIGHT, fill=Y)

        # Barra de desplazamiento horizontal
        scrol_x = ttk.Scrollbar(treFrame, orient=HORIZONTAL)
        scrol_x.pack(side=BOTTOM, fill=X)

        # Widget Treeview
        self.tre = ttk.Treeview(treFrame, yscrollcommand=scrol_y.set, xscrollcommand=scrol_x.set, height=40, 
                                columns=("ID", "PRODUCTO", "PROVEEDOR", "PRECIO", "COSTO", "STOCK"), show="headings")
        self.tre.pack(expand=True, fill=BOTH)

        scrol_y.config(command=self.tre.yview)
        scrol_x.config(command=self.tre.xview)

        self.tre.heading("ID", text="Id")
        self.tre.heading("PRODUCTO", text="Producto")    
        self.tre.heading("PROVEEDOR", text="Proveedor")
        self.tre.heading("PRECIO", text="Precio")
        self.tre.heading("COSTO", text="Costo")
        self.tre.heading("STOCK", text="Stock")

        self.tre.column("ID", width=70, anchor="center")
        self.tre.column("PRODUCTO", width=100, anchor="center")    
        self.tre.column("PROVEEDOR", width=100, anchor="center")
        self.tre.column("PRECIO", width=100, anchor="center")
        self.tre.column("COSTO", width=100, anchor="center")
        self.tre.column("STOCK", width=70, anchor="center")
        
        self.mostrar()
        
        btn_actualizar = Button(frame2, text="Actualizar Inventario", font="sans 14 bold", bg="#dddddd", fg="black", command=self.actualizar_inventario)
        btn_actualizar.place(x=440, y=480, width=260, height=50)
        
    def eje_consulta(self, consulta, parametros=()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(consulta, parametros)
            conn.commit()
        return result
    
    def validacion(self, nombre, prov, precio, costo, stock):
        # Verificar que todos los campos tengan datos
        if not (nombre and prov and precio and costo and stock):
            return False
        # Verificar que precio, costo y stock sean valores numéricos
        try:
            float(precio)
            float(costo)
            int(stock)
        except ValueError:
            return False
        return True
    
    def mostrar(self):  # mostrar en el Treeview
        consulta = "SELECT * FROM inventario ORDER BY id DESC"
        result = self.eje_consulta(consulta)
        for elem in result:
            try:
                precio_cop = "{:,.0f} COP".format(float(elem[3])) if elem[3] else ""  # Formatear el precio a moneda COP
                costo_cop = "{:,.0f} COP".format(float(elem[4])) if elem[4] else ""  # Formatear el costo a moneda COP
            except ValueError:
                precio_cop = elem[3]
                costo_cop = elem[4]
            self.tre.insert("", 0, text=elem[0], values=(elem[0], elem[1], elem[2], precio_cop, costo_cop, elem[5]))
    
    def registrar(self):
        result = self.tre.get_children()
        for i in result:
            self.tre.delete(i)
        nombre = self.nombre.get()  # recuperar o agarrar los datos de los entry
        prov = self.proveedor.get()
        precio = self.precio.get()
        costo = self.costo.get()
        stock = self.stock.get()
        if self.validacion(nombre, prov, precio, costo, stock):
            try:
                consulta = "INSERT INTO inventario VALUES(?,?,?,?,?,?)"
                parametros = (None, nombre, prov, precio, costo, stock)
                self.eje_consulta(consulta, parametros)    
                self.mostrar()
                self.nombre.delete(0, END)
                self.proveedor.delete(0, END)
                self.precio.delete(0, END)
                self.costo.delete(0, END)
                self.stock.delete(0, END)
            except Exception as e:
                messagebox.showwarning(title="Error", message=f"Error al registrar el producto: {e}")
        else:
            messagebox.showwarning(title="Error", message="Rellene todos los campos correctamente")
            self.mostrar()
    
    def actualizar_inventario(self):
        # Limpiar el Treeview antes de mostrar los datos actualizados
        for item in self.tre.get_children():
            self.tre.delete(item)
        
        # Mostrar los datos actualizados en el Treeview
        self.mostrar()
        
        messagebox.showinfo("Actualización", "El inventario ha sido actualizado correctamente.")
    
    def editar_producto(self):
        # Obtener el ítem seleccionado en el Treeview
        seleccion = self.tre.selection()
        if not seleccion:
            messagebox.showwarning("Editar Producto", "Seleccione un producto para editar.")
            return
        
        # Obtener los datos del ítem seleccionado
        item_id = self.tre.item(seleccion)["text"]
        item_values = self.tre.item(seleccion)["values"]
        
#=============Abrir una ventana para editar el producto=============================================================================#
        ventana_editar = Toplevel()
        ventana_editar.title("Editar Producto")
        ventana_editar.geometry("400x400")
        ventana_editar.config(bg="#C6D9E3")
        
        # Nombre
        lbl_nombre = Label(ventana_editar, text="Nombre:", font="sans 14 bold",bg="#C6D9E3")
        lbl_nombre.grid(row=0, column=0, padx=10, pady=10)
        entry_nombre = Entry(ventana_editar, font="sans 14 bold")
        entry_nombre.grid(row=0, column=1, padx=10, pady=10)
        entry_nombre.insert(0, item_values[1])
        
        # Proveedor
        lbl_proveedor = Label(ventana_editar, text="Proveedor:", font="sans 14 bold",bg="#C6D9E3")
        lbl_proveedor.grid(row=1, column=0, padx=10, pady=10)
        entry_proveedor = Entry(ventana_editar, font="sans 14 bold")
        entry_proveedor.grid(row=1, column=1, padx=10, pady=10)
        entry_proveedor.insert(0, item_values[2])
        
        # Precio
        lbl_precio = Label(ventana_editar, text="Precio (COP):", font="sans 14 bold",bg="#C6D9E3")
        lbl_precio.grid(row=2, column=0, padx=10, pady=10)
        entry_precio = Entry(ventana_editar, font="sans 14 bold")
        entry_precio.grid(row=2, column=1, padx=10, pady=10)
        entry_precio.insert(0, item_values[3].split()[0].replace(",", ""))
        
        # Costo
        lbl_costo = Label(ventana_editar, text="Costo (COP):", font="sans 14 bold",bg="#C6D9E3")
        lbl_costo.grid(row=3, column=0, padx=10, pady=10)
        entry_costo = Entry(ventana_editar, font="sans 14 bold")
        entry_costo.grid(row=3, column=1, padx=10, pady=10)
        entry_costo.insert(0, item_values[4].split()[0].replace(",", ""))
        
        # Stock
        lbl_stock = Label(ventana_editar, text="Stock:", font="sans 14 bold",bg="#C6D9E3")
        lbl_stock.grid(row=4, column=0, padx=10, pady=10)
        entry_stock = Entry(ventana_editar, font="sans 14 bold")
        entry_stock.grid(row=4, column=1, padx=10, pady=10)
        entry_stock.insert(0, item_values[5])
        
        # Función para guardar los cambios
        def guardar_cambios():
            nombre = entry_nombre.get()
            proveedor = entry_proveedor.get()
            precio = entry_precio.get()
            costo = entry_costo.get()
            stock = entry_stock.get()
            
            if not (nombre and proveedor and precio and costo and stock):
                messagebox.showwarning("Guardar Cambios", "Rellene todos los campos.")
                return
            
            try:
                precio = float(precio.replace(",", ""))
                costo = float(costo.replace(",", ""))
            except ValueError:
                messagebox.showwarning("Guardar Cambios", "Ingrese valores numéricos válidos para precio y costo.")
                return
            
            # Actualizar los datos en la base de datos
            consulta = "UPDATE inventario SET nombre=?, proveedor=?, precio=?, costo=?, stock=? WHERE id=?"
            parametros = (nombre, proveedor, precio, costo, stock, item_id)
            self.eje_consulta(consulta, parametros)
            
            # Actualizar el Treeview y el costo total
            self.actualizar_inventario()
            
            # Cerrar la ventana de edición
            ventana_editar.destroy()
        
        # Botón de guardar cambios
        btn_guardar = Button(ventana_editar, text="Guardar Cambios", font="sans 14 bold", bg="#dddddd", command=guardar_cambios)
        btn_guardar.place(x=80, y=250,width=240, height=40)