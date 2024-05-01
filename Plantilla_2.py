# !/usr/bin/python3
# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk
import sqlite3
from tkcalendar import DateEntry
import datetime
import ctypes
from pathlib import Path

PATH = str((Path(__file__).resolve()).parent)
ICONO = r"/img/LogoinscripcionesIco.ico"
DB = r""

class Inscripciones_2: 
    def __init__(self, master=None):
         # Ventana principal
        self.db_name = 'Inscripciones.db'    
        self.win = tk.Tk(master)

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
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('Inscripciones')
        self.win.iconbitmap(PATH + ICONO)

        # Crea los frames
        self.frm_1 = tk.Frame(self.win, name="frm_1")
        self.frm_1.configure(background="#f7f9fd", height=600, width=800)
        self.lblNoInscripcion = ttk.Label(self.frm_1, name="lblnoinscripcion")
        self.lblNoInscripcion.configure(background="#f7f9fd",font="{Arial} 11 {bold}",
                                        justify="left",state="normal",
                                        takefocus=False,text='No.Inscripción')
         #Label No. Inscripción
        self.lblNoInscripcion.place(anchor="nw", x=680, y=20)
        #Entry No. Inscripción
        self.num_Inscripcion = ttk.Entry(self.frm_1, name="num_inscripcion")
        self.num_Inscripcion.configure(justify="right")
        self.num_Inscripcion.place(anchor="nw", width=100, x=682, y=42)
        
        #Label Fecha
        self.lblFecha = ttk.Label(self.frm_1, name="lblfecha")
        self.lblFecha.configure(background="#f7f9fd", text='Fecha:')
        self.lblFecha.place(anchor="nw", x=630, y=80)

        self.fecha = DateEntry(self.frm_1,locale = 'es_Es', date_pattern = 'dd/mm/yyyy')
        self.fecha.configure(justify="center")
        self.fecha.place(anchor="nw", width=90, x=680, y=80)
        def cuandoEscriba(event): 
            if event.char.isdigit():
                texto = self.fecha.get()
                letras = 0 #verifica el numero de digitos
                for i in texto:
                    letras +=1
                if len(self.fecha.get()) > 9: #es 9 ya que al ingresar algo nuevo, primero aplica y luego verifica
                    self.fecha.delete(9, tk.END)

                if letras == 2:
                    self.fecha.insert(2,"/")
                elif letras == 5:
                    self.fecha.insert(5,"/")
            else:
                return "break"
        def validarFecha(event):
            try:
                self.vFecha = self.fecha.get()
                #compara el formato del texto con el formato y las fechas de libreria
                self.vFecha = datetime.datetime.strptime(self.vFecha,'%d/%m/%Y') 
                print ('fecha valida')
            except ValueError:
                print ('Error: Digite una fecha valida')

        #cuando oprima una tecla cualquiera, ejecuta
        self.fecha.bind("<Key>", cuandoEscriba) 

        #evita que valide el borrar como digito
        self.fecha.bind("<BackSpace>", lambda _:self.fecha.delete(tk.END)) 
        self.fecha.bind("<Return>", validarFecha)
        self.fecha.bind("<Tab>", validarFecha)

        #Label Alumno
        self.lblIdAlumno = ttk.Label(self.frm_1, name="lblidalumno")
        self.lblIdAlumno.configure(background="#f7f9fd", text='Id Alumno:')
        self.lblIdAlumno.place(anchor="nw", x=20, y=80)
        #Combobox Alumno
        self.cmbx_Id_Alumno = ttk.Combobox(self.frm_1, name="cmbx_id_alumno")
        self.cmbx_Id_Alumno.place(anchor="nw", width=112, x=100, y=80)
        #Label Alumno
        self.lblNombres = ttk.Label(self.frm_1, name="lblnombres")
        self.lblNombres.configure(text='Nombre(s):')
        self.lblNombres.place(anchor="nw", x=20, y=130)
        #Entry Alumno
        self.nombres = ttk.Entry(self.frm_1, name="nombres")
        self.nombres.place(anchor="nw", width=200, x=100, y=130)
        #Label Apellidos
        self.lblApellidos = ttk.Label(self.frm_1, name="lblapellidos")
        self.lblApellidos.configure(text='Apellido(s):')
        self.lblApellidos.place(anchor="nw", x=400, y=130)
        #Entry Apellidos
        self.apellidos = ttk.Entry(self.frm_1, name="apellidos")
        self.apellidos.place(anchor="nw", width=200, x=485, y=130)
        #Label Curso
        self.lblIdCurso = ttk.Label(self.frm_1, name="lblidcurso")
        self.lblIdCurso.configure(background="#f7f9fd",state="normal",text='Id Curso:')
        self.lblIdCurso.place(anchor="nw", x=20, y=185)
        #Entry Curso
        self.id_Curso = ttk.Entry(self.frm_1, name="id_curso")
        self.id_Curso.configure(justify="left", width=166)
        self.id_Curso.place(anchor="nw", width=166, x=100, y=185)
        #Label Descripción del Curso
        self.lblDscCurso = ttk.Label(self.frm_1, name="lbldsccurso")
        self.lblDscCurso.configure(background="#f7f9fd",state="normal",text='Curso:')
        self.lblDscCurso.place(anchor="nw", x=275, y=185)
        #Entry de Descripción del Curso 
        self.descripc_Curso = ttk.Entry(self.frm_1, name="descripc_curso")
        self.descripc_Curso.configure(justify="left", width=166)
        self.descripc_Curso.place(anchor="nw", width=300, x=325, y=185)
        #Label Horario
        self.lblHorario = ttk.Label(self.frm_1, name="label3")
        self.lblHorario.configure(background="#f7f9fd",state="normal",text='Hora:')
        self.lblHorario.place(anchor="nw", x=635, y=185)
        #Entry del Horario
        self.horario = ttk.Combobox(self.frm_1, name="entry6")
        self.horas = ("7:00am-9:00am","9:00am-11:00am","11:00am-12:00pm","2:00pm-4:00pm","4:00pm-6:00pm","6:00pm-8:00pm")
        self.cmbx_horario = ttk.Combobox(self.frm_1, name="cmbx_horas", values=self.horas)
        self.cmbx_horario.place(anchor="nw", width=120, x=670, y=185)

        ''' Botones  de la Aplicación'''
        #Botón Guardar
        self.btnConsultar = ttk.Button(self.frm_1, name="btnconsultar", cursor="hand2")
        self.btnConsultar.configure(text='Consultar')
        self.btnConsultar.place(anchor="nw", x=150, y=260, width=80)
        
        #Botón Editar
        self.btnEditar = ttk.Button(self.frm_1, name="btneditar", cursor="hand2")
        self.btnEditar.configure(text='Editar')
        self.btnEditar.place(anchor="nw", x=255, y=260,  width=80)
        #Botón Eliminar
        self.btnEliminar = ttk.Button(self.frm_1, name="btneliminar", cursor="hand2")
        self.btnEliminar.configure(text='Eliminar')
        self.btnEliminar.place(anchor="nw", x=360, y=260, width=80)
        #Botón Cancelar
        self.btnCancelar = ttk.Button(self.frm_1, name="btncancelar", cursor="hand2")
        self.btnCancelar.configure(text='Cancelar')
        self.btnCancelar.place(anchor="nw", x=465, y=260, width=80)
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
        self.tView_cols = ['Codigo', 'Curso_descripcion','tV_descripción', 'Horario' ]
        self.tView.bind("<Button-1>", cancel, add="+")
        self.tView.configure(columns=self.tView_cols)
        self.tView.column("#0", width=0)
        self.tView.column("Codigo",anchor="w",stretch=False,width=181)
        self.tView.column("Curso_descripcion",anchor="w",stretch=False,width=181)
        self.tView.column("tV_descripción",anchor="w",stretch=False,width=181)
        self.tView.column("Horario",anchor="w",stretch=False,width=181)
        #Cabeceras
        self.tView.heading("Codigo",anchor="w", text='Código')
        self.tView.heading("Curso_descripcion",anchor="w", text='Curso')
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

        # Main widget
        self.mainwindow = self.win

    def run(self):
        self.mainwindow.mainloop()


    ''' A partir de este punto se deben incluir las funciones
     para el manejo de la base de datos '''
    
