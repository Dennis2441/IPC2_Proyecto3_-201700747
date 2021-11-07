
import os


cc=0
ff=0
ncolumna=0
nfila=0
listahora=[]
listadia=[]
listamatriz=[]
numerocarnet=""
veryear=""
vermes=""
class Nodo1(): #Nodo que guarda las cantidades de combustible
    def __init__(self,fila,columna,carnet,nombre,descripcion,materia,fecha,hora,estado):
        self.carnet=carnet
        self.nombre=nombre
        self.descripcion=descripcion
        self.materia=materia
        self.fecha=fecha
        self.hora=hora
        self.fecha=fecha
        self.fila=fila
        self.estado=estado
        self.derecha=None
        self.izquierda=None
        self.abajo=None
        self.arriba=None
class nodoencabezado:
    def __init__(self,id):
        self.id=id
        self.siguiente=None
        self.anterior=None
        self.acceso=None
class listaencabezado:
    def __init__(self,primero=None):
        self.primero=primero
    def eliminarp(self):
        if(self.primero==None):
            print("vacio")
        
        if self.primero.siguiente==None:
                self.primero=None
                return
        
        self.primero=self.primero.siguiente
        self.primero.anterior=None
    def eliminar(self,id):
        if(self.primero==None):
            print("vacio")
        else:
            if(self.primero==id):
                print(self.primero.id)
                self.eliminarp()
                return

    def setencabezadp(self,nuevo):
        if (self.primero==None):
            self.primero=nuevo
        elif(nuevo.id<self.primero.id):
            nuevo.siguiente=self.primero
            self.primero.anterior=nuevo
            self.primero=nuevo
        else:
            actual=self.primero
            while actual.siguiente !=None:
                if(nuevo.id<self.primero.id):
                    nuevo.siguiente=actual.siguiente
                    actual.siguiente.anterior=nuevo
                    nuevo.anterior=actual
                    actual.siguiente=nuevo
                    break
                actual=actual.siguiente
            if(actual.siguiente==None):
                actual.siguiente=nuevo
                nuevo.anterior=actual
    def getencabezado(self,id):
        actual=self.primero
        while actual !=None:
            if(actual.id==id):
                return actual
            actual=actual.siguiente
        return None

