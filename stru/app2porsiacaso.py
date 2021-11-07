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

@app.route('/entrada', methods=['POST','GET'])
def getentrada():
    if request.method=="POST":
        hola="Carga Completa"
        jsonStr= request.data.decode('utf-8')
        aLists = json.loads(jsonStr)
        print(aLists)
        nombre=aLists["tipo"]
        ruta=aLists["path"]

        
        if(nombre=="estudiante"):
            f = open(ruta,"r", encoding="utf-8")
            mensaje = f.read()
            print(mensaje)
            f.close()
            parser.parse('¿ Elements ? ¿Element type = "task"?  ¿item Carnet = "201901425" $? ¿$Element? ¿ $Elements ?')
            parser.parse(mensaje)

            user_list.getList()
            print("------------------------")
            task_list.getList()
            
          #  av.imprimir2()
            
            user_list.getver()
            
        elif(nombre=="curso"):
            f = open(ruta,"r", encoding="utf-8")
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
        elif(nombre=="cursoestudiante"):
            f = open(ruta,"r", encoding="utf-8")
            mensaje = f.read()
            f.close()
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

                    

            

        return Response(hola,content_type='application/x-www-form-urlencoded')
    elif request.method=="GET":
        hola="hola"
        return Response(hola,content_type='application/x-www-form-urlencoded')


@app.route('/reporte', methods=['POST','GET'])
def getreporte():
    if request.method=="GET":
        hola="Buscar la Imagen"
        jsonStr= request.data.decode('utf-8')
        aList = json.loads(jsonStr)
        print(aList)
        nombre=aList["tipo"]
        if(nombre==0):
           hola="Buscar la Imagen"
           av.imprimir2()
        elif(nombre==1):
            carnet=aList["carnet"]
            year=aList["año"]
            mes=aList["mes"]
            matiz.buscar1(carnet,year,mes)
            matiz.imprimir()
        elif(nombre==2):
            carnet=aList["carnet"]
            year=aList["año"]
            mes=aList["mes"]
            dia=aList["dia"]
            hora=aList["hora"]
            matiz.buscar1(carnet,year,mes)
            matiz.imprimir2(dia,carnet,year,mes,hora)
        elif(nombre==3):
            arbol.graficaB(arbol.raiz)
        elif(nombre==4):
            ho=""
        
        #ruta=aList["path"]

        
        

            

        return Response(hola,content_type='application/x-www-form-urlencoded')
    elif request.method=="GET":
        hola="hola"
        return Response(hola,content_type='application/x-www-form-urlencoded')

@app.route('/estudiante', methods=['POST','GET','DELETE','PUT'])
def getestudiante():
    hola=""
    if request.method=="POST":
        jsonStr= request.data.decode('utf-8')
        aList = json.loads(jsonStr)
        carnet=aList['carnet']
        DPI=aList['DPI']
        nombre=aList['nombre']
        carrera=aList['carrera']
        correo=aList['correo']
        password=aList['password']
        creditos=str(aList['creditos'])
        edad=str(aList['edad'])

        user_list.insertValue(carnet,DPI,nombre,carrera,password,creditos,edad,correo,"","","","","","user")
        av.insert(carnet,nombre,carrera,DPI)
        hola="Hecho"
        return Response(hola,content_type='application/x-www-form-urlencoded')
    elif(request.method=="DELETE"):
        jsonStr= request.data.decode('utf-8')
        
        aList = json.loads(jsonStr)
        carnet=aList['carnet']
        av.delete_value(carnet)
        hola="Hecho"
        return Response(hola,content_type='application/x-www-form-urlencoded')
    elif(request.method=="PUT"):
        jsonStr= request.data.decode('utf-8')
        aList = json.loads(jsonStr)
        carnet=aList['carnet']
        DPI=aList['DPI']
        nombre=aList['nombre']
        carrera=aList['carrera']
        correo=aList['correo']
        password=aList['password']
        creditos=str(aList['creditos'])
        edad=str(aList['edad'])
        av.search(carnet,DPI,nombre,carrera,password,creditos,edad,correo)
        hola="Hecho"
        return Response(hola,content_type='application/x-www-form-urlencoded')
    elif(request.method=="GET"):
        jsonStr= request.data.decode('utf-8')
        
        aList = json.loads(jsonStr)
        carnet=aList['carnet']
        hola=av.search2(carnet)
        
        return Response(hola,content_type='application/x-www-form-urlencoded')

@app.route('/recordatorios', methods=['POST','GET','DELETE','PUT'])
def getrecordatorios():
    hola=""
    if request.method=="POST":
        jsonStr= request.data.decode('utf-8')
        aList = json.loads(jsonStr)
        carnet=aList['carnet']
        hola="Creado"
        nombre=aList['nombre']
        Descripcion=aList['Descripcion']
        Materia=aList['Materia']
        Fecha=str(aList['Fecha'])
        Hora=str(aList['Hora'])
        Estado=aList['Estado']
        matiz.insertar(carnet,nombre,Descripcion,Materia,Fecha,Hora,Estado)
        return Response(hola,content_type='application/x-www-form-urlencoded')
    elif request.method=="PUT":
        jsonStr= request.data.decode('utf-8')
        aList = json.loads(jsonStr)
        carnet=aList['carnet']
        hola="Creado"
        nombre=aList['nombre']
        Descripcion=aList['Descripcion']
        Materia=aList['Materia']
        Fecha=str(aList['Fecha'])
        Hora=str(aList['Hora'])
        Estado=aList['Estado']
        matiz.insertar(carnet,nombre,Descripcion,Materia,Fecha,Hora,Estado)
        return Response(hola,content_type='application/x-www-form-urlencoded')
    elif request.method=="GET":
        jsonStr= request.data.decode('utf-8')
        aList = json.loads(jsonStr)
        carnet=aList['carnet']
        
        Fecha=str(aList['Fecha'])
        Hora=str(aList['Hora'])
        
        hola=matiz.buscar9(carnet,Hora,Fecha)
        return Response(hola,content_type='application/x-www-form-urlencoded')
    elif request.method=="DELETE":
        jsonStr= request.data.decode('utf-8')
        aList = json.loads(jsonStr)
        carnet=aList['carnet']
        
        Fecha=str(aList['Fecha'])
        Hora=str(aList['Hora'])
        
        hola=matiz.buscar9(carnet,Hora,Fecha)
        return Response(hola,content_type='application/x-www-form-urlencoded')


@app.route('/cursosPensum', methods=['POST','GET'])
def getcursosPensum():
    if request.method=="POST":
        hola="Carga Completa"
        jsonStr= request.data.decode('utf-8')
        aList = json.loads(jsonStr)  
        
        for p in aList['Cursos']:
            codigo=p['Codigo']
            name=p['Nombre']
            credito=str(p['Creditos'])
            pre=str(p['Prerequisitos'])
            obligatorio=str(p['Obligatorio'])

            arbol.insertar(Curso(int(codigo),name,int(credito),pre,obligatorio))
        

 



if __name__=='__main__':
    app.run(host='0.0.0.0', debug=True, port=3000)