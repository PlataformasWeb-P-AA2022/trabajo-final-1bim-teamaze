from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import csv

# se importa las clases del  archivo genera_tablas y la informacion de la configuracion
from genera_tablas import Provincia, Canton
from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

#lectura del csv
with open('data\Listado-Instituciones-Educativas.csv', encoding='UTF8') as File:
    reader = csv.reader(File,delimiter='|', quotechar=',',
                        quoting=csv.QUOTE_MINIMAL)

#\Users\DELL\Desktop\trabajo-final-1bim-teamaze\data
    next(reader)
    cant=[] # Lista donde se guardan los cantones

    for row in reader: 
        if row[5] not in cant:
            cant.append(row[5])
            id_p = session.query(Provincia).filter_by(codigo_Pro = row[2]).first()
            #id_p= session.query(Provincia).filter_by(nombre_Pro = row[3]).first()  
            #c = Canton(nombre_cant =row[5], codigo_cant=row[4], provincia_id = id_p.id)
            c = Canton(codigo_cant = row[4], nombre_cant = row[5], provincia_id = id_p.id)

            session.add(c)

session.commit()
