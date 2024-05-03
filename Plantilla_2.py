# !/usr/bin/python3
# -*- coding: utf-8 -*-
import tkinter as tk
import tkinter.ttk as ttk
import sqlite3
#from tkcalendar import DateEntry
from tkinter import messagebox
import datetime
import ctypes
from pathlib import Path
from subprocess import run

PATH = str((Path(__file__).resolve()).parent)
ICONO = r"/img/LogoinscripcionesIco.png"
DB = r""


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
        self.win.geometry(f"+{self.x}+{self.y}")
        self.win.resizable(False, False)
        
        self.win.title("Inscripciones de Materias y Cursos")
        #ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('Inscripciones')
        #self.win.iconbitmap(PATH + ICONO)
        #icono = ttk.PhotoImage(file= PATH + ICONO)
        #self.win.wm_iconphoto(False, icono)

        # Crea los frames
        self.frm_1 = tk.Frame(self.win, name="frm_1")
        self.frm_1.configure(background="#f7f9fd", height=600, width=800)

        ''' Etiquetas y Campos de la Aplicación'''

        #Label No. Inscripción
        self.lblNoInscripcion = ttk.Label(self.frm_1, name="lblnoinscripcion")
        # self.lblNoInscripcion.configure(background="#f7f9fd",font="{Arial} 11 {bold}", justify="left",state="normal", takefocus=False,text='No.Inscripción')
        self.lblNoInscripcion.configure(background="#f7f9fd", text='No.Inscripción:')
        self.lblNoInscripcion.place(anchor="nw", x=20, y=185)
        #Conmbox No. Inscripción
        self.noInscripcion = ttk.Entry(self.frm_1, name="noInscripcion", state='readonly')
        self.noInscripcion.place(anchor="nw", width=100, x=120, y=185)

        #Label Fecha
        self.lblFecha = ttk.Label(self.frm_1, name="lblfecha")
        self.lblFecha.configure(background="#f7f9fd", text='Fecha:')
        self.lblFecha.place(anchor="nw", x=420, y=20)
        #Entry Fecha
        self.fecha = tk.Entry(self.frm_1, name="fechas", state='readonly')
        self.fecha.configure(justify="center")
        self.fecha.place(anchor="nw", width=100, x=500, y=20)
    
        #Label id_carrera
        self.lblIdCarrera = ttk.Label(self.frm_1, name="lblidcarrera")
        self.lblIdCarrera.configure(background="#f7f9fd", text='Id Carrera:')
        self.lblIdCarrera.place(anchor="nw", x=220, y=20)
        #Combobox id_carrera
        self.cmbx_Id_Carrera = ttk.Entry(self.frm_1, name="cmbx_id_carrera", state="readonly")
        self.cmbx_Id_Carrera.place(anchor="nw", width=100, x=300, y=20)

        #Label id_Alumno
        self.lblIdAlumno = ttk.Label(self.frm_1, name="lblidalumno")
        self.lblIdAlumno.configure(background="#f7f9fd", text='Id Alumno:')
        self.lblIdAlumno.place(anchor="nw", x=20, y=20)
        #Combobox id_Alumno
        self.cmbx_Id_Alumno = ttk.Combobox(self.frm_1, name="cmbx_id_alumno", state="readonly")

        self.cmbx_Id_Alumno.place(anchor="nw", width=100, x=100, y=20)

        #Label Alumno
        self.lblNombres = ttk.Label(self.frm_1, name="lblnombres")
        self.lblNombres.configure(background="#f7f9fd",text='Nombre(s):')
        self.lblNombres.place(anchor="nw", x=20, y=60)
        #Entry Alumno
        self.nombres = ttk.Entry(self.frm_1, name="nombres", state='readonly')
        self.nombres.place(anchor="nw", width=200, x=100, y=60)

        #Label Apellidos
        self.lblApellidos = ttk.Label(self.frm_1, name="lblapellidos")
        self.lblApellidos.configure(background="#f7f9fd", text='Apellido(s):')
        self.lblApellidos.place(anchor="nw", x=320, y=60)
        #Entry Apellidos
        self.apellidos = ttk.Entry(self.frm_1, name="apellidos", state='readonly')
        self.apellidos.place(anchor="nw", width=200, x=400, y=60)
        self.apellidos.insert(0,"")

        #Label Direccion
        self.lblDireccion = ttk.Label(self.frm_1, name="lbldireccion")
        self.lblDireccion.configure(background="#f7f9fd", text='Dirección: ')
        self.lblDireccion.place(anchor="nw", x=20, y=100)
        #Entry Direccion
        self.direccion = ttk.Entry(self.frm_1, name="direccion", state='readonly')
        self.direccion.place(anchor="nw", width=200, x=100, y=100)

        #Label Ciudad
        self.lblCiudad = ttk.Label(self.frm_1, name="lblciudad")
        self.lblCiudad.configure(background="#f7f9fd", text='Ciudad: ')
        self.lblCiudad.place(anchor="nw", x=520, y=100)
        #Entry Ciudad
        self.ciudad = ttk.Entry(self.frm_1, name="ciudad", state='readonly')
        self.ciudad.place(anchor="nw", width=100, x=600, y=100)

        #Label Departamento
        self.lblDepartamento = ttk.Label(self.frm_1, name="lbldepartamento")
        self.lblDepartamento.configure(background="#f7f9fd", text='Departamento: ')
        self.lblDepartamento.place(anchor="nw", x=320, y=100)
        #Entry Departamento
        self.departamento = ttk.Entry(self.frm_1, name="departamento", state='readonly')
        self.departamento.place(anchor="nw", width=100, x=410, y=100)

        #Label Telefono Celular
        self.lblTelCel = ttk.Label(self.frm_1, name="lbltelcel")
        self.lblTelCel.configure(background="#f7f9fd", text='Teléfono Celular: ')
        self.lblTelCel.place(anchor="nw", x=20, y=140)
        #Entry Telefono Celular
        self.telCel = ttk.Entry(self.frm_1, name="telcel", state='readonly')
        self.telCel.place(anchor="nw", width=200, x=120, y=140)

        #Label Telefono Fijo
        self.lblTelFijo = ttk.Label(self.frm_1, name="lbltelfijo")
        self.lblTelFijo.configure(background="#f7f9fd", text='Teléfono Fijo: ')
        self.lblTelFijo.place(anchor="nw", x=320, y=140)
        #Entry Telefono Fijo
        self.telFijo = ttk.Entry(self.frm_1, name="telfijo", state='readonly')
        self.telFijo.place(anchor="nw", width=200, x=420, y=140)

        #Label Codigo del Curso
        self.lblDscCurso = ttk.Label(self.frm_1, name="lbldsccurso")
        self.lblDscCurso.configure(background="#f7f9fd", state='readonly',text='Codigo del Curso:')
        self.lblDscCurso.place(anchor="nw", x=240, y=185)
        #Entry Codigo del Curso 
        self.descripc_Curso = ttk.Combobox(self.frm_1, name="descripc_curso", state='disabled')
        self.descripc_Curso.configure(justify="left", width=166)
        self.descripc_Curso.place(anchor="nw", width=300, x=350, y=185)


        ''' Botones  de la Aplicación'''
        @staticmethod
        def activar_boton_grabar():
            self.btnGrabar.config(state="normal")
        #Botón Consultar

        def consultar():
            valor=self.cmbx_Id_Alumno.get()
            if valor== '':
                messagebox.showerror("Inscripciones", "Debe seleccionar un alumno")
                return
            else:
                self.cmbx_Id_Alumno.config(state="disabled")
                self.btnConsultar.config(state="disabled")
                for i in self.lista_alumnos:
                    if valor == i[0]:
                        self.add_consultar(self.cmbx_Id_Carrera, i[1])
                        self.add_consultar(self.nombres, i[2])
                        self.add_consultar(self.apellidos, i[3])
                        self.add_consultar(self.fecha, i[4])
                        self.add_consultar(self.direccion, i[5])
                        self.add_consultar(self.telCel, i[6])
                        self.add_consultar(self.telFijo, i[7])
                        self.add_consultar(self.ciudad, i[8])
                        self.add_consultar(self.departamento, i[9])
                inscripciones=self.get_data_inscripciones(valor) 
                print(inscripciones)
                if inscripciones==None:
                    pass
                else:
                    insert_data(inscripciones)
                    self.numero_codigo_inscripcion(valor)
                

        self.btnConsultar = ttk.Button(self.frm_1, name="btnconsultar", cursor="hand2", command=consultar)
        self.btnConsultar.configure(text='Consultar')
        self.btnConsultar.place(anchor="nw", x=150, y=260, width=80)


        #Botón Editar
        def editar():
            activar_boton_grabar()
            if not self.is_fields_enabled:
                self.nombres.config(state="normal")
                self.apellidos.config(state="normal")
                self.descripc_Curso.config(state="readonly")
                self.fecha.config(state="normal")
                self.cmbx_Id_Alumno.config(state="disabled")
                self.cmbx_Id_Carrera.config(state="normal")
                self.ciudad.config(state="normal")
                self.departamento.config(state="normal")
                self.direccion.config(state="normal")
                self.telCel.config(state="normal")
                self.telFijo.config(state="normal")
                self.is_fields_enabled = True
            else:
                pass
        self.btnEditar = ttk.Button(self.frm_1, name="btneditar", cursor="hand2", command=editar)
        self.btnEditar.configure(text='Editar')
        self.btnEditar.place(anchor="nw", x=255, y=260,  width=80)

        #Botón Eliminar
        self.btnEliminar = ttk.Button(self.frm_1, name="btneliminar", cursor="hand2")
        self.btnEliminar.configure(text='Eliminar')
        self.btnEliminar.place(anchor="nw", x=360, y=260, width=80)
        #Botón Cancelar

        # def limpiar():
        #     self.num_Inscripcion.delete(0,tk.END)
        #     self.fecha.delete(0, tk.END)
        #     self.cmbx_Id_Alumno.delete(0,tk.END)
        #     self.id_Curso.delete(0,tk.END)
        #     self.cmbx_horario.delete(0,tk.END)

        #     # al estar ReadOnly 
        #     self.nombres.config(state="Normal")
        #     self.nombres.delete(0,tk.END)
        #     self.nombres.config(state='readonly')
            
        #     self.apellidos.config(state='normal')
        #     self.apellidos.delete(0,tk.END)
        #     self.apellidos.config(state='readonly')

        #     self.descripc_Curso.config(state="Normal")
        #     self.descripc_Curso.delete(0,tk.END)
        #     self.descripc_Curso.config(state='readonly')

        self.btnCancelar = ttk.Button(self.frm_1, name="btncancelar", cursor="hand2")
        self.btnCancelar.configure(text='Cancelar')
        self.btnCancelar.place(anchor="nw", x=465, y=260, width=80)

        self.btnCancelar.bind()
        #Botón Grabar
        #duncion para grabar
        def grabar():
            pass
        

        self.btnGrabar = ttk.Button(self.frm_1, name="btngrabar", cursor="hand2", command=grabar)
        self.btnGrabar.configure(text='Grabar')
        self.btnGrabar.config(state="disabled")
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
        self.tView_cols = ['Alumno','NoInscripción', 'CódigoCurso','tV_descripción', 'Horas' ]
        self.tView.bind("<Button-1>", cancel, add="+")
        self.tView.configure(columns=self.tView_cols)
        self.tView.column("#0", width=0)
        self.tView.column("Alumno",anchor="w",stretch=True,width=180)
        self.tView.column("NoInscripción",anchor="w",stretch=True,width=92)
        self.tView.column("CódigoCurso",anchor="w",stretch=True,width=120)
        self.tView.column("tV_descripción",anchor="w",stretch=True,width=240)
        self.tView.column("Horas",anchor="w",stretch=True,width=92)
        #Cabeceras
        self.tView.heading("Alumno",anchor="w", text='Alumno')
        self.tView.heading("NoInscripción",anchor="w", text='No.Inscripción')
        self.tView.heading("CódigoCurso",anchor="w", text='Código de Curso')
        self.tView.heading("tV_descripción", anchor="w", text='Descripción')
        self.tView.heading("Horas", anchor="w", text='No.Horas')
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

        #Inserts
        def insert_data(inscripciones):
            valornombre=self.nombres.get()
            valorapellido=self.apellidos.get()
            nombre = valornombre+" "+valorapellido
            self.tView.insert("", "end", values=(nombre, '', '', '', ''))
            for i in inscripciones:
                curso=self.get_data_cursos_estudiantes(i[3])
                for j in curso:
                    self.tView.insert("", "end", values=('', i[0], j[0], j[1], j[2]))

        # Main widget
        self.mainwindow = self.win
    def add_consultar(self,entry, value):
            entry.config(state="normal")
            entry.delete(0, 'end')
            entry.insert(0, value)
            entry.config(state="readonly")

    def run(self):
        self.mainwindow.mainloop()


    ''' A partir de este punto se deben incluir las funciones
     para el manejo de la base de datos '''
 
    def run_sqlite(self):
        self.conn = sqlite3.connect('db\\Inscripciones.db')
        self.conn.execute("PRAGMA foreign_keys = 1")
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS  Inscritos(
        No_Inscritos INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        Id_Alumno VARCHAR(20) NOT NULL,
        Fecha_de_Inscripción DATE NOT NULL,
        Código_Curso VARCHAR(20),
        FOREIGN KEY (Código_Curso) REFERENCES Cursos(Código_Curso),
        FOREIGN KEY (Id_Alumno) REFERENCES Alumnos(Id_Alumno)
        
        )''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS  Cursos(
            Código_Curso VARCHAR(20) NOT NULL PRIMARY KEY,
            Descripción_Curso VARCHAR(60),
            Num_Horas SMALLINT(2)
        )''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS  Carreras(
            Id_Carrera VARCHAR(15) PRIMARY KEY NOT NULL,
            Descripción VARCHAR(100),
            Num_Semestres SMALLINT(2)
        )''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS  Alumnos(
            Id_Alumno VARCHAR(20) NOT NULL PRIMARY KEY,
            Id_Carrera VARCHAR(15) NOT NULL,
            Nombres VARCHAR(50),
            Apellidos VARCHAR(50),
            Fecha_Ingreso DATE,
            Dirección VARCHAR(60),
            Telef_Cel VARCHAR (18),
            Telef_Fijo VARCHAR (15),
            Ciudad VARCHAR(60),
            Departamento VARCHAR(60),
            FOREIGN KEY (Id_Carrera) REFERENCES Carreras (Id_Carrera)
        )''')

        estudiantes = [
            ('8876295089', '2789', 'Juan', 'Pérez', '2019-01-15', 'Calle 1 # 2-3', '300-1234567', '300-1234567', 'Bogotá', 'Cundinamarca'),
            ('5269436393', '2789', 'Juan Camilo', 'Pérez Soza', '2024-11-15', 'Calle 65 # 20-3', '300-1234567', '300-1234', 'Bogotá', 'Cundinamarca'),
            ('8114559050', '2789', 'Pedro Pedro', 'Torres Castillo', '2024-03-16', 'Calle 72B # 23-30', '300-1234567', '300-1234', 'Bogotá', 'Cundinamarca'),
            ('7270566584', '2789', 'María Camila', 'González López', '2024-04-27', 'Calle 10 # 5-6', '310-9876543', '310-9876', 'Medellín', 'Antioquia'),
            ('7894756003', '2544', 'Andrés David', 'Martínez Rodríguez', '2024-04-28', 'Carrera 20 # 15-30', '320-7654321', '320-7654', 'Cali', 'Valle del Cauca'),
            ('8562305458', '2544', 'Laura Camila', 'Ramírez Pérez', '2024-04-29', 'Avenida 5 # 8-12', '315-5432109', '315-5432', 'Barranquilla', 'Atlántico'),
            ('6045534334', '2544', 'Carlos Felipe', 'López Gómez', '2024-04-30', 'Calle 7 # 12-15', '317-8765432', '317-8765', 'Bogotá', 'Cundinamarca'),
            ('2764144293', '2544', 'Ana Maria', 'Hernández Martínez', '2024-05-01', 'Carrera 15 # 25-18', '314-6543210', '314-6543', 'Medellín', 'Antioquia'),
            ('7511200463', '2544', 'Diego Alejandro', 'García Ramírez', '2024-05-02', 'Avenida 8 # 10-5', '312-9876543', '312-9876', 'Cali', 'Valle del Cauca'),
            ('9030779197', '2545', 'Sara Sofía', 'Pérez Martínez', '2024-05-03', 'Calle 12 # 20-7', '319-7654321', '319-7654', 'Barranquilla', 'Atlántico'),
            ('8605132377', '2545', 'Javier', 'López Ramírez', '2024-05-04', 'Carrera 18 # 22-10', '316-5433433', '320-5421', 'Valledupar', 'Cesar'),
            ('2550301257', '2545', 'Carla Valentina', 'Sánchez Pérez', '2024-05-05', 'Avenida 3 # 6-9', '313-8765432', '313-8765', 'Bogotá', 'Cundinamarca'),
            ('9997493368', '2545', 'Gabriel', 'Gómez Ramírez', '2024-05-06', 'Calle 5 # 8-11', '311-6543210', '311-6543', 'Medellín', 'Antioquia'),
            ('6514506224', '2546', 'Isabella', 'Martínez López', '2024-05-07', 'Carrera 12 # 18-25', '319-7654321', '319-7654', 'Cali', 'Valle del Cauca'),
            ('6223175366', '2546', 'Mateo', 'Hernández Ramírez', '2024-05-08', 'Avenida 7 # 10-14', '316-5432109', '316-5432', 'Barranquilla', 'Atlántico'),
            ('8221071329', '2546', 'Carlos Valentín', 'López Martínez', '2024-05-09', 'Calle 15 # 22-17', '314-9876543', '314-9876', 'Bogotá', 'Cundinamarca'),
            ('8782642282', '2548', 'Camila', 'García Ramírez', '2024-05-10', 'Carrera 25 # 30-22', '317-7654321', '317-7654', 'Medellín', 'Antioquia'),
            ('5301173864', '2548', 'Lucas Alejandro', 'Pérez Martínez', '2024-05-11', 'Avenida 10 # 12-19', '312-8765432', '312-8765', 'Cali', 'Valle del Cauca'),
            ('1008146001', '2548', 'Valentino', 'Ramírez Gómez', '2024-05-12', 'Calle 18 # 22-14', '318-7654321', '318-7654', 'Barranquilla', 'Atlántico'),
            ('2778948484', '2549', 'Isabel Maria', 'López Martínez', '2024-05-13', 'Avenida 12 # 15-20', '314-9876543', '314-9876', 'Bogotá', 'Cundinamarca'),
            ('9557617951', '2549', 'Sara Lucía', 'García Ramírez', '2024-05-14', 'Carrera 22 # 30-18', '317-7654321', '317-7654', 'Medellín', 'Antioquia'),
            ('1322078372', '2549', 'Damian Matías', 'Pérez Martínez', '2024-05-15', 'Avenida 15 # 18-22', '312-8765432', '312-8765', 'Cali', 'Valle del Cauca'),
            ('5547157920', '2549', 'Valeria', 'Hernández Ramírez', '2024-05-16', 'Calle 20 # 25-19', '319-6543210', '319-6543', 'Barranquilla', 'Atlántico')
        ]
        cursos =[
            ('2015734', 'Programación de Computadores', '12'),
            ('2015711','Dibujo Básico', '12'),
            ('2016375', 'Programación Orientada a Objetos', '12'),
            ('2016509', 'Taller de Electrónica', '12'),
            ('2016703', 'Pensamiento Sistémico', '12'),
            ('2017228', 'Tecnología Mecánica Básica', '16'),
            ('1000004', 'Cálculo Diferencial', '16'),
            ('1000005', 'Cálculo Integral','16'),
            ('1000006', 'Cálculo en Varia Variables', '16'),
            ('1000003', 'Algebra Lineal', '16'),
            ('1000017', 'Fundamentos de Electromagnetismo', '16'),
            ('1000019', 'Fundamentos de Mecánica', '16'),
            ('1000025', 'Laboratorio de Técnicas Básicas en Química', '12'),
            ('1000026','Principio de Análisis Químico', '16')
        ]
        carreras=[
            ('2789','Ingeniería de Sistemas y Computación', '10'),
            ('2544','Ingeniería Eléctrica', '10'),
            ('2545','Ingeniería Electrónica', '10'),
            ('2546','Ingeniería Industrial', '10'),
            ('2548','Ingeniería Mecatrónica', '10'),
            ('2549','Ingeniería Química', '10'),
            ('2879','Ingeniería de Sistemas', '10')
        ]
        self.cursor.executemany("INSERT OR IGNORE INTO Cursos(Código_Curso, Descripción_Curso, Num_Horas) VALUES(?,?,?)", cursos)

        self.cursor.executemany("INSERT OR IGNORE INTO Carreras(Id_Carrera, Descripción, Num_Semestres) VALUES(?,?,?)", carreras)

        self.cursor.executemany("INSERT OR IGNORE INTO Alumnos(Id_Alumno, Id_Carrera, Nombres, Apellidos, Fecha_Ingreso, Dirección, Telef_Cel, Telef_Fijo, Ciudad, Departamento) VALUES(?,?,?,?,?,?,?,?,?,?)", estudiantes)

    def get_data_idalumno(self):
        self.cursor.execute("SELECT Id_Alumno FROM Alumnos")
        self.data = self.cursor.fetchall()
        self.lista_idalumnos = []
        for i in self.data:
            str(i[0])
            self.lista_idalumnos.append(i[0])
        self.cmbx_Id_Alumno['values'] = self.lista_idalumnos
    
    def get_data_cursos(self):
        self.cursor.execute("SELECT * FROM Cursos")
        self.data = self.cursor.fetchall()
        self.lista_cursos = []
        for i in self.data:
            self.lista_cursos.append(f'{str(i[0])}-{str(i[1])}')
        self.descripc_Curso['values'] = self.lista_cursos

    def get_data_complete(self):
        self.cursor.execute("SELECT * FROM Alumnos")
        self.data = self.cursor.fetchall()
        self.lista_alumnos = []
        for i in self.data:
            self.lista_alumnos.append(i)
        
    def close_sqlite(self):
        self.conn.commit()
        self.conn.close()
        print('Conexión cerrada')
    def get_data_inscripciones(self, id_alumno):
        inscripciones_alumno = []
        for i in self.lista_alumnos:
            if id_alumno == i[0]:
                print(i[0])
                self.cursor.execute("SELECT * FROM Inscritos WHERE id_Alumno = ?", (i[0],))
                self.data = self.cursor.fetchall()
                for j in self.data:
                    inscripciones_alumno.append(j)
                    return inscripciones_alumno
                
    def get_data_cursos_estudiantes(self, codigo_curso):
        self.cursor.execute("SELECT * FROM Cursos WHERE Código_Curso = ?", (codigo_curso,))
        self.data = self.cursor.fetchall()
        return self.data
    def insertar_inscripciones(self, id_alumno, fecha, codigo_curso):
        self.cursor.execute("INSERT INTO Inscritos(Id_Alumno, Fecha_de_Inscripción, Código_Curso) VALUES(?,?,?)", (id_alumno, fecha, codigo_curso))
        self.conn.commit()

    def numero_codigo_inscripcion(self, id_alumno):
        inscripciones_alumno=self.data=self.get_data_inscripciones(id_alumno)
        lista_inscripciones = []
        for i in inscripciones_alumno:
            lista_inscripciones.append(i[0])
        self.add_consultar(self.noInscripcion, lista_inscripciones)


if __name__ == "__main__":
    app = Inscripciones_2()
    app.run_sqlite()
    app.get_data_idalumno()
    app.get_data_complete()
    app.get_data_cursos()
    app.run()
    app.close_sqlite()