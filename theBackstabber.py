from bs4 import BeautifulSoup
import requests
import argparse
import os

os.system("color 02")

parser = argparse.ArgumentParser(description='theBackstabber')
parser.add_argument('-r', '--rango', 
					type=int,
					default=None,
					required=False,
					help='Cantidad de paginas que se buscaran.')
parser.add_argument('-p', '--keyword', 
					type=str,default=None,required=False, 
					help='Palabra clave que buscara en el <h1>, por defecto no hay ninguna.')

args = parser.parse_args()

try:
	class Nivel20(object):
		"""docstring for Nivel20"""
		def __init__(self, url_aux):
			self.url_aux = url_aux
			self.rango = args.rango
			self.clave = args.keyword
			self.lista = []
			self.lista2 = []
			self.lista_links = []
			if self.clave != None:
				self.scraping_keyword()
				self.format()
				self.print_and_write()
			else:
				self.scraping_range()
				self.format()
				self.print_and_write()


		def scraping_keyword(self):
			for i in range(1,self.rango+1):
				self.url = self.url_aux + str(i)
				self.result = requests.get(self.url)
				self.doc = BeautifulSoup(self.result.text, "html.parser")
				try:
					self.libros = self.doc.find("h1")
					if str(self.result) == '<Response [200]>' and self.clave in str(self.libros.get_text()):
						self.lista_links.append(self.url)
						self.lista.append(self.libros.get_text())
						print('\n> '+self.url,'-',self.result)
					elif str(self.result) == '<Response [404]>':
						print('\n> El link', self.url, 'no ha tenido respuesta.')
					elif self.clave not in str(self.libros.get_text()):
						print('\n> El link', self.url, 'no es el rulebook que buscas.')
					else:
						print('\n> El link', self.url, 'no es un rulebook.')
				except:
						print("\n> Aparentemente, la pagina no existe o tiene un contenido ilegible.")


		def scraping_range(self):
			for i in range(1,self.rango+1):
				self.url = self.url_aux + str(i)
				self.result = requests.get(self.url)
				self.doc = BeautifulSoup(self.result.text, "html.parser")
				try:
					self.libros = self.doc.find("h1")
					if str(self.result) == '<Response [200]>' and str(self.libros.get_text()) != "\nInicio\n":
						self.lista_links.append(self.url)
						self.lista.append(self.libros.get_text())
						print('\n> '+self.url,'-',self.result)
					elif str(self.result) == '<Response [404]>':
						print('\n> El link', self.url, 'no ha tenido respuesta.')
					else:
						print('\n> El link', self.url, 'no es un rulebook.')
				except:
						print("\n> Aparentemente, la pagina no existe o tiene un contenido ilegible.")


		def format(self):
			self.characters='\n'

			for i in self.lista:
				i=str(i)
				for x in range(len(self.characters)):
				   		i = i.replace(self.characters[x],"")
				   		self.lista2.append(i)


		def print_and_write(self):
			self.text=open("links.txt","w")
			self.text.close()
			self.text=open("links.txt","a",encoding="utf-8")
			print("\n")
			self.aux=0
			for i in self.lista2:	
				i=str(i)
				print("> "+str(self.aux+1)+': '+i+' - '+str(self.lista_links[self.aux]+"\n"))
				self.text.write(str(self.aux+1)+': '+i+' - '+str(self.lista_links[self.aux]+"\n"))
				self.aux += 1
			self.text.close()
			input("> Pulsa Enter para continuar.")

	nivel20 = Nivel20("https://nivel20.com/games/dnd-5/rulebooks/")

except TypeError:

	print("\n	******************************************************")
	print("	                 ___====-_  _-====___")
	print("	           _--^^^#####//      \\\\#####^^^--_")
	print("	        _-^##########// (    ) \\\\##########^-_")
	print("	       -############//  |\\^^/|  \\\\############-")
	print("	     _/############//   (@::@)   \\############\\_")
	print("	    /#############((     \\\\//     ))#############\\")
	print("	   -###############\\\\    (oo)    //###############-")
	print("	  -#################\\\\  / VV \\  //#################-")
	print("	 -###################\\\\/      \\//###################-")
	print("	_#/|##########/\\######(   /\\   )######/\\##########|\\#_")
	print("	|/ |#/\\#/\\#/\\/  \\#/\\##\\  |  |  /##/\\#/  \\/\\#/\\#/\\#| \\|")
	print("	`  |/  V  V  `   V  \\#\\| |  | |/#/  V   '  V  V  \\|  '")
	print("	   `   `  `      `   / | |  | | \\   '      '  '   '")
	print("	                    (  | |  | |  )")
	print("	                   __\\ | |  | | /__")
	print("	                  (vvv(VVV)(VVV)vvv)")
	print("\n	theBackstabber 1.0.0")
	print("	Coded by @YImborrable & @StudiosBork")
	print("	cristianramirezmarin@gmail.com\n")
	print("		╭━━━━┳╮╱╱╱╱╭━━╮╱╱╱╱╱╱╭╮╱╱╱╱╭╮╱╱╱╭╮╱╭╮")
	print("		┃╭╮╭╮┃┃╱╱╱╱┃╭╮┃╱╱╱╱╱╱┃┃╱╱╱╭╯╰╮╱╱┃┃╱┃┃")
	print("		╰╯┃┃╰┫╰━┳━━┫╰╯╰┳━━┳━━┫┃╭┳━┻╮╭╋━━┫╰━┫╰━┳━━┳━╮")
	print("		╱╱┃┃╱┃╭╮┃┃━┫╭━╮┃╭╮┃╭━┫╰╯┫━━┫┃┃╭╮┃╭╮┃╭╮┃┃━┫╭╯")
	print("		╱╱┃┃╱┃┃┃┃┃━┫╰━╯┃╭╮┃╰━┫╭╮╋━━┃╰┫╭╮┃╰╯┃╰╯┃┃━┫┃")
	print("		╱╱╰╯╱╰╯╰┻━━┻━━━┻╯╰┻━━┻╯╰┻━━┻━┻╯╰┻━━┻━━┻━━┻╯")
	print("	******************************************************")
	print("\n	usage: theBackstabber [-h] -r Rango -p Palabra Clave")
	print("	options:")
	print("		-h, --help\n		            muestra este mensaje y termina el programa.")
	print("		-r, --rango\n		            Cantidad de paginas que se buscaran.")
	print("		-p, --keyword\n		            Palabra clave que buscara en el <h1>, por defecto no hay ninguna.")



	exit()