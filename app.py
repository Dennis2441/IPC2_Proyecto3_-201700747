from flask import Flask, jsonify, request,Response
from flask_cors import CORS
from tkinter import filedialog
from tkinter import Tk

import json
import types
from xml.dom.minidom import Node
from datetime import datetime
import numpy as np
import datetime
import plotly.graph_objects as go
import os
import re

from analizador.Syntactic import parser
from analizador.Syntactic import user_list, task_list
from stru.list import av
from stru.list import matiz
from stru.list import recordatorio
from stru.list import arbol
from stru.list import Curso
app= Flask(__name__)
CORS(app, resources={r"/*": {"origin": "*"}})

@app.route('/entradaestudiante', methods=['POST','GET'])
def getentrada():
    if request.method=="POST":
        hola="Carga Completa"
        hola="Carga Completa"
        jsonStr= request.data.decode('utf-8')
        hola=jsonStr
        f = open("estudia.txt","r")
        mensaje = f.read()
        print(mensaje)
        f.close()

        aList = json.loads(mensaje)  
        
        for p in aList['estudiantes']:
            carnet=str(p['carnet'])
            DPI=str(p['DPI'])
            nombre=str(p['nombre'])
            carrera=str(p['carrera'])
            correo=str(p['correo'])
            password=str(p['password'])
            #credito=str(p['creditos'])
            edad=str(p['edad'])

           # user_list.insertValue(carnet,DPI,nombre,carrera,password,edad,correo,"","","","","","user")
            user_list.insertValue(carnet,DPI,nombre,carrera,password,edad,edad,correo,"","","","","","user")
            av.insert(carnet,nombre,carrera,DPI,correo,password,edad,edad)
            hola="Hecho"
            return Response(hola,content_type='application/x-www-form-urlencoded')
        
@app.route('/cursopensum', methods=['POST','GET'])          
def getpensum():
    if request.method=="POST":   
        
            jsonStr= request.data.decode('utf-8')
            hola=jsonStr
            f = open(hola,"r", encoding="utf-8")
            mensaje = f.read()
            f.close()
            aList = json.loads(mensaje)
            for p in aList['Cursos']:
                codigo=p['Codigo']
                name=p['Nombre']
                credito=str(p['Creditos'])
                pre=str(p['Prerequisitos'])
                obligatorio=str(p['Obligatorio'])

                arbol.insertar(Curso(int(codigo),name,int(credito),pre,obligatorio))

@app.route('/cursopensum', methods=['POST','GET'])   
def getpenusmes():
     jsonStr= request.data.decode('utf-8')
     hola=jsonStr
     f = open(hola,"r", encoding="utf-8")
     mensaje = f.read()
     f.close()
     if request.method=="POST":  
            aList = json.loads(mensaje)
            for p in aList['Estudiantes']:
                Carnet=p['Carnet']
                print(Carnet)
                for i in p["Años"]:
                    Año=i['Año']
                    print(Año)
                    for j in i["Semestres"]:
                        Semestre=j['Semestre']
                        print(Semestre)
                        for po in j['Cursos']:
                            codigo=po['Codigo']
                            name=po['Nombre']
                            credito=str(po['Creditos'])
                            pre=str(po['Prerequisitos'])
                            obligatorio=str(po['Obligatorio'])
                            print(codigo)
                            print(name)
                            print(credito)
                            print(pre)
                            print(obligatorio)
                            av.insertarano(Carnet,Año)
                            av.insertarsemestre(Carnet,Año,Semestre)
                            av.insertararbol(Carnet,Año,Semestre,int(codigo),name,int(credito),pre,obligatorio)




if __name__=='__main__':
    app.run(host='0.0.0.0', debug=True, port=3000)