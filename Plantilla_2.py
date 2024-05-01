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

PATH = str((Path(__file__).resolve()).parent)
ICONO = r"/img/LogoinscripcionesIco.png"
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
        #ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('Inscripciones')
        #self.win.iconbitmap(PATH + ICONO)
        #icono = ttk.PhotoImage(file= PATH + ICONO)
        #self.win.wm_iconphoto(False, icono)

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

        self.fecha = tk.Entry(self.frm_1, name="fechas")
        self.fecha.configure(justify="center")
        self.fecha.place(anchor="nw", width=90, x=680, y=80)
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

        #Label Alumno
        self.lblIdAlumno = ttk.Label(self.frm_1, name="lblidalumno")
        self.lblIdAlumno.configure(background="#f7f9fd", text='Id Alumno:')
        self.lblIdAlumno.place(anchor="nw", x=20, y=80)
        #Combobox Alumno
        self.cmbx_Id_Alumno = ttk.Combobox(self.frm_1, name="cmbx_id_alumno")
        self.cmbx_Id_Alumno.place(anchor="nw", width=112, x=100, y=80)
        #Label Alumno
        self.lblNombres = ttk.Label(self.frm_1, name="lblnombres")
        self.lblNombres.configure(background="#f7f9fd",text='Nombre(s):')
        self.lblNombres.place(anchor="nw", x=20, y=130)
        #Entry Alumno
        self.nombres = ttk.Entry(self.frm_1, name="nombres", state='readonly')
        self.nombres.place(anchor="nw", width=200, x=100, y=130)
        #Label Apellidos
        self.lblApellidos = ttk.Label(self.frm_1, name="lblapellidos")
        self.lblApellidos.configure(background="#f7f9fd", text='Apellido(s):')
        self.lblApellidos.place(anchor="nw", x=400, y=130)
        #Entry Apellidos
        self.apellidos = ttk.Entry(self.frm_1, name="apellidos")
        self.apellidos.place(anchor="nw", width=200, x=485, y=130)
        self.apellidos.insert(0,"apellisodss")
        self.apellidos.config(state='readonly')
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
        self.descripc_Curso = ttk.Entry(self.frm_1, name="descripc_curso", state='readonly')
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

        def limpiar():
            self.num_Inscripcion.delete(0,tk.END)
            self.fecha.delete(0, tk.END)
            self.cmbx_Id_Alumno.delete(0,tk.END)
            self.id_Curso.delete(0,tk.END)
            self.cmbx_horario.delete(0,tk.END)

            # al estar ReadOnly 
            self.nombres.config(state="Normal")
            self.nombres.delete(0,tk.END)
            self.nombres.config(state='readonly')
            
            self.apellidos.config(state='normal')
            self.apellidos.delete(0,tk.END)
            self.apellidos.config(state='readonly')

            self.descripc_Curso.config(state="Normal")
            self.descripc_Curso.delete(0,tk.END)
            self.descripc_Curso.config(state='readonly')

        self.btnCancelar = ttk.Button(self.frm_1, name="btncancelar", command= limpiar, cursor="hand2")
        self.btnCancelar.configure(text='Cancelar')
        self.btnCancelar.place(anchor="nw", x=465, y=260, width=80)

        self.btnCancelar.bind()
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

if __name__ == "__main__":
    app = Inscripciones_2()
    app.run()
