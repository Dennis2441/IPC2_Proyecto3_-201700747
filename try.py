import re
import xml.dom.minidom
from datetime import datetime
import datetime

inp="""  <?xml version="1.0" encoding="UTF-8"?><EVENTOS>	<EVENTO>		Guatemala, 20/04/2021		Reportado por: bart@ing.usac.edu.gt		Usuarios afectados: homero@ing.usac.edu.gt, lisa@ing.usac.edu.gt		Error: 20001 - Desbordamiento de b�fer de memoria RAM		en el servidor de correo electr�nico.	</EVENTO>	<EVENTO>		Guatemala, 20/04/2021		Reportado por: homero@ing.usac.edu.gt		Usuarios afectados: bart@ing.usac.edu.gt, lisa@ing.usac.edu.gt		Error: 20002 - Error de destino, momento equivocado,		lugar equivocado y medios equivocados	</EVENTO>	<EVENTO>		Guatemala, 25/04/2021		Reportado por: barni@ing.usac.edu.gt		Usuarios afectados: homero@ing.usac.edu.gt, lisa@ing.usac.edu.gt, 		moe@ing.usac.edu.gt, bart@ing.usac.edu.gt		Error: 20003 - Sobrecarga de informacion	</EVENTO>	<EVENTO>		Guatemala, 20/04/2021		Reportado por: barni@ing.usac.edu.gt		Usuarios afectados: homero@ing.usac.edu.gt, lisa@ing.usac.edu.gt		Error: 20003 - Sobrecarga de informacion	</EVENTO>	<EVENTO>		Guatemala, 25/04/2021		Reportado por: lisa@ing.usac.edu.gt		Usuarios afectados: moe@ing.usac.edu.gt, bart@ing.usac.edu.gt		Error: 20002 - Error de destino, momento equivocado,		lugar equivocado y medios equivocados	</EVENTO>	<EVENTO>		Guatemala, 30/04/2021		Reportado por: mrburns@ing.usac.edu.gt		Usuarios afectados: apu@ing.usac.edu.gt, ned@ing.usac.edu.gt,		edna@ing.usac.edu.gt, moe@ing.usac.edu.gt, bart@ing.usac.edu.gt		Error: 20004 - Demasiados registros enviados,		no hay suficiente espacio de almacenamiento.	</EVENTO>	<EVENTO>		Guatemala, 30/04/2021		Reportado por: milhouse@ing.usac.edu.gt		Usuarios afectados: homero@ing.usac.edu.gt, lisa@ing.usac.edu.gt,		bart@ing.usac.edu.gt, moe@ing.usac.edu.gt		Error: 20003 - Sobrecarga de informacion	</EVENTO>	<EVENTO>		Guatemala, 20/04/2021		Reportado por: nelson@ing.usac.edu.gt		Usuarios afectados: edna@ing.usac.edu.gt, bart@ing.usac.edu.gt		Error: 20001 - Desbordamiento de b�fer de memoria RAM		en el servidor de correo electr�nico.	</EVENTO>	<EVENTO>		Guatemala, 25/04/2021		Reportado por: nelson@ing.usac.edu.gt		Usuarios afectados: moe@ing.usac.edu.gt, bart@ing.usac.edu.gt		Error: 20003 - Sobrecarga de informacion	</EVENTO>	<EVENTO>		Guatemala, 20/04/2021		Reportado por: Ralph321@ing.usac.edu.gt		Usuarios afectados: bart@ing.usac.edu.gt, lisa@ing.usac.edu.gt,		moe@ing.usac.edu.gt, skinner@ing.usac.edu.gt		Error: 20004 - Demasiados registros enviados,		no hay suficiente espacio de almacenamiento.	</EVENTO>	<EVENTO>		Guatemala, 25/04/2021		Reportado por: Ralph321@ing.usac.edu.gt		Usuarios afectados: apu@ing.usac.edu.gt, ned@ing.usac.edu.gt,		edna@ing.usac.edu.gt, moe@ing.usac.edu.gt, bart@ing.usac.edu.gt		Error: 20003 - Sobrecarga de informacion	</EVENTO>	<EVENTO>		Guatemala, 30/04/2021		Reportado por: Ralph321@ing.usac.edu.gt		Usuarios afectados: homero@ing.usac.edu.gt, lisa@ing.usac.edu.gt		Error: 20001 - Desbordamiento de b�fer de memoria RAM		en el servidor de correo electr�nico.	</EVENTO>	<EVENTO>		Guatemala, 30/04/2021		Reportado por: Ralph321@ing.usac.edu.gt		Usuarios afectados: lisa@ing.usac.edu.gt		Error: 20003 - Sobrecarga de informacion	</EVENTO>	<EVENTO>		Guatemala, 15/04/2021		Reportado por: carl092@ing.usac.edu.gt		Usuarios afectados: martin@ing.usac.edu.gt, maggy@ing.usac.edu.gt		Error: 20004 - Peticion no reconocida por el servidor,		not found error.	</EVENTO>	<EVENTO>		Guatemala, 30/04/2021		Reportado por: milhouse@ing.usac.edu.gt		Usuarios afectados: homero@ing.usac.edu.gt, lisa@ing.usac.edu.gt,		bart@ing.usac.edu.gt, moe@ing.usac.edu.gt		Error: 20004 - Peticion no reconocida por el servidor,		not found error.	</EVENTO>	<EVENTO>		Guatemala, 20/04/2021		Reportado por: nelson@ing.usac.edu.gt		Usuarios afectados: edna@ing.usac.edu.gt, bart@ing.usac.edu.gt		Error: 20004 - Peticion no reconocida por el servidor,		not found error.	</EVENTO>	<EVENTO>		Guatemala, 25/04/2021		Reportado por: nelson@ing.usac.edu.gt		Usuarios afectados: moe@ing.usac.edu.gt, bart@ing.usac.edu.gt		Error: 20004 - Peticion no reconocida por el servidor,		not found error.	</EVENTO></EVENTOS>"""






