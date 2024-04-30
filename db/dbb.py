import sqlite3

#No ejecutar aun

conn = sqlite3.connect('Inscripciones.db')

cursor = conn.cursor()

# cursor.execute('''CREATE TABLE IF NOT EXISTS  Inscritos(
#     No_Inscritos INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#     Id_Alumno VARCHAR(20) NOT NULL,
#     Fecha_de_Inscripción DATE NOT NULL,
#     Código_Curso VARCHAR(20),
#     FOREIGN KEY (Código_Curso) REFERENCES Cursos(Código_Curso),
#     FOREIGN KEY (Id_Alumno) REFERENCES Alumnos(Id_Alumno)
    
# )''')

# cursor.execute('''CREATE TABLE IF NOT EXISTS  Cursos(
#     Código_Curso VARCHAR(20) NOT NULL PRIMARY KEY,
#     Descripción_Curso VARCHAR(60),
#     Num_Horas SMALLINT(2)
# )''')

# cursor.execute('''CREATE TABLE IF NOT EXISTS  Carreras(
#     Código_Carrera VARCHAR(15) PRIMARY KEY NOT NULL,
#     Descripción VARCHAR(100),
#     Num_Semestres SMALLINT(2)
# )''')

# cursor.execute('''CREATE TABLE IF NOT EXISTS  [Alumnos](
#     [Id_Alumno] VARCHAR(20) NOT NULL PRIMARY KEY,
#     Id_Carrera VARCHAR(15) NOT NULL,
#     Nombres VARCHAR(50),
#     Apellidos VARCHAR(50),
#     Fecha_Ingreso DATE,
#     Dirección VARCHAR(60),
#     Telef_Cel VARCHAR (18),
#     Telef_Fijo VARCHAR (15),
#     Ciudad VARCHAR(60),
#     Departamento VARCHAR(60),
#     FOREIGN KEY (Id_Carrera) REFERENCES Carreras (Código_Carrera)
# )''')

# cursor.execute('''INSERT INTO Carreras(Código_Carrera, Descripción, Num_Semestres) VALUES('ISyC_2789', 'Ingeniería de Sistemas y Computación', 10)
#               ''')
# cursor.execute('''INSERT INTO Alumnos(Id_Alumno, Id_Carrera, Nombres, Apellidos, Fecha_Ingreso, Dirección, Telef_Cel, Telef_Fijo, Ciudad, Departamento) VALUES('2019-001', 'ISyC_2789', 'Juan', 'Pérez', '2019-01-15', 'Calle 1 # 2-3', '300-1234567', '300-1234567', 'Bogotá', 'Cundinamarca')
#                ''')
# cursor.execute('''INSERT INTO Cursos(Código_Curso, Descripción_Curso, Num_Horas) VALUES('PYT-001', 'Python Básico', 40)
#                ''')
# cursor.execute('''INSERT INTO Inscritos(Id_Alumno, Fecha_de_Inscripción, Código_Curso) VALUES('2019-001', '2020-01-15', 'PYT-001')
#                ''')

# cursos =[
#     ('2015734', 'Programación de Computadores', 'Lun,Mie 11:00am - 1:00pm'),
#     ('2015711','Dibujo Básico', 'Mie, Vie 11:00am - 1:00pm'),
#     ('2016375', 'Programación Orientada a Objetos', 'Mar,Jue 2:00pm - 4:00pm'),
#     ('2016509', 'Taller de Electrónica', 'Mie,Vie 2:00pm - 4:00pm'),
#     ('2016703', 'Pensamiento Sistémico', 'Mar, Jue 11:00am - 1:00pm'),
#     ('2017228', 'Tecnología Mecánica Básica', 'Mar, Jue 7:00am - 9:00am'),
#     ('1000004', 'Cálculo Diferencial', 'Lun,Mie 7:00am - 9:00am'),
#     ('1000005', 'Cálculo Integral','Lun,Mie 9:00am - 11:00am'),
#     ('1000006', 'Cálculo en Varia Variables', 'Mie,Vie 11:00am - 1:00pm'),
#     ('1000003', 'Algebra Lineal', 'Lun,Mier 2:00pm - 4:00pm'),
#     ('1000017', 'Fundamentos de Electromagnetismo', 'Lun, Mie 4:00pm - 6:00pm'),
#     ('1000019', 'Fundamentos de Mecánica', 'Mar,Mier,Jue 7:00am - 9:00am'),
#     ('1000025', 'Laboratorio de Técnicas Básicas en Química', 'Mie,Vie 7:00am - 9:00am'),
#     ('1000026','Principio de Análisis Químico', 'Lun,Mar 4:00pm - 6:00pm')
# ]

