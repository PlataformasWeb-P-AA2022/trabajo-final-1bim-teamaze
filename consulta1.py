from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_ # se importa el operador and

# se importa las clases de archivo genera_tablas
from genera_tablas import Provincia, Canton, Establecimiento, Parroquia

# se importa información del archivo configuracion
from configuracion import cadena_base_datos
# se genera enlace al gestor de base de datos
# para el ejemplo se usa la base de datos sqlite
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()



print("Consulta 1")
print("\033[1;33m"+"Establecimientos con el Código División Política Administrativa Parroquia con valor 110553"+'\033[0;m') 


est = session.query(Establecimiento).join(Parroquia, Canton, Provincia).filter(Parroquia.codigo_parro == '110553').all()
for e in est:
    print((e))
print(len(est))
