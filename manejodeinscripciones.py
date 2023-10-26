from aplicacion.modelos.usuario import Usuario
from aplicacion.repositorio.repositoriodeusuarios import RepositorioDeUsuarios

#===============================
# Clase ManejoDeInscripciones
# NO TIENE VARIABLES !!!
#===============================
class ManejoDeInscripciones:
    #====================================================================
    #  Decorador staticmethod
    #  El objeto solo tiene la funcion inscribirUsuario
    #  ENVUELVE LA FUNCIN SIN LLAMAR VARIABLES LOCALES
    #  el obejto ManejoDeInscripciones es la interface intercambiable
    #=====================================================================
    @staticmethod
    def inscribirUsuario(usuario: Usuario, repositorioDeUsuarios: RepositorioDeUsuarios) -> None:
        print("--------> Guardando usuario....\n")
        repositorioDeUsuarios.abrir()
        repositorioDeUsuarios.guardar(usuario)
        repositorioDeUsuarios.cerrar()