class node_de:
    def __init__(self, fecha=None, Nombre=None,  previous = None, next=None):
        self.fecha = fecha
        self.Nombre = Nombre
        self.previous = previous
        self.next = next
class linked_list_de:
    def __init__ (self, head=None):
        self.head = head
        self.last = head
        self.size = 0
    def vacio(self):
        val=False
        if self.head==None:
            print("Esta Vacio")
            val=True
            
        else:
            val=False
        return val
    def insertar (self, fecha, Nombre):
            if self.size == 0:
                self.head = node_de(fecha = fecha, Nombre = Nombre)
                self.last = self.head
            else:
                new_node = node_de(fecha = fecha, Nombre = Nombre, next=self.head)
                self.head.previous = new_node
                self.head = new_node
            self.size += 1
    def buscar(self,fecha,nombre):
        actual = self.head
        flag=False
        while actual != None:
            if fecha == actual.fecha and nombre==actual.Nombre:
                flag=True
                return True
            actual = actual.next
        return False
    def eliminar(self):
        print()
        if self.vacio():
            print("vacio")
        else:
            node = self.head
            while self.size!=0:
                if(self.head != self.last):
                    self.head=self.head.next
                    self.head.previous=None
                    self.size=self.size-1
                else:
                    self.head=self.last=None
                    self.size=self.size-1


    def imprimir (self):
        global lista_fcu

        if self.head is None:
            return
        node = self.head
        lista_fcu.append(fechausuario(node.fecha, node.Nombre))
        
        while node.next:
            node = node.next
            lista_fcu.append(fechausuario(node.fecha, node.Nombre))
class Token():
    def __init__(self ,fecha, nombre, reportado, afectado,codigo,informacion):
        self.fecha=fecha
        self.nombre = nombre
        self.reportado = reportado
        self.afectado=afectado
        self.codigo=codigo
        self.informacion=informacion


class fechausuario():
    def __init__(self ,fecha, reportado):
        self.fecha=fecha
        self.reportado = reportado
class Fecha():
    def __init__(self ,fecha):
        self.fecha=fecha
        
lista_Token=[]
lista_error=[]
lista_fecha=[]
lista_fcu=[]
lista_final=[]

