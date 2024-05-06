# !/usr/bin/python3
# -*- coding: utf-8 -*-
import tkinter as tk
import tkinter.ttk as ttk
import sqlite3
#from tkcalendar import DateEntry
from tkinter import StringVar, messagebox
import datetime
from pathlib import Path
from subprocess import run
from platform import system

if system() == "Windows":
    from ctypes import windll

PATH = str((Path(__file__).resolve()).parent)
ICONO = r"/img/LogoinscripcionesIco.png"
ICONO_CONSULTA = r"/img/lupa.png"
DB = r"db/Inscripciones.db"

class comunicacionBD():
    def __init__(self):
        self.conexion= sqlite3.connect(DB)
    
    def agregar_datos(self, bd, pront, NoInscritos, IdAlumno, FechaInscripcion, CodigoCurso):
        cursor = self.conexion.cursor()
        query = '''INSERT INTO Inscripciones (No_Inscritos, Id_Alumno, Fecha_de_Inscripción, Código_Curso) VALUES ('{}','{}','{}','{}')'''.format (NoInscritos, IdAlumno, FechaInscripcion, CodigoCurso)
        cursor.execute(query)
        self.conexion.commit()
        cursor.close()

    def eliminar_datos(self, codigo):
        cursor = self.conexion.cursor()
        query = '''DELETE FROM Inscritos WHERE Código_Curso = '{}' '''.format(codigo)
        cursor.execute(query)
        self.conexion.commit()
        cursor.close()
    
    def actualiza_datos(self, NoInscritos, IdAlumno, FechaInscripcion, CodigoCurso):
        cursor = self.conexion.cursor()
        query = ''' UPDATE Inscripciones SET No_Inscritos = '{}', Id_Alumno = '{}', Fecha_de_Inscripción = '{}', Código_Curso = '{}'  '''.format (NoInscritos, IdAlumno, FechaInscripcion, CodigoCurso)
        cursor.execute(query)
        dato = cursor.rowcount
        self.conexion.commit()
        cursor.close()
        return dato