# conn = sqlite3.connect('db\\Inscripciones.db')

# cursor = conn.cursor()

# cursor.execute('''CREATE TABLE IF NOT EXISTS  Inscritos(
#         No_Inscritos INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#         Id_Alumno VARCHAR(20) NOT NULL,
#         Fecha_de_Inscripción DATE NOT NULL,
#         Código_Curso VARCHAR(20),
#         FOREIGN KEY (Código_Curso) REFERENCES Cursos(Código_Curso),
#         FOREIGN KEY (Id_Alumno) REFERENCES Alumnos(Id_Alumno)
        
#     )''')

# cursor.execute('''CREATE TABLE IF NOT EXISTS  Cursos(
#         Código_Curso VARCHAR(20) NOT NULL PRIMARY KEY,
#         Descripción_Curso VARCHAR(60),
#         Num_Horas SMALLINT(2)
#     )''')

# cursor.execute('''CREATE TABLE IF NOT EXISTS  Carreras(
#         Código_Carrera VARCHAR(15) PRIMARY KEY NOT NULL,
#         Descripción VARCHAR(100),
#         Num_Semestres SMALLINT(2)
#     )''')

# cursor.execute('''CREATE TABLE IF NOT EXISTS  [Alumnos](
#         [Id_Alumno] VARCHAR(20) NOT NULL PRIMARY KEY,
#         Id_Carrera VARCHAR(15) NOT NULL,
#         Nombres VARCHAR(50),
#         Apellidos VARCHAR(50),
#         Fecha_Ingreso DATE,
#         Dirección VARCHAR(60),
#         Telef_Cel VARCHAR (18),
#         Telef_Fijo VARCHAR (15),
#         Ciudad VARCHAR(60),
#         Departamento VARCHAR(60),
#         FOREIGN KEY (Id_Carrera) REFERENCES Carreras (Código_Carrera)
#     )''')

