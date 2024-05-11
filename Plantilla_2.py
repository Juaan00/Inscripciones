# !/usr/bin/python3
# -*- coding: utf-8 -*-
import tkinter as tk
import tkinter.ttk as ttk
import sqlite3
#from tkcalendar import DateEntry
from tkinter import StringVar, messagebox
import datetime
import calendar
from pathlib import Path
from subprocess import run
from platform import system
import signal

if system() == "Windows":
    from ctypes import windll

PATH = str((Path(__file__).resolve()).parent)
ICONO = r"/img/LogoinscripcionesIco.png"
ICONO_CONSULTA = r"/img/busqueda.png"
ICONO_EDITAR = r"/img/editar.png"
ICONO_ELIMINAR = r"/img/eliminar.png"
ICONO_CANCELAR = r"/img/escoba.png"
ICONO_GUARDAR = r"/img/disco.png"
DB = r"db/Inscripciones.db"

class Inscripciones_2:    
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
            
        self.tvNoInscripcion = tk.StringVar()
        self.tvNombres = tk.StringVar()
        self.tvApellidos = tk.StringVar()
        self.tvFechaInscripcion = tk.StringVar()
        self.tvCodigoCurso = tk.StringVar()

        # Crea los frames
        self.frm_1 = tk.Frame(self.win, name="frm_1")
        self.frm_1.configure(background="#f7f9fd", height=600, width=800)

        def habilitar_caracteres_entry(entrada, caracter):

            def verificarNumeros(char):        
                return char.isdigit()
            
            def verificarLetras(char):        
                return char.isalpha()
            
            def convertir_mayusculas(*args):
                contenido = entrada.get()
                entrada.delete(0, tk.END)
                entrada.insert(0, contenido.upper())

            if caracter == 'N':
                entrada.validate_cmd = self.frm_1.register(verificarNumeros)
                entrada.config(validate="key", validatecommand=(entrada.validate_cmd,"%S"))
            elif caracter == 'L':
                entrada.config(validate="key", validatecommand=(entrada.register(verificarLetras), "%S"))
                entrada.bind('<KeyRelease>', convertir_mayusculas)

        #Label id_Alumno
        self.lblIdAlumno = ttk.Label(self.frm_1, name="lblidalumno")
        self.lblIdAlumno.configure(background="#f7f9fd",font="{Arial} 8 {bold}", justify="left",
                                state="normal", takefocus=False,text='Id Alumno')
        self.lblIdAlumno.place(anchor="nw", x=20, y=20)
        #Combobox id_Alumno
        self.cmbx_Id_Alumno = ttk.Combobox(self.frm_1, name="cmbx_id_alumno",state=tk.DISABLED)
        self.cmbx_Id_Alumno.place(anchor="nw", width=110, x=20, y=40)
        
        #Label Nombres
        self.lblNombres = ttk.Label(self.frm_1, name="lblnombres")
        self.lblNombres.configure(background="#f7f9fd",font="{Arial} 8 {bold}", justify="left",
                                state="normal", takefocus=False,text='Nombre(s)')
        self.lblNombres.place(anchor="nw", x=150, y=20)
        #Entry Nombres
        self.nombres = ttk.Entry(self.frm_1, name="nombres",state=tk.DISABLED)
        self.nombres.place(anchor="nw", width=190, x=150, y=40)
        habilitar_caracteres_entry(self.nombres, 'L')

        #Label Apellidos
        self.lblApellidos = ttk.Label(self.frm_1, name="lblapellidos")
        self.lblApellidos.configure(background="#f7f9fd",font="{Arial} 8 {bold}", justify="left",
                                state="normal", takefocus=False,text='Apellido(s)')
        self.lblApellidos.place(anchor="nw", x=360, y=20)
        #Entry Apellidos
        self.apellidos = ttk.Entry(self.frm_1, name="apellidos",state=tk.DISABLED)
        self.apellidos.place(anchor="nw", width=190, x=360, y=40)
        self.apellidos.insert(0,"")
        
        #Label Fecha
        self.lblFecha = ttk.Label(self.frm_1, name="lblfecha")
        self.lblFecha.configure(background="#f7f9fd",font="{Arial} 8 {bold}", justify="left",
                                state="normal", takefocus=False,text='Fecha Ingreso')
        self.lblFecha.place(anchor="nw", x=570, y=20)

        self.fecha = tk.Entry(self.frm_1, name="fechas",state=tk.DISABLED)
        self.fecha.configure(justify="right")
        self.fecha.place(anchor="nw", width=90, x=570, y=40)
            
        self.act_date = False

        def cuandoEscriba(event):
            #coloca los / al escribir
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
            #Evita el exceso de numeros
            fechaRef = self.fecha.get()
            try:
                if len(fechaRef) > 10:
                    raise ValueError("digite maximo 8 numeros")
            except ValueError as problem:
                messagebox.showerror("Error", str(problem))
                self.fecha.delete(10, tk.END)

        def verificarNumeros(char):
            #permite borrar los /
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
        self.fecha.bind("<FocusOut>", validarFecha)#no borrar

        ############################################################
        self.fecha.bind("<Key>", cuandoEscriba)
        self.fecha.validate_cmd = self.frm_1.register(verificarNumeros)
        self.fecha.config(validate="key", validatecommand=(self.fecha.validate_cmd,"%S"))
        self.fecha.bind("<KeyRelease>", limite)
        
        #Label No. Inscripción
        self.lblNoInscripcion = ttk.Label(self.frm_1, name="lblnoinscripcion")
        self.lblNoInscripcion.configure(background="#f7f9fd",font="{Arial} 8 {bold}", justify="left",
                                        state="normal",text='No.Inscripción')
        self.lblNoInscripcion.place(anchor="nw", x=680, y=20)
        #Conmbox No. Inscripción
        self.noInscripcion = ttk.Combobox(self.frm_1, name="noInscripcion",state=tk.DISABLED)
        self.noInscripcion.place(anchor="nw", width=100, x=680, y=40)
        
        #Label Direccion
        self.lblDireccion = ttk.Label(self.frm_1, name="lbldireccion")
        self.lblDireccion.configure(background="#f7f9fd",font="{Arial} 8 {bold}", justify="left",
                                state="normal", takefocus=False,text='Dirección')
        self.lblDireccion.place(anchor="nw", x=20, y=80)
        #Entry Direccion
        self.direccion = ttk.Entry(self.frm_1, name="direccion",state=tk.DISABLED)
        self.direccion.place(anchor="nw", width=200, x=20, y=100)

        #Label Ciudad
        self.lblCiudad = ttk.Label(self.frm_1, name="lblciudad")
        self.lblCiudad.configure(background="#f7f9fd",font="{Arial} 8 {bold}", justify="left",
                                state="normal", takefocus=False,text='Ciudad')
        self.lblCiudad.place(anchor="nw", x=240, y=80)
        #Entry Ciudad
        self.ciudad = ttk.Entry(self.frm_1, name="ciudad",state=tk.DISABLED)
        self.ciudad.place(anchor="nw", width=130, x=240, y=100)
        
        #Label Departamento
        self.lblDepartamento = ttk.Label(self.frm_1, name="lbldepartamento")
        self.lblDepartamento.configure(background="#f7f9fd",font="{Arial} 8 {bold}", justify="left",
                        state="normal", takefocus=False,text='Departamento')
        self.lblDepartamento.place(anchor="nw", x=390, y=80)
        #Entry Departamento
        self.departamento = ttk.Entry(self.frm_1, name="departamento",state=tk.DISABLED)
        self.departamento.place(anchor="nw", width=130, x=390, y=100)
        

        #Label Telefono Celular
        self.lblTelCel = ttk.Label(self.frm_1, name="lbltelcel")
        self.lblTelCel.configure(background="#f7f9fd",font="{Arial} 8 {bold}", justify="left",
                        state="normal", takefocus=False,text='Teléfono Celular')
        self.lblTelCel.place(anchor="nw", x=540, y=80)
        
        #Entry Telefono Celular
        self.telCel = ttk.Entry(self.frm_1, name="telcel",state=tk.DISABLED)
        self.telCel.place(anchor="nw", width=110, x=540, y=100)
        habilitar_caracteres_entry(self.telCel, 'N')

        #Label Telefono Fijo
        self.lblTelFijo = ttk.Label(self.frm_1, name="lbltelfijo")
        self.lblTelFijo.configure(background="#f7f9fd",font="{Arial} 8 {bold}", justify="left",
                        state="normal", takefocus=False,text='Teléfono Fijo')
        self.lblTelFijo.place(anchor="nw", x=670, y=80)
        #Entry Telefono Fijo
        self.telFijo = ttk.Entry(self.frm_1, name="telfijo",state=tk.DISABLED)
        self.telFijo.place(anchor="nw", width=110, x=670, y=100)
    
        #Label id_carrera
        self.lblIdCarrera = ttk.Label(self.frm_1, name="lblidcarrera")
        self.lblIdCarrera.configure(background="#f7f9fd",font="{Arial} 8 {bold}", justify="left",
                                state="normal", takefocus=False,text='Id Carrera')
        self.lblIdCarrera.place(anchor="nw", x=20, y=140)
        #Combobox id_carrera
        self.cmbx_Id_Carrera = ttk.Entry(self.frm_1, name="cmbx_id_carrera",state=tk.DISABLED)
        self.cmbx_Id_Carrera.place(anchor="nw", width=60, x=20, y=160)

        #Label Codigo del Curso
        self.lblDscCurso = ttk.Label(self.frm_1, name="lbldsccurso")
        self.lblDscCurso.configure(background="#f7f9fd",font="{Arial} 8 {bold}", justify="left",
                        state="normal", takefocus=False,text='Código del Curso')
        self.lblDscCurso.place(anchor="nw", x=100, y=140)
        #Entry Codigo del Curso 
        self.codigo_Curso = ttk.Combobox(self.frm_1, name="descripc_curso",state=tk.DISABLED)
        self.codigo_Curso.configure(justify="left", width=166)
        self.codigo_Curso.place(anchor="nw", width=110, x=100, y=160)
        
        #Label Nombre de Curso
        self.lblNombreCurso = ttk.Label(self.frm_1, name="lblnombrecurso")
        self.lblNombreCurso.configure(background="#f7f9fd",font="{Arial} 8 {bold}", justify="left",
                        state="normal", takefocus=False,text='Nombre del Curso')
        self.lblNombreCurso.place(anchor="nw", x=230, y=140)
        #Entry Nombre de Curso
        self.nombreCurso = ttk.Entry(self.frm_1, name="nombrecurso",state=tk.DISABLED)
        self.nombreCurso.place(anchor="nw", width=240, x=230, y=160)
        
        #Label Horario
        self.lblHorario = ttk.Label(self.frm_1, name="lblhorario")
        self.lblHorario.configure(background="#f7f9fd",font="{Arial} 8 {bold}", justify="left",
                        state="normal", takefocus=False,text='Horario')
        self.lblHorario.place(anchor="nw", x=490, y=140)
        #Entry Horario
        self.horario = ttk.Entry(self.frm_1, name="horario",state=tk.DISABLED)
        self.horario.place(anchor="nw", width=180, x=490, y=160)
        
        #Fecha de Inscripción
        self.lblFechaInscripcion = ttk.Label(self.frm_1, name="lblfechainscripcion")
        self.lblFechaInscripcion.configure(background="#f7f9fd",font="{Arial} 8 {bold}", justify="left",
                        state="normal", takefocus=False,text='Fecha Inscripción')
        self.lblFechaInscripcion.place(anchor="nw", x=686, y=140)
        #Entry Fecha de Inscripción
        self.fechaInscripcion = ttk.Entry(self.frm_1, name="fechainscripcion",state=tk.DISABLED)
        self.fechaInscripcion.place(anchor="nw", width=90, x=690, y=160)
        

        ''' Botones  de la Aplicación'''
        
        #Botón Consultar
        self.icono_c = tk.PhotoImage(file= PATH + ICONO_CONSULTA)
        self.btnConsultar = tk.Button(self.frm_1, name="btnconsultar",
                                      command=lambda: self.consultar_ventana("Consultar Datos", "Seleccione una opción",3),
                                      cursor="hand2", image=self.icono_c,compound=tk.LEFT,bd=0, relief="flat", bg="#f7f9fd")
        self.btnConsultar.configure(text='  Consultar',font=('Arial', 9, 'bold'), width=90, height=30)
        self.btnConsultar.place(anchor="nw", x=100, y=235)
        
        
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
        self.icono_e = tk.PhotoImage(file= PATH + ICONO_EDITAR)
        self.btnEditar = tk.Button(self.frm_1, name="btneditar", cursor="hand2", image=self.icono_e, compound=tk.LEFT,bd=0)
        self.btnEditar.configure(text='  Editar',font=('Arial', 9, 'bold'), width=90, height=30, bg="#f7f9fd")
        self.btnEditar.place(anchor="nw", x=220, y=235)
        
        #Botón Eliminar
        self.icono_d = tk.PhotoImage(file= PATH + ICONO_ELIMINAR)
        self.btnEliminar = tk.Button(self.frm_1, name="btneliminar", cursor="hand2",command = self.ventana_eliminar,
                                     image=self.icono_d,compound=tk.LEFT)
        self.btnEliminar.configure(text='   Eliminar',font=('Arial', 9, 'bold'), width=90, height=30, bg = "#f7f9fd", bd =0)
        self.btnEliminar.place(anchor="nw", x=340, y=235)
        
        #Botón Cancelar
        self.icono_n = tk.PhotoImage(file= PATH + ICONO_CANCELAR)
        self.btnCancelar = tk.Button(self.frm_1, name="btncancelar", cursor="hand2", command=self.limpiar,
                                     image=self.icono_n,compound=tk.LEFT,bd=0, bg="#f7f9fd")
        self.btnCancelar.configure(text='  Cancelar',font=('Arial', 9, 'bold'), width=90, height=30 )
        self.btnCancelar.place(anchor="nw", x=460, y=235)
        # self.btnCancelar = ttk.Button(self.frm_1, name="btncancelar", cursor="hand2", command=self.limpiar)
        # self.btnCancelar.configure(text='Cancelar')
        # self.btnCancelar.place(anchor="nw", x=465, y=260, width=80)
        # self.btnCancelar.bind()
        
    
        #Botón Grabar
        self.icono_g = tk.PhotoImage(file= PATH + ICONO_GUARDAR)
        self.btnGrabar = tk.Button(self.frm_1, name="btngrabar", cursor="hand2",command= self.agregar_data,
                                   image=self.icono_g,compound=tk.LEFT, bd=0, bg="#f7f9fd")
        self.btnGrabar.configure(text='  Grabar',font=('Arial', 9, 'bold'), width=90, height=30)
        self.btnGrabar.place(anchor="nw", x=580, y=235)
        
        #Separador
        separator1 = ttk.Separator(self.frm_1)
        separator1.configure(orient="horizontal")
        separator1.place(anchor="nw", width=796, x=2, y=215)

        ''' Treeview de la Aplicación'''

        #Treeview
        self.argumentos = ('inicial', [''],[735])
        self.tree_view_prueba(*self.argumentos)

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

    def agregar_datos(self, NoInscritos, IdAlumno, FechaInscripcion, CodigoCurso):
        if not self.cursor:
            self.cursor = self.conn.cursor()
        query = '''INSERT INTO Inscritos (No_Inscritos, Id_Alumno, Fecha_de_Inscripción, Código_Curso) VALUES ('{}','{}','{}','{}')'''.format (NoInscritos, IdAlumno, FechaInscripcion, CodigoCurso)
        self.cursor.execute(query)
        self.conn.commit()
        self.cursor.close()

    def eliminar_datos(self, codigo):
        if not self.cursor:
            self.cursor = self.conn.cursor()
        query = '''DELETE FROM Inscritos WHERE Código_Curso = '{}' '''.format(codigo)
        self.cursor.execute(query)
        self.conn.commit()
        self.cursor.close()
    
    def actualiza_datos(self, NoInscritos, IdAlumno, FechaInscripcion, CodigoCurso):
        if not self.cursor:
            self.cursor = self.conn.cursor()
        query = ''' UPDATE Inscritos SET No_Inscritos = '{}', Id_Alumno = '{}', Fecha_de_Inscripción = '{}', Código_Curso = '{}'  '''.format (NoInscritos, IdAlumno, FechaInscripcion, CodigoCurso)
        self.cursor.execute(query)
        dato = self.cursor.rowcount
        self.conn.commit()
        self.cursor.close()
        return dato

    def combx_id_alumno(self):
        self.cmbx_Id_Alumno.config(state="normal")
        self.cursor.execute(f" SELECT Id_Alumno FROM Alumnos")
        self.dato_id = self.cursor.fetchall()
        self.cmbx_Id_Alumno['values'] = self.dato_id
        self.cmbx_Id_Alumno.config(state="readonly")

    def combx_no_incripcion(self):
        self.noInscripcion.config(state="normal")
        self.cursor.execute(f" SELECT No_Inscritos FROM Inscritos")
        self.dato_no_inscripcion = self.cursor.fetchall()
        self.noInscripcion['values'] = self.dato_no_inscripcion
        self.noInscripcion.config(state="readonly")
        
    def combx_codigo_curso(self):
        self.codigo_Curso.config(state="normal")
        self.cursor.execute(f" SELECT Código_Curso FROM Cursos")
        self.dato_codigo_curso = self.cursor.fetchall()
        self.codigo_Curso['values'] = self.dato_codigo_curso
        self.codigo_Curso.config(state="readonly")
        
    def fecha_split(self,fecha):
        self.split = fecha.split("-")
        self.fecha_n = f"{self.split[2]}/{self.split[1]}/{self.split[0]}"
        return self.fecha_n
    
    def fecha_split_al_reves(self,fecha):
        self.split = fecha.split("/")
        self.fecha_n = f"{self.split[2]}-{self.split[1]}-{self.split[0]}"
        return self.fecha_n
    
    def limpiar(self):
        self.entry = [self.noInscripcion, self.cmbx_Id_Alumno, self.fecha, self.fechaInscripcion, 
                        self.cmbx_Id_Carrera, self.nombres, self.apellidos, self.direccion, self.ciudad, 
                        self.departamento, self.telCel, self.telFijo, self.codigo_Curso, self.nombreCurso, 
                        self.horario]
        for i in self.entry:
            i.config(state="normal")
            i.delete(0, tk.END)
        
        # self.tView.delete(*self.tView.get_children())
        self.tViews.delete(*self.tViews.get_children())
        
        self.argumentos = ('inicial', [''],[735])
        self.tree_view_prueba(*self.argumentos)
    
    def abrir_ventana(self):
        self.botones = [ self.btnEliminar, self.btnCancelar, self.btnGrabar, self.btnConsultar, self.btnEditar]
        for i in self.botones:
            i.config(state=tk.DISABLED)
        
    def cerrar_ventana(self):
        self.botones = [self.btnEliminar, self.btnCancelar, self.btnGrabar, self.btnConsultar, self.btnEditar]  
        for i in self.botones:
            i.config(state=tk.NORMAL)
        self.ventana_emergente.destroy()
    
    def consultar_ventana(self, *args):
        self.abrir_ventana()
        self.ventana_emergente = tk.Toplevel(self.win)
        self.ventana_emergente.title(args[0])
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
        self.lblOpciones.configure(background="#f7f9fd",font="{Arial} 8 {bold}", justify="left",
                                state="normal", takefocus=False,text=args[1])
        self.lblOpciones.place(anchor="nw", x=20, y=20)
        
        for i in range(args[2]):
            int = tk.IntVar()
            
        # self.int = tk.IntVar()
        # self.int1 = tk.IntVar()
        # self.int2 = tk.IntVar()
            
        
        self.checkNoInscripcion = ttk.Checkbutton(self.frm_consulta, name="checkNoInscripcion", variable=int[0], onvalue=1, offvalue=0)
        self.checkNoInscripcion.configure(text="No. Inscripción")
        self.checkNoInscripcion.place(anchor="nw", x=40, y=50)
        
        self.checkIdAlumno = ttk.Checkbutton(self.frm_consulta, name="checkIdAlumno")
        self.checkIdAlumno.configure(text="Id Alumno", variable=int[1], onvalue=1, offvalue=0)
        self.checkIdAlumno.place(anchor="nw", x=40, y=80)
        
        self.checkCursos = ttk.Checkbutton(self.frm_consulta, name="checkCursos")
        self.checkCursos.configure(text="Cursos", variable=int[2], onvalue=1, offvalue=0)
        self.checkCursos.place(anchor="nw", x=40, y=110)
        
        self.btnEscoger = ttk.Button(self.frm_consulta, name="btnEscoger", cursor="hand2", command=self.boton_escoger)
        self.btnEscoger.configure(text="Consultar Datos")
        self.btnEscoger.place(anchor="nw", x=153, y=140)
        
        
        self.ventana_emergente.protocol("WM_DELETE_WINDOW", self.cerrar_ventana)
        self.ventana_emergente.mainloop()
        
    def ventana_eliminar(self): # no modificar
        #crea la ventana
        ALTO = 100
        ANCHO = 240
        self.winEmerDelete = tk.Toplevel(self.win)
        self.winEmerDelete.grab_set()
        self.winEmerDelete.title("Borrar Datos")
        self.winEmerDelete.iconphoto(False, self.icon_consulta)
        self.winEmerDelete.resizable(False, False)
        self.winEmerDelete.geometry("{}x{}".format(ANCHO, ALTO))
        self.centrar(self.winEmerDelete, ANCHO, ALTO)
        self.winEmerDelete.geometry(f"+{self.x}+{self.y}")
        #crea el Frame
        self.frm_EmerDelete = tk.Frame(self.winEmerDelete, name="frm_borrar")
        self.frm_EmerDelete.configure(background= "#f7f9fd", height=200, width=400)
        self.frm_EmerDelete.pack(fill='both', expand=True)

        def respuesta():
            self.eliminar_data(self.var.get())
        
        self.var = tk.IntVar() #variable de respuesta

        #crea los option
        self.radio1 = tk.Radiobutton(self.frm_EmerDelete, text="Eliminar un curso", variable=self.var, value=1,background= "#f7f9fd" )
        self.radio1.place(anchor="nw", x=40, y=0)

        radioAll = tk.Radiobutton(self.frm_EmerDelete, text="Eliminar todos los cursos", variable=self.var, value=2, background= "#f7f9fd")
        radioAll.place(anchor="nw", x=40, y=30)
        #crea el boton
        botonVemerEliminiar = tk.Button(self.frm_EmerDelete, text="Seleccionar", command= respuesta)
        botonVemerEliminiar.place(anchor="nw", x=60, y=60)

    def boton_escoger(self):
        self.combx_id_alumno()
        self.combx_no_incripcion()
        self.combx_codigo_curso()
        if self.int.get() == 1 and self.int1.get() == 0 and self.int2.get() == 0:
            self.cerrar_ventana()
            return self.consultar_no_inscripción()
        elif self.int1.get() == 1 and self.int.get() == 0 and self.int2.get() == 0:
            self.cerrar_ventana()
            return self.consultar_id_alumno()
        elif self.int2.get() == 1 and self.int.get() == 0 and self.int1.get() == 0:
            self.cerrar_ventana()
            return self.consultar_cursos()
        else:
            messagebox.showwarning("Advertencia", "Debe seleccionar una opción")
            self.int.set(0)
            self.int1.set(0)
            self.int2.set(0)
            self.cerrar_ventana()
            
    def click(self,event):
        self.item = self.tViews.selection()[0]
        self.values = self.tViews.item(self.item, 'values')
        return self.consultar(self.values[0])
    
    def tree_view_prueba(self, *kargs):
        def restrictor(Event):
            # Reviso si una zona especifica alrededor del cursor toca el separador de columnas
            # Esta zona la obtuve con prueba y error.
            for x in range(-10, 10):
                for y in range(1):
                    #Si el separador de columnas está dentro de la zona, entonces doy por hecho que el usuario está intentando cambiar de tamaño la columna.
                    if(self.tViews.identify_region(Event.x+x, Event.y+y) == "separator"):
                        self.tViews.event_generate("<ButtonRelease-1>") # si esta en el rango, hace creer al equipo que solto el clic
                        break        
        self.tViews = ttk.Treeview(self.frm_1, name=kargs[0],show='headings')
        self.tViews.configure(selectmode="extended")
        self.tViews.place(anchor="nw", height=264, width=730, x=30, y=281)
        self.tViews.configure(columns=kargs[1])
        self.tViews.column("#0", width=0)
        self.a = 0
        for i in kargs[1]:
            self.tViews.column(kargs[1][self.a],anchor="w",stretch=False,width=kargs[2][self.a])
            self.a += 1
        #Cabeceras
        self.b = 0
        for i in kargs[1]:
            self.tViews.heading(kargs[1][self.b],anchor="w", text=kargs[1][self.b])
            self.b += 1
        #Scrollbars
        self.scroll_H = ttk.Scrollbar(self.frm_1, name="scroll_h")
        self.scroll_H.configure(orient="horizontal")
        self.scroll_H.place(anchor="nw", height=15, width=725, x=30, y=534)
        self.scroll_Y = ttk.Scrollbar(self.frm_1, name="scroll_y")
        self.scroll_Y.configure(orient="vertical")
        self.scroll_Y.place(anchor="nw", height=268, width=16, x=754, y=281)
        self.scroll_H.configure(command=self.tViews.xview)
        self.scroll_Y.configure(command=self.tViews.yview)
        self.tViews.configure(xscrollcommand=self.scroll_H.set, yscrollcommand=self.scroll_Y.set)
        self.frm_1.pack(side="top")
        self.frm_1.pack_propagate(0)
        # Hago que mi función sea llamada cada vez que el usuario hace clic y mueve el cursor.
        self.tViews.bind("<B1-Motion>", restrictor)
        self.tViews.bind("<<TreeviewSelect>>", self.obtener_fila)
    
    def consultar_no_inscripción(self):
        self.limpiar()
        if self.cursor:
            self.cursor = self.conn.cursor()
        self.argumentos = ('c_inscripción',['No. Inscripción', 'Nombres', 'Apellidos', 'Fecha_Inscripción', 'Código_Curso'],[100,110,290,224,224])
        self.tree_view_prueba(*self.argumentos)
        self.cursor.execute(''' SELECT Inscritos.No_Inscritos, Nombres, Apellidos, Inscritos.Fecha_de_Inscripción, Código_Curso FROM Inscritos
                            JOIN Alumnos ON Inscritos.Id_Alumno = Alumnos.Id_Alumno
                            ''')
        self.datos = self.cursor.fetchall()
        for i in self.datos:
            # self.fecha = self.fecha_split(i[3])
            self.tViews.insert("", tk.END, values=(i[0], i[1], i[2], i[3], i[4]))
        
        self.tViews.bind("<Double-1>", self.click)
        # print(self.tView_c_inscripcion.selection())
        
    def consultar_id_alumno(self):
        self.limpiar()
        self.argumentos = ('c_alumnos',['Id Alumno', 'Nombres', 'Apellidos', 'Id Carrera', 'Fecha de Ingreso', 'Dirección', 'Ciudad', 'Departamento', 'Telefono Celular', 'Telefono Fijo'],
                           [100,200,200,100,120,200,200,200,100,100])
        self.tree_view_prueba(*self.argumentos)
        
        self.cursor.execute(''' SELECT Id_alumno, Nombres, Apellidos, Id_Carrera, Fecha_Ingreso, Dirección, Ciudad, Departamento, Telef_Cel, Telef_Fijo FROM Alumnos''') 
        self.datos = self.cursor.fetchall()
        for i in self.datos:
            self.tViews.insert("", tk.END, values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9]))

    def consultar_cursos(self):
        self.limpiar()
        self.argumentos = ('tView_c_cursos',['Código_Curso','Descripción_Curso','Num_Horas'],[110,320,300])
        self.tree_view_prueba(*self.argumentos)
        
        self.cursor.execute(''' SELECT Código_Curso, Descripción_Curso, Num_Horas FROM Cursos''')
        self.datos = self.cursor.fetchall()
        for i in self.datos:
            self.tViews.insert("", tk.END, values=(i[0], i[1], i[2]))
   
    def consultar(self, event):
        self.cursor.execute(f''' SELECT Inscritos.Id_Alumno, Nombres, Apellidos, Fecha_Ingreso, No_Inscritos, Dirección, Ciudad, Departamento, 
                            Telef_Cel, Telef_Fijo, Id_Carrera, Inscritos.Código_Curso, Descripción_Curso, Num_Horas, Fecha_de_Inscripción  FROM Inscritos 
                    JOIN Alumnos ON Inscritos.Id_Alumno = Alumnos.Id_Alumno 
                    JOIN Cursos ON Inscritos.Código_Curso = Cursos.Código_Curso 
                    JOIN Carreras ON Alumnos.Id_Carrera = Carreras.Código_Carrera 
                    WHERE Inscritos.No_Inscritos = {event}''')
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
        
        self.argumentos = ('c_registros',['No Inscripción', 'Código Curso', 'Nombre del Curso', 'Horario'],[110,110,290,224]) 
        self.tree_view_prueba(*self.argumentos)

        self.cursor.execute(f'''SELECT * FROM Inscritos
                   JOIN Cursos ON Inscritos.Código_Curso = Cursos.Código_Curso
                   WHERE Inscritos.Id_Alumno = {self.lista[0]}
                   ''')
        datos_materias = self.cursor.fetchall()
        for i in datos_materias:
            self.lista_materia = []
            self.lista_materia += i
            self.tViews.insert("", tk.END, values=(self.lista_materia[0], self.lista_materia[4], self.lista_materia[5], self.lista_materia[6]))

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
        self.tvNoInscripcion.set('')
        self.tvCodigoCurso.set('')
        self.tvFechaInscripcion.set('')
        self.tvNombres.set('')
        self.tvApellidos.set('')

    def obtener_fila(self, event):
        item = self.tViews.focus()
        if not item:
            return
        self.data = self.tViews.item(item)
        self.tvNoInscripcion.set(self.data["values"][0])
        self.tvNombres.set(self.data['values'][1])
        self.tvApellidos.set(self.data['values'][2])
        self.tvFechaInscripcion.set(self.data["values"][3])
        self.tvCodigoCurso.set(self.data["values"][4])

        #observador de funcion
        print(str(self.tvNoInscripcion.get()))
        print(str(self.tvNombres.get()))
        print(str(self.tvApellidos.get()))
        print(str(self.tvFechaInscripcion.get()))
        print(str(self.tvCodigoCurso.get()))
    
    def eliminar_data (self,seleccion):
        self.limpiar_data()
        try:
            item = self.tViews.selection()
            if not item: raise TypeError
            print(seleccion)

            if seleccion == 1:
                self.winEmerDelete.destroy()
                alert = messagebox.askquestion('Eliminando datos', 'Desea eliminar este valor?')
                if alert == 'yes':            
                    self.tViews.delete(item)
                    self.eliminar_datos(self.data['values'][4])

            elif seleccion == 2:
                self.winEmerDelete.destroy()
                alert = messagebox.askquestion('Eliminando datos', 'Desea eliminar todos los cursos?')
                if alert == 'yes':            
                    self.tViews.delete(item)
                    self.eliminar_datos(self.data['values'][0])
            else: 
                raise Exception("No se escogio una opcion")

        except TypeError:
            messagebox.showerror("Error", str('Debe seleccionar primero un valor a eliminar en el cuadro de abajo'))
            pass
        except Exception:
            messagebox.showerror("Error", str('no se selecciono ninguna opcion'))
            pass

    def agregar_data(self):
        noInscripcion = self.noInscripcion
        nombre = self.nombres.get()
        apellido = self.apellidos.get()
        fechaInscripcion = self.fechaInscripcion.get()
        codigo = self.codigo_Curso.get()
        if not fechaInscripcion:
            fechaInscripcion = '{}-{}-{}'.format(datetime.date.year,datetime.date.month,
            datetime.date.day)
        datos = (noInscripcion, nombre, apellido, fechaInscripcion, codigo)

        if (noInscripcion and nombre and apellido and fechaInscripcion and codigo) != '':
            self.tViews.insert(values=datos)
            self.agregar_datos(self.noInscripcion.get(), self.cmbx_Id_Alumno.get(), fechaInscripcion, self.codigo_Curso.get())

        
    # def get_data_idalumno(self):
    #     self.cmbx_Id_Alumno = ttk.Combobox(self.frm_1, name="cmbx_id_alumno", state="normal")
    #     self.cursor.execute("SELECT Id_Alumno FROM Alumnos")
    #     self.data = self.cursor.fetchall()
    #     self.lista_idalumnos = []
    #     for i in self.data:
    #         str(i[0])
    #         self.lista_idalumnos.append(i[0])
    #     self.cmbx_Id_Alumno['values'] = self.lista_idalumnos
    #     self.cmbx_Id_Alumno.config(state="readonly")
    
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
    
    def agregar_estudiantes(self):
        self.entry_datos = [self.cmbx_Id_Alumno, self.cmbx_Id_Carrera, self.nombres, self.apellidos, self.fecha, self.direccion, 
                            self.telCel, self.telFijo, self.ciudad, self.departamento]
        self.datos_ingresados = []
        for i in self.entry_datos:
            if i == self.fecha:
                self.datos_ingresados.append(self.fecha_split_al_reves(i.get()))
            else:
                self.datos_ingresados.append(i.get())
        self.limpiar()
        self.cursor.execute('''INSERT INTO Alumnos (Id_Alumno, Id_Carrera, Nombres, Apellidos, Fecha_Ingreso, Dirección, Telef_Cel, Telef_Fijo, Ciudad, Departamento)   
                            VALUES (?,?,?,?,?,?,?,?,?,?)''', tuple(self.datos_ingresados))
        self.conn.commit()
        return messagebox.showinfo("Ingreso de Datos", "Datos ingresados correctamente")
        
    def close_sqlite(self):
        self.conn.commit()
        self.conn.close()
        if system() == "Windows":
            run("cls", shell=True)
        elif system() == "Linux" or system() == "Darwin":
            run("clear", shell=True) 
        print('Conexión SQL cerrada, programa finalizado')

if __name__ == "__main__":
    app = Inscripciones_2()
    app.run_sqlite()
    # handling_interrupt = False
    # app.get_data_idalumno()
    # app.get_data_complete()
    # app.get_data_cursos()
    signal.signal(signal.SIGINT, signal.SIG_IGN) # Ignorar la señal de interrupción versión mejorada
    app.run()
    app.close_sqlite()