# cursor.executemany("INSERT INTO Cursos(Código_Curso, Descripción_Curso, Num_Horas) VALUES(?,?,?)", cursos)

# estudiantes = [
#     ('8876295089', '2789', 'Juan', 'Pérez', '2019-01-15', 'Calle 1 # 2-3', '300-1234567', '300-1234567', 'Bogotá', 'Cundinamarca'),
#     ('5269436393', '2789', 'Juan Camilo', 'Pérez Soza', '2024-11-15', 'Calle 65 # 20-3', '300-1234567', '300-1234', 'Bogotá', 'Cundinamarca'),
#     ('8114559050', '2789', 'Pedro Pedro', 'Torres Castillo', '2024-03-16', 'Calle 72B # 23-30', '300-1234567', '300-1234', 'Bogotá', 'Cundinamarca'),
#     ('7270566584', '2789', 'María Camila', 'González López', '2024-04-27', 'Calle 10 # 5-6', '310-9876543', '310-9876', 'Medellín', 'Antioquia'),
#     ('7894756003', '2544', 'Andrés David', 'Martínez Rodríguez', '2024-04-28', 'Carrera 20 # 15-30', '320-7654321', '320-7654', 'Cali', 'Valle del Cauca'),
#     ('8562305458', '2544', 'Laura Camila', 'Ramírez Pérez', '2024-04-29', 'Avenida 5 # 8-12', '315-5432109', '315-5432', 'Barranquilla', 'Atlántico'),
#     ('6045534334', '2544', 'Carlos Felipe', 'López Gómez', '2024-04-30', 'Calle 7 # 12-15', '317-8765432', '317-8765', 'Bogotá', 'Cundinamarca'),
#     ('2764144293', '2544', 'Ana Maria', 'Hernández Martínez', '2024-05-01', 'Carrera 15 # 25-18', '314-6543210', '314-6543', 'Medellín', 'Antioquia'),
#     ('7511200463', '2544', 'Diego Alejandro', 'García Ramírez', '2024-05-02', 'Avenida 8 # 10-5', '312-9876543', '312-9876', 'Cali', 'Valle del Cauca'),
#     ('9030779197', '2545', 'Sara Sofía', 'Pérez Martínez', '2024-05-03', 'Calle 12 # 20-7', '319-7654321', '319-7654', 'Barranquilla', 'Atlántico'),
#     ('8605132377', '2545', 'Javier', 'López Ramírez', '2024-05-04', 'Carrera 18 # 22-10', '316-5433433', '320-5421', 'Valledupar', 'Cesar'),
#     ('2550301257', '2545', 'Carla Valentina', 'Sánchez Pérez', '2024-05-05', 'Avenida 3 # 6-9', '313-8765432', '313-8765', 'Bogotá', 'Cundinamarca'),
#     ('9997493368', '2545', 'Gabriel', 'Gómez Ramírez', '2024-05-06', 'Calle 5 # 8-11', '311-6543210', '311-6543', 'Medellín', 'Antioquia'),
#     ('6514506224', '2546', 'Isabella', 'Martínez López', '2024-05-07', 'Carrera 12 # 18-25', '319-7654321', '319-7654', 'Cali', 'Valle del Cauca'),
#     ('6223175366', '2546', 'Mateo', 'Hernández Ramírez', '2024-05-08', 'Avenida 7 # 10-14', '316-5432109', '316-5432', 'Barranquilla', 'Atlántico'),
#     ('8221071329', '2546', 'Carlos Valentín', 'López Martínez', '2024-05-09', 'Calle 15 # 22-17', '314-9876543', '314-9876', 'Bogotá', 'Cundinamarca'),
#     ('8782642282', '2548', 'Camila', 'García Ramírez', '2024-05-10', 'Carrera 25 # 30-22', '317-7654321', '317-7654', 'Medellín', 'Antioquia'),
#     ('5301173864', '2548', 'Lucas Alejandro', 'Pérez Martínez', '2024-05-11', 'Avenida 10 # 12-19', '312-8765432', '312-8765', 'Cali', 'Valle del Cauca'),
#     ('1008146001', '2548', 'Valentino', 'Ramírez Gómez', '2024-05-12', 'Calle 18 # 22-14', '318-7654321', '318-7654', 'Barranquilla', 'Atlántico'),
#     ('2778948484', '2549', 'Isabel Maria', 'López Martínez', '2024-05-13', 'Avenida 12 # 15-20', '314-9876543', '314-9876', 'Bogotá', 'Cundinamarca'),
#     ('9557617951', '2549', 'Sara Lucía', 'García Ramírez', '2024-05-14', 'Carrera 22 # 30-18', '317-7654321', '317-7654', 'Medellín', 'Antioquia'),
#     ('1322078372', '2549', 'Damian Matías', 'Pérez Martínez', '2024-05-15', 'Avenida 15 # 18-22', '312-8765432', '312-8765', 'Cali', 'Valle del Cauca'),
#     ('5547157920', '2549', 'Valeria', 'Hernández Ramírez', '2024-05-16', 'Calle 20 # 25-19', '319-6543210', '319-6543', 'Barranquilla', 'Atlántico')
# ]