# # cursor.execute('''INSERT INTO Carreras(Código_Carrera, Descripción, Num_Semestres) VALUES('ISyC_2789', 'Ingeniería de Sistemas y Computación', 10)
# #                   ''')
# # cursor.execute('''INSERT INTO Alumnos(Id_Alumno, Id_Carrera, Nombres, Apellidos, Fecha_Ingreso, Dirección, Telef_Cel, Telef_Fijo, Ciudad, Departamento) VALUES('2019-001', 'ISyC_2789', 'Juan', 'Pérez', '2019-01-15', 'Calle 1 # 2-3', '300-1234567', '300-1234567', 'Bogotá', 'Cundinamarca')
# #                    ''')
# # cursor.execute('''INSERT INTO Cursos(Código_Curso, Descripción_Curso, Num_Horas) VALUES('PYT-001', 'Python Básico', 40)
# #                    ''')
# # cursor.execute('''INSERT INTO Inscritos(Id_Alumno, Fecha_de_Inscripción, Código_Curso) VALUES('2019-001', '2020-01-15', 'PYT-001')
# #                    ''')

# cursos =[
#         ('2015734', 'Programación de Computadores', 'Lun,Mie 11:00am - 1:00pm'),
#         ('2015711','Dibujo Básico', 'Mie, Vie 11:00am - 1:00pm'),
#         ('2016375', 'Programación Orientada a Objetos', 'Mar,Jue 2:00pm - 4:00pm'),
#         ('2016509', 'Taller de Electrónica', 'Mie,Vie 2:00pm - 4:00pm'),
#         ('2016703', 'Pensamiento Sistémico', 'Mar, Jue 11:00am - 1:00pm'),
#         ('2017228', 'Tecnología Mecánica Básica', 'Mar, Jue 7:00am - 9:00am'),
#         ('1000004', 'Cálculo Diferencial', 'Lun,Mie 7:00am - 9:00am'),
#         ('1000005', 'Cálculo Integral','Lun,Mie 9:00am - 11:00am'),
#         ('1000006', 'Cálculo en Varia Variables', 'Mie,Vie 11:00am - 1:00pm'),
#         ('1000003', 'Algebra Lineal', 'Lun,Mier 2:00pm - 4:00pm'),
#         ('1000017', 'Fundamentos de Electromagnetismo', 'Lun, Mie 4:00pm - 6:00pm'),
#         ('1000019', 'Fundamentos de Mecánica', 'Mar,Mier,Jue 7:00am - 9:00am'),
#         ('1000025', 'Laboratorio de Técnicas Básicas en Química', 'Mie,Vie 7:00am - 9:00am'),
#         ('1000026','Principio de Análisis Químico', 'Lun,Mar 4:00pm - 6:00pm')
#     ]
# # cursor.executemany("INSERT INTO Cursos(Código_Curso, Descripción_Curso, Num_Horas) VALUES(?,?,?)", cursos)

