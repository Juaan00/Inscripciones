# !/usr/bin/python3
# -*- coding: utf-8 -*-
import tkinter as tk
import tkinter.ttk as ttk
import sqlite3
#from tkcalendar import DateEntry
from tkinter import messagebox
import datetime
from ctypes import windll
from pathlib import Path
from subprocess import run

PATH = str((Path(__file__).resolve()).parent)
ICONO = r"/img/LogoinscripcionesIco.png"
ICONO_CONSULTA = r"/img/lupa.png"
DB = r"db/Inscripciones.db"


class Inscripciones_2:

        
    def __init__(self, master=None):
         # Ventana principal
        self.db_name = 'Inscripciones.db'    
        self.win = tk.Tk(master)
        self.is_fields_enabled = False

        def centrar(win, ancho, alto):
             self.altura_pantalla = win.winfo_screenheight()
             self.ancho_pantalla = win.winfo_screenwidth()

             self.x = (self.ancho_pantalla // 2) - (ancho // 2)
             self.y = (self.altura_pantalla // 2) - (alto // 2)

        self.win.configure(background="#f7f9fd", height=600, width=800)
        centrar(self.win, 800, 600)
        self.win.geometry(f"+{self.x-8}+{self.y-12}")
        self.win.resizable(False, False)
        # Título de la ventana
        self.win.title("Inscripciones de Materias y Cursos")
        # Icono de la ventana
        windll.shell32.SetCurrentProcessExplicitAppUserModelID('Inscripciones')
        self.win.iconbitmap(PATH + ICONO)
        icono = tk.PhotoImage(file= PATH + ICONO)
        self.win.wm_iconphoto(False, icono)

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
        # def cuandoEscriba(event): 
        #     if event.char.isdigit():
        #         texto = self.fecha.get()
        #         letras = 0 #verifica el numero de digitos
        #         for i in texto:
        #             letras +=1
        #         if len(self.fecha.get()) > 9: #es 9 ya que al ingresar algo nuevo, primero aplica y luego verifica
        #             self.fecha.delete(9, tk.END)

        #         if letras == 2:
        #             self.fecha.insert(2,"/")
        #         elif letras == 5:
        #             self.fecha.insert(5,"/")
        #     else:
        #         return "break"
            
        # self.act_date = False

        # def cuandoEscriba(event):
        #     #global act_date
        #     if event.char.isdigit() or event.char =='/':
        #         fechaRef = self.fecha.get()
        #         if len(fechaRef) == 2 or len(fechaRef) ==5:
        #             self.act_date = True

        #         if len(fechaRef) == 2:
        #             self.fecha.insert(2,"/")
                    
        #         if len(fechaRef) == 5:
        #             self.fecha.insert(5,"/")
        #     if event.char.isdigit() or event.char =='\x08' or event.char =='': # \x08 = Backspace, '' = Delete
        #         self.act_date=True

        # def limite(event):
        #     fechaRef = self.fecha.get()
        #     #print (fecha)
        #     try:
        #         if len(fechaRef) > 10:
        #             raise ValueError("digite maximo 8 numeros")
        #     except ValueError as problem:
        #         messagebox.showerror("Error", str(problem))
        #         self.fecha.delete(10, tk.END)

        # def verificarNumeros(char):
        #     #global act_date

        #     if self.act_date:
        #         self.act_date = False 
        #         return char.isdigit() or char == '/'
        #     else:
        #         if char == '/' and self.act_date:
        #             return char.isdigit() or char == '/'
        #         else:
        #             return char.isdigit()

        # def validarFecha(event):
        #     try:
        #         self.vFecha = self.fecha.get()
        #         #compara el formato del texto con el formato y las fechas de libreria
        #         self.vFecha = datetime.datetime.strptime(self.vFecha,'%d/%m/%Y') 
        #         print ('fecha valida')
        #     except ValueError:
        #         messagebox.showerror("Error", 'Digite un formato de fecha valida')
        #         #print ('Error: Digite una fecha valida')

        # #cuando oprima una tecla cualquiera, ejecuta
        # self.fecha.bind("<Key>", cuandoEscriba) 
        # ##############################################################
        # #evita que valide el borrar como digito
        # #self.fecha.bind("<BackSpace>", lambda _:self.fecha.delete(tk.END)) 

        # self.fecha.bind("<Return>", validarFecha)
        # self.fecha.bind("<Tab>", validarFecha)
        # #self.fecha.bind("<FocusOut>", validarFecha)#no borrar

        # ############################################################
        # self.fecha.bind("<Key>", cuandoEscriba)
        # self.fecha.validate_cmd = self.frm_1.register(verificarNumeros)
        # self.fecha.config(validate="key", validatecommand=(self.fecha.validate_cmd,"%S"))
        # self.fecha.bind("<KeyRelease>", limite)
        
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
        self.btnConsultar = ttk.Button(self.frm_1, name="btnconsultar",command=self.consultar, cursor="hand2")
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
        self.btnEliminar = ttk.Button(self.frm_1, name="btneliminar", cursor="hand2")
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
        def cancel(event):
            return "break"

        #Treeview
        self.tView = ttk.Treeview(self.frm_1, name="tview",show='headings')
        self.tView.configure(selectmode="extended")
        #Columnas del Treeview
        self.tView_cols = ['NoInscripción', 'Alumno', 'CódigoCurso','tV_descripción', 'Horario' ]
        self.tView.bind("<Button-1>", cancel, add="+")
        self.tView.configure(columns=self.tView_cols)
        self.tView.column("#0", width=0)
        self.tView.column("NoInscripción",anchor="w",stretch=False,width=60)
        self.tView.column("Alumno",anchor="w",stretch=False,width=180)
        self.tView.column("CódigoCurso",anchor="w",stretch=False,width=100)
        self.tView.column("tV_descripción",anchor="w",stretch=False,width=240)
        self.tView.column("Horario",anchor="w",stretch=False,width=144)
        #Cabeceras
        self.tView.heading("NoInscripción",anchor="w", text='No.Inscripción')
        self.tView.heading("Alumno",anchor="w", text='Alumno')
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
        
        def insert_data():
            valornombre=self.nombres.get()
            valorapellido=self.apellidos.get()
            nombre = valornombre+" "+valorapellido
            print(nombre)
            self.tView.insert("", "end", values=(nombre, "1", "2015734", "Programación de Computadores", "12"))

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
    
    def consultar(self):
        
        self.ventana_emergente = tk.Toplevel()
        self.ventana_emergente.title("Consulta de Datos")
        self.icon_consulta = tk.PhotoImage(file= PATH + ICONO_CONSULTA)
        self.ventana_emergente.iconphoto(False, self.icon_consulta)
                
        self.ventana_emergente.resizable(False, False)
        self.altura_pantalla_1 = self.win.winfo_screenheight()
        self.ancho_pantalla_1 = self.win.winfo_screenwidth()
        print(f"Alto: {self.altura_pantalla_1} Ancho: {self.ancho_pantalla_1}")
        self.ventana_emergente.geometry("400x300")
        # self.ventana_emergente.eval('tk::PlaceWindow . center')
        self.x_1 = (self.ancho_pantalla_1 / 2) - (400 / 2)
        self.y_1 = (self.altura_pantalla_1 / 2) - (300 / 2)
        print(f"X: {int(self.x_1)} Y: {int(self.y_1)}")
        self.ventana_emergente.geometry(f"400x300+{int(self.x_1)}+{int(self.y_1)-9}")
        self.frm_consulta = tk.Frame(self.win, name="frm_consulta")
        self.frm_consulta.configure(background="#f7f9fd", height=600, width=800)
        
        
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
                 
        self.tView_c1 = ttk.Treeview(self.frm_1, name="tview",show='headings')
        self.tView_c1.configure(selectmode="extended")
        self.tView_c1.place(anchor="nw", height=250, width=740, x=30, y=300)
        self.tView_cols_c1 = ['NoInscripción', 'CódigoCurso','tV_descripción', 'Horario' ]
        self.tView_c1.configure(columns=self.tView_cols_c1)
        self.tView_c1.column("#0", width=0)
        self.tView_c1.column("NoInscripción",anchor="w",stretch=False,width=100)
        self.tView_c1.column("CódigoCurso",anchor="w",stretch=False,width=110)
        self.tView_c1.column("tV_descripción",anchor="w",stretch=False,width=290)
        self.tView_c1.column("Horario",anchor="w",stretch=False,width=224)
        #Cabeceras
        self.tView_c1.heading("NoInscripción",anchor="w", text='No.Inscripción')
        self.tView_c1.heading("CódigoCurso",anchor="w", text='Código de Curso')
        self.tView_c1.heading("tV_descripción", anchor="w", text='Descripción')
        self.tView_c1.heading("Horario", anchor="w", text='Horario')
        self.tView_c1.place(anchor="nw", height=250, width=740, x=30, y=300)
        
        #Scrollbars
        self.scroll_H_c1 = ttk.Scrollbar(self.frm_1, name="scroll_h")
        self.scroll_H_c1.configure(orient="horizontal")
        self.scroll_H_c1.place(anchor="nw", height=15, width=724, x=31, y=534)
        self.scroll_Y_c1 = ttk.Scrollbar(self.frm_1, name="scroll_y")
        self.scroll_Y_c1.configure(orient="vertical")
        self.scroll_Y_c1.place(anchor="nw", height=248, width=16, x=753, y=301)
        self.frm_1.pack(side="top")
        self.frm_1.pack_propagate(0)

        self.cursor.execute(f'''SELECT * FROM Inscritos
                   JOIN Cursos ON Inscritos.Código_Curso = Cursos.Código_Curso
                   WHERE Inscritos.Id_Alumno = {self.lista[0]}
                   ''')
        datos_materias = self.cursor.fetchall()
        for i in datos_materias:
            self.lista_materia = []
            self.lista_materia += i
            self.tView_c1.insert("", tk.END, values=(self.lista_materia[0], self.lista_materia[4], self.lista_materia[5], self.lista_materia[6]))
        
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
        run("cls", shell=True)
        # run("clear", shell=True) opcion mac
        print('Conexión cerrada')

if __name__ == "__main__":
    app = Inscripciones_2()
    app.run_sqlite()
    # app.get_data_idalumno()
    # app.get_data_complete()
    # app.get_data_cursos()
    app.run()
    app.close_sqlite()