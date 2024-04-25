import sqlite3

#No ejecutar aun

conn = sqlite3.connect('db/Inscripciones.db')

cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS  Inscritos(
    No_Incripción INTEGER PRIMARY KEY AUTOINCREMENT,
    ID_Alumno VARCHAR(20) NOT NULL,
    Fecha_Inscripción DATE NOT NULL,
    Código_Curso VARCHAR(20),
    FOREIGN KEY (ID_Alumno) REFERENCES Alumnos(ID_Alumno),
    FOREIGN KEY (Código_Curso) REFERENCES Cursos(Código_Curso)
    
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS  Cursos(
    Código_Curso VARCHAR(20) PRIMARY KEY,
    Descrip_Curso VARCHAR(60),
    Horario_Curso VARCHAR(20)
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS  Carreras(
    Código_Carrera VARCHAR(15) PRIMARY KEY NOT NULL,
    Descrip_Carrera VARCHAR(100),
    Num_Semestres SMALLINT(2)
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS  [Alumnos](
    [Id_Alumno] VARCHAR(20) PRIMARY KEY NOT NULL,
    Id_Carrera VARCHAR(15),
    Nombres VARCHAR(50),
    Apellidos VARCHAR(50),
    Fecha_Ingreso DATE,
    Dirección VARCHAR(60),
    Telef_Cell VARCHAR(18),
    Telef_Fijo VARCHAR(15),
    Ciudad VARCHAR(60),
    Departamento VARCHAR(60),
    FOREIGN KEY (Id_Carrera) REFERENCES Carreras(Id_Carrera)
)''')