class matrizx:
    
    
    def __init__(self):
        
        self.efilas=listaencabezado()
        self.ecolumnas=listaencabezado()
    def insertar(self,carnet,nombre,descripcion,materia,fecha,hora,estado):
        
        global ff
        global cc
        nuevo=Nodo1(ff,cc,carnet,nombre,descripcion,materia,fecha,hora,estado)
        ecolumna=self.ecolumnas.getencabezado(cc)
        print(ecolumna)
        if ecolumna==None:
            ecolumna=nodoencabezado(cc)
            ecolumna.acceso=nuevo
            self.ecolumnas.setencabezadp(ecolumna)
           
        else:
            if (nuevo.fila < ecolumna.acceso.fila):
                nuevo.abajo=ecolumna.acceso
                ecolumna.acceso.arriba=nuevo
                ecolumna.acceso=nuevo
            else:
                actual=ecolumna.acceso
                while actual.abajo !=None:
                    if nuevo.fila< actual.abajo.fila:
                        nuevo.abajo=actual.abajo
                        actual.abajo.arriba=nuevo
                        nuevo.arriba=actual
                        actual.abajo=nuevo
                        break
                    actual=actual.abajo
                if(actual.abajo==None):
                    actual.abajo=nuevo
                    nuevo.arriba=actual
        #insercion encabezado por filas
        efila= self.efilas.getencabezado(ff)
        if efila==None:
            efila=nodoencabezado(ff)
            efila.acceso=nuevo
            self.efilas.setencabezadp(efila)
        else:
            if (nuevo.columna < efila.acceso.columna):
                nuevo.derecha=efila.acceso
                efila.acceso.izquierda=nuevo
                efila.acceso=nuevo
            else:
                actual=efila.acceso
                while actual.derecha !=None:
                    if nuevo.columna< actual.derecha.columna:
                        nuevo.derecha=actual.derecha
                        actual.derecha.izquierda=nuevo
                        nuevo.izquierda=actual
                        actual.derecha=nuevo
                        break
                    actual=actual.derecha
                if(actual.derecha==None):
                    actual.derecha=nuevo
                    nuevo.izquierda=actual
        cc=cc+1
        ff=ff+1
   
    def buscar3(self,dia,hora,carnet,year,mes):
        global listadia
        global listahora
        global ncolumna
        global nfila
        
        global numerocarnet
        
        
        ecolumna=self.ecolumnas.primero
        ver=False
        quotes='"'
        estado=0
        contado=0
        while ecolumna !=None:
            actual=ecolumna.acceso
            while actual !=None:
                if actual.carnet==carnet:
                    
                    strin=str(actual.fecha)
                    dayy=strin.split("/")[0]
                    mess=strin.split("/")[1]
                    yearr=strin.split("/")[2]

                    if(year==yearr):

                        if(mes==mess):
                            if(dayy==dia):
                                if(actual.hora==hora):
                                    contado=contado+1
                                    
                                        
                actual=actual.abajo
            ecolumna=ecolumna.siguiente


                
        return contado

    def imprimir(self):
        global numerocarnet
        global ncolumna
        global nfila
        kf=nfila+1
        kc=ncolumna+1
        global veryear
        global vermes
        inde=0
        inde2=0
        inde3=0
        ver=False
        MapaRuta = open(r"C:\Users\denni\OneDrive\Desktop\ima2.txt",'w')
        MapaRuta.write('digraph {' + "\n")
        MapaRuta.write('node [shape=plaintext]' + "\n")
        MapaRuta.write('some_node [' + "\n")
        MapaRuta.write('label=<' + "\n")
        MapaRuta.write('<table border="0" cellborder="1" cellspacing="0">' + "\n")
        MapaRuta.write('<tr>' + "\n")
        MapaRuta.write('<td>' + "\n")
        MapaRuta.write(numerocarnet + "\n")
        MapaRuta.write('</td>' + "\n")
        for i in listadia:
            MapaRuta.write('<td>' + "\n")
            MapaRuta.write("Dia: "+str(i) + "\n")
            MapaRuta.write('</td>' + "\n")
        MapaRuta.write('</tr>' + "\n")
        for i in range(1,kf):
            MapaRuta.write('<tr>' + "\n")
            MapaRuta.write('<td>' + "\n")
            MapaRuta.write("Hora: "+str(listahora[inde3]) + "\n")
            MapaRuta.write('</td>' + "\n")
            inde3=inde3+1
            if(ver==False):
                inde2=0
            else:
                inde=inde+1
                inde2=0
            for j in range(1,kc):
                val=self.buscar3(str(listadia[inde2]),str(listahora[inde]),numerocarnet,veryear,vermes)
                inde2=inde2+1
                if(val==0):
                    val=""
                    MapaRuta.write('<td>' + "\n")
                    MapaRuta.write(val + "\n")
                    MapaRuta.write('</td>' + "\n")
                    ver=True
                else:
                    MapaRuta.write('<td>' + "\n")
                    MapaRuta.write(str(val) + "\n")
                    MapaRuta.write('</td>' + "\n")
                    ver=True
                if(j==ncolumna):
                    MapaRuta.write('</tr>' + "\n")
                    ver=True
        MapaRuta.write(' </table>>' + "\n")
        MapaRuta.write('  ];' + "\n")
        MapaRuta.write(' }' + "\n")
        MapaRuta.close()
        os.system("dot -Tsvg "r"C:\Users\denni\OneDrive\Desktop\ima2.txt -o "r"C:\Users\denni\OneDrive\Desktop\ima2.svg")
       
        os.system("dot -Tpng "r"C:\Users\denni\OneDrive\Desktop\ima2.txt -o "r"C:\Users\denni\OneDrive\Desktop\ima2.png")


    def buscar2(self,dia,carnet,year,mes):
        global listadia
        global listahora
        global ncolumna
        global nfila
        temporal=[]
        ecolumna=self.ecolumnas.primero
        for x in listadia:
            fecha=str(x)+"/"+mes+"/"+year
            while ecolumna !=None:
                actual=ecolumna.acceso
                while actual !=None:
                    if actual.carnet==carnet:
                        
                        strin=str(actual.fecha)
                        if(strin==fecha):
                            listahora.append(int(actual.hora))
                    actual=actual.abajo
                ecolumna=ecolumna.siguiente
            listahora.sort()
            temporal.extend(listahora)
            listahora=[]

            for x in temporal:
                if(x in listahora):
                    hola=""
                else:
                    print(x)
                    listahora.append(int(x))
            nfila=len(listahora)
            ncolumna=len(listadia)                
 
    def imprimir2(self,dia,carnet,year,mes,hora):
        global listadia
        global listahora
        global ncolumna
        global nfila
        
        global numerocarnet
        arhivo=""
        anterior=""
        ecolumna=self.ecolumnas.primero
        ver=False
        quotes='"'
        estado=0
        contado=0
        br ="\n"
        MapaRuta = open(r"C:\Users\denni\OneDrive\Desktop\listatarea.txt",'w')
        MapaRuta.write('digraph foo {' + "\n")
        MapaRuta.write('rankdir=LR;' + "\n")
        MapaRuta.write('node [shape=record]' + "\n")
        ver=False
        while ecolumna !=None:
            actual=ecolumna.acceso
            while actual !=None:
                if actual.carnet==carnet:
                    nodooo="nodo"+str(contado)
                    strin=str(actual.fecha)
                    dayy=strin.split("/")[0]
                    mess=strin.split("/")[1]
                    yearr=strin.split("/")[2]

                    if(year==yearr):

                        if(mes==mess):
                            if(dayy==dia):
                                if(actual.hora==hora):
                                    ver=True
                                    MapaRuta.write(br+nodooo+"[label=\"Carnet:"+actual.carnet+"|Nombre:"+actual.nombre+"|Descripcion:"+actual.descripcion+"|Materia:"+actual.materia+"|fecha:"+actual.fecha+"|Hora:"+actual.hora+"|Estado:"+actual.estado+"\"];\n")

                                    if(anterior==""):
                                        MapaRuta.write(br+nodooo)
                                    
                                        anterior=nodooo
                                        nodooo=""
                                    else:
                                    
                                        MapaRuta.write("\n"+anterior+"->"+nodooo+"\n")
                                        
                                        anterior=nodooo
                                        nodooo=""

            
                                    contado=contado+1
                                    
                                        
                actual=actual.abajo
            ecolumna=ecolumna.siguiente
        if(ver==False):
            return "ver"                     
        else:
            MapaRuta.write(' }' + "\n")
            MapaRuta.close()
            os.system("dot -Tsvg "r"C:\Users\denni\OneDrive\Desktop\listatarea.txt -o "r"C:\Users\denni\OneDrive\Desktop\listatarea.svg")
            os.system("dot -Tjpg "r"C:\Users\denni\OneDrive\Desktop\listatarea.txt -o "r"C:\Users\denni\OneDrive\Desktop\listatarea.jpg") 
            return "Okey"                          
                            

                    


    def buscar1(self,carnet,year,mes):
        hola=""

         
        global listadia
        global listahora
        temporal=[]
        global numerocarnet
        global veryear
        global vermes
        vermes=mes
        veryear=year
        numerocarnet=carnet
        ecolumna=self.ecolumnas.primero
        ver=False
        quotes='"'
        while ecolumna !=None:
            actual=ecolumna.acceso
            while actual !=None:
                if actual.carnet==carnet:
                    
                    strin=str(actual.fecha)
                    dayy=strin.split("/")[0]
                    mess=strin.split("/")[1]
                    yearr=strin.split("/")[2]

                    if(year==yearr):

                        if(mes==mess):
                            ver=True
                            listadia.append(int(dayy))    
                actual=actual.abajo
            

                
                        
            

            ecolumna=ecolumna.siguiente
            if(ver==False):
                return ver
            else:
                listadia.sort()
                temporal.extend(listadia)
                listadia=[]

                for x in temporal:
                    if(x in listadia):
                        hola=""
                    else:
                        print(x)
                        listadia.append(int(x))
                temporal=[]
                for i in listadia:
                    self.buscar2(i,carnet,year,mes)


       
            

                
                        
            



