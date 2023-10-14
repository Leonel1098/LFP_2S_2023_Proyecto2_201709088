from tkinter import *
import tkinter
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText

class Interfaz():
    
    def __init__(self):

        self.ventana = Tk()
        self.ventana.title("ENCRIPTADOR DE MENSAJES")
        self.ventana.geometry("%dx%d+%d+%d" % (900,500,350,100))
        self.ventana.resizable(0,0)

        self.panel_Frame = Frame()
        self.panel_Frame.pack(side="top")
        self.panel_Frame.place(width="900", height="500")
        self.panel_Frame.config(background="black")

        self.boton_archivo_entrada = Button(self.panel_Frame, text = "Cargar Archivo", command= self.cargar_archivo_entrada, foreground="white" )
        self.boton_archivo_entrada.pack()
        self.boton_archivo_entrada.config(bg="black")
        self.boton_archivo_entrada.place(x = 20, y = 18, width = 165, height = 40)

        self.button_cargar = Button(self.panel_Frame, text = "Área de Texto", command = "", foreground="white" )
        self.button_cargar.pack()
        self.button_cargar.config(bg="black")
        self.button_cargar.place(x = 20, y = 60, width = 165, height = 40)

        self.button_generar = Button(self.panel_Frame, text = "Analizar Archivo", command ="", foreground="white" )
        self.button_generar.pack()
        self.button_generar.config(bg="black")
        self.button_generar.place(x = 20, y = 102, width = 165, height = 40)

        self.button_gestionar_drones = Button(self.panel_Frame, text = "Consola", command ="", foreground="white" )
        self.button_gestionar_drones.pack()
        self.button_gestionar_drones.config(bg="black")
        self.button_gestionar_drones.place(x = 20, y = 144, width = 165, height = 40)

        self.button_gestionar_sistemas = Button(self.panel_Frame, text = "Menú Reportes", command ="", foreground="white" )
        self.button_gestionar_sistemas.pack()
        self.button_gestionar_sistemas.config(bg="black")
        self.button_gestionar_sistemas.place(x = 20, y = 186, width = 165, height = 40)

        self.button_gestionar_mensajes = Button(self.panel_Frame, text = "Gestionar Mensajes", command ="", foreground="white" )
        self.button_gestionar_mensajes.pack()
        self.button_gestionar_mensajes.config(bg="black")
        self.button_gestionar_mensajes.place(x = 20, y = 230, width = 165, height = 40)

        self.boton_salir = Button(self.panel_Frame, text = "Salir", command= self.salir, foreground="white" )
        self.boton_salir.pack()
        self.boton_salir.config(bg="black")
        self.boton_salir.place(x = 20, y = 272, width = 165, height = 40)

        self.campo_texto = ScrolledText(self.panel_Frame, wrap = tkinter.WORD)
        self.campo_texto.pack()
        self.campo_texto.place(x = 190, y = 18, width = 700, height = 475)

        self.ventana.mainloop()

    def informacion_estudiante(self):
        messagebox.showinfo(title="Mi ejemplo interfaz",message="Erwin Vásquez - 202001534")
        self.boton_datos_estudiante.config(command=self.informacion_estudiante)


        # Funcion cargar archivo de entrada
    def cargar_archivo_entrada(self):
            route=askopenfilename()
            archivo=open(route,'r')
            archivo.close()
            # Aqui deberia ir su lógica de como leer el xml y llenar sus listas 
            # Mensajito exitoso
            messagebox.showinfo(title="Mi ejemplo interfaz",message="Archivo de entrada cargado con éxito")
            


        # Función para salir del sistema
    def salir(self):
         self.ventana.destroy()
            
       

 