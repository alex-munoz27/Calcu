#EJEMPLO INTRODUCCIÓN DE DATOS EN NOTACIÓN POLACA INVERSA: 
#PARA 2+8-3: "2"-->"ENTER"-->"8"-->"ENTER"-->"+"-->"3"-->"ENTER"-->"-"
from tkinter import *
ventana=Tk()
ventana.title("CALCULADORA-RPN")
ventana.configure(background="gray20")
ventana.geometry("392x488")
color_boton=("gray50")
cn=("white")
from math import *

def digit(n):
    global numero
    global l_numeros
    global blocked_ce
    blocked_ce=False
    long=len(l_numeros)
    if long<2 and numero!=str(pi):
        if numero=="0":
            numero=numero.replace("0",n)
        else:
            numero=numero+n
        input_text.set(numero)

def loga():
    global l_numeros
    global numero
    if len(l_numeros)==2:
        try:
            numero=str(eval("log("+l_numeros[0]+")/log("+l_numeros[1]+")")) #l_numeros[0] es el numero y l_numeros[1] es la base
            input_text.set(numero)
            l_numeros[0]=numero
            l_numeros.pop()
        except:
            input_text.set("ERROR")
            l_numeros=[]
        numero=""

def pee():
    global numero
    global l_numeros
    global comas
    global blocked_ce
    if len(l_numeros)<2 and numero=="":
        numero=str(pi)
        input_text.set(numero)
        comas+=1
        blocked_ce=False

def coma():
    global numero
    global comas
    if numero!="" and comas==0:
        numero=numero+"."
        input_text.set(numero)
        comas+=1

def enter():
    global numero
    global l_numeros
    global comas
    global blocked_ce
    if numero!="" and numero!="0.":
        l_numeros.append(numero)
        input_text.set(numero)
        numero=""
        comas=0
        blocked_ce=True
        print(l_numeros)

def operacion(s):
    global numero
    global l_numeros
    if len(l_numeros)==2:
        try:
            numero=str(eval(l_numeros[0]+s+l_numeros[1]))
            input_text.set(numero)
            l_numeros[0]=numero
            l_numeros.pop()
        except:
            input_text.set("ERROR")
            l_numeros=[]
        numero=""
        print(l_numeros)

def funci(s):
    global numero
    global l_numeros
    if len(l_numeros)==1:
        try:
            numero=str(eval(s+"("+l_numeros[0]+")"))
            input_text.set(numero)
            l_numeros[0]=numero
        except:
            input_text.set("ERROR")
            l_numeros=[]
        numero=""
        print(l_numeros)
    
def cambia_signo(): 
    global numero
    global l_numeros
    if numero!="0" and numero!="":
        numero=str(eval(numero+"*(-1)"))
        input_text.set(numero)
    elif numero=="" and len(l_numeros)==1: #nuevo
        if l_numeros[0]!="0":
            l_numeros[0]=str(eval(l_numeros[0]+"*(-1)"))
            input_text.set(l_numeros[0])

def clear():
    global numero
    global l_numeros
    global comas
    numero=""
    l_numeros=[]
    input_text.set("0")
    comas=0

def clear_error():
    global numero
    global comas
    global blocked_ce
    if blocked_ce==False:
        numero=""
        input_text.set("0")
        comas=0
        blocked_ce=True

