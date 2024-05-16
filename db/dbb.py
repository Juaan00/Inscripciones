import sqlite3

#No ejecutar aun

conn = sqlite3.connect('db/Inscripciones.db')

conn.execute("PRAGMA foreign_keys = 1")

cursor = conn.cursor()


# cursor.execute('''CREATE TABLE IF NOT EXISTS  Inscritos(
#     No_Inscripción INTEGER NOT NULL,
#     Id_Alumno VARCHAR (20) NOT NULL,
#     Fecha_de_Inscripción DATE NOT NULL,
#     Código_Curso VARCHAR(20) NOT NULL,
#     Horario_Curso VARCHAR(60),
#     PRIMARY KEY (No_Inscripción, Id_Alumno, Código_Curso),
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
#     Id_Alumno VARCHAR(20) NOT NULL PRIMARY KEY,
#     Id_Carrera VARCHAR(15) NOT NULL,
#     Nombres VARCHAR(50),
#     Apellidos VARCHAR(50),
#     Fecha_Ingreso DATE NOT NULL,
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
#     ('2015734', 'Programación de Computadores', 'Lun,Mie 11:00am - 1:00pm',40),
#     ('2015711','Dibujo Básico', 'Mie, Vie 11:00am - 1:00pm',30),
#     ('2016375', 'Programación Orientada a Objetos', 'Mar,Jue 2:00pm - 4:00pm',20),
#     ('2016509', 'Taller de Electrónica', 'Mie,Vie 2:00pm - 4:00pm',40),
#     ('2016703', 'Pensamiento Sistémico', 'Mar, Jue 11:00am - 1:00pm',30),
#     ('2017228', 'Tecnología Mecánica Básica', 'Mar, Jue 7:00am - 9:00am',20),
#     ('1000004', 'Cálculo Diferencial', 'Lun,Mie 7:00am - 9:00am',40),
#     ('1000005', 'Cálculo Integral','Lun,Mie 9:00am - 11:00am',30),
#     ('1000006', 'Cálculo en Varia Variables', 'Mie,Vie 11:00am - 1:00pm',20),
#     ('1000003', 'Algebra Lineal', 'Lun,Mier 2:00pm - 4:00pm',40),
#     ('1000017', 'Fundamentos de Electromagnetismo', 'Lun, Mie 4:00pm - 6:00pm',30),
#     ('1000019', 'Fundamentos de Mecánica', 'Mar,Mier,Jue 7:00am - 9:00am',20),
#     ('1000025', 'Laboratorio de Técnicas Básicas en Química', 'Mie,Vie 7:00am - 9:00am',40),
#     ('1000026','Principio de Análisis Químico', 'Lun,Mar 4:00pm - 6:00pm',30)
# ]
cursos =[
    ('2015734', 'Programación de Computadores',40),
    ('2015711','Dibujo Básico',30),
    ('2016375', 'Programación Orientada a Objetos',20),
    ('2016509', 'Taller de Electrónica',40),
    ('2016703', 'Pensamiento Sistémico',30),
    ('2017228', 'Tecnología Mecánica Básica',20),
    ('1000004', 'Cálculo Diferencial',40),
    ('1000005', 'Cálculo Integral',30),
    ('1000006', 'Cálculo en Varia Variables',20),
    ('1000003', 'Algebra Lineal',40),
    ('1000017', 'Fundamentos de Electromagnetismo',30),
    ('1000019', 'Fundamentos de Mecánica',20),
    ('1000025', 'Laboratorio de Técnicas Básicas en Química',40),
    ('1000026','Principio de Análisis Químico',30)
]


# cursor.executemany("INSERT INTO Cursos(Código_Curso, Descripción_Curso, Num_Horas) VALUES(?,?,?)", cursos)

