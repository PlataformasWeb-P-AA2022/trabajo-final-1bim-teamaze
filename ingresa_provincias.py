from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import csv

# se importa las clases del  archivo genera_tablas y la informacion de la configuracion
from genera_tablas import Provincia
from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

#Lectura del csv
with open('data/Listado-Instituciones-Educativas.csv', encoding='UTF8') as File:
    reader = csv.reader(File, delimiter='|', quotechar=',',
                        quoting=csv.QUOTE_MINIMAL)

    next(reader)
    aux=[]

    for row in reader:
        if row[3] not in aux:
            aux.append(row[3])
            p = Provincia(nombre_Pro=row[3], codigo_Pro=row[2]) 
            session.add(p)  

session.commit()
