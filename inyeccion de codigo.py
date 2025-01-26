# Ejemplo de código inseguro
import os

def leer_archivo(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        return archivo.read()

def ejecutar_comando(comando):
    os.system(comando)

# Uso inseguro de la función
nombre_archivo = "datos.txt"
contenido = leer_archivo(nombre_archivo)
print(contenido)

# Vulnerabilidad de inyección de comandos
comando = "ls -la /"
ejecutar_comando(comando)