if __name__=='__main__':
    hola=matrizx()

    hola.insertar("201700747","descripcion","descripcion","hdfskhdfs","10/5/2020","8","activado")
    hola.insertar("201700747","descripcion","descripcion","hdfskhdfs","10/5/2020","8","activado")
    hola.insertar("201700747","descripcion","hsdkfkdsf","hdfskhdfs","9/5/2020","6","deactivado")
    hola.insertar("201700747","descripcion","sfddsf","hdfskhdfs","9/5/2020","6","activado")
    hola.insertar("201700747","descripcion","descripcion","hdfskhdfs","9/5/2020","7","activado")
    hola.buscar1("201700747","2020","5")
    hola.imprimir()
    hola.imprimir2("9","201700747","2020","5","6")
    
import os

class Curso:
    def __init__(self, _codigo, _nombre, _creditos, _preRequisitos, _esObligatorio):
        self.codigo = _codigo
        self.nombre = _nombre
        self.creditos = _creditos
        self.preRequisitos = _preRequisitos
        self.esObligatorio = _esObligatorio


class Pagina:
    def __init__(self, orden):
        self.cuenta = 0
        self.m = orden
        self.claves = [Curso(0,"",0,None,None) for x in range(orden)]
        self.ramas = [Pagina for x in range(orden)]

        #INICIALIZAMOS LAS PAGINAS
        for i in range(orden):
            self.ramas[i] = None

    def pagina_llena(self):
        return self.cuenta == self.m - 1

    def pagina_semi_llena(self):
        return self.cuenta < self.m / 2

#aqui empieza el arbol B
from graphviz.files import Source
import queue
import copy

class arbolB:
    def __init__(self, _orden):
        self.orden = _orden
        self.raiz = Pagina(5)


    def insertar(self,curso):

                    # [SUBE_ARRIBA, MEDIANA, ND, P]
        array_valores = [False,0,None, None]

        self.empujar(self.raiz, curso, array_valores)

        if array_valores[0]:
            array_valores[3] = Pagina(self.orden)
            array_valores[3].cuenta = 1
            array_valores[3].claves[1] = array_valores[1]
            array_valores[3].ramas[0] = self.raiz
            array_valores[3].ramas[1] = array_valores[2]
            self.raiz = array_valores[3]


    # flag_pagina = [bool sube_arriba, int mediana, pagina nuevo,P)
    def empujar(self, pagina_actual, curso, flag_pagina):
        camino = [0]  # a que rama irse
        if pagina_actual == None:
            flag_pagina[0] = True # sube_arriba
            flag_pagina[1] = curso # mediana
            flag_pagina[2] = None # pagina nuevo
        else:
            esta = self.buscarPagina(pagina_actual, curso, camino)
            if esta:
                print("hay una clave duplicada: " + curso.codigo)
                flag_pagina[0] = False
                return
            self.empujar(pagina_actual.ramas[camino[0]], curso, flag_pagina)
            if flag_pagina[0]:
                if pagina_actual.pagina_llena():
                    self.dividirNodo(pagina_actual,flag_pagina[1],copy.deepcopy(flag_pagina[2]),camino,flag_pagina)
                else:
                    flag_pagina[0] = False
                    self.meterHoja(pagina_actual,flag_pagina[1],flag_pagina[2],camino[0])


    def buscarPagina(self,pagina_actual, curso, camino):
        # Tomar en cuenta que "camino" es la direccion de las ramas por las que puede bajar la busqueda
        encontrado = False
        if curso.codigo < pagina_actual.claves[1].codigo : 
            camino[0] = 0   # Indica que vajaremos por la rama 0
            encontrado = False

        else: # Examina las claves del nodo en orden descendente

            camino[0] = pagina_actual.cuenta     #iniciamos desde la clave actual

            # Busacamos una posicion hasta donde el valor deje de ser menor
            # (por si viene un valor a los que hay en le nodo )
            while (curso.codigo < pagina_actual.claves[camino[0]].codigo) and (camino[0] > 1):
                camino[0] = camino[0] - 1
            encontrado = curso.codigo == pagina_actual.claves[camino[0]].codigo
        return encontrado

    def meterHoja(self , actual, curso, rd, k):
        # DESPLAZAR A LA DERECHA LOS ELEMENTOS PARA HACER UN HUECO
        i = actual.cuenta
        while i >= k + 1:
            actual.claves[i + 1] = actual.claves[i]
            actual.ramas[i + 1] = actual.ramas[i]
            i = i-1

        actual.claves[k + 1] = curso
        actual.ramas[k + 1] = rd
        actual.cuenta = actual.cuenta + 1

    def dividirNodo(self, pagina_actual, valor, rd, camino, flag_pagina):
        posMdna = self.orden / 2 if (camino[0] <= self.orden / 2) else self.orden / 2 + 1
        posMdna = int(posMdna)
        flag_pagina[2] = Pagina(5)
        i = posMdna + 1
        while i < self.orden:
            # Es desplazada  la mitad drecha al nuevo nodo, la clave mediana se queda en el nodo origen
            flag_pagina[2].claves[i - posMdna] = pagina_actual.claves[i]
            flag_pagina[2].ramas[i - 1] = pagina_actual.ramas[i]
            i = i + 1
        flag_pagina[2].cuenta = (self.orden -1) - posMdna #numero de claves en le nuevo nodo
        pagina_actual.cuenta = posMdna # numero de claves en el nodo origen

        # Es insertada la clave y rama en el nodo que le corresponde
        if camino[0] <= self.orden / 2: # si el camino[0 es menor al minimo de claves que puede haber en la pagina
            self.meterHoja(pagina_actual,valor, rd, camino[0])
        else:
            self.meterHoja(flag_pagina[2], valor, rd, camino[0] - posMdna) # se inserta el nuevo alvor que trajimos en el nodo nuevo

        # se extrae la clave media del nodo origen
        flag_pagina[1] = pagina_actual.claves[pagina_actual.cuenta]

        # rama 0 del nuevo nodo es la rama de la mediana
        flag_pagina[2].ramas[0] = pagina_actual.ramas[pagina_actual.cuenta]
        pagina_actual.cuenta = pagina_actual.cuenta -1

    def graficaB(self, raiz):

        # [ ACUMULADOR, ACUMULADORE DE ENLACES, CONTADOR PAGINA, CONTADOR AUX ]
        acumulador = ["digraph G\n{\nnode[shape = record, height= .1];\n", "", 0, 0]

        if raiz != None:
            cola = queue.Queue()
            cola.put(raiz)

            while not(cola.empty()): # Mientras la cola no este vacia
                tmpPagina = cola.get()
                self.imprimir(tmpPagina, acumulador)
                i = 0
                while i <= tmpPagina.cuenta:
                    if tmpPagina.ramas[i] != None:
                        cola.put(tmpPagina.ramas[i])
                    i += 1
                acumulador[2] += 1 #contador de pagina
            acumulador[0] += "\n" + acumulador[1]

        acumulador[0] += "}\n"
        
        s = Source(acumulador[0],filename="arbolB2", format="pdf")
        
        s.view()
        os.system("dot -Tsvg arbolB2 -o "r"C:\Users\denni\OneDrive\Desktop\listatarea.svg")
        #os.system(prog)

    def imprimir(self, actual, acumulador):
        acumulador[0] += 'node{}[label="<r0>'.format(str(acumulador[2]))

        if actual.ramas[0] != None:
            acumulador[3] += 1 # contador auxiliar
            acumulador[1] += '"node{}":r0 -> "node{}"\n'.format(str(acumulador[2]) , str(acumulador[3]))

        i = 1
        while i <= actual.cuenta:
            acumulador[0] += '|<c{}> {} |<r{}>'.format(str(i),"Codig:"+str(actual.claves[i].codigo) +"\n Curso:"+actual.claves[i].nombre,str(i))

            if actual.ramas[i] != None:
                acumulador[3] += 1 # contador auxiliar
                acumulador[1] += '"node{}":r{} -> "node{}"\n'.format(str(acumulador[2]) ,str(i), str(acumulador[3]))
            i += 1
        acumulador[0] += '"];\n'