ancho_boton=6
numero=("")
blocked_ce=False
comas=0
alto_boton=2
input_text=StringVar()
clear()#MUESTRA VALOR "0" AL INICIAR LA CALCULADORA
bd=10
Boton0=Button(ventana,text="0",bg=color_boton,fg=cn,width=ancho_boton,height=alto_boton,command=lambda:digit("0")).place(x=21,y=180)
Boton1=Button(ventana,text="1",bg=color_boton,fg=cn,width=ancho_boton,height=alto_boton,command=lambda:digit("1")).place(x=80,y=180)
Boton2=Button(ventana,text="2",bg=color_boton,fg=cn,width=ancho_boton,height=alto_boton,command=lambda:digit("2")).place(x=139,y=180)
Boton3=Button(ventana,text="3",bg=color_boton,fg=cn,width=ancho_boton,height=alto_boton,command=lambda:digit("3")).place(x=198,y=180)
Boton4=Button(ventana,text="4",bg=color_boton,fg=cn,width=ancho_boton,height=alto_boton,command=lambda:digit("4")).place(x=21,y=228)
Boton5=Button(ventana,text="5",bg=color_boton,fg=cn,width=ancho_boton,height=alto_boton,command=lambda:digit("5")).place(x=80,y=228)
Boton6=Button(ventana,text="6",bg=color_boton,fg=cn,width=ancho_boton,height=alto_boton,command=lambda:digit("6")).place(x=139,y=228)
Boton7=Button(ventana,text="7",bg=color_boton,fg=cn,width=ancho_boton,height=alto_boton,command=lambda:digit("7")).place(x=198,y=228)
Boton8=Button(ventana,text="8",bg=color_boton,fg=cn,width=ancho_boton,height=alto_boton,command=lambda:digit("8")).place(x=257,y=228)
Boton9=Button(ventana,text="9",bg=color_boton,fg=cn,width=ancho_boton,height=alto_boton,command=lambda:digit("9")).place(x=316,y=228)
BotonC=Button(ventana,text="π",bg=color_boton,fg=cn,width=ancho_boton,height=alto_boton,command=pee).place(x=21,y=276)
BotonComa=Button(ventana,text=".",bg=color_boton,fg=cn,width=ancho_boton,height=alto_boton,command=coma).place(x=80,y=276)
BotonSuma=Button(ventana,text="+",bg=color_boton,fg=cn,width=ancho_boton,height=alto_boton,command=lambda:operacion("+")).place(x=139,y=276)
BotonResta=Button(ventana,text="-",bg=color_boton,fg=cn,width=ancho_boton,height=alto_boton,command=lambda:operacion("-")).place(x=198,y=276)
BotonMulti=Button(ventana,text="*",bg=color_boton,fg=cn,width=ancho_boton,height=alto_boton,command=lambda:operacion("*")).place(x=257,y=276)
BotonDiv=Button(ventana,text="/",bg=color_boton,fg=cn,width=ancho_boton,height=alto_boton,command=lambda:operacion("/")).place(x=316,y=276)
BotonSqrt=Button(ventana,text="√",bg=color_boton,fg=cn,width=ancho_boton,height=alto_boton,command=lambda:funci("sqrt")).place(x=21,y=324)
BotonParen1=Button(ventana,text="1/x",bg=color_boton,fg=cn,width=ancho_boton,height=alto_boton,command=lambda:funci("1/")).place(x=198,y=324)
BotonParen2=Button(ventana,text="log",bg=color_boton,fg=cn,width=ancho_boton,height=alto_boton,command=loga).place(x=257,y=324)
BotonResto=Button(ventana,text="%",bg=color_boton,fg=cn,width=ancho_boton,height=alto_boton,command=lambda:operacion("%")).place(x=80,y=324)
Botonln=Button(ventana,text="ln",bg=color_boton,fg=cn,width=ancho_boton,height=alto_boton,command=lambda:funci("log")).place(x=21,y=372)
BotonSn=Button(ventana,text="sin",bg=color_boton,fg=cn,width=ancho_boton,height=alto_boton,command=lambda:funci("sin")).place(x=80,y=372)
BotonCs=Button(ventana,text="cos",bg=color_boton,fg=cn,width=ancho_boton,height=alto_boton,command=lambda:funci("cos")).place(x=139,y=372)
BotonTn=Button(ventana,text="tan",bg=color_boton,fg=cn,width=ancho_boton,height=alto_boton,command=lambda:funci("tan")).place(x=198,y=372)
BotonR=Button(ventana,text="R",bg=color_boton,fg=cn,width=ancho_boton,height=alto_boton,command=lambda:funci("round")).place(x=257,y=372)
BotonCE=Button(ventana,text="CE",bg="red",fg=cn,width=ancho_boton,height=alto_boton,command=clear_error).place(x=257,y=180)
BotonCS=Button(ventana,text="+/-",bg=color_boton,fg=cn,width=ancho_boton,height=alto_boton,command=cambia_signo).place(x=139,y=324)
BotonC=Button(ventana,text="C",bg="red",fg=cn,width=ancho_boton,height=alto_boton,command=clear).place(x=316,y=180)
BotonExp=Button(ventana,text="EXP",bg=color_boton,fg=cn,width=ancho_boton,height=alto_boton,command=lambda:operacion("**")).place(x=316,y=324)
BotonResul=Button(ventana,text="ENTER",bg=color_boton,fg=cn,width=ancho_boton,height=alto_boton,command=enter).place(x=316,y=372)


Salida=Entry(ventana,font=('Arial',20,"bold"),width=21,textvariable=input_text,bd=20,insertwidth=4,bg="lavender",justify="right").place(x=16,y=60)


ventana.mainloop()




