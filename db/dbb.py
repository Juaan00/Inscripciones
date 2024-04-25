import sqlite3

#No ejecutar aun

conn = sqlite3.connect('Inscripciones.db')

cursor = conn.cursor()

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

cursor.execute('''INSERT INTO Carreras(Código_Carrera, Descripción, Num_Semestres) VALUES('ISyC_2789', 'Ingeniería de Sistemas y Computación', 10)
              ''')
cursor.execute('''INSERT INTO Alumnos(Id_Alumno, Id_Carrera, Nombres, Apellidos, Fecha_Ingreso, Dirección, Telef_Cel, Telef_Fijo, Ciudad, Departamento) VALUES('2019-001', 'ISyC_2789', 'Juan', 'Pérez', '2019-01-15', 'Calle 1 # 2-3', '300-1234567', '300-1234567', 'Bogotá', 'Cundinamarca')
               ''')
cursor.execute('''INSERT INTO Cursos(Código_Curso, Descripción_Curso, Num_Horas) VALUES('PYT-001', 'Python Básico', 40)
               ''')
cursor.execute('''INSERT INTO Inscritos(Id_Alumno, Fecha_de_Inscripción, Código_Curso) VALUES('2019-001', '2020-01-15', 'PYT-001')
               ''')

cursos =[
    ('PYT-002', 'Python Intermedio', 40),
    ('PYT-003', 'Python Avanzado', 40),
    ('PYT-004', 'Django Básico', 40),
    ('PYT-005', 'Django Intermedio', 40),
    ('PYT-006', 'Django Avanzado', 40),
    ('PYT-007', 'Flask Básico', 40),
    ('PYT-008', 'Flask Intermedio', 40),
    ('PYT-009', 'Flask Avanzado', 40),
    ('PYT-010', 'PyQt5 Básico', 40),
    ('PYT-011', 'PyQt5 Intermedio', 40),
    ('PYT-012', 'PyQt5 Avanzado', 40),
    ('PYT-013', 'Tkinter Básico', 40),
    ('PYT-014', 'Tkinter Intermedio', 40),
    ('PYT-015', 'Tkinter Avanzado', 40)
]

cursor.executemany("INSERT INTO Cursos(Código_Curso, Descripción_Curso, Num_Horas) VALUES(?,?,?)", cursos)


def Inscribir_Curso():
    cursos = []
    entrada_1 = input("Ingrese los datos del curso en una sola linea separado por el símbolo #:     ").split("#")
    datos = tuple(entrada_1)
    print(datos)
    cursor.execute("INSERT INTO Cursos(Código_Curso, Descripción_Curso, Num_Horas) VALUES (?,?,?)", datos)
    
    
# Inscribir_Cursos()




conn.commit()

conn.close() 

print('Base de Datos creada con éxito')