estudiantes = [
    ('8876295089', '2880', 'Juan','Perez' , '2019-01-15', 'Calle 1 # 2-3', '300-1234567', '300-1234567', 'Bogotá', 'Cundinamarca'),
    ('5269436393', '2880', 'Juan Camilo', 'Pérez Soza', '2024-11-15', 'Calle 65 # 20-3', '300-1234567', '300-1234', 'Bogotá', 'Cundinamarca'),
    ('8114559050', '2880', 'Pedro Pedro', 'Torres Castillo', '2024-03-16', 'Calle 72B # 23-30', '300-1234567', '300-1234', 'Bogotá', 'Cundinamarca'),
    ('7270566584', '2880', 'María Camila', 'González López', '2024-04-27', 'Calle 10 # 5-6', '310-9876543', '310-9876', 'Medellín', 'Antioquia'),
    ('7894756003', '2544', 'Andrés David', 'Martínez Rodríguez', '2024-04-28', 'Carrera 20 # 15-30', '320-7654321', '320-7654', 'Cali', 'Valle del Cauca'),
    ('8562305458', '2544', 'Laura Camila', 'Ramírez Pérez', '2024-04-29', 'Avenida 5 # 8-12', '315-5432109', '315-5432', 'Barranquilla', 'Atlántico'),
    ('6045534334', '2544', 'Carlos Felipe', 'López Gómez', '2024-04-30', 'Calle 7 # 12-15', '317-8765432', '317-8765', 'Bogotá', 'Cundinamarca'),
    ('2764144293', '2544', 'Ana Maria', 'Hernández Martínez', '2024-05-01', 'Carrera 15 # 25-18', '314-6543210', '314-6543', 'Medellín', 'Antioquia'),
    ('7511200463', '2880', 'Diego Alejandro', 'García Ramírez', '2024-05-02', 'Avenida 8 # 10-5', '312-9876543', '312-9876', 'Cali', 'Valle del Cauca'),
    ('9030779197', '2545', 'Sara Sofía', 'Pérez Martínez', '2024-05-03', 'Calle 12 # 20-7', '319-7654321', '319-7654', 'Barranquilla', 'Atlántico'),
    ('8605132377', '2545', 'Javier', 'López Ramírez', '2024-05-04', 'Carrera 18 # 22-10', '316-5433433', '320-5421', 'Valledupar', 'Cesar'),
    ('2550301257', '2545', 'Carla Valentina', 'Sánchez Pérez', '2024-05-05', 'Avenida 3 # 6-9', '313-8765432', '313-8765', 'Bogotá', 'Cundinamarca'),
    ('9997493368', '2545', 'Gabriel', 'Gómez Ramírez', '2024-05-06', 'Calle 5 # 8-11', '311-6543210', '311-6543', 'Medellín', 'Antioquia'),
    ('6514506224', '2546', 'Isabella', 'Martínez López', '2024-05-07', 'Carrera 12 # 18-25', '319-7654321', '319-7654', 'Cali', 'Valle del Cauca'),
    ('6223175366', '2546', 'Mateo', 'Hernández Ramírez', '2024-05-08', 'Avenida 7 # 10-14', '316-5432109', '316-5432', 'Barranquilla', 'Atlántico'),
    ('8221071329', '2880', 'Carlos Valentín', 'López Martínez', '2024-05-09', 'Calle 15 # 22-17', '314-9876543', '314-9876', 'Bogotá', 'Cundinamarca'),
    ('8782642282', '2548', 'Camila', 'García Ramírez', '2024-05-10', 'Carrera 25 # 30-22', '317-7654321', '317-7654', 'Medellín', 'Antioquia'),
    ('5301173864', '2548', 'Lucas Alejandro', 'Pérez Martínez', '2024-05-11', 'Avenida 10 # 12-19', '312-8765432', '312-8765', 'Cali', 'Valle del Cauca'),
    ('1008146001', '2548', 'Valentino', 'Ramírez Gómez', '2024-05-12', 'Calle 18 # 22-14', '318-7654321', '318-7654', 'Barranquilla', 'Atlántico'),
    ('2778948484', '2549', 'Isabel Maria', 'López Martínez', '2024-05-13', 'Avenida 12 # 15-20', '314-9876543', '314-9876', 'Bogotá', 'Cundinamarca'),
    ('9557617951', '2880', 'Sara Lucía', 'García Ramírez', '2024-05-14', 'Carrera 22 # 30-18', '317-7654321', '317-7654', 'Medellín', 'Antioquia'),
    ('1322078372', '2549', 'Damian Matías', 'Pérez Martínez', '2024-05-15', 'Avenida 15 # 18-22', '312-8765432', '312-8765', 'Cali', 'Valle del Cauca'),
    ('5547157920', '2880', 'Valeria', 'Hernández Ramírez', '2024-05-16', 'Calle 20 # 25-19', '319-6543210', '319-6543', 'Barranquilla', 'Atlántico')
]
# estudiantes_1 =[
# ('1322078372', '2549', 'Damian Matías', 'Pérez Martínez', '2024-05-15', 'Avenida 15 # 18-22', '312-8765432', '312-8765', 'Cali', 'Valle del Cauca'),
# ('5547157920', '2880', 'Valeria', 'Hernández Ramírez', '2024-05-16', 'Calle 20 # 25-19', '319-6543210', '319-6543', 'Barranquilla', 'Atlántico')

