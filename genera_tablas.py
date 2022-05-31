from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column, Integer, String, ForeignKey

# se importa información de la configuracion
from configuracion import cadena_base_datos
    
# se genera en enlace al gestor de base de datos
engine = create_engine(cadena_base_datos)
Base = declarative_base()

# Hacemos la creacion de las diferentes clases(Provincia, Canton, Parroquia, Establecimiento)
#Tabla de Provincias
class Provincia(Base):
    __tablename__ = 'provincia'
    id = Column(Integer, primary_key=True)
    nombre_Pro = Column(String(100)) #nombre de la provincia
    codigo_Pro = Column(String(50)) #codigo division politica administrativa provincia
    cantones = relationship("Canton", back_populates="provincia")
    
    def __repr__(self):
        return "Provincia: %s | Código de División Política: %s \n "% (
                          self.nombre_Pro,
                          self.codigo_Pro)
# Tabla de Cantones
class Canton(Base):
    __tablename__ = 'canton'
    id = Column(Integer, primary_key=True)
    nombre_cant = Column(String(100)) # nombre de canton
    codigo_cant = Column(String(50))#Código División Política Administrativa  Cantón
    provincia_id = Column(Integer, ForeignKey('provincia.id'))
    provincia = relationship("Provincia", back_populates="cantones")
    parroquias = relationship("Parroquia", back_populates="canton")

    def __repr__(self):
        return "Canton: %s |  Código de División Política: %s | Id de provincia: %d\n"% (
                          self.nombre_cant, 
                          self.provincia,
                          self.provincia_id)
# Tabla de Parroquias

class Parroquia(Base):
    __tablename__ = 'parroquia'
    id = Column(Integer, primary_key=True)
    nombre_parro = Column(String(100)) # nombre de parroquia
    codigo_distrito = Column(String(50)) #Código de Distrito
    codigo_parro = Column(String(50))#Código División Política Administrativa  Parroquia
    canton_id = Column(Integer, ForeignKey('canton.id'))
    canton = relationship("Canton", back_populates="parroquias")
    establecimientos= relationship("Establecimiento", back_populates="parroquias")
    def __repr__(self):
        return "Parroquia: %s |  Código de División Política: %s |  Código de Distrito: %s | Id Canton: %d\n"% (
                          self.nombre_parro, 
                          self.codigo_parro,
                          self.codigo_distrito,
                          self.canton_id)

# Creación de la tabla Establecimiento con sus atributos.
class Establecimiento(Base):
    __tablename__ = 'establecimiento'
    codigo_AMIE = Column(String(100), primary_key=True)  #codigo AMIE
    nombre_estable = Column(String(100)) # nombre del establecimiento
    sostenimiento = Column(String(50)) #sostenimiento
    tipo_educacion = Column(String(100)) #tipo de educacion
    modalidad = Column(String(500)) #modalidad de estudios
    jornada = Column(String(100)) #jornada
    acceso = Column(String(100)) #acceso al establecimiento
    num_estudiantes = Column(Integer) #numero de estudiantes del establecimiento
    num_docentes = Column(Integer) #numero de docentes del establecimiento
    parroquia_id = Column(Integer, ForeignKey('parroquia.id'))
    parroquias = relationship("Parroquia", back_populates="establecimientos")
    
    def __repr__(self):
        return "Establecimiento: %s | Codigo Institución: %s | Sostenimiento: %s | Tipo Educación: %s| Modalidad: %s | Jornada: %s | Acceso: %s |  Numero Estudiante: %d | Numero Docentes: %d | Id Parroquia: %d" % (
                self.nombre_estable,
                self.codigo_AMIE,
                self.sostenimiento,
                self.tipo_educacion,
                self.modalidad,
                self.jornada,
                self.acceso,
                self.num_estudiantes,
                self.num_docentes,
                self.parroquia_id)

Base.metadata.create_all(engine)
