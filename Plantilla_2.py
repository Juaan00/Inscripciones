# !/usr/bin/python3
# -*- coding: utf-8 -*-
import tkinter as tk
import tkinter.ttk as ttk
import sqlite3
import datetime
from pathlib import Path
from subprocess import run
from platform import system
from signal import signal, SIGINT, SIG_IGN
import re
from functools import partial
from operator import itemgetter
from tkinter import messagebox

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
            
        self.tvEntry0= tk.StringVar()
        self.tvEntry1= tk.StringVar()
        self.tvEntry2= tk.StringVar()
        self.tvEntry3= tk.StringVar()
        self.tvEntry4= tk.StringVar()
        # self.tvNoInscripcion = tk.StringVar()
        # self.tvNombreCurso = tk.StringVar()
        # self.tvHorarios = tk.StringVar()
        # self.tvFechaInscripcion = tk.StringVar()
        # self.tvCodigoCurso = tk.StringVar()

        # Crea los frames
        self.frm_1 = tk.Frame(self.win, name="frm_1")
        self.frm_1.configure(background="#f7f9fd", height=600, width=800)

        #Label id_Alumno
        self.lblIdAlumno = ttk.Label(self.frm_1, name="lblidalumno")
        self.lblIdAlumno.configure(background="#f7f9fd",font="{Arial} 8 {bold}", justify="left",
                                state="normal", takefocus=False,text='Id Alumno')
        self.lblIdAlumno.place(anchor="nw", x=20, y=20)
        #Combobox id_Alumno
        vcmd = (self.frm_1.register(self.onValidate),'%P' ,'%S')
        self.cmbx_Id_Alumno = ttk.Combobox(self.frm_1, name="cmbx_id_alumno",postcommand=self.combx_id_alumno, state="readonly"
                                           )
        self.cmbx_Id_Alumno.place(anchor="nw", width=110, x=20, y=40)
        self.cmbx_Id_Alumno.bind("<<ComboboxSelected>>", lambda _: self.consultar_estudiantes_cmbx(self.cmbx_Id_Alumno.get()))
        
        #Label Nombres
        self.lblNombres = ttk.Label(self.frm_1, name="lblnombres")
        self.lblNombres.configure(background="#f7f9fd",font="{Arial} 8 {bold}", justify="left",
                                state="normal", takefocus=False,text='Nombre(s)')
        self.lblNombres.place(anchor="nw", x=150, y=20)
        #Entry Nombres
        self.nombres = ttk.Entry(self.frm_1, name="nombres",state=tk.DISABLED)
        self.nombres.place(anchor="nw", width=190, x=150, y=40)


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

        self.fecha = ttk.Entry(self.frm_1, name="fechas",state=tk.DISABLED, validate="key", validatecommand=(self.frm_1.register(self.onValidate), '%P', '%S'))
        self.fecha.configure(justify="right")
        self.fecha.place(anchor="nw", width=90, x=570, y=40)
        self.act_date = False
        self.fecha.bind("<Key>", lambda event, entry=self.fecha: self.cuandoEscriba(event, entry))
        self.fecha.bind("<FocusOut>", lambda event, entry=self.fecha: self.validarFecha(entry))
        self.fecha.bind("<Return>", lambda event, entry=self.fecha: self.validarFecha(entry))   
        
        #Label No. Inscripción
        self.lblNoInscripcion = ttk.Label(self.frm_1, name="lblnoinscripcion")
        self.lblNoInscripcion.configure(background="#f7f9fd",font="{Arial} 8 {bold}", justify="left",
                                        state="normal",text='No.Inscripción')
        self.lblNoInscripcion.place(anchor="nw", x=680, y=20)
        #Conmbox No. Inscripción
        vcdm = (self.frm_1.register(self.onValidate),'%P' ,'%S')
        self.noInscripcion = ttk.Combobox(self.frm_1, name="noInscripcion",state="readonly", postcommand=self.combx_no_incripcion,
                                          validate="key", validatecommand=vcmd)
        self.noInscripcion.place(anchor="nw", width=100, x=680, y=40)
        self.noInscripcion.place(anchor="nw", width=100, x=680, y=40)
        self.noInscripcion.bind("<<ComboboxSelected>>", lambda _: self.consultar(self.noInscripcion.get()))
        self.noInscripcion.bind("<Return>", self.enter)  
        self.noInscripcion.bind("<FocusIn>", self.noInscripcion.config(state="normal"))   
        
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
        # self.habilitar_caracteres_entry(self.telCel, 'N')

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
        self.codigo_Curso = ttk.Combobox(self.frm_1, name="descripc_curso",state="readonly", postcommand=self.combx_codigo_curso)
        self.codigo_Curso.configure(justify="left", width=166)
        self.codigo_Curso.place(anchor="nw", width=110, x=100, y=160)
        self.codigo_Curso.bind("<<ComboboxSelected>>", lambda _: self.consultar_cursos_cmbx(self.codigo_Curso.get()))
        self.codigo_Curso.bind("<<ComboboxSelected>>", self.cmbx_codigo_curso)
        
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
        self.horario = ttk.Combobox(self.frm_1, name="horario",state=tk.DISABLED)
        self.horario.place(anchor="nw", width=180, x=490, y=160)
        self.horario.config(values=["Lun, Mier 7:00am - 9:00am", "Lun, Mier 9:00am - 11:00am", "Lun, Mier 11:00am - 1:00pm", "Lun, Mier 2:00pm - 4:00pm", "Lun, Mier 4:00pm - 6:00pm", 
                                    "Mar, Jue 7:00am - 9:00am", "Mar, Jue 9:00am - 11:00am", "Mar, Jue 11:00am - 1:00pm", "Mar, Jue 2:00pm - 4:00pm", "Mar, Jue 4:00pm - 6:00pm",
                                    "Mier, Vier 7:00am - 9:00am", "Mier, Vier 9:00am - 11:00am", "Mier, Vier 11:00am - 1:00pm", "Mier, Vier 2:00pm - 4:00pm", "Mier, Vier 4:00pm - 6:00pm",])
        
        #Fecha de Inscripción
        self.lblFechaInscripcion = ttk.Label(self.frm_1, name="lblfechainscripcion")
        self.lblFechaInscripcion.configure(background="#f7f9fd",font="{Arial} 8 {bold}", justify="left",
                        state="normal", takefocus=False,text='Fecha Inscripción')
        self.lblFechaInscripcion.place(anchor="nw", x=686, y=140)
        #Entry Fecha de Inscripción
        self.fechaInscripcion = ttk.Entry(self.frm_1, name="fechainscripcion",state=tk.DISABLED,
                                          validate="key", validatecommand=(self.frm_1.register(self.onValidate), '%P', '%S'))
        self.fechaInscripcion.place(anchor="nw", width=90, x=690, y=160)
        self.fechaInscripcion.bind("<FocusOut>", lambda event, entry=self.fechaInscripcion: self.validarFecha(entry))
        self.fechaInscripcion.bind("<Key>", lambda event, entry=self.fechaInscripcion: self.cuandoEscriba(event, entry))
        self.fechaInscripcion.bind("<Return>", lambda event, entry=self.fechaInscripcion: self.validarFecha(entry))


        ''' Botones  de la Aplicación'''
        
        #Botón Consultar
        self.icono_c = tk.PhotoImage(file= PATH + ICONO_CONSULTA)
        self.btnConsultar = tk.Button(self.frm_1, name="btnconsultar",
                                      command=lambda: self.consultar_ventana("Consultar Datos", "Seleccione una opción", ["No. Inscripción", "Id Alumno", "Cursos","Carrera"], "Consultar",self.boton_escoger_consulta),
                                      cursor="hand2", image=self.icono_c,compound=tk.LEFT,bd=0, relief="flat", bg="#f7f9fd")
        self.btnConsultar.configure(text='  Consultar',font=('Arial', 9, 'bold'), width=90, height=30)
        self.btnConsultar.place(anchor="nw", x=100, y=235)

        
        self.icono_e = tk.PhotoImage(file= PATH + ICONO_EDITAR)
        self.btnEditar = tk.Button(self.frm_1, name="btneditar", cursor="hand2", image=self.icono_e, compound=tk.LEFT,bd=0, command=self.editar)
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
        self.btnGrabar = tk.Button(self.frm_1, name="btngrabar", cursor="hand2",
                                   command= self.grabar,
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

        # Main widget
        self.mainwindow = self.win

    def run(self):
        self.mainwindow.mainloop()


    ''' A partir de este punto se deben incluir las funciones
     para el manejo de la base de datos '''

    def cmbx_codigo_curso(self,event):

        selected_item = self.codigo_Curso.get()

        print(selected_item)
        data=self.get_data_curso(selected_item)
        for i in data:
            print(i)
            self.add_consultar(self.nombreCurso, i[1])
            self.nombreCurso.config(state="readonly")
            self.horario.config(state="readonly")
            self.add_consultar(self.fechaInscripcion, datetime.date.today().strftime("%d/%m/%Y"))
            self.fechaInscripcion.config(state="enabled")

    def editar(self):
        string=''
        no_inscripcion=self.noInscripcion.get()
        id_alumno=self.cmbx_Id_Alumno.get()
        if self.noInscripcion.get() == '':
                pass
        else:
            string+=f'No. Inscripción {no_inscripcion}, '
            numero_inscripcion=''
            nuevo_curso=self.codigo_Curso.get()
            self.lista_inscripciones=self.get_data_inscricpiones_complete(id_alumno)
            for i in self.lista_inscripciones: 
                if i[0] == numero_inscripcion:
                    self.cursor.execute("UPDATE Inscritos SET Código_Curso = ? WHERE No_Registro = ?", (nuevo_curso, numero_inscripcion))
                    self.conn.commit()
        string= string.rstrip(', ')
        messagebox.showinfo(f"Edición Exitosa, estudiante {id_alumno}", f"Se realizaron cambios en:\n{string}")
        self.limpiar()
        return
     
    def centrar(self, win, ancho, alto):
        self.altura_pantalla = win.winfo_screenheight()
        self.ancho_pantalla = win.winfo_screenwidth()

        self.x = (self.ancho_pantalla // 2) - (ancho // 2)
        self.y = (self.altura_pantalla // 2) - (alto // 2)
     
    def get_data_inscricpiones_complete(self, id_alumno):
        self.cursor.execute("SELECT * FROM Inscritos WHERE Id_Alumno = ?", (id_alumno,))
        self.data = self.cursor.fetchall()
        self.lista_inscripciones = []
        for i in self.data:
            self.lista_inscripciones.append(i)
        return self.lista_inscripciones
     
     
    def cuandoEscriba(self,event, entry):
        #coloca los / al escribir
        if event.char.isdigit() or event.char =='/':
            fechaRef = entry.get()
            if len(fechaRef) == 2 or len(fechaRef) ==5:
                self.act_date = True

            if len(fechaRef) == 2:
                entry.insert(2,"/")
                
            if len(fechaRef) == 5:
                entry.insert(5,"/")
        if event.char.isdigit() or event.char =='\x08' or event.char =='': # \x08 = Backspace, '' = Delete
            self.act_date=True

    def limite(self,event):
        #Evita el exceso de numeros
        fechaRef = self.fecha.get()
        try:
            if len(fechaRef) > 10:
                raise ValueError("digite maximo 8 numeros")
        except ValueError as problem:
            messagebox.showerror("Error", str(problem))
            self.fecha.delete(10, tk.END)

    def verificarNumeros(self,char):
        #permite borrar los /
        if self.act_date:
            self.act_date = False 
            return char.isdigit() or char == '/'
        else:
            if char == '/' and self.act_date:
                return char.isdigit() or char == '/'
            else:
                return char.isdigit()

    def validarFecha(self,entry):
        try:
            self.vFecha = entry.get()
            #compara el formato del texto con el formato y las fechas de libreria
            self.vFecha = datetime.datetime.strptime(self.vFecha,'%d/%m/%Y') 
        except ValueError:
            messagebox.showerror("Error", 'Digite un formato de fecha valida')
            self.fecha_insert = datetime.datetime.now().strftime('%d/%m/%Y')
            entry.delete(0, tk.END)
            entry.insert(0,self.fecha_insert)    

    def habilitar_caracteres_entry(self,entrada, caracter):

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
    
    def onValidate(self,P, S):
        self.numeros = re.compile('^[0-9]*$')
        self.largo = re.compile("^[0-9]{0,10}$")
        self.largo_fecha = re.compile("^[0-9/]{0,10}$")
        if re.match(self.numeros, S) and re.match(self.largo, P):
            return True
        elif re.match(self.largo_fecha, P) and re.match(self.largo_fecha, S):
            return True
        else:
            self.frm_1.bell()
            return False
    
    def run_sqlite(self):
        self.conn = sqlite3.connect(DB)
        self.conn.execute("PRAGMA foreign_keys = 1")
        self.cursor = self.conn.cursor()

    def agregar_datos(self, NoInscritos, IdAlumno, FechaInscripcion, CodigoCurso):
        if not self.cursor:
            self.cursor = self.conn.cursor()
        query = '''INSERT INTO Inscritos (No_Inscripción, Id_Alumno, Fecha_de_Inscripción, Código_Curso) VALUES ('{}','{}','{}','{}')'''.format (NoInscritos, IdAlumno, FechaInscripcion, CodigoCurso)
        self.cursor.execute(query)
        self.conn.commit()
        # self.cursor.close()

    def eliminar_datos(self, codigo, pront):
        if not self.cursor:
            self.cursor = self.conn.cursor()
        query = f"DELETE FROM Inscritos WHERE {pront} = '{codigo}' " #es más fácil este en terminos de sintaxis pero dejo el otro igual comentado
        # query = '''DELETE FROM Inscritos WHERE ''' + pront + ''' = '{}' '''.format(codigo) 
        self.cursor.execute(query)
        self.conn.commit()
        # self.cursor.close()
    
    def actualiza_datos(self, NoInscritos, IdAlumno, FechaInscripcion, CodigoCurso):
        if not self.cursor:
            self.cursor = self.conn.cursor()
        query = ''' UPDATE Inscritos SET No_Inscripción = '{}', Id_Alumno = '{}', Fecha_de_Inscripción = '{}', Código_Curso = '{}'  '''.format (NoInscritos, IdAlumno, FechaInscripcion, CodigoCurso)
        self.cursor.execute(query)
        dato = self.cursor.rowcount
        self.conn.commit()
        # self.cursor.close()
        return dato

    def combx_id_alumno(self):
        self.cmbx_Id_Alumno.config(state="normal")
        self.cursor.execute(f" SELECT Id_Alumno FROM Alumnos")
        self.dato_id = self.cursor.fetchall()
        self.cmbx_Id_Alumno['values'] = self.dato_id
        self.cmbx_Id_Alumno.config(state="readonly")

    def combx_no_incripcion(self):
        self.noInscripcion.config(state="normal")
        self.cursor.execute(f" SELECT DISTINCT No_Inscripción FROM Inscritos ORDER BY No_Inscripción")
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
        
        self.boton = [self.btnCancelar, self.btnConsultar, self.btnEditar, self.btnEliminar]
        for i in self.boton:
            i.config(state='normal')
        
        self.guardado = False

        self.tViews.delete(*self.tViews.get_children())
        
        self.argumentos = ('inicial', [''],[735])
        self.tree_view_prueba(*self.argumentos)
    
    
    def consultar_ventana(self, *args): #ventana emergente, permite máximo 4 opciones para escoger, los parametros son: Titulo, Texto, Opciones, Botón y Función de botón
        self.limpiar()
        self.ventana_emergente = tk.Toplevel(self.win)
        self.ventana_emergente.title(args[0])
        self.icon_consulta = tk.PhotoImage(file= PATH + ICONO)
        self.ventana_emergente.iconphoto(False, self.icon_consulta)
         
        self.ventana_emergente.resizable(False, False)
        self.centrar(self.ventana_emergente, 400, 110 + 30*len(args[2]))
        self.ventana_emergente.geometry(f"400x{110 + 30*len(args[2])}+{self.x}+{self.y}")
        self.ventana_emergente.grab_set()
        self.frm_consulta = tk.Frame(self.ventana_emergente, name=f"frm_{args[0]}")
        self.frm_consulta.configure(background= "#f7f9fd", height=200, width=400)
        self.frm_consulta.pack(fill='both', expand=True)
        
        self.lblOpciones = ttk.Label(self.frm_consulta, name="lblOpciones")
        self.lblOpciones.configure(background="#f7f9fd",font="{Arial} 8 {bold}", justify="left",
                                state="normal", takefocus=False,text=args[1])
        self.lblOpciones.place(anchor="nw", x=20, y=20)
        
        self.int = tk.IntVar()
        self.int.set(0)
        
        self.c = 1
        for i in range(len(args[2])):
            self.check = ttk.Radiobutton(self.frm_consulta, name=f"check{i}", variable=self.int, value=self.c)
            self.check.configure(text=args[2][i])
            self.check.place(anchor="nw", x=40, y=50 + 30*i)
            self.c += 1
    
        self.btnEscoger = ttk.Button(self.frm_consulta, name="btnEscoger", cursor="hand2", command=args[4])
        self.btnEscoger.configure(text=args[3])
        self.btnEscoger.place(anchor="nw", x=153, y=50 + 30*len(args[2]))
        
        self.ventana_emergente.mainloop()
        
    def ventana_eliminar(self): # no modificar
        #crea la ventana
        ALTO = 100
        ANCHO = 240
        self.winEmerDelete = tk.Toplevel(self.win)
        self.winEmerDelete.grab_set()
        self.winEmerDelete.title("Borrar Datos")
        self.winEmerDelete.iconphoto(False, self.icono_d)
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
        self.radio1 = tk.Radiobutton(self.frm_EmerDelete,name="checkpara1", text="Eliminar un curso", variable=self.var, value=1,background= "#f7f9fd" )
        self.radio1.place(anchor="nw", x=40, y=0)

        radioAll = tk.Radiobutton(self.frm_EmerDelete,name="checkparatodo", text="Eliminar todos los cursos", variable=self.var, value=2, background= "#f7f9fd")
        radioAll.place(anchor="nw", x=40, y=30)

        #crea el boton
        botonVemerEliminiar = tk.Button(self.frm_EmerDelete, text="Seleccionar", command= respuesta)
        botonVemerEliminiar.place(anchor="nw", x=60, y=60)

    def boton_escoger_consulta(self): # Función que se ejecuta al presionar el botón de la ventana emergente cuando se está consultando
        if self.int.get() == 1: 
            self.ventana_emergente.destroy()
            return self.consultar_no_inscripción()
        elif self.int.get() == 2:
            self.ventana_emergente.destroy()
            return self.consultar_id_alumno()
        elif self.int.get() == 3:
            self.ventana_emergente.destroy()
            return self.consultar_cursos()
        elif self.int.get() == 4:
            self.ventana_emergente.destroy()
            return self.consultar_carreras()
        else:
            messagebox.showwarning("Advertencia", "Debe seleccionar una opción")
            self.int.set(0)
            
    def click(self,event):
        try:
            self.item = self.tViews.selection()[0]
            self.values = self.tViews.item(self.item, 'values')
            print(self.values[0])
            return self.consultar(self.values[0])
        except IndexError:
            pass

    def enter(self,event):
        self.combx_no_incripcion()
        self.enter_accion = []
        for i in self.noInscripcion['values']:
            self.enter_accion.append(str(i[0]))
        if str(self.noInscripcion.get()) in self.enter_accion:
            self.consultar(self.noInscripcion.get())
        else:
            messagebox.showinfo("Consulta Inscripción","No se encontraron datos con ese número de inscripción")

    
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
            self.tViews.heading(kargs[1][self.b],anchor="w", text=kargs[1][self.b], command=lambda c=i: self.sort_by_column(c, False))
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

    def sort_by_column(self, column_name, reverse=False):
        column_index = self.tViews["columns"].index(column_name)
        sorted_items = sorted(
            ((self.tViews.item(item)["values"][column_index], item)
             for item in self.tViews.get_children()),
            key=itemgetter(0), reverse=reverse)

        for index, (_, item) in enumerate(sorted_items):
            self.tViews.move(item, '', index)

        self.tViews.heading(
            column_name,
            command=partial(
                self.sort_by_column, column_name, not reverse
                )
            )
    
    def consultar_no_inscripción(self):
        self.limpiar()
        if self.cursor:
            self.cursor = self.conn.cursor()
        self.argumentos = ('c_inscripción',['No. Inscripción', 'Nombres', 'Apellidos', 'Fecha_Inscripción', 'Código_Curso', 'Horario'],[100,180,180,140,140,210])
        self.tree_view_prueba(*self.argumentos)
        self.cursor.execute(''' SELECT Inscritos.No_Inscripción, Nombres, Apellidos, Inscritos.Fecha_de_Inscripción, Código_Curso, Horario_Curso FROM Inscritos
                            JOIN Alumnos ON Inscritos.Id_Alumno = Alumnos.Id_Alumno ORDER BY Inscritos.No_Inscripción
                            ''')
        self.datos = self.cursor.fetchall()
        for i in self.datos:
            self.f_inscripcion = self.fecha_split(i[3]) 
            self.tViews.insert("", tk.END, values=(i[0], i[1], i[2], self.f_inscripcion, i[4], i[5]))
        
        self.tViews.bind("<Double-1>", self.click)
        # print(self.tView_c_inscripcion.selection())
        
    def consultar_id_alumno(self):
        self.limpiar()
        self.argumentos = ('c_alumnos',['Id Alumno', 'Nombres', 'Apellidos', 'Id Carrera', 'Fecha de Ingreso', 'Dirección', 'Ciudad', 'Departamento', 'Telefono Celular', 'Telefono Fijo'],
                           [100,200,200,100,120,200,200,200,100,100])
        self.tree_view_prueba(*self.argumentos)
        
        self.cursor.execute(''' SELECT Id_alumno, Nombres, Apellidos, Id_Carrera, Fecha_Ingreso, Dirección, Ciudad, Departamento, Telef_Cel, Telef_Fijo FROM Alumnos
                            ORDER BY Id_Alumno''') 
        self.datos = self.cursor.fetchall()
        for i in self.datos:
            self.f_ingreso = self.fecha_split(i[4])
            self.tViews.insert("", tk.END, values=(i[0], i[1], i[2], i[3], self.f_ingreso, i[5], i[6], i[7], i[8], i[9]))
        self.tViews.bind("<Double-1>", self.click)

    def consultar_cursos(self):
        self.limpiar()
        self.argumentos = ('tView_c_cursos',['Código_Curso','Descripción_Curso','Num_Horas'],[110,270,110])
        self.tree_view_prueba(*self.argumentos)
        
        self.cursor.execute(''' SELECT Código_Curso, Descripción_Curso, Num_Horas FROM Cursos''')
        self.datos = self.cursor.fetchall()
        for i in self.datos:
            self.tViews.insert("", tk.END, values=(i[0], i[1], i[2]))
    
    def consultar_carreras(self): # Consulta los datos de la base de datos según el código de la carrera
        self.limpiar()
        self.argumentos = ('tView_c_carreras',['Código_Carrera','Descripción_Carrera', 'No Semestres'],[120,320,120])
        self.tree_view_prueba(*self.argumentos)
        
        self.cursor.execute(''' SELECT * FROM Carreras''')
        self.datos = self.cursor.fetchall()
        for i in self.datos:
            self.tViews.insert("", tk.END, values=(i[0], i[1], i[2]))
   
    def consultar(self, event):

        self.get_data_entrys()
        self.argumentos = ('c_registros',['No Inscripción', 'Código Curso', 'Nombre del Curso', 'Horario', 'Fecha de Inscripción'],[90,90,270,150,130]) 
        self.tree_view_prueba(*self.argumentos)
        self.cursor.execute(f'''SELECT * FROM Inscritos WHERE No_Inscripción = {event}''')

        self.data = self.cursor.fetchall()

        #para no_inscripciones
        if self.data!=[]:
            id_alumno=self.data[0][1]
            self.cursor.execute(f'''SELECT * FROM Alumnos WHERE Id_Alumno = {id_alumno}''')
            self.data_alumno = self.cursor.fetchall()

        #para id_alumno
        else:
            self.cursor.execute(f'''SELECT * FROM Alumnos WHERE Id_Alumno = {event}''')
            self.data_alumno = self.cursor.fetchall()

        self.add_consultar(self.cmbx_Id_Alumno, self.data_alumno[0][0])
        self.add_consultar(self.cmbx_Id_Carrera, self.data_alumno[0][1])
        self.add_consultar(self.nombres, self.data_alumno[0][2])
        self.add_consultar(self.apellidos, self.data_alumno[0][3])    
        self.add_consultar(self.direccion, self.data_alumno[0][5])
        self.add_consultar(self.ciudad, self.data_alumno[0][8])
        self.add_consultar(self.departamento, self.data_alumno[0][9])
        self.add_consultar(self.telCel, self.data_alumno[0][6])
        self.add_consultar(self.telFijo, self.data_alumno[0][7])
        self.fecha_ing = self.fecha_split(self.data_alumno[0][4])
        self.add_consultar(self.fecha, self.fecha_ing)

        self.cursor.execute(f'''SELECT * FROM Inscritos WHERE Id_Alumno = {self.data_alumno[0][0]}''')
        self.datos = self.cursor.fetchall()
        for i in self.datos:
            self.cursor.execute(f'''SELECT * FROM Cursos WHERE Código_Curso = {i[3]}''')
            self.data_cursos = self.cursor.fetchall()
            print(self.data_cursos)
            self.tViews.insert("", tk.END, values=(i[0], i[3], self.data_cursos[0][1], i[4], i[2]))
        self.tViews.bind("<Double-1>", self.treeview_cmbx_curso)

        # self.cursor.execute(f''' SELECT Inscritos.Id_Alumno, Nombres, Apellidos, Alumnos.Fecha_Ingreso, No_Inscripción, Dirección, Ciudad, Departamento, 
        #                     Telef_Cel, Telef_Fijo, Id_Carrera, Inscritos.Código_Curso, Descripción_Curso, Num_Horas, Fecha_de_Inscripción  FROM Inscritos 
        #             JOIN Alumnos ON Inscritos.Id_Alumno = Alumnos.Id_Alumno 
        #             JOIN Cursos ON Inscritos.Código_Curso = Cursos.Código_Curso 
        #             JOIN Carreras ON Alumnos.Id_Carrera = Carreras.Código_Carrera 
        #             WHERE Inscritos.No_Inscripción = {event}''')
        # self.datos = self.cursor.fetchall()
        # self.lista_consulta_i = []
        # for i in self.datos:
        #     self.lista_consulta_i += i 
        
        # self.fecha_ins = self.fecha_split(self.lista_consulta_i[3])
        
        # self.fecha_ing = self.fecha_split(self.lista_consulta_i[14])
        
        # self.limpiar()
        
        # self.entry_datos = [self.cmbx_Id_Alumno, self.nombres, self.apellidos, self.fecha, self.noInscripcion, self.direccion, self.ciudad,
        #          self.departamento, self.telCel, self.telFijo, self.cmbx_Id_Carrera, self.codigo_Curso, self.nombreCurso, self.horario, 
        #          self.fechaInscripcion]
        # self.a = 0
        # for i in self.entry_datos:
        #     if i == self.fecha:
        #         i.insert(0, self.fecha_ing)
        #         i.config(state="readonly")
        #     elif i == self.fechaInscripcion:
        #         i.insert(0, self.fecha_ins)
        #         i.config(state="readonly")
        #     else:
        #         i.insert(0, self.lista_consulta_i[self.a])
        #         i.config(state="readonly")
        #     self.a += 1
        # self.cursor.execute(f'''SELECT Inscritos.No_Inscripción, Inscritos.Código_Curso, Cursos.Descripción_Curso, Inscritos.Horario_Curso, Inscritos.Fecha_de_Inscripción FROM Inscritos
        #            JOIN Cursos ON Inscritos.Código_Curso = Cursos.Código_Curso
        #            WHERE Inscritos.Id_Alumno = {self.lista_consulta_i[0]}
        #            ''')
        # datos_materias_i = self.cursor.fetchall()
        # for i in datos_materias_i:
        #     self.lista_materia = []
        #     self.lista_materia += i
        #     self.tViews.insert("", tk.END, values=(self.lista_materia[0], self.lista_materia[1], self.lista_materia[2], self.lista_materia[3], self.lista_materia[4]))
    def treeview_cmbx_curso(self, event):
        
        self.add_consultar(self.noInscripcion, self.tvEntry0)
        self.noInscripcion.config(state="readonly")
        self.add_consultar(self.codigo_Curso, self.tvEntry1)
        self.codigo_Curso.config(state="readonly")
        self.add_consultar(self.nombreCurso, self.tvEntry2)
        self.add_consultar(self.horario, self.tvEntry3)
        self.fecha_ins= self.fecha_split(self.tvEntry4)
        self.add_consultar(self.fechaInscripcion, self.fecha_ins)
        self.fechaInscripcion.config(state="enabled")
        self.obtener_curso_anterior()

    def obtener_curso_anterior(self):
        self.codigo_curso_antiguo=self.codigo_Curso.get()

    def limpiar_data(self):
        self.tvNoInscripcion.set('')
        self.tvCodigoCurso.set('')
        self.tvFechaInscripcion.set('')
        self.tvNombreCurso.set('')
        self.tvHorarios.set('')
    
    def obtener_fila(self, event):
        item = self.tViews.focus()
        if not item:
            return
        self.data= self.tViews.item(item)
        self.tvEntry0=self.data["values"][0]
        self.tvEntry1=self.data["values"][1]
        self.tvEntry2=self.data["values"][2]
        if len(self.data["values"]) > 3:
            self.tvEntry3=self.data["values"][3]
            if len(self.data["values"]) > 4:
                self.tvEntry4=self.data["values"][4]

    def eliminar_data (self,seleccion):
        self.limpiar_data()
        if seleccion == 1:
            try:
                item = self.tViews.selection()
                if not item: raise TypeError

                self.winEmerDelete.destroy()
                alert = messagebox.askquestion('Eliminando datos', 'Desea eliminar este valor?')
                if alert == 'yes':            
                    self.eliminar_datos(self.data['values'][1], 'Código_Curso')
                    self.tViews.delete(item)

            except TypeError:
                messagebox.showerror("Error", str('Debe seleccionar primero un valor a eliminar en el cuadro de abajo'))
                self.winEmerDelete.destroy()
                pass

        elif seleccion == 2:
            item = self.tViews.get_children()[0]
            self.data = self.tViews.item(item)
            self.winEmerDelete.destroy()
            alert = messagebox.askquestion('Eliminando datos', 'Desea eliminar todos los cursos?')
            if alert == 'yes':            
                # print(self.tViews.get_children()[0])
                self.eliminar_datos(self.data['values'][0], 'No_Inscripción')
                self.tViews.delete(*self.tViews.get_children())
        else: 
            messagebox.showerror("Error", str('no se selecciono ninguna opcion'))
            pass

    guardado = False

    def grabar(self):
        self.btnConsultar.config(state='disabled')
        self.btnEliminar.config(state='disabled')
        self.btnEditar.config(state='disabled')
        
        if not self.cmbx_Id_Alumno.get():
            messagebox.showwarning("Advertencia", "Debe seleccionar su id de alumno")
        elif self.cmbx_Id_Alumno.get() and self.guardado == False:
            self.consultar_ventana("Guardar Datos", "Seleciona una opción", ["Guardar Inscripción", "Guardar Estudiante"], "Seleccionar", self.boton_escoger_guardar)
        elif self.cmbx_Id_Alumno.get() and self.guardado == True:
            self.verificar_agregar_data()
        else:
            pass

    def boton_escoger_guardar(self):
        if self.int.get() == 1:
            self.guardado = True
            self.cerrar_ventana()
            self.verificar_agregar_data()

        elif self.int.get() == 2:
            self.guardado = True
            self.cerrar_ventana()
        else: #tal vez se puede omitir este else
            self.guardado = False
            messagebox.showwarning("Advertencia", "Debe seleccionar una opción")
            self.int.set(0)
            self.cerrar_ventana()
            
    def verificar_agregar_data(self):
        hoy = datetime.date.today()
        nombreCurso = self.nombreCurso.get()
        Horario = self.horario.get()

        for item_id in self.tViews.get_children():#lee los datos obtenidos en el treeview y revisa que no se agrege un curso repetido
            item = self.tViews.item(item_id)
            if nombreCurso == item['values'][2]:
                messagebox.showwarning("Advertencia", "el curso que esta por agregar ya existe, por favor, solicite otro curso")
                return
        try: #revisa si en el treeview tiene un no de inscripcion asociado
            if item['values']:
                self.noInscripcion.set(item['values'][0])
                noInscripcion = self.noInscripcion.get()
        except: # sino le asigna el mayor +1
            query = '''SELECT MAX(No_Inscripción) FROM Inscritos;'''
            self.cursor.execute(query)
            self.conn.commit()
            ultimoNoInscrito = self.cursor.fetchall()
            ultimoNoInscrito = int(ultimoNoInscrito[0][0])
            self.noInscripcion.set(ultimoNoInscrito + 1)
            noInscripcion = self.noInscripcion

        fechaInscripcion = self.fechaInscripcion.get() #le asigna a la fecha de inscripcion del dia actual
        if not fechaInscripcion:
            fechaInscripcion = tk.StringVar()
            fechaInscripcion = hoy.strftime('%Y-%m-%d') #revisar si se deja ese formato o el de dd/mm/yyyy por lo que de la otra forma aparecen los datos de la db
            self.fechaInscripcion.insert(tk.END, fechaInscripcion)
        else:
            pass

        if self.guardado == True: #verifica si la bandera de guardar esta activa
            fechaInscripcion = self.fechaInscripcion.get()
            codigo = self.codigo_Curso.get()
            datos = (noInscripcion, codigo, nombreCurso, Horario, fechaInscripcion)

            if noInscripcion and nombreCurso and Horario and fechaInscripcion and codigo:
                self.tViews.insert("", tk.END, values=datos)
                self.agregar_datos(self.noInscripcion.get(), self.cmbx_Id_Alumno.get(), fechaInscripcion, self.codigo_Curso.get())#guarda en la db
                self.guardado = False # baja la bandera de guardado
        
    def agregar_estudiantes(self): #ESTA FUNCION NO ESTA ACTIVA
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
    
    def consultar_estudiantes_cmbx(self, event):
        self.limpiar()
        self.cursor.execute(f'''SELECT Id_Alumno, Id_Carrera, Nombres, Apellidos, Fecha_Ingreso, Dirección, Telef_Cel, Telef_Fijo, Ciudad, Departamento FROM Alumnos WHERE Id_Alumno = {event}''') 
        self.datos_estudiantes_cmbx = self.cursor.fetchall()
        self.entry_datos = [self.cmbx_Id_Alumno, self.cmbx_Id_Carrera, self.nombres, self.apellidos, self.fecha, self.direccion, 
                    self.telCel, self.telFijo, self.ciudad, self.departamento]
        self.d = 0
        for i in self.datos_estudiantes_cmbx[0]:
            if self.entry_datos[self.d] == self.fecha:
                self.entry_datos[self.d].insert(0, self.fecha_split(i))
            else:
                self.entry_datos[self.d].insert(0, i)
            self.entry_datos[self.d].config(state="readonly")
            self.d += 1

        self.argumentos = ('c_registros',['No Inscripción', 'Código Curso', 'Nombre del Curso', 'Horario', 'Fecha de Inscripción'],[110,110,290,224,130]) 
        self.tree_view_prueba(*self.argumentos)

        self.cursor.execute(f'''SELECT Inscritos.No_inscripción, Inscritos.Código_Curso, Cursos.Descripción_Curso, Inscritos.Horario_Curso, Inscritos.Fecha_de_Inscripción FROM Inscritos
                   JOIN Cursos ON Inscritos.Código_Curso = Cursos.Código_Curso
                   WHERE Inscritos.Id_Alumno = {event}
                   ''')
        datos_materias_cmbx = self.cursor.fetchall()
        for i in datos_materias_cmbx:
            self.lista_materia = []
            self.lista_materia += i
            self.tViews.insert("", tk.END, values=(self.lista_materia[0], self.lista_materia[1], self.lista_materia[2], self.lista_materia[3], self.lista_materia[4]))
    
    def consultar_cursos_cmbx(self,event):
        #self.limpiar()
        self.cursor.execute(f'''SELECT Código_Curso, Descripción_Curso, Horario_Curso FROM Cursos WHERE Código_Curso = {event}''')
        self.datos = self.cursor.fetchall()
        self.entry_datos = [self.codigo_Curso, self.nombreCurso, self.horario]
        self.d = 0
        for i in self.datos[0]:
            self.entry_datos[self.d].insert(0, i)
            self.entry_datos[self.d].config(state="readonly")
            self.d += 1
        
        self.argumentos = ('c_registros',['No Inscripción', 'Id Alumno', 'Nombres', 'Apellidos', 'Fecha de Inscripción'],[110,110,290,224,110])
        
        if self.guardado == False:
            self.tree_view_prueba(*self.argumentos)
        # else:self.tViews.delete()
        
        self.cursor.execute(f'''SELECT Inscritos.No_Inscripción, Inscritos.Id_Alumno, Nombres, Apellidos, Inscritos.Fecha_de_Inscripción FROM Inscritos
                            JOIN Alumnos ON Inscritos.Id_Alumno = Alumnos.Id_Alumno
                            WHERE Inscritos.Código_Curso = {event}''')
        datos_materias = self.cursor.fetchall()
        if self.guardado == False:
            for i in datos_materias:
                self.lista_materia = []
                self.lista_materia += i
                self.tViews.insert("", tk.END, values=(self.lista_materia[0], self.lista_materia[1], self.lista_materia[2], self.lista_materia[3], self.lista_materia[4]))
    
    def get_data_curso(self, curso):
        self.cursor.execute("SELECT * FROM Cursos WHERE Código_Curso = ?", (curso,))
        self.data = self.cursor.fetchall()
        return self.data
    
    def get_data_entrys(self):
        self.nombre_actual=self.nombres.get()
        self.apellido_actual=self.apellidos.get()
        self.fecha_actual=self.fecha.get()
        self.direccion_actual=self.direccion.get()
        self.telcel_actual=self.telCel.get()
        self.telfijo_actual=self.telFijo.get()
        self.ciudad_actual=self.ciudad.get()
        self.departamento_actual=self.departamento.get()
        self.noinscripcion_actual=self.noInscripcion.get()
        self.idalumno_actual=self.cmbx_Id_Alumno.get()
        self.idcarrera_actual=self.cmbx_Id_Carrera.get()
        self.noInscripcion_actual=self.noInscripcion.get()
        self.id_curso_actual=self.codigo_Curso.get()
        self.nombre_curso_actual=self.nombreCurso.get()
        self.horario_actual=self.horario.get()
        self.fecha_inscripcion_actual=self.fechaInscripcion.get()
    def add_editar(self, entry):
            return entry.get()
    def add_consultar(self,entry, value):
            entry.config(state="normal")
            entry.delete(0, 'end')
            entry.insert(0, value)
            entry.config(state="readonly")
            
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
    signal(SIGINT, SIG_IGN) # Ignorar la señal de interrupción versión mejorada
    app.run()
    app.close_sqlite()