class Nodosemestre():
    def __init__(self, nombre):
        self.nombre = nombre
        self.arbol=arbolB(5)
        self.siguiente = None
        
class semestre:
    def __init__(self):
        self.start_node = None


    def insertararbol(self,value,_codigo, _nombre, _creditos, _preRequisitos, _esObligatorio):
        actua=self.start_node
        if self.start_node == None:
            print("Vacio")
            return False
        while actua!=None:
            if(actua.nombre==value):
                print(value)
                actua.arbol.insertar(Curso(_codigo,_nombre,_creditos,_preRequisitos,_esObligatorio))
                return True
            
            actua=actua.siguiente
        return False

    def imprimirarbol(self,value):
        actua=self.start_node
        if self.start_node == None:
            print("Vacio")
            return False
        while actua!=None:
            if(actua.nombre==value):
                print(value)
                actua.arbol.graficaB(actua.arbol.raiz)
                return True
            
            actua=actua.siguiente
        return False

    def insert_at_start(self, data):
            if self.start_node is None:
                new_node = Nodosemestre(data)
                self.start_node = new_node
                print("Hecho")
                return
            if(self.search(data)==True):
                print("ya existe")
            else:
                new_node = Nodosemestre(data)
                new_node.nref = self.start_node
                self.start_node.pref = new_node
                self.start_node = new_node
    def search(self,value):
        actua=self.start_node
        if self.start_node == None:
            print("Vacio")
            return False
        while actua!=None:
            if(actua.nombre==value):
                print(value)
                return True
            
            actua=actua.siguiente
        return False



class Nodomes():
    def __init__(self, nombre):
        self.nombre = nombre
        self.listasemestre=semestre()
        self.siguiente = None


class DoublyLinkedList:
    def __init__(self):
        self.start_node = None
    
    def insertararbol(self,value,value2,_codigo, _nombre, _creditos, _preRequisitos, _esObligatorio):
        actua=self.start_node
        if self.start_node == None:
            print("Vacio")
            return False
        while actua!=None:
            if(actua.nombre==value):
                actua.listasemestre.insertararbol(value2,_codigo, _nombre, _creditos, _preRequisitos, _esObligatorio)


                return True
            
            actua=actua.siguiente
        return False

    def imprimirarbol(self,value,value2):
        actua=self.start_node
        if self.start_node == None:
            print("Vacio")
            return False
        while actua!=None:
            if(actua.nombre==value):
                actua.listasemestre.imprimirarbol(value2)


                return True
            
            actua=actua.siguiente
        return False
    def insertarsemestre(self,value,value2):
        actua=self.start_node
        if self.start_node == None:
            print("Vacio")
            return False
        while actua!=None:
            if(actua.nombre==value):
                actua.listasemestre.insert_at_start(value2)


                return True
            
            actua=actua.siguiente
        return False
    def insert_at_start(self, data):
            if self.start_node is None:
                new_node = Nodomes(data)
                self.start_node = new_node
                print("Hecho")
                return
            if(self.search(data)==True):
                print("ya existe")
            else:
                new_node = Nodomes(data)
                new_node.nref = self.start_node
                self.start_node.pref = new_node
                self.start_node = new_node
    def search(self,value):
        actua=self.start_node
        if self.start_node == None:
            print("Vacio")
            return False
        while actua!=None:
            if(actua.nombre==value):
                print(value)
                return True
            
            actua=actua.siguiente
        return False


class Nodo():
    def __init__(self, nombre):
        self.nombre = nombre
        self.listasemestre=semestre()
        self.listames=DoublyLinkedList()
        self.siguiente = None


