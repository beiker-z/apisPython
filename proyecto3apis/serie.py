# -*- coding: utf-8 -*-
import requests
import json
from PIL import Image
from io import BytesIO """Created on Sat Nov 15 14:16:11 2022   @author: Kevin Ramos"""
class Personaje:
    def __init__(self, id):
        self.id=id
    def buscarPesonaje(self):
        url='https://rickandmortyapi.com/api/character/{}'.format(self.id)
        r=requests.get(url)
        j=r.json()
        print(f""" ***********PERSONAJE RICK Y MORTY******************
              Id:{j["id"]}
              Nombre:{j["name"]}
              Status:{j["status"]}
              Especie:{j["species"]}
              """)              
        Image.open(BytesIO(requests.get('https://rickandmortyapi.com/api/character/avatar/'+str(id)+'.jpeg').content))
class Capitulo:
    def __init__(self, id):
        self.id=id
    def buscarPesonaje(self):
        url='https://rickandmortyapi.com/api/episode/{}'.format(self.id)
        r=requests.get(url)
        j=r.json()
        print(f""" ***********EPISODIO RICK Y MORTY******************
              Id:{j["id"]}
              Nombre:{j["name"]}
              Fecha de publicación:{j["air_date"]}
              """)
if __name__=="__main__":
    buscar=" "
    while(buscar!="s"):
        print("""
                1. Buscar personaje por id
                2. Buscar capitulo por id
              """)
        opcion=input("Ingrese una opcion...")
        while opcion!="1" and opcion!="2":
            print("INGRESO UNA OPCION EQUIVOCADA...")
            print("""
                    1. Buscar personaje por id
                    2. Buscar capitulo por id
                  """)
            opcion=input("Ingrese una opcion...")
        if opcion=="1":
            print("********************PERSONAJE********************")
            id=input("Ingrese el id del personaje: ")
            personaje=Personaje((id))
            personaje.buscarPesonaje()
        else:
            print("************EPISODIO*************************")
            id=input("Ingrese el id del episodio: ")
            episodio=Capitulo(id)
            episodio.buscarPesonaje()
        buscar=input("presione s para salir del programa ")