# estudiantes = [
#         ('8876295089', '2789', 'Juan', 'Pérez', '2019-01-15', 'Calle 1 # 2-3', '300-1234567', '300-1234567', 'Bogotá', 'Cundinamarca'),
#         ('5269436393', '2789', 'Juan Camilo', 'Pérez Soza', '2024-11-15', 'Calle 65 # 20-3', '300-1234567', '300-1234', 'Bogotá', 'Cundinamarca'),
#         ('8114559050', '2789', 'Pedro Pedro', 'Torres Castillo', '2024-03-16', 'Calle 72B # 23-30', '300-1234567', '300-1234', 'Bogotá', 'Cundinamarca'),
#         ('7270566584', '2789', 'María Camila', 'González López', '2024-04-27', 'Calle 10 # 5-6', '310-9876543', '310-9876', 'Medellín', 'Antioquia'),
#         ('7894756003', '2544', 'Andrés David', 'Martínez Rodríguez', '2024-04-28', 'Carrera 20 # 15-30', '320-7654321', '320-7654', 'Cali', 'Valle del Cauca'),
#         ('8562305458', '2544', 'Laura Camila', 'Ramírez Pérez', '2024-04-29', 'Avenida 5 # 8-12', '315-5432109', '315-5432', 'Barranquilla', 'Atlántico'),
#         ('6045534334', '2544', 'Carlos Felipe', 'López Gómez', '2024-04-30', 'Calle 7 # 12-15', '317-8765432', '317-8765', 'Bogotá', 'Cundinamarca'),
#         ('2764144293', '2544', 'Ana Maria', 'Hernández Martínez', '2024-05-01', 'Carrera 15 # 25-18', '314-6543210', '314-6543', 'Medellín', 'Antioquia'),
#         ('7511200463', '2544', 'Diego Alejandro', 'García Ramírez', '2024-05-02', 'Avenida 8 # 10-5', '312-9876543', '312-9876', 'Cali', 'Valle del Cauca'),
#         ('9030779197', '2545', 'Sara Sofía', 'Pérez Martínez', '2024-05-03', 'Calle 12 # 20-7', '319-7654321', '319-7654', 'Barranquilla', 'Atlántico'),
#         ('8605132377', '2545', 'Javier', 'López Ramírez', '2024-05-04', 'Carrera 18 # 22-10', '316-5433433', '320-5421', 'Valledupar', 'Cesar'),
#         ('2550301257', '2545', 'Carla Valentina', 'Sánchez Pérez', '2024-05-05', 'Avenida 3 # 6-9', '313-8765432', '313-8765', 'Bogotá', 'Cundinamarca'),
#         ('9997493368', '2545', 'Gabriel', 'Gómez Ramírez', '2024-05-06', 'Calle 5 # 8-11', '311-6543210', '311-6543', 'Medellín', 'Antioquia'),
#         ('6514506224', '2546', 'Isabella', 'Martínez López', '2024-05-07', 'Carrera 12 # 18-25', '319-7654321', '319-7654', 'Cali', 'Valle del Cauca'),
#         ('6223175366', '2546', 'Mateo', 'Hernández Ramírez', '2024-05-08', 'Avenida 7 # 10-14', '316-5432109', '316-5432', 'Barranquilla', 'Atlántico'),
#         ('8221071329', '2546', 'Carlos Valentín', 'López Martínez', '2024-05-09', 'Calle 15 # 22-17', '314-9876543', '314-9876', 'Bogotá', 'Cundinamarca'),
#         ('8782642282', '2548', 'Camila', 'García Ramírez', '2024-05-10', 'Carrera 25 # 30-22', '317-7654321', '317-7654', 'Medellín', 'Antioquia'),
#         ('5301173864', '2548', 'Lucas Alejandro', 'Pérez Martínez', '2024-05-11', 'Avenida 10 # 12-19', '312-8765432', '312-8765', 'Cali', 'Valle del Cauca'),
#         ('1008146001', '2548', 'Valentino', 'Ramírez Gómez', '2024-05-12', 'Calle 18 # 22-14', '318-7654321', '318-7654', 'Barranquilla', 'Atlántico'),
#         ('2778948484', '2549', 'Isabel Maria', 'López Martínez', '2024-05-13', 'Avenida 12 # 15-20', '314-9876543', '314-9876', 'Bogotá', 'Cundinamarca'),
#         ('9557617951', '2549', 'Sara Lucía', 'García Ramírez', '2024-05-14', 'Carrera 22 # 30-18', '317-7654321', '317-7654', 'Medellín', 'Antioquia'),
#         ('1322078372', '2549', 'Damian Matías', 'Pérez Martínez', '2024-05-15', 'Avenida 15 # 18-22', '312-8765432', '312-8765', 'Cali', 'Valle del Cauca'),
#         ('5547157920', '2549', 'Valeria', 'Hernández Ramírez', '2024-05-16', 'Calle 20 # 25-19', '319-6543210', '319-6543', 'Barranquilla', 'Atlántico')
#     ]