# cursor.executemany("INSERT INTO Alumnos(Id_Alumno, Id_Carrera, Nombres, Apellidos, Fecha_Ingreso, Dirección, Telef_Cel, Telef_Fijo, Ciudad, Departamento) VALUES(?,?,?,?,?,?,?,?,?,?)", estudiantes)

carreras = [
    ('2544','Ingeniería Eléctrica','10'),
    ('2545','Ingeniería Electrónica','10'),
    ('2546','Ingeniería Industrial','10'),
    ('2548','Ingeniería Mecatrónica','10'),
    ('2549','Ingeniería Química','10'),
    ('2879','Ingeniería de Sistemas','10')
]

cursor.executemany("INSERT INTO Carreras(Código_Carrera, Descripción, Num_Semestres) VALUES(?,?,?)", carreras)

# cursor.execute("DELETE FROM Carreras")

def Inscribir_Curso():
    cursos = []
    entrada_1 = input("Ingrese los datos del curso en una sola linea separado por el símbolo #:     ").split("#")
    datos = tuple(entrada_1)
    print(datos)
    cursor.execute("INSERT INTO Cursos(Código_Curso, Descripción_Curso, Num_Horas) VALUES (?,?,?)", datos)
    
    
#Inscribir_Curso()

def Obtener_Datos():
    opcion = input("Ingrese los datos de la tabla que desea recuperar:  ")
    cursor.execute(f" SELECT * FROM {opcion}")
    datos = cursor.fetchall()
    for i in datos:
        print(i)

#Obtener_Datos()

def Obtener_Un_Dato():
    opción = input("Ingrese dato(s) que desea recuperar de la siguiente manera (Tabla&Columna&Valor):  ").split("&")
    # print(opción)
    cursor.execute(f" SELECT * FROM {opción[0]} WHERE {opción[1]} = '{opción[2]}' ")
    # cursor.execute(f" SELECT * FROM {opción[0]} WHERE Código_Curso = '{opción[1]}' ")
    # cursor.execute("SELECT * FROM Cursos WHERE Código_Curso = 'PYT-015' ")
    datos = cursor.fetchall()
    for i in datos:
        print(i)
    
#Obtener_Un_Dato()

def Eliminar_Un_Dato():
    opcion = input("Ingrese dato que desea eliminar de la siguiente manera (Tabla&Columna&Valor):   ").split("&")
    cursor.execute(f"DELETE FROM {opcion[0]} WHERE {opcion[1]} = '{opcion[2]}' ")
    print("El dato ha sido eliminado")

#Eliminar_Un_Dato()

def Obtener_Info_Estudiante():
    info = []
    opcion = input("Ingrese el número de registro al que desea conocer la respectiva información")
    cursor.execute(f"SELECT * FROM Inscritos WHERE No_Inscritos = '{opcion}' ")
    datos = cursor.fetchall()
    info.append(datos[0])
    acciones = [f"SELECT * FROM Alumnos WHERE Id_Alumno = '{datos[0][1]}' ",
                f"SELECT * FROM Cursos WHERE Código_Curso = '{datos[0][3]}' "
    ]
    for i in acciones:
        cursor.execute(i)
        datos_1 = cursor.fetchall()
        info.append(datos_1[0])
    cursor.execute(f"SELECT * FROM Carreras WHERE Código_Carrera = '{info[1][1]}' ")
    datos_2 = cursor.fetchall()
    info.append(datos_2[0])
    for i in info:
        print(i)
        # for u in i:
        #     print(u)
    print(info)

#Obtener_Info_Estudiante()

conn.commit()

conn.close() 

print('Base de Datos creada con éxito')