class lista_circular():
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def vacia(self):
        return self.primero == None
    
    def arbolinsertar(self,value,value2,_codigo,_nombre,_creditos,_preRequisitos,_esObligatorio):
        aux = self.primero
        encontrado = False
        if self.primero == None:
            print("Vacio")
            return False
        while (True):
            if (aux.nombre == value):
                aux.listlistasemestre.insertararbol(value2,_codigo, _nombre, _creditos, _preRequisitos, _esObligatorio)
                encontrado = True
                break
            aux = aux.siguiente
            if (aux == self.primero):
                break
        if (encontrado == True):
            print("Ya esta en la lista")
        else:
            print("No esta en la lista")
        return encontrado

    def semestreinsert(self,value,value2,):
        aux = self.primero
        encontrado = False
        if self.primero == None:
            print("Vacio")
            return False
        while (True):
            if (aux.nombre == value):
                aux.listlistasemestre.insert_at_start(value2)
                encontrado = True
                break
            aux = aux.siguiente
            if (aux == self.primero):
                break
        if (encontrado == True):
            print("Ya esta en la lista")
        else:
            print("No esta en la lista")
        return encontrado

    
    def imprimirarbol(self,value,value2,value3):
        aux = self.primero
        encontrado = False
        if self.primero == None:
            print("Vacio")
            return False
        while (True):
            if (aux.nombre == value):
                aux.listames.imprimirarbol(value2,value3)
                encontrado = True
                break
            aux = aux.siguiente
            if (aux == self.primero):
                break
        if (encontrado == True):
            print("Ya esta en la lista")
        else:
            print("No esta en la lista")
        return encontrado

    def insertararbol(self,value,value2,value3,_codigo,_nombre,_creditos,_preRequisitos,_esObligatorio):
        aux = self.primero
        encontrado = False
        if self.primero == None:
            print("Vacio")
            return False
        while (True):
            if (aux.nombre == value):
                aux.listames.insertararbol(value2,value3,_codigo,_nombre,_creditos,_preRequisitos,_esObligatorio)
                encontrado = True
                break
            aux = aux.siguiente
            if (aux == self.primero):
                break
        if (encontrado == True):
            print("Ya esta en la lista")
        else:
            print("No esta en la lista")
        return encontrado
            

    def Agregarinicio(self, Nodo):
        if self.primero == None:
            self.primero = Nodo
            self.primero.siguiente = self.primero
        else:
            aux = self.primero
            while aux.siguiente is not self.primero:
                aux = aux.siguiente
            aux.siguiente = Nodo
            Nodo.siguiente = self.primero

    

    def insertarmes(self,value,value2):
        aux=self.primero
        while aux!=None:
            if (aux.nombre == value):
                encontrado = True
                aux.listames.insert_at_start(value2)
                break
            aux = aux.siguiente
            if (aux == self.primero):
                break
    def insertarsemestre(self,value,value2,value3):
        aux = self.primero
        encontrado = False
        if self.primero == None:
            print("Vacio")
            return False
        while (True):
            if (aux.nombre == value):
                aux.listames.insertarsemestre(value2,value3)
                encontrado = True
                break
            aux = aux.siguiente
            if (aux == self.primero):
                break
        if (encontrado == True):
            print("Ya esta en la lista")
        else:
            print("No esta en la lista")
        return encontrado
            

    def agregarfinal(self, Nodo):
        if self.primero == None:
            self.primero = self.ultimo = Nodo
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = Nodo
            self.ultimo.siguiente = self.primero

    def Recorrer(self):
        aux = self.primero
        while aux:
            print(aux.nombre)
            aux = aux.siguiente
            if aux == self.primero:
                break

    def buscar(self, data):
        aux = self.primero
        encontrado = False
        if self.primero == None:
            print("Vacio")
            return False
        while (True):
            if (aux.nombre == data):
                encontrado = True
                break
            aux = aux.siguiente
            if (aux == self.primero):
                break
        if (encontrado == True):
            print("Ya esta en la lista")
        else:
            print("No esta en la lista")
        return encontrado


class nodeavl:
    def __init__(self, value=None,nombre=None,carrera=None,dpi=None,correo=None,Password=None,Creditos=None,edad=None):
        self.value = value
        self.nombre=nombre
        self.carrera=carrera
        self.dpi=dpi
        self.correo=correo
        self.Password=Password
        self.Creditos=Creditos
        self.edad=edad
        self.listaayear=lista_circular()
        self.left_child = None
        self.right_child = None
        self.parent = None  
        self.height = 1

