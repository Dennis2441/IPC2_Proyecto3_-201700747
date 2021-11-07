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
        
        s = Source(acumulador[0],filename="arbolB", format="pdf")
        s.view()
        #prog = "dot -Tpng  grafo.dot -o grafo.png"
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

if __name__=='__main__':
    hola=arbolB(5)
    curso1 = Curso(772,"SOG 1",4,"56,89,77",True)
    hola.insertar(curso1)
    curso2 = Curso(7867,"FGG 1",11,"56,89,77",True)
    curso3 = Curso(281,"FGG 1",5,"56,89,77",True)
    curso4 = Curso(787,"FGG 1",5,"56,89,77",True)
    
    hola.insertar(curso2)
    hola.insertar(curso3)
    hola.insertar(curso4)
    hola.insertar(Curso(201700747,"FGG 1",4,"56,89,77",True))
    hola.insertar(Curso(293292323,"FGG 1",5,"56,89,77",True))
    hola.insertar(Curso(423233232,"FGG 1",10,"56,89,77",True))
    hola.graficaB(hola.raiz)