def analizar(cadena):
    global lista_Token
    global lista_error
    global lista_fecha
    global lista_fcu
    global lista_final
    strin=""
    char = '' #caracter actual
    next_char = '' #caracter siguiente
    lexema = ""
    fecha=""
    nombre=""
    reportado=""
    afectado=""
    codigo=""
    informacion=""
    estado=0
    n=0
    j=0
    y=""
    me=""
    d=""
    l="/"
    date=""
    flag=False
    ver=False
    aceptar=True
    aceptar=True
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
                    date=date+char
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
                        n=0
                        if(aceptar==True):
                            lista_Token.append(Token(fecha, nombre, reportado, afectado, codigo, informacion))
                            lista_final.extend(lista_Token)
                            afectado=""
                        else:
                            
                            aceptar=True 
                            afectado=""   
                        ver=False

                    else:
                        print("no Se PUEDE el cierre de EVENTO")
                        aceptar=False
                        lexema=""
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
                        aceptar=False
                        lexema=""
                    estado=0


        elif(estado==10):
            
            if(char.isalnum() or  char=="/"):
                if(char=="/"):
                    date=date+char
                    print()
                    if(j==0):
                        d=lexema
                        j=1
                        lexema=""
                    elif(j==1):
                        me=lexema
                        j=0
                        lexema=""
                    
                        

                else:    
                    lexema=lexema+char
                    date=date+char
            else:
                y=lexema
                lexema=""
                lexema=y+"-"+me+"-"+d
                if re.search(r"^([0-2][0-9]|3[0-1])(\/|-)(0[1-9]|1[0-2])\2(\d{4})$", date):    
                    print(lexema)
                    print(lexema + " Es una fecha")
                    
                    d = datetime.datetime.strptime(lexema, '%Y-%m-%d')
                    fecha=str(d.strftime('%d/%m/%Y'))
                    lista_fecha.append(Fecha(fecha))
                    print(fecha)
                    
                    estado=0
                    lexema=""
                    date=""
        elif(estado==1):
            if(n==0):
                if(char.isalpha()and next_char.isalpha()):
                    lexema=lexema+char
                elif(","):
                    lexema=lexema+char
                    n=1
                    estado=0
                    print("Nombre")
                    nombre=lexema
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
                    
                    
                    else:
                        print(not okey)
                print(lexema)
        elif(estado==12):

            if(char.isalnum() or char=="@" or char=="."):
                lexema=lexema+char
            
            elif(char.isspace() and lexema=="Usuarios"):
                lexema=lexema+char
            elif(char.isspace()):
                print()
                if re.search(r"^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$", lexema):

                    print(lexema)
                    print("ok al correo "+ lexema)
                   
                        
                    reportado=lexema
                    lista_fcu.append(fechausuario(fecha, reportado))
                    lexema=""
                elif(re.search(r'Usuarios afectados', lexema)):
                    print("ok "+ lexema)
                    estado=13
                    lexema=""
                
                lexema=""
            elif(char==":"):
                if(re.search(r'Usuarios afectados', lexema)):
                    print("ok "+ lexema)
                    estado=13
                    lexema=""
               
                        
            print(lexema)
        elif(estado==13):
            if(char.isalnum() or char=="@" or char=="." or char==":" ):
                lexema=lexema+char
            
            if(char.isspace()):
                print()
                if re.search(r"^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$", lexema):
                    if(afectado==""):
                        afectado=afectado+lexema
                    else:
                        afectado=afectado+","+lexema
                    print(lexema)
                    print("ok al correo "+ lexema)
                    lexema="" 
                elif(re.search(r'Error:', lexema)):
                        print("si es error "+ lexema)
                        estado=14
                        lexema=""
            elif(char==":"):
                if(re.search(r'Error:', lexema)):
                    print("si es error "+ lexema)
                    estado=14
                    lexema=""
                lexema=""
            print(lexema)
        elif(estado==14):

            if(char.isdigit()):
                lexema=lexema+char

            elif(char.isspace()):
                print()
            
            elif(char=="-" or char==":"):
                print(lexema)
                print("error numero :"+ lexema)
                lista_error.append(lexema)
                codigo=lexema
                estado=141
                lexema=""
            print(lexema)
        elif(estado==141):
            if(char.isspace()):
                if(char.isspace() and next_char=="<"):
                   print("infomarcion de error "+ lexema)
                   informacion=lexema
                   lexema="" 
                   flag=False
                   estado=0
                elif(char.isspace() and next_char.isspace()):
                    char=="\n"
                    lexema=lexema+char
                
                else:
                    lexema=lexema+char
            
            else:
                lexema=lexema+char