# ]


# cursor.executemany("INSERT INTO Alumnos(Id_Alumno, Id_Carrera, Nombres, Apellidos, Fecha_Ingreso, Dirección, Telef_Cel, Telef_Fijo, Ciudad, Departamento) VALUES(?,?,?,?,?,?,?,?,?,?)", estudiantes)

carreras = [
    ('2544','Ingeniería Eléctrica','10'),
    ('2545','Ingeniería Electrónica','10'),
    ('2546','Ingeniería Industrial','10'),
    ('2548','Ingeniería Mecatrónica','10'),
    ('2549','Ingeniería Química','10'),
    ('2880','Ingeniería de Sistemas','10')
]
# executemany = cursor.executemany("INSERT INTO Carreras(Código_Carrera, Descripción, Num_Semestres) VALUES(?,?,?)", carreras)

# import random

# from datetime import datetime, timedelta

# # Genera una fecha aleatoria
# def random_date(start, end):
#     return start + timedelta(
#         seconds=random.randint(0, int((end - start).total_seconds())))

# start = datetime(2024, 1, 1)
# end = datetime(2024, 12, 31)

# inscripciones = []

# for _ in range(80):
#     estudiante = random.choice(estudiantes)[0]  # Selecciona aleatoriamente un estudiante
#     fecha_inscripcion = random_date(start, end)  # Genera una fecha de inscripción aleatoria
#     curso = random.choice(cursos)[0]  # Selecciona aleatoriamente un curso

#     inscripcion = (estudiante, fecha_inscripcion, curso)
#     inscripciones.append(inscripcion)
    
# print(inscripciones)8114559050

inscritos_4 = [
    (1, '8605132377', '2024-07-06', '2017228','Lun,Mar 4:00pm - 6:00pm'),
    (1, '8605132377', '2024-09-18', '2016375','Lun,Mar 4:00pm - 6:00pm'),
    (1, '8605132377', '2024-04-14', '1000025','Lun,Mar 4:00pm - 6:00pm'),
    (1, '8605132377', '2024-07-06', '2016703','Lun,Mar 4:00pm - 6:00pm'),
    (1, '8605132377', '2024-08-16', '1000004','Lun,Mar 4:00pm - 6:00pm'),
    (1, '8605132377', '2024-01-10', '2016509','Lun,Mar 4:00pm - 6:00pm'),
    (1, '8605132377', '2024-01-10', '1000006','Lun,Mar 4:00pm - 6:00pm')
    
]

cursor.executemany("INSERT INTO Inscritos(No_Inscripción, Id_Alumno, Fecha_de_Inscripción, Código_Curso, Horario_Curso) VALUES(?,?,?,?,?)", inscritos_4)

