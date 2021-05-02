from flask import Flask, jsonify, request,Response
from flask_cors import CORS
from tkinter import filedialog
from tkinter import Tk
import xml.dom.minidom
from xml.dom import minidom
from bs4 import BeautifulSoup
from xml.dom.minidom import Node
import os
import re
cadenaxml=[]
hola=[]
app= Flask(__name__)
CORS(app, resources={r"/*": {"origin": "*"}})
nomb=" "
@app.route('/Principal', methods=['GET'])
def getDatos():
    return 'Funciona'

@app.route('/suma', methods=['POST','GET'])
def getsuma():
    global cadenaxml
    h="d"
    global nomb
    if h=="d":
        if request.method=="POST":

            Tk().withdraw()
            filename = filedialog.askopenfilename(initialdir = "/",
                                                title = "Select un archivo xml",
                                                filetypes = (("xml files",
                                                                "*.xml*"),
                                                            ("all files",
                                                                "*.*")))
            print(filename)
            nomb=filename
            archivo = open(filename, "r", encoding='utf-8')
            mm = archivo.read()
            cadenaxml=mm
            print(mm)
            textfile = open("output.txt", 'w')
            textfile.write(mm)
            textfile.close()

            
            
            return Response("Hecho",content_type='application/x-www-form-urlencoded')
        elif request.method=="GET":
            archivo = open("output.txt", "r", encoding='utf-8')
            mm = archivo.read()
            print(mm)
            cadenaxml=mm 
            return Response(mm,content_type='application/x-www-form-urlencoded')
        else:
            return Response("not hecho",content_type='application/x-www-form-urlencoded')
  
    
@app.route('/salida', methods=['POST','GET'])
def getsalida():
    global cadenaxml
    h="d"
    global nomb
    if h=="d":
        if request.method=="POST":
            
            mm=cadenaxml
            leer(cadenaxml)

            return Response("Hecho",content_type='application/x-www-form-urlencoded')
        else:
            mm=cadenaxml
            per=cadenaxml
            return Response(mm,content_type='application/x-www-form-urlencoded')






#--------------------------------Funciones--------------------------------------------------------------------------
class Token():
    def __init__(self, id, nombre,):
        self.nombre = nombre
        self.id = id
lista_Token=[]
lista_error=[]
lista_fecha=[]
def leer(cadena):
    
    analizar(cadena)
    


def analizar(cadena):
    global lista_Token
    global lista_error
    global lista_fecha
    char = '' #caracter actual
    next_char = '' #caracter siguiente
    lexema = ""
    lista_Token=[]
    estado=0
    n=0
    flag=False
    ver=False
    for i in range(len(cadena)):
        char=cadena[i]
        try:
         next_char=cadena[i+1]
         tercero=cadena[i+2]
        except:
          next_char= ' '
        print(estado, "::", char,"::", next_char)
        if(estado==0):
            if(flag==True):
                if(char.isalpha() and next_char.isalpha()):
                    lexema=lexema+char
                    estado=1
                    print()
                elif(char.isalnum()):
                    lexema=lexema+char
                    estado=10
            else:
                if(char=="<" and next_char=="/"):
                    print(char)
                    estado=11
                    ver=True
                elif(char=="<" and next_char=="?" ):
                    print()
                elif(char=="<"):
                    estado=11
                
                
                    
#fecha  elif re.search(r"^([0-2][0-9]|3[0-1])(\/|-)(0[1-9]|1[0-2])\2(\d{4})$", lexema):
        elif(estado==11):
            if(char.isalpha()):
                lexema=lexema+char
                print(lexema)
            elif(char==">"):
                if(ver==True):
                    if(lexema=="EVENTOS"):
                        print("FInlizado")
                        lexema=""
                    elif(lexema=="EVENTO"):
                        print("termino evento")
                        lexema=""
                        ver=False

                    else:
                        print("no Se PUEDE el cierre de EVENTO")
                    estado=0
                else:
                    if(lexema=="EVENTOS"):
                        print("EMPEZO EVENTO")
                        lexema=""
                    elif(lexema=="EVENTO"):
                        if(lexema=="EVENTO"):
                            print("COMIENZA EVENTO")
                            lexema=""
                            flag=True
                    else:
                        print("No se puede abrir")
                    estado=0


        elif(estado==10):
            if(char.isalnum() or  char=="/"):
                lexema=lexema+char
            else:
                if re.search(r"^([0-2][0-9]|3[0-1])(\/|-)(0[1-9]|1[0-2])\2(\d{4})$", lexema):    
                    print(lexema)
                    print(lexema + " Es una fecha")
                    estado=0
                    lexema=""
        elif(estado==1):
            if(n==0):
                if(char.isalpha()and next_char.isalpha()):
                    lexema=lexema+char
                else:
                    lexema=lexema+char
                    n=1
                    estado=0
                    print("Nombre")
                    lexema=""

            else:
                if(char.isalpha()):
                    lexema=lexema+char
                    
                elif(char.isspace()):
                    lexema=lexema+char
                    
                elif(char.isspace()):
                    lexema=lexema+char
                    
                elif(char==":"):
                    
                    if re.search(r'Reportado por', lexema):
                        print("ok "+ lexema)
                        estado=12
                        lexema=""
                    elif(re.search(r'Usuarios afectados', lexema)):
                        print("ok "+ lexema)
                        estado=13
                        lexema=""
                    elif(re.search(r'Error', lexema)):
                        print("si es error "+ lexema)
                        estado=14
                        lexema=""
                    else:
                        print(not okey)
                print(lexema)
        elif(estado==12):

            if(char.isalnum() or char=="@" or char=="."):
                lexema=lexema+char
            
            if(char.isspace()):
                print()
                if re.search(r"^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$", lexema):

                    print(lexema)
                    print("ok al correo "+ lexema)
                    lexema="" 
                if(char=="\n"):
                    estado=0
                    lexema=""
                lexema=""
                        
            print(lexema)
        elif(estado==13):
            if(char.isalnum() or char=="@" or char=="."):
                lexema=lexema+char
            
            if(char.isspace()):
                print()
                if re.search(r"^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$", lexema):

                    print(lexema)
                    print("ok al correo "+ lexema)
                    lexema="" 
                if(char=="\n"):
                    estado=0
                    lexema=""
                lexema=""
            print(lexema)
        elif(estado==14):

            if(char.isdigit()):
                lexema=lexema+char

            elif(char.isspace()):
                if(char=="\n"):
                    estado=0
            else:
                print(lexema)
                print("error numero :"+ lexema)
                estado=141
                lexema=""
            print(lexema)
        elif(estado==141):
            if(char.isspace()):
                if(char.isspace() and next_char=="<"):
                   print("infomarcion de error "+ lexema)
                   lexema="" 
                   flag=False
                   estado=0

                elif(char=="\n"):
                    lexema=lexema+char
                
                else:
                    lexema=lexema+char
            
            else:
                lexema=lexema+char

if __name__=='__main__':
    app.run(host='0.0.0.0', debug=True, port=4000)