from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import csv

# se importa las clases del  archivo genera_tablas y la informacion de la configuracion
from genera_tablas import  Canton, Parroquia
from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

#Lectura del csv
with open('data/Listado-Instituciones-Educativas.csv', encoding='UTF8') as File:
    reader = csv.reader(File,delimiter='|', quotechar=',',
                        quoting=csv.QUOTE_MINIMAL)

    next(reader)
    aux=[]    

    for row in reader:
        if row[7] not in aux:
            aux.append(row[7]) 
            print(row[7])
            id_c= session.query(Canton).filter_by(codigo_cant = row[4]).first()
            p = Parroquia(nombre_parro=row[7], codigo_parro=row[6], codigo_distrito=row[8],canton_id=id_c.id)
            session.add(p)
                     
session.commit()