inscritos_1 = [
    
    
    (9, '8605132377', '2024-07-06', '2017228'), 
    (2, '8782642282', '2024-04-14', '1000025'), (12, '5547157920', '2024-04-14', '2016375'), 
    (3, '8114559050', '2024-05-01', '2015734'), (11, '8221071329', '2024-07-07', '2016703'), 
    (4, '7270566584', '2024-05-01', '1000003'), (9, '8605132377', '2024-04-14', '1000025'), 
    (5, '9997493368', '2024-09-18', '2016509'), (2, '8782642282', '2024-07-06', '1000005'), 
    (5, '9997493368', '2024-04-14', '2015711'), (17, '8876295089', '2024-04-14', '1000006'), 
    (4, '7270566584', '2024-05-01', '2016509'), (17, '8876295089', '2024-07-07', '1000004'), 
    (6, '9030779197', '2024-05-01', '2017228'), (14, '5269436393', '2024-04-14', '2015734'), 
    (7, '2550301257', '2024-09-18', '2016375'), (13, '2764144293', '2024-07-06', '1000025'), 
    (7, '2550301257', '2024-04-14', '1000017'), (18, '6514506224', '2024-04-14', '1000003'), 
    (8, '1008146001', '2024-05-01', '1000006'), (8, '1008146001', '2024-07-07', '2015711'), 
    (7, '2550301257', '2024-09-18', '2016375'), (9, '8605132377', '2024-07-06', '2016703'), 
    (9, '8605132377', '2024-09-18', '2016375'), (3, '8114559050', '2024-07-06', '2015734'), 
    (10, '1008146001', '2024-07-06', '2015734'), (7, '2550301257', '2024-04-14', '1000003'), 
    (8, '1008146001', '2024-05-01', '1000003'), (17, '8876295089', '2024-07-07', '2016375'), 
    (11, '8221071329', '2024-05-01', '2016703'), (16, '7511200463', '2024-04-14', '2015711'), 
    (8, '1008146001', '2024-09-18', '2015711'), (19, '2778948484', '2024-07-06', '2016375'), 
    (12, '5547157920', '2024-04-14', '2015711'), (10, '1008146001', '2024-04-14', '1000004'), 
    (13, '2764144293', '2024-09-18', '2017228'), (14, '5269436393', '2024-07-06', '1000026'), 
    (14, '5269436393', '2024-04-14', '1000017'), (9, '8605132377', '2024-04-14', '1000025'), 
    (1, '8782642282', '2024-03-14', '1000019'), (14, '5269436393', '2024-05-07', '1000004'), 
    (5, '9997493368', '2024-09-24', '2016509'), (11, '8221071329', '2024-05-31', '2015711'), 
    (15, '7894756003', '2024-07-21', '1000005'), (16, '7511200463', '2024-05-31', '2016509'), 
    (7, '2550301257', '2024-01-10', '2015734'), (14, '5269436393', '2024-05-31', '2016375'), 
    (8, '1008146001', '2024-02-10', '1000006'), (3, '8114559050', '2024-08-16', '1000005'), 
    (15, '7894756003', '2024-11-02', '2015711'), (12, '5547157920', '2024-04-20', '1000017'), 
    (16, '7511200463', '2024-03-10', '2016375'), (3, '8114559050', '2024-04-20', '1000005'), 
    (8, '1008146001', '2024-03-10', '1000025'), (12, '5547157920', '2024-11-02', '2016375'), 
    (12, '5547157920', '2024-04-20', '1000025'), (3, '8114559050', '2024-08-16', '1000004'), 
    (1, '8782642282', '2024-11-02', '2015734'), (9, '8605132377', '2024-08-16', '1000004'), 
    (9, '8605132377', '2024-01-10', '2016509'), (12, '5547157920', '2024-05-31', '1000017'), 
    (11, '8221071329', '2024-04-20', '1000019'), (18, '6514506224', '2024-03-10', '2015734'), 
    (14, '5269436393', '2024-04-20', '1000026'), (13, '2764144293', '2024-05-31', '1000005')]

