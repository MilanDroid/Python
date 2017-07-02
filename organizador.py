import os, sys
import re
import shutil

def obtenerDirectorio():
	#Obtengo la ruta donde extraere los archivos
	path = raw_input("Escriba la ruta donde estan los archivos (Ejemplo: /home/USUARIO/Documentos/): \n")
	dirs = os.listdir(path)

	#Obtengo la ruto donde almacenare los archivos
	for file in dirs:
   		print file
   	outpath = raw_input("Escriba la ruta hacia donde desea mover los archivos (Ejemplo: /home/USUARIO/Documentos/): \n")

   	#Llamo el metodo para crear las carpetas
   	crearDirectorios(outpath)

   	#LLamo a los metodos para clasificar y mover los archivos
   	musica(path, outpath)
   	video(path, outpath)
   	exe(path, outpath)
   	pdf(path, outpath)
   	imagenes(path, outpath)
   	pythonC(path, outpath)
   	documentos(path, outpath)
   	archivosComprimidos(path, outpath)
   	otros(path, outpath)

def crearDirectorios(outpath):
	#Verifico si la direccion existe, si no existe la creo
	if not os.path.exists(outpath):
		os.makedirs(outpath)
		print 'Directorio creado'
	#Creo las carpetas
	if not os.path.exists(outpath + "Imagenes/"):
		os.makedirs(outpath + "Imagenes/")
	if not os.path.exists(outpath + "Musica/"):
		os.makedirs(outpath + "Musica/")
		print 'Carpeta Musica ha sido creada'
	if not os.path.exists(outpath + "Documentos/"):
		os.makedirs(outpath + "Documentos/")
		print 'Carpeta Documentos ha sido creada'
	if not os.path.exists(outpath + "Python/"):
		os.makedirs(outpath + "Python/")
		print 'Carpeta Python a sido creada'
	if not os.path.exists(outpath + "Video/"):
		os.makedirs(outpath + "Video/")
		print 'Carpeta Video ha sido crada'
	if not os.path.exists(outpath + "Archivos Comprimidos/"):
		os.makedirs(outpath + "Archivos Comprimidos/")
		print 'Carpeta Archivos Comprimidos ha sido creada'
	if not os.path.exists(outpath + "PDF/"):
		os.makedirs(outpath + "PDF/")
		print 'Carpeta PDF ha sido creada'
	if not os.path.exists(outpath + "EXE/"):
		os.makedirs(outpath + "EXE/")
		print 'Carpeta EXE ha sido creada'
	if not os.path.exists(outpath + "Otros/"):
		os.makedirs(outpath + "Otros/")
		print 'Carpeta Otros ha sido creada'
	print	'\n Todas las carpetas fueron creadas. \n'

def documentos(path, outpath):
	extensiones = [".txt",".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods", ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox", 
	".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt", "pptx", ".in", ".out"]
	dirs = os.listdir(path)
	#Se recorre el directorio archivo por archivo y se compara su extension con las extensiones en el arreglo
	for file in dirs:
		(nombreFichero, extension) = os.path.splitext(file)

		for tipo in extensiones:
			if not extension == '':
				if re.match(extension, tipo):
					shutil.move(path + file, outpath + "Documentos/")
					print 'El archivo ' + file + " ha sido movido a " + outpath  + "Documentos/"

def musica(path, outpath):
	extensiones = [".aac", ".aa", ".aac", ".dvf", ".flac",".m4a", ".m4b", ".m4p", ".mp3", ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"]
	dirs = os.listdir(path)
	#Se recorre el directorio archivo por archivo y se compara su extension con las extensiones en el arreglo
	for file in dirs:
		(nombreFichero, extension) = os.path.splitext(file)

		for tipo in extensiones:
			if not extension == '':
				if re.match(extension, tipo):
					shutil.move(path + file, outpath + "Musica/")
					print 'El archivo ' + file + " ha sido movido a " + outpath  + "Musica/"

def video(path, outpath):
	extensiones = [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng", ".qt", ".mpg", ".mpeg", ".3gp"]
	dirs = os.listdir(path)
	#Se recorre el directorio archivo por archivo y se compara su extension con las extensiones en el arreglo
	for file in dirs:
		(nombreFichero, extension) = os.path.splitext(file)

		for tipo in extensiones:
			if not extension == '':
				if re.match(extension, tipo):
					shutil.move(path + file, outpath + "Video/")
					print 'El archivo ' + file + " ha sido movido a " + outpath  + "Video/"

def pythonC(path, outpath):
	extensiones = ['.py']
	dirs = os.listdir(path)
	#Se recorre el directorio archivo por archivo y se compara su extension con las extensiones en el arreglo
	for file in dirs:
		(nombreFichero, extension) = os.path.splitext(file)

		for tipo in extensiones:
			if not extension == '':
				if re.match(extension, tipo):
					shutil.move(path + file, outpath + "Python/")
					print 'El archivo ' + file + " ha sido movido a " + outpath  + "Python/"

def archivosComprimidos(path, outpath):
	extensiones = [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z", ".dmg", ".rar", ".xar", ".zip"]
	dirs = os.listdir(path)
	#Se recorre el directorio archivo por archivo y se compara su extension con las extensiones en el arreglo
	for file in dirs:
		(nombreFichero, extension) = os.path.splitext(file)

		for tipo in extensiones:
			if not extension == '':
				if re.match(extension, tipo):
					shutil.move(path + file, outpath + "Archivos Comprimidos/")
					print 'El archivo ' + file + " ha sido movido a " + outpath  + "Archivos Comprimidos/"


def pdf(path, outpath):
	extensiones = ['.pdf']
	dirs = os.listdir(path)
	#Se recorre el directorio archivo por archivo y se compara su extension con las extensiones en el arreglo
	for file in dirs:
		(nombreFichero, extension) = os.path.splitext(file)

		for tipo in extensiones:
			if not extension == '':
				if re.match(extension, tipo):
					shutil.move(path + file, outpath + "PDF/")
					print 'El archivo ' + file + " ha sido movido a " + outpath  + "PDF/"

def exe(path, outpath):
	extensiones = ['.exe']
	dirs = os.listdir(path)
	#Se recorre el directorio archivo por archivo y se compara su extension con las extensiones en el arreglo
	for file in dirs:
		(nombreFichero, extension) = os.path.splitext(file)

		for tipo in extensiones:
			if not extension == '':
				if re.match(extension, tipo):
					shutil.move(path + file, outpath + "EXE/")
					print 'El archivo ' + file + " ha sido movido a " + outpath  + "EXE/"

def imagenes(path, outpath):
	extensiones = [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg", ".heif", ".psd"]
	dirs = os.listdir(path)
	#Se recorre el directorio archivo por archivo y se compara su extension con las extensiones en el arreglo
	for file in dirs:
		(nombreFichero, extension) = os.path.splitext(file)

		for tipo in extensiones:
			if not extension == '':
				if re.match(extension, tipo):
					shutil.move(path + file, outpath + "Imagenes/")
					print 'El archivo ' + file + " ha sido movido a " + outpath  + "Imagenes/"

def otros(path, outpath):
	dirs = os.listdir(path)
	#Los archivos que no fueron almacenados por ninguno de los metodos anteriores son lo que quedan y seran almacenados en la carpeta Otros
	for file in dirs:
		(nombreFichero, extension) = os.path.splitext(file)
		if not extension == '':
			shutil.move(path + file, outpath + "Otros/")
			print 'El archivo ' + file + " ha sido movido a " + outpath  + "Otros/"

obtenerDirectorio()