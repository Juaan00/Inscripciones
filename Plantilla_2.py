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
        self.lblNoInscripcion.configure(background="#f7f9fd", text='No.Inscripción:')
        self.lblNoInscripcion.place(anchor="nw", x=20, y=185)
        #Conmbox No. Inscripción
        self.noInscripcion = ttk.Entry(self.frm_1, name="noInscripcion", state="readonly")
        self.noInscripcion.place(anchor="nw", width=100, x=120, y=185)
        #Label Codigo del Curso
        self.lblDscCurso = ttk.Label(self.frm_1, name="lbldsccurso")
        self.lblDscCurso.configure(background="#f7f9fd", state='readonly',text='Codigo del Curso:')
        self.lblDscCurso.place(anchor="nw", x=240, y=185)
        #Entry Codigo del Curso 
        self.descripc_Curso = ttk.Combobox(self.frm_1, name="descripc_curso", state='disabled')
        self.descripc_Curso.configure(justify="left", width=166)
        self.descripc_Curso.place(anchor="nw", width=300, x=350, y=185)

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

        ''' Botones  de la Aplicación'''
        @staticmethod
        def activar_boton_grabar():
            self.btnGrabar.config(state="normal")
        #Botón Consultar

        def consultar():
            self.btnConsultar.config(state="disabled")
            valor=self.cmbx_Id_Alumno.get()
            if valor== '':
                messagebox.showerror("Inscripciones", "Para Consultar Debe seleccionar un id Alumno primero")
                return
            else:
                self.cmbx_Id_Alumno.config(state="disabled")
                self.lista_alumnos=self.get_data_complete()
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
                if inscripciones==None:
                    pass
                else:
                    insert_data(inscripciones)
                

        self.btnConsultar = ttk.Button(self.frm_1, name="btnconsultar", cursor="hand2", command=consultar)
        self.btnConsultar.configure(text='Consultar')
        self.btnConsultar.place(anchor="nw", x=150, y=260, width=80)


        #Botón Editar

        def editar_validacion():
            self.run_sqlite()
            print(self.nombres.cget('state'))
            if self.nombres.get() == '':
                    messagebox.showerror("Inscripciones", "Para Editar Debe CONSULTAR un id Alumno primero")
                    return
            elif self.nombres.cget('state') == 'disabled':
                    self.nombres.config(state="normal")
                    self.apellidos.config(state="normal")
                    self.fecha.config(state="normal")
                    self.cmbx_Id_Alumno.config(state="disabled")
                    self.cmbx_Id_Carrera.config(state="normal")
                    self.ciudad.config(state="normal")
                    self.departamento.config(state="normal")
                    self.direccion.config(state="normal")
                    self.telCel.config(state="normal")
                    self.telFijo.config(state="normal")
                    if self.noInscripcion.get() == '':
                        return
                    else:
                        self.descripc_Curso.config(state="readonly")
                        return
            elif self.noInscripcion.get()== '':
                    return
            elif self.descripc_Curso.get()!= '':
                    self.descripc_Curso.config(state="readonly")
                    return
        def editar():
            editar_validacion()
            self.cursor.execute("UPDATE Alumnos SET Nombres = ?, Apellidos = ?, Fecha_Ingreso = ?, Dirección = ?, Telef_Cel = ?, Telef_Fijo = ?, Ciudad = ?, Departamento = ? WHERE Id_Alumno = ?", (self.add_editar(self.nombres), self.add_editar(self.apellidos), self.add_editar(self.fecha), self.add_editar(self.direccion), self.add_editar(self.telCel), self.add_editar(self.telFijo), self.add_editar(self.ciudad), self.add_editar(self.departamento), self.cmbx_Id_Alumno.get()))
            if self.noInscripcion.get() == '':
                pass
            else:
                numero_inscripcion=self.add_editar(self.noInscripcion)
                numero_inscripcion=int(numero_inscripcion)
                id_alumno=self.cmbx_Id_Alumno.get()
                nuevo_curso=self.descripc_Curso.get()
                nuevo_curso=nuevo_curso.split('-')[0]
                cursos=self.get_data_cursos_estudiantes(nuevo_curso)
                self.lista_inscripciones=self.get_data_inscricpiones_complete(id_alumno)
                print(numero_inscripcion, id_alumno, cursos, nuevo_curso)
                for i in self.lista_inscripciones: 
                    if i[0] == numero_inscripcion:
                        self.cursor.execute("UPDATE Inscritos SET Código_Curso = ? WHERE No_Inscritos = ?", (nuevo_curso, numero_inscripcion))
            self.conn.commit()
            limpiar()

        self.btnEditar = ttk.Button(self.frm_1, name="btneditar", cursor="hand2", command=editar)
        self.btnEditar.configure(text='Editar')
        self.btnEditar.place(anchor="nw", x=255, y=260,  width=80)

        #Botón Eliminar
        self.btnEliminar = ttk.Button(self.frm_1, name="btneliminar", cursor="hand2")
        self.btnEliminar.configure(text='Eliminar')
        self.btnEliminar.place(anchor="nw", x=360, y=260, width=80)
        #Botón Cancelar

        def limpiar():
            self.run_sqlite()
            self.cmbx_Id_Alumno.config(state="enabled")
            self.cmbx_Id_Alumno.delete(0, 'end')
            self.cmbx_Id_Alumno.config(state="enabled")
            self.add_limpiar(self.cmbx_Id_Carrera)
            self.add_limpiar(self.nombres)
            self.add_limpiar(self.apellidos)
            self.add_limpiar(self.fecha)
            self.add_limpiar(self.direccion)
            self.add_limpiar(self.ciudad)
            self.add_limpiar(self.departamento)
            self.add_limpiar(self.telCel)
            self.add_limpiar(self.telFijo)
            self.add_limpiar(self.descripc_Curso)
            self.add_limpiar(self.noInscripcion)
            self.tView.delete(*self.tView.get_children())
            self.btnConsultar.config(state="enabled")

        self.btnCancelar = ttk.Button(self.frm_1, name="btncancelar", cursor="hand2", command=limpiar)
        self.btnCancelar.configure(text='Cancelar')
        self.btnCancelar.place(anchor="nw", x=465, y=260, width=80)

        self.btnCancelar.bind()
        #Botón Grabar
        #duncion para grabar
        def grabar():
            self.run_sqlite()
            pass
        

        self.btnGrabar = ttk.Button(self.frm_1, name="btngrabar", cursor="hand2", command=grabar)
        self.btnGrabar.configure(text='Grabar')
        self.btnGrabar.config(state="enabled")
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
        self.tView_cols = ['NoInscripción', 'CódigoCurso','tV_descripción', 'Horas' ]
        self.tView.bind("<B1-Motion>", cancel, add="+")
        self.tView.configure(columns=self.tView_cols)
        self.tView.column("#0", width=0)
        self.tView.column("NoInscripción",anchor="w",stretch=True,width=92)
        self.tView.column("CódigoCurso",anchor="w",stretch=True,width=120)
        self.tView.column("tV_descripción",anchor="w",stretch=True,width=240)
        self.tView.column("Horas",anchor="w",stretch=True,width=92)
        #Cabeceras
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
            self.tView.delete(*self.tView.get_children())
            for i in inscripciones:
                curso=self.get_data_cursos_estudiantes(i[3])
                for j in curso:
                    self.tView.insert("", "end", values=( i[0], j[0], j[1], j[2]))
            
                    
        #Función para seleccionar un item del Treeview
        def selected_item(event):
            selected = self.tView.focus()
            values = self.tView.item(selected, 'values')
            if values == '':
                return
            else:
                self.add_consultar(self.noInscripcion, values[0])
                curso=values[1]+'-'+values[2]    
                self.add_consultar(self.descripc_Curso, curso)

        # vincula el evento de selección a la función
        self.tView.bind('<ButtonRelease-1>', selected_item)

        # Main widget
        self.mainwindow = self.win
    def add_consultar(self,entry, value):
        entry.config(state="normal")
        entry.delete(0, 'end')
        entry.insert(0, value)
        entry.config(state="disabled")
    def add_limpiar(self, entry):
        entry.config(state="normal")
        entry.delete(0, 'end')
        entry.config(state="disabled")
    def add_editar(self, entry):
        return entry.get()
    def run(self):
        self.mainwindow.mainloop()

    ''' A partir de este punto se deben incluir las funciones
     para el manejo de la base de datos '''
 
    def run_sqlite(self):
        self.conn = sqlite3.connect('db\\Inscripciones.db')
        self.conn.execute("PRAGMA foreign_keys = 1")
        self.cursor = self.conn.cursor()
        
    def close_sqlite(self):
        self.conn.commit()
        self.conn.close()
        print('Conexión cerrada')

# Funciones para obtener datos de la base de datos

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
        return self.lista_alumnos

    def get_data_inscripciones(self, id_alumno):
        inscripciones_alumno = []
        for i in self.lista_alumnos:
            if id_alumno == i[0]:
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

    def get_data_inscricpiones_complete(self, id_alumno):
        self.cursor.execute("SELECT * FROM Inscritos WHERE Id_Alumno = ?", (id_alumno,))
        self.data = self.cursor.fetchall()
        self.lista_inscripciones = []
        for i in self.data:
            self.lista_inscripciones.append(i)
        return self.lista_inscripciones
    # def crear_inscripcion(self):
    #     for i in self.lista_alumnos:
    #         self.insertar_inscripciones(i[0], datetime.date.today(), '1000004')
    #         self.insertar_inscripciones(i[0], datetime.date.today(), '1000006')
    #         self.insertar_inscripciones(i[0], datetime.date.today(), '1000005')
    #         self.insertar_inscripciones(i[0], datetime.date.today(), '1000003')


if __name__ == "__main__":
    app = Inscripciones_2()
    app.run_sqlite()
    app.get_data_idalumno()
    app.get_data_complete()
    app.get_data_cursos()
    # app.crear_inscripcion()
    app.run()
    app.close_sqlite()