dou=linked_list_de()               
def ordenar():
    global lista_fcu
    temporal=[]
    temporal.extend(lista_fcu)
    lista_fcu=[]
    fecha=""
    Nombre=""
    for x in temporal:
        fecha=x.fecha
        Nombre=x.reportado
        if(dou.vacio()):
            dou.insertar(fecha, Nombre)
        elif(dou.buscar(fecha, Nombre)==True):
            print()
        else:
            dou.insertar(fecha, Nombre)
    dou.imprimir()
    dou.eliminar()
    if(dou.vacio()):
        print("madasucka")
    
    for i in lista_fcu:
        print(i.reportado+" : "+i.fecha)
lista_fecha2=[]
def ordenarfecha():
    global lista_fecha
    global lista_fecha2
    temporal=[]
    temporal.extend(lista_fecha)
    lista_fecha=[]
    dates=[]
    temp=[]
    fecha=""
    for x in temporal:
        if(fecha==""):
            fecha=x.fecha
            temp.append(fecha)
            lista_fecha2.append(fecha)
        elif(x.fecha==fecha):
            print()
            lista_fecha2.append(fecha)

        else:
            fecha=x.fecha
            temp.append(fecha)
            fecha=x.fecha
            lista_fecha2.append(fecha)
    
        
    for k in temp:
        if k in dates:
            print()
        else:
            dates.append(k)

    dates.sort(key = lambda date: datetime.datetime.strptime(date, '%d/%m/%Y'))

    for y in dates:
        lista_fecha.append(Fecha(y))
        

    for i in lista_fecha:
        print(i.fecha)

class err():
    def __init__(self,codigo,numero):
        self.codigo=codigo
        self.numero=numero
def estadistica():
    global lista_Token
    global lista_fecha
    global lista_fecha2
    global lista_fcu
    error=[]
    error2=[]
    afectado=[]
    error3=[]
    afectado2=[]
    fecha=""
    fecha2=""
    reportado=""
    fecha3=""
    reportado2=""
    reportado3=""
    n=0
    rn=0
    cn=0
    flag=False
    flag2=False
    salida=open("salida.txt","w")
    salida.write("<Estadisticas>" +'\n')
    for x in lista_fecha:
        fecha=x.fecha
        salida.write("  <Estadistica>"+'\n')
        n = lista_fecha2.count(fecha)
        salida.write("    <FECHA>"+fecha+"</FECHA>"+'\n')
        salida.write("    <CANTIDAD_MENSAJES>"+str(n)+"</CANTIDAD_MENSAJES>"+'\n')
        salida.write("    <REPORTADO_POR>"+'\n')
        for i in lista_fcu:
            fecha2=i.fecha
            reportado=i.reportado
            if(fecha==fecha2):
            
                for j in lista_Token:
                    fecha3=j.fecha
                    reportado2=j.reportado
                    print()
                    if(fecha2==fecha3 and reportado==reportado2):
                        rn=rn+1
                        reportado3=reportado
                        r=j.afectado
                        j=j.codigo
                        afectado=afectado+(r.split(","))
                        error.append(j)
                salida.write("     <USUARIO>"+'\n')
                salida.write("      <EMAIL>"+reportado3+"</EMAIL>"+'\n')
                salida.write("      <CANTIDAD_MENSAJES>"+str(rn)+"</CANTIDAD_MENSAJES>"+'\n')
                rn=0

                salida.write("     </USUARIO>"+'\n')
        salida.write("    </AFECTADOS>"+'\n')
        for pp in afectado:
            if pp in afectado2:
                print()
            else:
                afectado2.append(pp)
        for p in afectado2:
            salida.write("     <AFECTADO>"+p+"</AFECTADO>"+'\n')

        salida.write("    </AFECTADOS>"+'\n')
        afectado=[]
        afectado2=[]
        salida.write("    </REPORTADO_POR>"+'\n')
        salida.write("    <ERRORES>"+'\n')
        for mmm in error:
            if mmm in error2:
                print()
            else:
                error2.append(mmm)
        
        for mm in error2:
            
            cn = error.count(mm)
            salida.write("     <CODIGO>"+mm+"</CODIGO>"+'\n')
            salida.write("     <CANTIDAD_MENSAJES>"+str(cn)+"</CANTIDAD_MENSAJES>"+'\n')
        cn=0
        salida.write("    </ERRORES>"+'\n')
        error=[]
        error2=[]
        salida.write("  </Estadistica>"+'\n')
    salida.write("</Estadisticas>")

    salida.close()

    



        
                
analizar(inp)
ordenar()
ordenarfecha()
estadistica()
for i in lista_Token:
    print(i.reportado+" "+i.fecha)
    