# cursor.executemany("INSERT INTO Cursos(Código_Curso, Descripción_Curso, Horario_Curso, Num_Horas) VALUES(?,?,?,?)", cursos)
# cursor.executemany('''INSERT INTO Carreras(Código_Carrera, Descripción, Num_Semestres) VALUES(?,?,?)''', carreras)
# cursor.executemany("INSERT INTO Alumnos(Id_Alumno, Id_Carrera, Nombres, Apellidos, Fecha_Ingreso, Dirección, Telef_Cel, Telef_Fijo, Ciudad, Departamento) VALUES(?,?,?,?,?,?,?,?,?,?)", estudiantes)
# cursor.executemany("INSERT INTO Inscritos(No_Inscripción, Id_Alumno, Fecha_de_Inscripción, Código_Curso) VALUES(?,?,?,?)", inscritos_1)


# inscritos_2 = [(3, '8114559050', '2024-07-06', '2015734'),
            

# toma los datos de alumno, carrera y curso y crea 40 inscritos de manera aleatoria pero que sea lo mas variado en cuanto a los cursos inscritos

# i = 3

# cursor.execute(f''' SELECT Inscritos.Id_Alumno, Nombres, Apellidos, Alumnos.Fecha_Ingreso, No_Inscripción, Dirección, Ciudad, Departamento, 
#                     Telef_Cel, Telef_Fijo, Id_Carrera, Inscritos.Código_Curso, Descripción_Curso, Num_Horas, Fecha_de_Inscripción  FROM Inscritos 
#             JOIN Alumnos ON Inscritos.Id_Alumno = Alumnos.Id_Alumno 
#             JOIN Cursos ON Inscritos.Código_Curso = Cursos.Código_Curso 
#             JOIN Carreras ON Alumnos.Id_Carrera = Carreras.Código_Carrera 
#             WHERE Inscritos.No_Inscripción = {i}''')

# cursor.execute('''DELETE FROM Inscritos''')
# cursor.execute('''DELETE FROM Cursos''')
# cursor.execute('''DELETE FROM Alumnos''')
# cursor.execute('''DELETE FROM Carreras''')

# cursor.execute("DROP TABLE IF EXISTS Inscritos")
# cursor.execute("DROP TABLE IF EXISTS Cursos")
# cursor.execute("DROP TABLE IF EXISTS Alumnos")
# cursor.execute("DROP TABLE IF EXISTS Carreras")

# datos = cursor.fetchall()
# print(datos)


# cursor.executemany("INSERT INTO Inscritos(No_Inscripción, Id_Alumno, Fecha_de_Inscripción, Código_Curso) VALUES(?,?,?,?)", inscritos_2)

# cursor.executemany("INSERT INTO Carreras(Código_Carrera, Descripción, Num_Semestres) VALUES(?,?,?)", carreras)

# cursor.execute("DELETE FROM Inscritos")
# cursor.execute("INSERT INTO Inscritos(Id_Alumno,Fecha_de_Inscripción,Código_Curso) VALUES('5547157920','2024-05-05','1000026')")
# cursor.execute("DROP TABLE IF EXISTS Inscritos")
# cursor.execute("DELETE FROM Inscritos WHERE No_Inscritos = 1")

# cursor.execute("ALTER TABLE Inscritos ADD COLUMN No_Inscrito INTEGER PRIMARY KEY DROP COLUMN No_Inscritos")

def Nuevo_Inscrito():
    # inscrito = []
    entrada_1 = input("Ingrese los datos del inscrito en una sola linea separado por el símbolo &:     ").split("&")
    datos = tuple(entrada_1)
    print(datos)
    cursor.execute("INSERT INTO Inscritos(Id_Alumno, Fecha_de_Inscripción, Código_Curso) VALUES (?,?,?)", datos)

# Nuevo_Inscrito()

