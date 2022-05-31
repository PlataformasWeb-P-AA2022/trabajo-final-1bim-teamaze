from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import csv

# se importa las clases del  archivo genera_tablas y la informacion de la configuracion
from genera_tablas import  Parroquia, Establecimiento
from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()
parroquias = session.query(Parroquia).all()

#Lectura del csv
with open('data/Listado-Instituciones-Educativas.csv', encoding='UTF8') as File:
    reader = csv.reader(File,delimiter='|', quotechar=',',
                        quoting=csv.QUOTE_MINIMAL)
    
    next(reader) 

    for row in reader:
        num_estud=int(row[14], base=0)
        num_Docen=int(row[15], base=0)
        id_p = session.query(Parroquia).filter_by(codigo_parro = row[6]).first() 
        est = Establecimiento(codigo_AMIE=row[0], nombre_estable=row[1], sostenimiento=row[9],tipo_educacion=row[10],
        modalidad=row[11], jornada=row[12], acceso=row[13],num_estudiantes=num_estud,num_docentes=num_Docen, parroquia_id=id_p.id) 
        session.add(est) 

session.commit()