class avl:
    def __init__(self):
        self.root = None
    
    def __repr__(self):
        if self.root == None: return ''
        content='\n'
        cur_nodes = [self.root]
        cur_height = self.root.height
        sep=' '*(2**(cur_height-1))
        while True:
            cur_height += -1
            if len(cur_nodes) == 0: break
            cur_row=' '
            next_row=''
            next_nodes = []

            if all(n is None for n in cur_nodes):
                break

            for n in cur_nodes:
                if n == None:
                    cur_row+='   '+sep
                    next_row+='   '+sep
                    next_nodes.extend([None, None])
                    continue
                if n.value != None:
                    buf=' '*int((5-len(str(n.value)))/2)
                    cur_row+='%s%s%s'%(buf,str(n.value+'*'),buf)+sep
                    
                else:
                    cur_row+=' '*5+sep
                                                                                    
                if n.left_child != None:
                    next_nodes.append(n.left_child)
                    next_row+=' / '+sep
                else:
                    next_row+='  '+sep
                    next_nodes.append(None)
                if n.right_child!=None: 
                    next_nodes.append(n.right_child)
                    next_row+='\ '+sep
                else:
                    next_row+='  '+sep
                    next_nodes.append(None)

            content+=(cur_height*'   '+cur_row+'\n'+cur_height*'   '+next_row+'\n')
            cur_nodes = next_nodes
            sep=' '*int(len(sep)/2)
        return content


    def imprimir2(self):
        if self.root == None: return ''
        content='\n'
        cur_nodes = [self.root]
        co=0
        izquierdo=0
        derecho=""
        derechonombre=""
        derechocarrera=""
        anterior=0
        siguienteiz=""
        siguientede=""
        actual=""
        cur_height = self.root.height
        sep=' '*(2**(cur_height-1))
        MapaRuta = open(r"C:\Users\denni\OneDrive\Desktop\avl.txt",'w')
        MapaRuta.write('digraph {' + "\n")
        MapaRuta.write('rankdir=TB;' + "\n")
        MapaRuta.write('node [shape = record, style=filled, fillcolor=seashell2];' + "\n")
        while True:
            cur_height += -1
            if len(cur_nodes) == 0: break
            cur_row=' '
            next_row=''
            next_nodes = []
            

            if all(n is None for n in cur_nodes):
                break

            for n in cur_nodes:
               
                     
                if n == None:
                    cur_row+='   '+sep
                    next_row+='   '+sep
                    next_nodes.extend([None, None])
                    continue
                if n.value != None:
                    buf=' '*int((5-len(str(n.value)))/2)
                    cur_row+='%s%s%s'%(buf,str(n.value+'*'),buf)+sep
                    co=co+1
                    if(co==1):
                        MapaRuta.write("nodo"+str(n.value)+"[label=\"<C0>|Carnet:"+n.value+"|Nombre:"+n.nombre+"|Descripcion:"+n.carrera+"|<C1>\"];"+ "\n")
                        MapaRuta.write("nodo"+str(n.value)+ "\n")
                        actual="nodo"+str(n.value)
                    else:
                        MapaRuta.write("nodo"+str(n.value)+"[label=\"<C0>|Carnet:"+n.value+"|Nombre:"+n.nombre+"|Descripcion:"+n.carrera+"|<C1>\"];"+ "\n")
                        actual="nodo"+str(n.value)
                else:
                    cur_row+=' '*5+sep
                                                                                    
                if n.left_child != None:
                    next_nodes.append(n.left_child)
                    
                    next_row+=' / '+sep
                    if(co==1):
                        MapaRuta.write("nodo"+str(n.left_child.value)+"[label=\"<C0>|Carnet:"+n.left_child.value+"|Nombre:"+n.left_child.nombre+"|Descripcion:"+n.left_child.carrera+"|<C1>\"];"+ "\n")
                        siguienteiz="nodo"+str(n.left_child.value)  
                    else:   
                        MapaRuta.write("nodo"+str(n.left_child.value)+"[label=\"<C0>|Carnet:"+n.left_child.value+"|Nombre:"+n.left_child.nombre+"|Descripcion:"+n.left_child.carrera+"|<C1>\"];"+ "\n")
                        siguienteiz="nodo"+str(n.left_child.value)                     
                else:
                    next_row+='  '+sep
                    next_nodes.append(None)
                if n.right_child!=None: 
                    next_nodes.append(n.right_child)
                    next_row+='\ '+sep
                    if(co==1):
                        derecho=n.right_child.value
                        derechonombre="nodo"+str(n.value)
                        
                    else:
                        MapaRuta.write("nodo"+str(n.right_child.value)+"[label=\"<C0>|"+n.right_child.value+"|"+n.right_child.nombre+"|"+n.right_child.carrera+"|<C1>\"];"+ "\n")
                        siguientede="nodo"+str(n.right_child.value)  
                else:
                    next_row+='  '+sep
                    next_nodes.append(None)
                if(co==1):
                    h=""
                    if(siguienteiz==""):
                        nada=""
                    else:
                        MapaRuta.write(actual+":<C0>->"+siguienteiz+ "\n")
                else:

                    if(derecho==n.value):
                        MapaRuta.write(derechonombre+":<C1>->"+actual+ "\n")
                        derechonombre=actual
                        print(n.parent.value)
                    elif(n.parent.value==derecho):
                        MapaRuta.write(derechonombre+":<C1>->"+actual+ "\n")
                    elif(n.right_child==None and n.left_child==None):
                        po=""
                    
                    else:
                        if(siguienteiz==""):
                            nada=""
                        else:
                            MapaRuta.write(actual+":<C0>->"+siguienteiz+ "\n")
                        
                        if(siguientede==""):
                            nada=""
                        else:
                            MapaRuta.write(actual+":<C1>->"+siguientede+ "\n")

                siguientede=""
                siguienteiz=""

            content+=(cur_height*'   '+cur_row+'\n'+cur_height*'   '+next_row+'\n')
            cur_nodes = next_nodes
            sep=' '*int(len(sep)/2)
        MapaRuta.write('}')   
        MapaRuta.close()
        os.system("dot -Tsvg "r"C:\Users\denni\OneDrive\Desktop\avl.txt -o "r"C:\Users\denni\OneDrive\Desktop\avl.svg")
        os.system("dot -Tjpg "r"C:\Users\denni\OneDrive\Desktop\avl.txt -o "r"C:\Users\denni\OneDrive\Desktop\avl.jpg") 
        return content

    def search4(self,value,value2):
        if self.root == None:
            print("No hay Datos")
        else:

             return self._search4(value,value2,self.root)
    
    def _search4(self, value,value2, cur_node):
        if value == cur_node.value:
            cur_node.listaayear.Recorrer()
            return True
        elif value<cur_node.value and cur_node.left_child!=None:
            return self._search4(value,cur_node.left_child)
        elif value>cur_node.value and cur_node.right_child!=None:
            return self._search4(value,cur_node.right_child)
        return False

    
    
    def insertarano(self,value,value2):
        if self.root == None:
            print("No hay Datos")
        else:

             return self._search3(value,value2,self.root)
    
    def _search3(self, value,value2, cur_node):
        if value == cur_node.value:
            if(cur_node.listaayear.buscar(value2)==True):
                print()
            else:
                
                cur_node.listaayear.Agregarinicio(Nodo(value2))
            return True
        elif value<cur_node.value and cur_node.left_child!=None:
            return self._search3(value,cur_node.left_child)
        elif value>cur_node.value and cur_node.right_child!=None:
            return self._search3(value,cur_node.right_child)
        return False
    def insertarmes(self, value,value2,value3):
        if self.root == None:
            print("No hay Datos")
        else:

             return self._insertarmes(value,value2,value3,self.root)
    def _insertarmes(self, value,value2,value3, cur_node):
        if value == cur_node.value:
            if(cur_node.listaayear.buscar(value2)==True):
                cur_node.listaayear.insertarmes(value2,value3)
            
            return True
        elif value<cur_node.value and cur_node.left_child!=None:
            return self.insertarmes(value,cur_node.left_child)
        elif value>cur_node.value and cur_node.right_child!=None:
            return self.insertarmes(value,cur_node.right_child)
        return False
    

    def imprimirarbol(self,value,value2,value3,value4):
        hola=""
        if self.root == None:
            print("No hay Datos")
        else:

             return self._imprimirarbol(value,value2,value3,value4,self.root)

    def _imprimirarbol(self,value,value2,value3,value4,cur_node):
        if value == cur_node.value:
            if(cur_node.listaayear.buscar(value2)==True):
                hola=""
                cur_node.listaayear.imprimirarbol(value2,value3,value4)
            return True
        elif value<cur_node.value and cur_node.left_child!=None:
            return self.imprimirarbol(value,cur_node.left_child)
        elif value>cur_node.value and cur_node.right_child!=None:
            return self.imprimirarbol(value,cur_node.right_child)
        return False
    def insertararbol(self,value,value2,value3,value4,_codigo,_nombre,_creditos,_preRequisitos,_esObligatorio):
        hola=""
        if self.root == None:
            print("No hay Datos")
        else:

             return self._insertararbol(value,value2,value3,value4,_codigo,_nombre,_creditos,_preRequisitos,_esObligatorio,self.root)

    
    def _insertararbol(self,value,value2,value3,value4,_codigo,_nombre,_creditos,_preRequisitos,_esObligatorio,cur_node):
        if value == cur_node.value:
            if(cur_node.listaayear.buscar(value2)==True):
                cur_node.listaayear.insertararbol(value2,value3,value4,_codigo,_nombre,_creditos,_preRequisitos,_esObligatorio)
            
            return True
        elif value<cur_node.value and cur_node.left_child!=None:
            return self.insertararbol(value,cur_node.left_child)
        elif value>cur_node.value and cur_node.right_child!=None:
            return self.insertararbol(value,cur_node.right_child)
        return False

    def insertarsemestre(self, value,value2,value3,value4):
        if self.root == None:
            print("No hay Datos")
        else:

             return self._insertarsemestre(value,value2,value3,value4,self.root)
    def _insertarsemestre(self, value,value2,value3,value4 ,cur_node):
        if value == cur_node.value:
            if(cur_node.listaayear.buscar(value2)==True):
                cur_node.listaayear.insertarsemestre(value2,value3,value4)
            
            return True
        elif value<cur_node.value and cur_node.left_child!=None:
            return self.insertarmes(value,cur_node.left_child)
        elif value>cur_node.value and cur_node.right_child!=None:
            return self.insertarmes(value,cur_node.right_child)
        return False

    def insert(self, value,nombre,carrera,dpi,correo,password,creditos,edad):
        if self.root == None:
            self.root = nodeavl(value,nombre,carrera,dpi,correo,password,creditos,edad)
        else:
            self._insert(value, nombre,carrera,dpi,correo,password,creditos,edad,self.root)

    def _insert(self, value,nombre,carrera,dpi,correo,password,creditos,edad, cur_node):
        if value < cur_node.value:
            if cur_node.left_child == None:
                cur_node.left_child = nodeavl(value,nombre,carrera,dpi,correo,password,creditos,edad)
                cur_node.left_child.parent = cur_node
                self._inspect_insertion(cur_node.left_child)
            else:
                self._insert(value,nombre,carrera,dpi,correo,password,creditos,edad, cur_node.left_child)
        elif value > cur_node.value:
            if cur_node.right_child == None:
                cur_node.right_child = nodeavl(value,nombre,carrera,dpi,correo,password,creditos,edad)

                
                cur_node.right_child.parent = cur_node
                self._inspect_insertion(cur_node.right_child)
            else:
                self._insert(value,nombre,carrera,dpi,correo,password,creditos,edad, cur_node.right_child)
        else:
            print('El valor ya existe en el arbol')

    def print_tree(self):
        if self.root != None:
            self._print_tree(self.root)

    def _print_tree(self, cur_node):
        if cur_node != None:
            self._print_tree(cur_node.left_child)
            print('%s, h=%d' % (str(cur_node.value), cur_node.height))
            self._print_tree(cur_node.right_child)

    def height(self):
        if self.root != None:
            return self._height(self.root, 0)
        else:
            return 0

    def _height(self, cur_node, cur_height):
        if cur_node == None:
            return cur_height
        left_height = self._height(cur_node.left_child, cur_height+1)
        right_height = self._height(cur_node.right_child, cur_height+1)
        return max(left_height, right_height)

    def find(self, value):
        if self.root != None:
            return self._find(value, self.root)
        else:
            return None

    def _find(self, value, cur_node):
        if value == cur_node.value:
            return cur_node
        elif value<cur_node.value and cur_node.left_child!=None:
            return self._find(value,cur_node.left_child)
        elif value>cur_node.value and cur_node.right_child!=None:
            return self._find(value,cur_node.right_child)
    
    def delete_value(self,value):
        return self.delete_node(self.find(value))
    def delete_node(self,node):
        if node==None or self.find(node.value)==None:
            print("Node to be deleted not found in the tree!")
            return None
        def min_value_node(n):
            current=n
            while current.left_child!=None:
                current=current.left_child
            return current
        def num_children(n):
            num_children=0
            if n.left_child!=None: num_children+=1
            if n.right_child!=None: num_children+=1
            return num_children
        node_parent=node.parent
        node_children=num_children(node)
        if node_children == 0:
            if node_parent !=None:
                if node_parent.left_child==node:
                    node_parent.left_child=None
                else:
                    node_parent.right_child=None
            else:
                self.root=None
        if node_children == 1:
            if node.left_child!=None:
                child=node.left_child
            else:
                child=node.right_child
            
            if node_parent!=None:
                if node_parent.left_child==node:
                    node_parent.left_child=child
                else:
                    node_parent.right_child=child
            else:
                self.root=child
            
            child.parent=node_parent
        if node_children == 2:
            successor=min_value_node(node.right_child)
            node.value=successor.value
            self.delete_node(successor)
            return
        if node_parent!=None:
            node_parent.height=1+max(self.get_height(node_parent.left_child),self.get_height(node_parent.right_child))
            self._inspect_deletion(node_parent)
    def search(self,value,nombre,carrera,dpi,correo,password,creditos,edad):
        if self.root != None:
            return self._search(value,nombre,carrera,dpi,correo,password,creditos,edad,self.root)
        else:
            return False
    
    def _search(self, value,nombre,carrera,dpi,correo,password,creditos,edad, cur_node):
        if value == cur_node.value:
            cur_node.nombre=nombre
            cur_node.carrera=carrera
            cur_node.dpi=dpi
            cur_node.correo=correo
            cur_node.Password=password
            cur_node.creditos=creditos
            cur_node.edad=edad
            return True
        elif value<cur_node.value and cur_node.left_child!=None:
            return self._search(value,nombre,carrera,dpi,correo,password,creditos,edad,cur_node.left_child)
        elif value>cur_node.value and cur_node.right_child!=None:
            return self._search(value,nombre,carrera,dpi,correo,password,creditos,edad,cur_node.right_child)
        return False
    
    def _inspect_insertion(self,cur_node,path=[]):
        if cur_node.parent==None: return
        path=[cur_node]+path

        left_height =self.get_height(cur_node.parent.left_child)
        right_height=self.get_height(cur_node.parent.right_child)

        if abs(left_height-right_height)>1:
            path=[cur_node.parent]+path
            self._rebalance_node(path[0],path[1],path[2])
            return
        new_height=1+cur_node.height
        if new_height>cur_node.parent.height:
            cur_node.parent.height=new_height
        self._inspect_insertion(cur_node.parent,path)
    def _inspect_deletion(self,cur_node):
        if cur_node==None: return
        left_height =self.get_height(cur_node.left_child)
        right_height=self.get_height(cur_node.right_child)

        if abs(left_height-right_height)>1:
            y=self.taller_child(cur_node)
            x=self.taller_child(y)
            self._rebalance_node(cur_node,y,x)
        self._inspect_deletion(cur_node.parent)
    def _rebalance_node(self,z,y,x):
        if y==z.left_child and x==y.left_child:
            self._right_rotate(z)
        elif y==z.left_child and x==y.right_child:
            self._left_rotate(y)
            self._right_rotate(z)
        elif y==z.right_child and x==y.right_child:
            self._left_rotate(z)
        elif y==z.right_child and x==y.left_child:
            self._right_rotate(y)
            self._left_rotate(z)
        else:
            raise Exception('_rebalance_node: z,y,x node configuration not recognized!')
    def _right_rotate(self,z):
        sub_root=z.parent
        y=z.left_child
        t3=y.right_child
        y.right_child=z
        z.parent=y
        z.left_child=t3
        if t3!=None: t3.parent=z
        y.parent=sub_root
        if y.parent==None:
            self.root=y
        else:
            if y.parent.left_child==z:
                y.parent.left_child=y
            else:
                y.parent.right_child=y
            z.height=1+max(self.get_height(z.left_child),self.get_height(z.right_child))
            y.height=1+max(self.get_height(y.left_child),self.get_height(y.right_child))

    def _left_rotate(self,z):
        sub_root=z.parent 
        y=z.right_child
        t2=y.left_child
        y.left_child=z
        z.parent=y
        z.right_child=t2
        if t2!=None: t2.parent=z
        y.parent=sub_root
        if y.parent==None:
            self.root=y
        else:
            if y.parent.left_child==z:
                y.parent.left_child=y
            else:
                y.parent.right_child=y
        z.height=1+max(self.get_height(z.left_child),self.get_height(z.right_child))
        y.height=1+max(self.get_height(y.left_child),self.get_height(y.right_child))

    def get_height(self,cur_node):
        if cur_node==None: return 0
        return cur_node.height
    
    def taller_child(self,cur_node):
        left=self.get_height(cur_node.left_child)
        right=self.get_height(cur_node.right_child)
        return cur_node.left_child if left>=right else cur_node.right_child

    def search2(self,value):
        if self.root != None:
            return self._search2(value,self.root)
        else:
            return False
    
    def _search2(self, value, cur_node):
        if value == cur_node.value:
            ho=" Carnet:"+cur_node.value+ "\n Nombre:"+cur_node.nombre+ "\n Carrera:"+cur_node.carrera+ "\n DPI:"+cur_node.dpi+ "\n Correo:"+cur_node.correo+ "\n Password:"+cur_node.Password+ "\n Creditos:"+str(cur_node.Creditos)+ "\n Edad:"+str(cur_node.edad)
           # ho=" Carnet:"+cur_node.value+ "\n Nombre:"+cur_node.nombre+ "\n Carrera:"+cur_node.carrera+ "\n DPI:"+cur_node.dpi
            return ho
        elif value<cur_node.value and cur_node.left_child!=None:
            return self._search2(value,cur_node.left_child)
        elif value>cur_node.value and cur_node.right_child!=None:
            return self._search2(value,cur_node.right_child)
        return False
    
    

if __name__=='__main__':
    hola=avl()
    
    hola.insert("20","kjds","jdsjkds","jkdskds","jdsjds","jsdkjds","dsds","jkdskjds")
    print(hola.height())
    print(hola.imprimir2())
    
    print(hola.imprimir2())
    print(hola.search2("20"))
    hola.insertarano("20","2018")
    hola.insertarano("20","2017")
    hola.insertarano("20","2018")
    hola.search4("20","2018")
    hola.insertarmes("20","2018","Octubre")
    
    hola.insert("20","kjds","jdsjkds","jkdskds","jdsjds","jsdkjds","dsds","jkdskjds")
    hola.insertarsemestre("20","2018","Octubre","semestre1")
    hola.insertararbol("20","2018","semestre1",10,"hola",10,"nada","si")
    hola.insertararbol("20","2018","semestre1",20,"holados",20,"nada","si")
    hola.insertararbol("20","2018","semestre1",30,"holados",20,"nada","si")
    hola.insertararbol("20","2018","semestre1",423233232,"holados",20,"nada","si")
    hola.insertararbol("20","2018","semestre1",201700747,"holados",20,"nada","si")
    hola.imprimirarbol("20","2018","semestre1")

    