# # cursor.executemany("INSERT INTO Alumnos(Id_Alumno, Id_Carrera, Nombres, Apellidos, Fecha_Ingreso, Dirección, Telef_Cel, Telef_Fijo, Ciudad, Departamento) VALUES(?,?,?,?,?,?,?,?,?,?)", estudiantes)

# carreras = [
#         ('2544','Ingeniería Eléctrica','10'),
#         ('2545','Ingeniería Electrónica','10'),
#         ('2546','Ingeniería Industrial','10'),
#         ('2548','Ingeniería Mecatrónica','10'),
#         ('2549','Ingeniería Química','10'),
#         ('2879','Ingeniería de Sistemas','10')
# ]

# # cursor.executemany("INSERT INTO Carreras(Código_Carrera, Descripción, Num_Semestres) VALUES(?,?,?)", carreras)

#     # cursor.execute("DELETE FROM Carreras")

# def Inscribir_Curso():
#         cursos = []
#         entrada_1 = input("Ingrese los datos del curso en una sola linea separado por el símbolo #:     ").split("#")
#         datos = tuple(entrada_1)
#         print(datos)
#         cursor.execute("INSERT INTO Cursos(Código_Curso, Descripción_Curso, Num_Horas) VALUES (?,?,?)", datos)
        
        
#     #Inscribir_Curso()

# def Obtener_Datos():
#         opcion = input("Ingrese los datos de la tabla que desea recuperar:  ")
#         cursor.execute(f" SELECT * FROM {opcion}")
#         datos = cursor.fetchall()
#         for i in datos:
#             print(i)