class Inscripciones_2:
    def tree_view(self):
        def restrictor(Event):
            # Reviso si una zona especifica alrededor del cursor toca el separador de columnas
            # Esta zona la obtuve con prueba y error.
            for x in range(-10, 10):
                for y in range(1):
                    #Si el separador de columnas está dentro de la zona, entonces doy por hecho que el usuario está intentando cambiar de tamaño la columna.
                    if(self.tView.identify_region(Event.x+x, Event.y+y) == "separator"):
                        self.tView.event_generate("<ButtonRelease-1>") # si esta en el rango, hace creer al equipo que solto el clic
                        break

        self.tView = ttk.Treeview(self.frm_1, name="tview",show='headings')
        self.tView.configure(selectmode="extended")
        #Columnas del Treeview
        self.tView_cols = ['NoInscripción', 'CódigoCurso','tV_descripción', 'Horario' ]

        #self.tView.place(anchor="nw", height=250, width=740, x=30, y=300)

        self.tView.configure(columns=self.tView_cols)
        self.tView.column("#0", width=0) # este es necesario? 
        self.tView.column("NoInscripción",anchor="w",stretch=False,width=110)
        self.tView.column("CódigoCurso",anchor="w",stretch=False,width=110)
        self.tView.column("tV_descripción",anchor="w",stretch=False,width=290)
        self.tView.column("Horario",anchor="w",stretch=False,width=224)

        #Cabeceras
        self.tView.heading("NoInscripción",anchor="w", text='No.Inscripción')
        self.tView.heading("CódigoCurso",anchor="w", text='Código de Curso')
        self.tView.heading("tV_descripción", anchor="w", text='Descripción')
        self.tView.heading("Horario", anchor="w", text='Horario')
        self.tView.place(anchor="nw", height=250, width=740, x=30, y=300)
        
        #Scrollbars
        self.scroll_H = ttk.Scrollbar(self.frm_1, name="scroll_h")
        self.scroll_H.configure(orient="horizontal")
        self.scroll_H.place(anchor="nw", height=15, width=724, x=31, y=534)
        self.scroll_Y = ttk.Scrollbar(self.frm_1, name="scroll_y")
        self.scroll_Y.configure(orient="vertical")
        self.scroll_Y.place(anchor="nw", height=248, width=16, x=753, y=301)
    
        self.frm_1.pack(side="top")
        self.frm_1.pack_propagate(0)

        # Hago que mi función sea llamada cada vez que el usuario hace clic y mueve el cursor.
        self.tView.bind("<B1-Motion>", restrictor)
        
    def centrar(self, win, ancho, alto):
             self.altura_pantalla = win.winfo_screenheight()
             self.ancho_pantalla = win.winfo_screenwidth()

             self.x = (self.ancho_pantalla // 2) - (ancho // 2)
             self.y = (self.altura_pantalla // 2) - (alto // 2)
        
    def __init__(self, master=None):
         # Ventana principal
        self.db_name = 'Inscripciones.db'    
        self.win = tk.Tk(master)
        self.is_fields_enabled = False

        self.win.configure(background="#f7f9fd", height=600, width=800)
        self.centrar(self.win, 800, 600)
        self.win.geometry(f"+{self.x}+{self.y}")
        self.win.resizable(False, False)
        # Título de la ventana
        self.win.title("Inscripciones de Materias y Cursos")
        # Icono de la ventana
        if system() == "Windows":
            windll.shell32.SetCurrentProcessExplicitAppUserModelID('Inscripciones')
            self.win.iconbitmap(PATH + ICONO)
            icono = tk.PhotoImage(file= PATH + ICONO)
            self.win.wm_iconphoto(False, icono)
        elif system() == "Linux" or system() == "Darwin":
            self.icon = tk.PhotoImage(file= PATH + ICONO)
            self.win.iconphoto(True, self.icon)
            

        self.DatosBD = comunicacionBD()
        self.NoInscripcion = tk.StringVar()
        self.IdAlumno = tk.StringVar()
        self.CodigoCurso = tk.StringVar()
        self.FechaInscripcion = tk.StringVar()

        # Crea los frames
        self.frm_1 = tk.Frame(self.win, name="frm_1")
        self.frm_1.configure(background="#f7f9fd", height=600, width=800)

        #Label id_Alumno
        self.lblIdAlumno = ttk.Label(self.frm_1, name="lblidalumno")
        self.lblIdAlumno.configure(background="#f7f9fd",font="{Arial} 9 {bold}", justify="left",
                                state="normal", takefocus=False,text='Id Alumno')
        self.lblIdAlumno.place(anchor="nw", x=20, y=40)
        #Combobox id_Alumno
        self.cmbx_Id_Alumno = ttk.Combobox(self.frm_1, name="cmbx_id_alumno", 
                                           postcommand=self.combx_id_alumno)

        self.cmbx_Id_Alumno.place(anchor="nw", width=110, x=20, y=60)
        
        #Label Nombres
        self.lblNombres = ttk.Label(self.frm_1, name="lblnombres")
        self.lblNombres.configure(background="#f7f9fd",font="{Arial} 9 {bold}", justify="left",
                                state="normal", takefocus=False,text='Nombre(s)')
        self.lblNombres.place(anchor="nw", x=150, y=40)
        #Entry Nombres
        self.nombres = ttk.Entry(self.frm_1, name="nombres")
        self.nombres.place(anchor="nw", width=190, x=150, y=60)

        #Label Apellidos
        self.lblApellidos = ttk.Label(self.frm_1, name="lblapellidos")
        self.lblApellidos.configure(background="#f7f9fd",font="{Arial} 9 {bold}", justify="left",
                                state="normal", takefocus=False,text='Apellido(s)')
        self.lblApellidos.place(anchor="nw", x=360, y=40)
        #Entry Apellidos
        self.apellidos = ttk.Entry(self.frm_1, name="apellidos")
        self.apellidos.place(anchor="nw", width=190, x=360, y=60)
        self.apellidos.insert(0,"")
        
        #Label Fecha
        self.lblFecha = ttk.Label(self.frm_1, name="lblfecha")
        self.lblFecha.configure(background="#f7f9fd",font="{Arial} 9 {bold}", justify="left",
                                state="normal", takefocus=False,text='Fecha Ingreso')
        self.lblFecha.place(anchor="nw", x=570, y=40)

        self.fecha = tk.Entry(self.frm_1, name="fechas")
        self.fecha.configure(justify="right")
        self.fecha.place(anchor="nw", width=90, x=570, y=60)
            
        self.act_date = False

        def cuandoEscriba(event):
            #global act_date
            if event.char.isdigit() or event.char =='/':
                fechaRef = self.fecha.get()
                if len(fechaRef) == 2 or len(fechaRef) ==5:
                    self.act_date = True

                if len(fechaRef) == 2:
                    self.fecha.insert(2,"/")
                    
                if len(fechaRef) == 5:
                    self.fecha.insert(5,"/")
            if event.char.isdigit() or event.char =='\x08' or event.char =='': # \x08 = Backspace, '' = Delete
                self.act_date=True

        def limite(event):
            fechaRef = self.fecha.get()
            #print (fecha)
            try:
                if len(fechaRef) > 10:
                    raise ValueError("digite maximo 8 numeros")
            except ValueError as problem:
                messagebox.showerror("Error", str(problem))
                self.fecha.delete(10, tk.END)

        def verificarNumeros(char):
            #global act_date

            if self.act_date:
                self.act_date = False 
                return char.isdigit() or char == '/'
            else:
                if char == '/' and self.act_date:
                    return char.isdigit() or char == '/'
                else:
                    return char.isdigit()

        def validarFecha(event):
            try:
                self.vFecha = self.fecha.get()
                #compara el formato del texto con el formato y las fechas de libreria
                self.vFecha = datetime.datetime.strptime(self.vFecha,'%d/%m/%Y') 
                print ('fecha valida')
            except ValueError:
                messagebox.showerror("Error", 'Digite un formato de fecha valida')
                #print ('Error: Digite una fecha valida')

        #cuando oprima una tecla cualquiera, ejecuta
        self.fecha.bind("<Key>", cuandoEscriba) 
        ##############################################################
        #evita que valide el borrar como digito
        #self.fecha.bind("<BackSpace>", lambda _:self.fecha.delete(tk.END)) 

        self.fecha.bind("<Return>", validarFecha)
        self.fecha.bind("<Tab>", validarFecha)
        #self.fecha.bind("<FocusOut>", validarFecha)#no borrar

        ############################################################
        self.fecha.bind("<Key>", cuandoEscriba)
        self.fecha.validate_cmd = self.frm_1.register(verificarNumeros)
        self.fecha.config(validate="key", validatecommand=(self.fecha.validate_cmd,"%S"))
        self.fecha.bind("<KeyRelease>", limite)
        
        #Label No. Inscripción
        self.lblNoInscripcion = ttk.Label(self.frm_1, name="lblnoinscripcion")
        self.lblNoInscripcion.configure(background="#f7f9fd",font="{Arial} 9 {bold}", justify="left",
                                        state="normal",text='No.Inscripción')
        self.lblNoInscripcion.place(anchor="nw", x=680, y=40)
        #Conmbox No. Inscripción
        self.noInscripcion = ttk.Combobox(self.frm_1, name="noInscripcion", postcommand=self.combx_no_incripcion)
        self.noInscripcion.place(anchor="nw", width=100, x=680, y=60)
        
        #Label Direccion
        self.lblDireccion = ttk.Label(self.frm_1, name="lbldireccion")
        self.lblDireccion.configure(background="#f7f9fd",font="{Arial} 9 {bold}", justify="left",
                                state="normal", takefocus=False,text='Dirección')
        self.lblDireccion.place(anchor="nw", x=20, y=100)
        #Entry Direccion
        self.direccion = ttk.Entry(self.frm_1, name="direccion")
        self.direccion.place(anchor="nw", width=200, x=20, y=120)

        #Label Ciudad
        self.lblCiudad = ttk.Label(self.frm_1, name="lblciudad")
        self.lblCiudad.configure(background="#f7f9fd",font="{Arial} 9 {bold}", justify="left",
                                state="normal", takefocus=False,text='Ciudad')
        self.lblCiudad.place(anchor="nw", x=240, y=100)
        #Entry Ciudad
        self.ciudad = ttk.Entry(self.frm_1, name="ciudad",)
        self.ciudad.place(anchor="nw", width=130, x=240, y=120)
        
        #Label Departamento
        self.lblDepartamento = ttk.Label(self.frm_1, name="lbldepartamento")
        self.lblDepartamento.configure(background="#f7f9fd",font="{Arial} 9 {bold}", justify="left",
                        state="normal", takefocus=False,text='Departamento')
        self.lblDepartamento.place(anchor="nw", x=390, y=100)
        #Entry Departamento
        self.departamento = ttk.Entry(self.frm_1, name="departamento")
        self.departamento.place(anchor="nw", width=130, x=390, y=120)
        

        #Label Telefono Celular
        self.lblTelCel = ttk.Label(self.frm_1, name="lbltelcel")
        self.lblTelCel.configure(background="#f7f9fd",font="{Arial} 9 {bold}", justify="left",
                        state="normal", takefocus=False,text='Teléfono Celular')
        self.lblTelCel.place(anchor="nw", x=540, y=100)
        #Entry Telefono Celular
        self.telCel = ttk.Entry(self.frm_1, name="telcel")
        self.telCel.place(anchor="nw", width=110, x=540, y=120)

        #Label Telefono Fijo
        self.lblTelFijo = ttk.Label(self.frm_1, name="lbltelfijo")
        self.lblTelFijo.configure(background="#f7f9fd",font="{Arial} 9 {bold}", justify="left",
                        state="normal", takefocus=False,text='Teléfono Fijo')
        self.lblTelFijo.place(anchor="nw", x=670, y=100)
        #Entry Telefono Fijo
        self.telFijo = ttk.Entry(self.frm_1, name="telfijo")
        self.telFijo.place(anchor="nw", width=110, x=670, y=120)
    
        #Label id_carrera
        self.lblIdCarrera = ttk.Label(self.frm_1, name="lblidcarrera")
        self.lblIdCarrera.configure(background="#f7f9fd",font="{Arial} 9 {bold}", justify="left",
                                state="normal", takefocus=False,text='Id Carrera')
        self.lblIdCarrera.place(anchor="nw", x=20, y=160)
        #Combobox id_carrera
        self.cmbx_Id_Carrera = ttk.Entry(self.frm_1, name="cmbx_id_carrera")
        self.cmbx_Id_Carrera.place(anchor="nw", width=60, x=20, y=180)

        #Label Codigo del Curso
        self.lblDscCurso = ttk.Label(self.frm_1, name="lbldsccurso")
        self.lblDscCurso.configure(background="#f7f9fd",font="{Arial} 9 {bold}", justify="left",
                        state="normal", takefocus=False,text='Código del Curso')
        self.lblDscCurso.place(anchor="nw", x=100, y=160)
        #Entry Codigo del Curso 
        self.codigo_Curso = ttk.Combobox(self.frm_1, name="descripc_curso")
        self.codigo_Curso.configure(justify="left", width=166)
        self.codigo_Curso.place(anchor="nw", width=110, x=100, y=180)
        
        #Label Nombre de Curso
        self.lblNombreCurso = ttk.Label(self.frm_1, name="lblnombrecurso")
        self.lblNombreCurso.configure(background="#f7f9fd",font="{Arial} 9 {bold}", justify="left",
                        state="normal", takefocus=False,text='Nombre del Curso')
        self.lblNombreCurso.place(anchor="nw", x=230, y=160)
        #Entry Nombre de Curso
        self.nombreCurso = ttk.Entry(self.frm_1, name="nombrecurso")
        self.nombreCurso.place(anchor="nw", width=240, x=230, y=180)
        
        #Label Horario
        self.lblHorario = ttk.Label(self.frm_1, name="lblhorario")
        self.lblHorario.configure(background="#f7f9fd",font="{Arial} 9 {bold}", justify="left",
                        state="normal", takefocus=False,text='Horario')
        self.lblHorario.place(anchor="nw", x=490, y=160)
        #Entry Horario
        self.horario = ttk.Entry(self.frm_1, name="horario")
        self.horario.place(anchor="nw", width=180, x=490, y=180)
        
        #Fecha de Inscripción
        self.lblFechaInscripcion = ttk.Label(self.frm_1, name="lblfechainscripcion")
        self.lblFechaInscripcion.configure(background="#f7f9fd",font="{Arial} 9 {bold}", justify="left",
                        state="normal", takefocus=False,text='Fecha Inscripción')
        self.lblFechaInscripcion.place(anchor="nw", x=686, y=160)
        #Entry Fecha de Inscripción
        self.fechaInscripcion = ttk.Entry(self.frm_1, name="fechainscripcion")
        self.fechaInscripcion.place(anchor="nw", width=90, x=690, y=180)
        

        ''' Botones  de la Aplicación'''
        
        #Botón Consultar
        self.btnConsultar = ttk.Button(self.frm_1, name="btnconsultar",command=self.consultar_ventana, cursor="hand2")
        self.btnConsultar.configure(text='Consultar')
        self.btnConsultar.place(anchor="nw", x=150, y=260)
        
        
        # @staticmethod
        # def activar_boton_grabar():
        #     self.btnGrabar.config(state="normal")
        #Botón Guardar
        # self.btnConsultar = ttk.Button(self.frm_1, name="btnconsultar", cursor="hand2")
        # self.btnConsultar.configure(text='Consultar')
        # self.btnConsultar.place(anchor="nw", x=150, y=260, width=80)
        
        #Botón Editar
        # def editar():
        #     activar_boton_grabar()
        #     if not self.is_fields_enabled:
        #         self.nombres.config(state="normal")
        #         self.apellidos.config(state="normal")
        #         self.descripc_Curso.config(state="readonly")
        #         self.fecha.config(state="normal")
        #         self.cmbx_Id_Alumno.config(state="disabled")
        #         self.cmbx_Id_Carrera.config(state="normal")
        #         self.ciudad.config(state="normal")
        #         self.departamento.config(state="normal")
        #         self.direccion.config(state="normal")
        #         self.telCel.config(state="normal")
        #         self.telFijo.config(state="normal")
        #         self.is_fields_enabled = True
        #     else:
        #         pass
        self.btnEditar = ttk.Button(self.frm_1, name="btneditar", cursor="hand2")
        self.btnEditar.configure(text='Editar')
        self.btnEditar.place(anchor="nw", x=255, y=260,  width=80)
        
        #Botón Eliminar
        self.btnEliminar = ttk.Button(self.frm_1, name="btneliminar", cursor="hand2",command = self.eliminar_data)
        self.btnEliminar.configure(text='Eliminar')
        self.btnEliminar.place(anchor="nw", x=360, y=260, width=80)
        
        #Botón Cancelar
        # def limpiar(self):
        #     self.entry = [self.noInscripcion, self.cmbx_Id_Alumno, self.fecha, self.fechaInscripcion, 
        #                   self.cmbx_Id_Carrera, self.nombres, self.apellidos, self.direccion, self.ciudad, 
        #                   self.departamento, self.telCel, self.telFijo, self.codigo_Curso, self.nombreCurso, 
        #                   self.horario]
        #     for i in self.entry:
        #         return i.delete(0, tk.END)

        self.btnCancelar = ttk.Button(self.frm_1, name="btncancelar", cursor="hand2", command=self.limpiar)
        self.btnCancelar.configure(text='Cancelar')
        self.btnCancelar.place(anchor="nw", x=465, y=260, width=80)
        # self.btnCancelar = ttk.Button(self.frm_1, name="btncancelar", cursor="hand2", command=self.limpiar)
        # self.btnCancelar.configure(text='Cancelar')
        # self.btnCancelar.place(anchor="nw", x=465, y=260, width=80)
        # self.btnCancelar.bind()
        
    
        #Botón Grabar
        self.btnGrabar = ttk.Button(self.frm_1, name="btngrabar", cursor="hand2")
        self.btnGrabar.configure(text='Grabar')
        self.btnGrabar.place(anchor="nw", x=570, y=260, width=80)
        #Separador
        separator1 = ttk.Separator(self.frm_1)
        separator1.configure(orient="horizontal")
        separator1.place(anchor="nw", width=796, x=2, y=245)

        ''' Treeview de la Aplicación'''

        #Treeview
        self.tree_view()

        #Probar data, borrable
        # def insert_data():
        #     valornombre=self.nombres.get()
        #     valorapellido=self.apellidos.get()
        #     nombre = valornombre+" "+valorapellido
        #     print(nombre)
        #     self.tView.insert("", "end", values=(nombre, "1", "2015734", "Programación de Computadores", "12"))

        # Main widget
        self.mainwindow = self.win

    def run(self):
        self.mainwindow.mainloop()


    ''' A partir de este punto se deben incluir las funciones
     para el manejo de la base de datos '''
    
    def run_sqlite(self):
        self.conn = sqlite3.connect(DB)
        self.conn.execute("PRAGMA foreign_keys = 1")
        self.cursor = self.conn.cursor()
        
    def combx_id_alumno(self):
        self.cursor.execute(f" SELECT Id_Alumno FROM Alumnos")
        self.dato_id = self.cursor.fetchall()
        self.cmbx_Id_Alumno['values'] = self.dato_id

    def combx_no_incripcion(self):
        self.cursor.execute(f" SELECT No_Inscritos FROM Inscritos")
        self.dato_no_inscripcion = self.cursor.fetchall()
        self.noInscripcion['values'] = self.dato_no_inscripcion
        
    def fecha_split(self,fecha):
        self.split = fecha.split("-")
        self.fecha_n = f"{self.split[2]}/{self.split[1]}/{self.split[0]}"
        return self.fecha_n
    
    def limpiar(self):
        self.entry = [self.noInscripcion, self.cmbx_Id_Alumno, self.fecha, self.fechaInscripcion, 
                        self.cmbx_Id_Carrera, self.nombres, self.apellidos, self.direccion, self.ciudad, 
                        self.departamento, self.telCel, self.telFijo, self.codigo_Curso, self.nombreCurso, 
                        self.horario]
        for i in self.entry:
            i.config(state="normal")
            i.delete(0, tk.END)
        
        self.tView.delete(*self.tView.get_children())
    
    def consultar_ventana(self):
        
        self.ventana_emergente = tk.Toplevel(self.win)
        self.ventana_emergente.title("Consulta de Datos")
        self.icon_consulta = tk.PhotoImage(file= PATH + ICONO)
        self.ventana_emergente.iconphoto(False, self.icon_consulta)
         
        self.ventana_emergente.resizable(False, False)
        self.ventana_emergente.geometry("400x200")
        self.centrar(self.ventana_emergente, 400, 200)
        self.ventana_emergente.geometry(f"+{self.x}+{self.y}")
        
        self.frm_consulta = tk.Frame(self.ventana_emergente, name="frm_consulta")
        self.frm_consulta.configure(background= "#f7f9fd", height=200, width=400)
        self.frm_consulta.pack(fill='both', expand=True)
        
        self.lblOpciones = ttk.Label(self.frm_consulta, name="lblOpciones")
        self.lblOpciones.configure(background="#f7f9fd",font="{Arial} 9 {bold}", justify="left",
                                state="normal", takefocus=False,text="Para realizar la consulta escoja una de las siguientes opciones: ")
        self.lblOpciones.place(anchor="nw", x=20, y=20)
        
        self.int = tk.IntVar()
        self.int.set(0)
        self.int1 = tk.IntVar()
        self.int1.set(0)
        self.int2 = tk.IntVar()
        self.int2.set(0)
          
        self.checkNoInscripcion = ttk.Checkbutton(self.frm_consulta, name="checkNoInscripcion", variable=self.int, onvalue=1, offvalue=0)
        self.checkNoInscripcion.configure(text="No. Inscripción")
        self.checkNoInscripcion.place(anchor="nw", x=40, y=50)
        self.checkIdAlumno = ttk.Checkbutton(self.frm_consulta, name="checkIdAlumno")
        self.checkIdAlumno.configure(text="Id Alumno", variable=self.int1, onvalue=1, offvalue=0)
        self.checkIdAlumno.place(anchor="nw", x=40, y=80)
        self.checkCursos = ttk.Checkbutton(self.frm_consulta, name="checkCursos")
        self.checkCursos.configure(text="Cursos", variable=self.int2, onvalue=1, offvalue=0)
        self.checkCursos.place(anchor="nw", x=40, y=110)
        self.btnEscoger = ttk.Button(self.frm_consulta, name="btnEscoger", cursor="hand2", command=self.boton_escoger)
        self.btnEscoger.configure(text="Consultar Datos")
        self.btnEscoger.place(anchor="nw", x=135, y=160)
        
 
    def boton_escoger(self):
        if self.int.get() == 1 and self.int1.get() == 0 and self.int2.get() == 0:
            self.ventana_emergente.destroy()
            self.consultar_no_inscripción()
        elif self.int1.get() == 1 and self.int.get() == 0 and self.int2.get() == 0:
            print("Escoger Id Alumno")
            self.ventana_emergente.destroy()
            self.consultar_id_alumno()
        elif self.int2.get() == 1 and self.int.get() == 0 and self.int1.get() == 0:
            self.ventana_emergente.destroy()
            self.consultar_cursos()

        else:
            messagebox.showwarning("Advertencia", "Debe seleccionar una opción")
            self.int.set(0)
            self.int1.set(0)
            self.int2.set(0)
    
    def consultar_no_inscripción(self):
        self.tView_c_inscripcion = ttk.Treeview(self.frm_1, name="tview",show='headings')
        self.tView_c_inscripcion.configure(selectmode="extended")
        self.tView_c_inscripcion.place(anchor="nw", height=250, width=740, x=30, y=300)
        self.tView_cols_c1 = ['NoInscripción', 'Nombres','Apellidos', 'Fecha_Inscripción', 'Código_Curso' ]
        self.tView_c_inscripcion.configure(columns=self.tView_cols_c1)
        self.tView_c_inscripcion.column("#0", width=0)
        self.tView_c_inscripcion.column("NoInscripción",anchor="w",stretch=False,width=100)
        self.tView_c_inscripcion.column("Nombres",anchor="w",stretch=False,width=110)
        self.tView_c_inscripcion.column("Apellidos",anchor="w",stretch=False,width=290)
        self.tView_c_inscripcion.column("Fecha_Inscripción",anchor="w",stretch=False,width=224)
        self.tView_c_inscripcion.column("Código_Curso",anchor="w",stretch=False,width=224)
        #Cabeceras
        self.tView_c_inscripcion.heading("NoInscripción",anchor="w", text='No.Inscripción')
        self.tView_c_inscripcion.heading("Nombres",anchor="w", text='Nombre(s)')
        self.tView_c_inscripcion.heading("Apellidos", anchor="w", text='Apellido(s)')
        self.tView_c_inscripcion.heading("Fecha_Inscripción", anchor="w", text='Fecha de Inscripción')
        self.tView_c_inscripcion.heading("Código_Curso", anchor="w", text='Código de Curso')
        self.tView_c_inscripcion.place(anchor="nw", height=250, width=740, x=30, y=300)
        #Scrollbars
        self.scroll_H_c_inscripcion = ttk.Scrollbar(self.frm_1, name="scroll_h")
        self.scroll_H_c_inscripcion.configure(orient="horizontal")
        self.scroll_H_c_inscripcion.place(anchor="nw", height=15, width=724, x=31, y=534)
        self.scroll_Y_c_inscripcion = ttk.Scrollbar(self.frm_1, name="scroll_y")
        self.scroll_Y_c_inscripcion.configure(orient="vertical")
        self.scroll_Y_c_inscripcion.place(anchor="nw", height=248, width=16, x=753, y=301)
        self.scroll_H_c_inscripcion.configure(command=self.tView_c_inscripcion.xview)
        self.scroll_Y_c_inscripcion.configure(command=self.tView_c_inscripcion.yview)   
        self.tView_c_inscripcion.configure(xscrollcommand=self.scroll_H_c_inscripcion.set, yscrollcommand=self.scroll_Y_c_inscripcion.set)
        self.frm_1.pack(side="top")
        self.frm_1.pack_propagate(0)
        
        self.cursor.execute(''' SELECT Inscritos.No_Inscritos, Nombres, Apellidos, Inscritos.Fecha_de_Inscripción, Código_Curso FROM Inscritos
                            JOIN Alumnos ON Inscritos.Id_Alumno = Alumnos.Id_Alumno
                            ''')
        self.datos = self.cursor.fetchall()
        for i in self.datos:
            self.tView_c_inscripcion.insert("", tk.END, values=(i[0], i[1], i[2], i[3], i[4]))
        
    def consultar_id_alumno(self):
        self.tView_c_alumno = ttk.Treeview(self.frm_1, name="tview",show='headings')
        self.tView_c_alumno.configure(selectmode="extended")
        self.tView_c_alumno.place(anchor="nw", height=250, width=740, x=30, y=300)
        self.tView_cols_c1 = ['Id_Alumno','Nombres','Apellidos','Id_Carrera','Fecha_de_Ingreso','Dirección','Ciudad','Departamento','Tel_Cel','Tel_Fijo']
        self.tView_c_alumno.configure(columns=self.tView_cols_c1)
        self.tView_c_alumno.column("#0", width=0)
        self.tView_c_alumno.column("Id_Alumno",anchor="w",stretch=False,width=100)
        self.tView_c_alumno.column("Nombres",anchor="w",stretch=False,width=110)
        self.tView_c_alumno.column("Apellidos",anchor="w",stretch=False,width=200)
        self.tView_c_alumno.column("Id_Carrera",anchor="w",stretch=False,width=204)
        self.tView_c_alumno.column("Fecha_de_Ingreso",anchor="w",stretch=False,width=204)
        self.tView_c_alumno.column("Dirección",anchor="w",stretch=False,width=204)
        self.tView_c_alumno.column("Ciudad",anchor="w",stretch=False,width=204)
        self.tView_c_alumno.column("Departamento",anchor="w",stretch=False,width=204)
        self.tView_c_alumno.column("Tel_Cel",anchor="w",stretch=False,width=204)
        self.tView_c_alumno.column("Tel_Fijo",anchor="w",stretch=False,width=204)
        #Cabeceras
        self.tView_c_alumno.heading("Id_Alumno",anchor="w", text='Id Alumno')
        self.tView_c_alumno.heading("Nombres",anchor="w", text='Nombre(s)')
        self.tView_c_alumno.heading("Apellidos", anchor="w", text='Apellido(s)')
        self.tView_c_alumno.heading("Id_Carrera", anchor="w", text='Id Carrera')
        self.tView_c_alumno.heading("Fecha_de_Ingreso", anchor="w", text='Fecha de Ingreso')
        self.tView_c_alumno.heading("Dirección", anchor="w", text='Dirección')
        self.tView_c_alumno.heading("Ciudad", anchor="w", text='Ciudad')
        self.tView_c_alumno.heading("Departamento", anchor="w", text='Departamento')
        self.tView_c_alumno.heading("Tel_Cel", anchor="w", text='Teléfono Celular')
        self.tView_c_alumno.heading("Tel_Fijo", anchor="w", text='Teléfono Fijo')

        self.tView_c_alumno.place(anchor="nw", height=250, width=740, x=30, y=300)
        #Scrollbars
        self.scroll_H_c_alumno = ttk.Scrollbar(self.frm_1, name="scroll_h")
        self.scroll_H_c_alumno.configure(orient="horizontal")
        self.scroll_H_c_alumno.place(anchor="nw", height=15, width=724, x=31, y=534)
        self.scroll_Y_c_alumno = ttk.Scrollbar(self.frm_1, name="scroll_y")
        self.scroll_Y_c_alumno.configure(orient="vertical")
        self.scroll_Y_c_alumno.place(anchor="nw", height=248, width=16, x=753, y=301)
        self.scroll_H_c_alumno.configure(command=self.tView_c_alumno.xview)
        self.scroll_Y_c_alumno.configure(command=self.tView_c_alumno.yview)   
        self.tView_c_alumno.configure(xscrollcommand=self.scroll_H_c_alumno.set, yscrollcommand=self.scroll_Y_c_alumno.set)
        self.frm_1.pack(side="top")
        self.frm_1.pack_propagate(0)
        
        self.cursor.execute(''' SELECT Id_alumno, Nombres, Apellidos, Id_Carrera, Fecha_Ingreso, Dirección, Ciudad, Departamento, Telef_Cel, Telef_Fijo FROM Alumnos''') 
        self.datos = self.cursor.fetchall()
        for i in self.datos:
            self.tView_c_alumno.insert("", tk.END, values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9]))
        
    
    def consultar_cursos(self):
        self.tView_c_cursos = ttk.Treeview(self.frm_1, name="tview",show='headings')
        self.tView_c_cursos.configure(selectmode="extended")
        self.tView_c_cursos.place(anchor="nw", height=250, width=740, x=30, y=300)
        self.tView_cols_c1 = ['Código_Curso','Descripción_Curso','Num_Horas']
        self.tView_c_cursos.configure(columns=self.tView_cols_c1)
        self.tView_c_cursos.column("#0", width=0)
        self.tView_c_cursos.column("Código_Curso",anchor="w",stretch=False,width=100)
        self.tView_c_cursos.column("Descripción_Curso",anchor="w",stretch=False,width=250)
        self.tView_c_cursos.column("Num_Horas",anchor="w",stretch=False,width=250)
        #Cabeceras
        self.tView_c_cursos.heading("Código_Curso",anchor="w", text='Código Curso')
        self.tView_c_cursos.heading("Descripción_Curso", anchor="w", text='Descripción Curso')
        self.tView_c_cursos.heading("Num_Horas", anchor="w", text='Número de Horas')
        self.tView_c_cursos.place(anchor="nw", height=250, width=740, x=30, y=300)
        #Scrollbars
        self.scroll_H_c_cursos = ttk.Scrollbar(self.frm_1, name="scroll_h")
        self.scroll_H_c_cursos.configure(orient="horizontal")
        self.scroll_H_c_cursos.place(anchor="nw", height=15, width=724, x=31, y=534)
        self.scroll_Y_c_cursos = ttk.Scrollbar(self.frm_1, name="scroll_y")
        self.scroll_Y_c_cursos.configure(orient="vertical")
        self.scroll_Y_c_cursos.place(anchor="nw", height=248, width=16, x=753, y=301)
        self.scroll_H_c_cursos.configure(command=self.tView_c_cursos.xview)
        self.scroll_Y_c_cursos.configure(command=self.tView_c_cursos.yview)
        self.tView_c_cursos.configure(xscrollcommand=self.scroll_H_c_cursos.set, yscrollcommand=self.scroll_Y_c_cursos.set)
        self.frm_1.pack(side="top")
        self.frm_1.pack_propagate(0)
        
        self.cursor.execute(''' SELECT Código_Curso, Descripción_Curso, Num_Horas FROM Cursos''')
        self.datos = self.cursor.fetchall()
        for i in self.datos:
            self.tView_c_cursos.insert("", tk.END, values=(i[0], i[1], i[2]))

        
    def consultar(self):
                
        self.cursor.execute(f''' SELECT Inscritos.Id_Alumno, Nombres, Apellidos, Fecha_Ingreso, No_Inscritos, Dirección, Ciudad, Departamento, 
                            Telef_Cel, Telef_Fijo, Id_Carrera, Inscritos.Código_Curso, Descripción_Curso, Num_Horas, Fecha_de_Inscripción  FROM Inscritos 
                    JOIN Alumnos ON Inscritos.Id_Alumno = Alumnos.Id_Alumno 
                    JOIN Cursos ON Inscritos.Código_Curso = Cursos.Código_Curso 
                    JOIN Carreras ON Alumnos.Id_Carrera = Carreras.Código_Carrera 
                    WHERE Inscritos.No_Inscritos = {self.noInscripcion.get()}''')
        self.datos = self.cursor.fetchall()
        self.lista = []
        for i in self.datos:
            self.lista += i 
        
        self.fecha_ins = self.fecha_split(self.lista[3])
        
        self.fecha_ing = self.fecha_split(self.lista[14])
        
        self.limpiar()
        
        self.entry_datos = [self.cmbx_Id_Alumno, self.nombres, self.apellidos, self.fecha, self.noInscripcion, self.direccion, self.ciudad,
                 self.departamento, self.telCel, self.telFijo, self.cmbx_Id_Carrera, self.codigo_Curso, self.nombreCurso, self.horario, 
                 self.fechaInscripcion]
        self.a = 0
        for i in self.entry_datos:
            if i == self.fecha:
                i.insert(0, self.fecha_ing)
                i.config(state="readonly")
            elif i == self.fechaInscripcion:
                i.insert(0, self.fecha_ins)
                i.config(state="readonly")
            else:
                i.insert(0, self.lista[self.a])
                i.config(state="readonly")
            self.a += 1
                 
        self.tree_view()

        self.cursor.execute(f'''SELECT * FROM Inscritos
                   JOIN Cursos ON Inscritos.Código_Curso = Cursos.Código_Curso
                   WHERE Inscritos.Id_Alumno = {self.lista[0]}
                   ''')
        datos_materias = self.cursor.fetchall()
        for i in datos_materias:
            self.lista_materia = []
            self.lista_materia += i
            self.tView.insert("", tk.END, values=(self.lista_materia[0], self.lista_materia[4], self.lista_materia[5], self.lista_materia[6]))

    #borrable
    # def eliminar_data (self):
    #     print('Eliminar')
    #     print(str(self.tView.selection()[0]))
    #     try:
    #         print(str(self.tView.item(self.tView.selection())))
    #         self.tView.item(self.tView.selection())['text'][0]
            
    #     except IndexError as problem:
    #         messagebox.showerror("Error", str(problem))
    #         return
        
    def limpiar_data(self):
        self.NoInscripcion.set('')
        self.IdAlumno.set('')
        self.CodigoCurso.set('')
        self.FechaInscripcion.set('')

    def obtener_fila(self, event):
        item = self.tView.focus()
        self.data = self.tView.item(item)
        self.NoInscripcion.set(self.data["values"][0])
        self.CodigoCurso.set(self.data["values"][1])
        self.IdAlumno.set(self.data["values"][2])
        self.FechaInscripcion.set(self.data["values"][3])

        print(str(self.NoInscripcion.get()))
        print(str(self.IdAlumno.get()))
        print(str(self.CodigoCurso.get()))
        print(str(self.FechaInscripcion.get()))
    
    def eliminar_data (self):
        self.limpiar_data()
        item = self.tView.selection()[0]
        alert = messagebox.askquestion('Eliminando datos', 'Desea eliminar este valor?')
        if alert == 'yes':            
            self.tView.delete(item)
            self.DatosBD.eliminar_datos(self.data["values"][1])
            print('Borrado')
        

        # name = self.tView.item(self.tView.selection())['text']
        # query = 'DELETE FROM product WHERE name = ?'
        # self.run_query(query, (name,))

        # self.cursor.execute(f"DELETE from inscpciones where ID=" + self)
        # self.cursor.close()
        # self.cursor.commit()

        
    # def get_data_idalumno(self):
    #     self.cursor.execute("SELECT Id_Alumno FROM Alumnos")
    #     self.data = self.cursor.fetchall()
    #     self.lista_idalumnos = []
    #     for i in self.data:
    #         str(i[0])
    #         self.lista_idalumnos.append(i[0])
    #     self.cmbx_Id_Alumno['values'] = self.lista_idalumnos
    
    # def get_data_cursos(self):
    #     self.cursor.execute("SELECT * FROM Cursos")
    #     self.data = self.cursor.fetchall()
    #     self.lista_cursos = []
    #     for i in self.data:
    #         self.lista_cursos.append(f'{str(i[0])}-{str(i[1])}')
    #     self.descripc_Curso['values'] = self.lista_cursos
    # def get_data_complete(self):
    #     self.cursor.execute("SELECT * FROM Alumnos")
    #     self.data = self.cursor.fetchall()
    #     self.lista_alumnos = []
    #     for i in self.data:
    #         self.lista_alumnos.append(i)
        
    def close_sqlite(self):
        self.conn.commit()
        self.conn.close()
        if system() == "Windows":
            run("cls", shell=True)
        elif system() == "Linux" or system() == "Darwin":
            run("clear", shell=True) 
        print('Conexión cerrada')

if __name__ == "__main__":
    app = Inscripciones_2()
    app.run_sqlite()
    # app.get_data_idalumno()
    # app.get_data_complete()
    # app.get_data_cursos()
    app.run()
    app.close_sqlite()