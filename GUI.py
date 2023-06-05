import tkinter as tk
from tkinter import ttk
from Futbolista import Futbolista

class GUI:
    def __init__(self):
        self.lista_futbolistas = []
        self.lista_camisetas = []
        
        self.ventana = tk.Tk()
        self.ventana.title("Interfaz en Python")
        self.ventana.geometry("500x500")
        
        # Esto lo hacemos para crear los tabs o pestañas
        self.notebook = ttk.Notebook(self.ventana)
        self.notebook.pack(fill="both", expand=True)

        self.tab1 = ttk.Frame(self.notebook)
        self.tab2 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab1, text="Futbolistas")
        self.notebook.add(self.tab2, text="Camisetas")

        # Esto lo hacemos para no permitir que se pueda redimensionar
        self.ventana.resizable(width=False, height=False)

        # Creamos una instancia de PhotoImage, se usa para cargar imagenes con tkinter
        self.fondo = tk.PhotoImage(file="fubol.png")
        self.fondo1 = tk.Label(self.tab1, image=self.fondo)
        self.fondo1.place(x=0, y=-210, relwidth=1, relheight=1)

        self.fondo2 = tk.PhotoImage(file="fubol.png")
        self.fondo3 = tk.Label(self.tab2, image=self.fondo2)
        self.fondo3.place(x=0, y=-210, relwidth=1, relheight=1)

        # Labels
        self.lblnombre = tk.Label(self.tab1, text="Nombre", width=20)
        self.lblnombre.place(x=55, y=70)

        self.lbledad = tk.Label(self.tab1, text="Edad", width=20)
        self.lbledad.place(x=55, y=110)

        self.lblfutbolista = tk.Label(self.tab2, text="Futbolista", width=20)
        self.lblfutbolista.place(x=55, y=70)

        self.lblcamisa = tk.Label(self.tab2, text="# Camiseta", width=20)
        self.lblcamisa.place(x=55, y=110)

        # Entradas
        self.nombre_futbolista = tk.StringVar()
        self.edad_futbolista = tk.StringVar()
        self.camisa_futbolista = tk.StringVar()

        self.entrada_nombre = tk.Entry(self.tab1, textvar=self.nombre_futbolista, width=30, relief="flat")
        self.entrada_nombre.place(x=180, y=70)

        self.entrada_edad = tk.Entry(self.tab1, textvar=self.edad_futbolista, width=30, relief="flat")
        self.entrada_edad.place(x=180, y=110)

        self.entrada_camisa = tk.Entry(self.tab2, textvar=self.camisa_futbolista, width=30, relief="flat")
        self.entrada_camisa.place(x=180, y=110)

        # Combobox
        self.combobox = ttk.Combobox(self.tab2, textvariable=self.nombre_futbolista)
        self.combobox.pack()
        self.combobox.place(x=180, y=70)

        # BOTONES
        self.boton_agregar = tk.Button(self.tab1, text="Agregar Futbolista", bg="#e5e5e5",
                                       width=18, height=1, relief="flat",
                                       command=self.agregar_futbolista)
        self.boton_agregar.place(x=180, y=150)

        self.boton_eliminar = tk.Button(self.tab1, text="Eliminar Futbolista", bg="#e5e5e5",
                                        width=18, height=1, relief="flat",
                                        command=self.eliminar_futbolista)
        self.boton_eliminar.place(x=330, y=150)

        self.boton_agregar_camisa = tk.Button(self.tab2, text="Agregar Camiseta", bg="#e5e5e5",
                                              width=18, height=1, relief="flat",
                                              command=self.agregar_camisa)
        self.boton_agregar_camisa.place(x=180, y=150)

        # Tabla Futbolistas
        self.table = ttk.Treeview(self.tab1, columns=("Nombre", "Edad"), show="headings")
        self.table.heading("Nombre", text="Nombre")
        self.table.heading("Edad", text="Edad")
        self.table.pack(pady=50)
        self.table.place(x=55, y=200)

        # Tabla Camisetas
        self.table2 = ttk.Treeview(self.tab2, columns=("Futbolista", "Camiseta"), show="headings")
        self.table2.heading("Futbolista", text="Futbolista")
        self.table2.heading("Camiseta", text="# Camiseta")
        self.table2.pack(pady=50)
        self.table2.place(x=55, y=200)

    def agregar_futbolista(self):
        nombre = self.nombre_futbolista.get()
        edad = self.edad_futbolista.get()

        futbolista = Futbolista(nombre, edad)
        self.lista_futbolistas.append(futbolista)
        self.actualizar_tabla_futbolistas()

    def eliminar_futbolista(self):
        seleccionado = self.table.selection()
        if seleccionado:
            item = self.table.item(seleccionado)
        nombre = item['values'][0]  # Obtener el nombre del futbolista seleccionado
        futbolista_a_eliminar = None
        
        for futbolista in self.lista_futbolistas:
            if futbolista.nombre == nombre:
                futbolista_a_eliminar = futbolista
                break

        if futbolista_a_eliminar:
            self.lista_futbolistas.remove(futbolista_a_eliminar)
            self.actualizar_tabla_futbolistas()

    def agregar_camisa(self):
        futbolista = self.combobox.get()
        camisa = self.camisa_futbolista.get()

        self.lista_camisetas.append((futbolista, camisa))
        self.actualizar_tabla_camisetas()

    def actualizar_tabla_futbolistas(self):
        self.table.delete(*self.table.get_children())
        self.combobox['values'] = [futbolista.nombre for futbolista in self.lista_futbolistas]
        for futbolista in self.lista_futbolistas:
            self.table.insert('', 'end', values=(futbolista.nombre, futbolista.edad))

    def actualizar_tabla_camisetas(self):
        self.table2.delete(*self.table2.get_children())
        for futbolista, camisa in self.lista_camisetas:
            self.table2.insert('', 'end', values=(futbolista, camisa))

    def iniciar(self):
        self.ventana.mainloop()

gui = GUI()
gui.iniciar()