def Inscribir_Curso():
    cursos = []
    entrada_1 = input("Ingrese los datos del curso en una sola linea separado por el símbolo #:     ").split("#")
    datos = tuple(entrada_1)
    print(datos)
    cursor.execute("INSERT INTO Cursos(Código_Curso, Descripción_Curso, Num_Horas) VALUES (?,?,?)", datos)
    
    
#Inscribir_Curso()

def Obtener_Datos():
    opcion = input("Ingrese el número de registro al que desea conocer la respectiva información:  ")
    # cursor.execute(f" SELECT * FROM Inscritos")
    # self.entry = [self.noInscripcion, self.cmbx_Id_Alumno, self.fecha, self.fechaInscripcion, 
    #             self.cmbx_Id_Carrera, self.nombres, self.apellidos, self.direccion, self.ciudad, 
    #             self.departamento, self.telCel, self.telFijo, self.codigo_Curso, self.nombreCurso, 
    #             self.horario]
    cursor.execute(f''' SELECT Inscritos.Id_Alumno, Nombres, Apellidos, Fecha_Ingreso, No_Inscritos, Dirección, Ciudad, Departamento, 
                   Telef_Cel, Telef_Fijo, Id_Carrera, Inscritos.Código_Curso, Descripción_Curso, Num_Horas, Inscritos.Fecha_de_Inscripción  FROM Inscritos 
                   JOIN Alumnos ON Inscritos.Id_Alumno = Alumnos.Id_Alumno 
                   JOIN Cursos ON Inscritos.Código_Curso = Cursos.Código_Curso 
                   JOIN Carreras ON Alumnos.Id_Carrera = Carreras.Código_Carrera 
                   WHERE Inscritos.No_Inscritos = {opcion}''')
    # cursor.execute(f'''SELECT * FROM Inscritos
    #                JOIN Cursos ON Inscritos.Código_Curso = Cursos.Código_Curso
    #                WHERE Inscritos.Id_Alumno = {opcion}
    #                ''')
    datos = cursor.fetchall()
    for i in datos:
        print(i)

    # fecha_split = datos[0][2].split("-")
    # fecha = f"{fecha_split[2]}/{fecha_split[1]}/{fecha_split[0]}"
    # print(fecha)
# Obtener_Datos()

def Obtener_Datos_Columna():
    # opcion = input("Ingrese los datos de la tabla/columna que desea recuperar separados por una &:  ").split("&")
    # cursor.execute(f" SELECT {opcion[1]} FROM {opcion[0]}")
    cursor.execute(f" SELECT Código_Curso FROM Inscritos WHERE Id_Alumno = '5547157920' ")
    datos = cursor.fetchall()
    lista_cursos = []
    for i in datos:
        lista_cursos += i
    print(lista_cursos)

# Obtener_Datos_Columna()

def Obtener_Un_Dato():
    opción = input("Ingrese dato(s) que desea recuperar de la siguiente manera (Tabla&Columna&Valor):  ").split("&")
    # print(opción)
    cursor.execute(f" SELECT * FROM {opción[0]} WHERE {opción[1]} = {opción[2]} ")
    # cursor.execute(f" SELECT * FROM {opción[0]} WHERE Código_Curso = '{opción[1]}' ")
    # cursor.execute("SELECT * FROM Cursos WHERE Código_Curso = 'PYT-015' ")
    datos = cursor.fetchall()
    lista = []
    for i in datos:
        lista += i
    # cursor.execute(f"SELECT Nombres, Apellidos FROM Alumnos WHERE Id_Alumno = {lista[1]}")
    # datos_1 = cursor.fetchall()
    # for i in datos_1:
    #     lista += i
    # cursor.execute(f"SELECT Descripción_Curso FROM Cursos WHERE Código_Curso = '{lista[3]}'")
    # datos_2 = cursor.fetchall()
    # for i in datos_2:
    #     lista += i
    print(lista)
# Obtener_Un_Dato()

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