#     #Obtener_Datos()

# def Obtener_Un_Dato():
#         opción = input("Ingrese dato(s) que desea recuperar de la siguiente manera (Tabla&Columna&Valor):  ").split("&")
#         # print(opción)
#         cursor.execute(f" SELECT * FROM {opción[0]} WHERE {opción[1]} = '{opción[2]}' ")
#         # cursor.execute(f" SELECT * FROM {opción[0]} WHERE Código_Curso = '{opción[1]}' ")
#         # cursor.execute("SELECT * FROM Cursos WHERE Código_Curso = 'PYT-015' ")
#         datos = cursor.fetchall()
#         for i in datos:
#             print(i)
        
#     #Obtener_Un_Dato()

# def Eliminar_Un_Dato():
#         opcion = input("Ingrese dato que desea eliminar de la siguiente manera (Tabla&Columna&Valor):   ").split("&")
#         cursor.execute(f"DELETE FROM {opcion[0]} WHERE {opcion[1]} = '{opcion[2]}' ")
#         print("El dato ha sido eliminado")

#     #Eliminar_Un_Dato()

# def Obtener_Info_Estudiante():
#         info = []
#         opcion = input("Ingrese el número de registro al que desea conocer la respectiva información")
#         cursor.execute(f"SELECT * FROM Inscritos WHERE No_Inscritos = '{opcion}' ")
#         datos = cursor.fetchall()
#         info.append(datos[0])
#         acciones = [f"SELECT * FROM Alumnos WHERE Id_Alumno = '{datos[0][1]}' ",
#                     f"SELECT * FROM Cursos WHERE Código_Curso = '{datos[0][3]}' "
#         ]
#         for i in acciones:
#             cursor.execute(i)
#             datos_1 = cursor.fetchall()
#             info.append(datos_1[0])
#         cursor.execute(f"SELECT * FROM Carreras WHERE Código_Carrera = '{info[1][1]}' ")
#         datos_2 = cursor.fetchall()
#         info.append(datos_2[0])
#         for i in info:
#             print(i)
#             # for u in i:
#             #     print(u)
#         print(info)

#     #Obtener_Info_Estudiante()

# conn.commit()

# conn.close() 
    conn=sqlite3.connect('db\\Inscripciones.db')
    cursor =conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS  Inscritos(
        No_Inscritos INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        Id_Alumno VARCHAR(20) NOT NULL,
        Fecha_de_Inscripción DATE NOT NULL,
        Código_Curso VARCHAR(20),
        FOREIGN KEY (Código_Curso) REFERENCES Cursos(Código_Curso),
        FOREIGN KEY (Id_Alumno) REFERENCES Alumnos(Id_Alumno)
        
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS  Cursos(
        Código_Curso VARCHAR(20) NOT NULL PRIMARY KEY,
        Descripción_Curso VARCHAR(60),
        Num_Horas SMALLINT(2)
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS  Carreras(
        Código_Carrera VARCHAR(15) PRIMARY KEY NOT NULL,
        Descripción VARCHAR(100),
        Num_Semestres SMALLINT(2)
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS  [Alumnos](
        [Id_Alumno] VARCHAR(20) NOT NULL PRIMARY KEY,
        Id_Carrera VARCHAR(15) NOT NULL,
        Nombres VARCHAR(50),
        Apellidos VARCHAR(50),
        Fecha_Ingreso DATE,
        Dirección VARCHAR(60),
        Telef_Cel VARCHAR (18),
        Telef_Fijo VARCHAR (15),
        Ciudad VARCHAR(60),
        Departamento VARCHAR(60),
        FOREIGN KEY (Id_Carrera) REFERENCES Carreras (Código_Carrera)
    )''')
    conn.commit()
    conn.close()

if __name__ == "__main__":
    app = Inscripciones_2()
    app.run()
