import turtle
from tkinter import *




def dibujar(tam,angu,lados):
    t= turtle.Pen()
    d=turtle.Pen()
    for x in range (1,lados+1):
        t.forward(tam)
        t.left(angu)
    turtle.getscreen()._root.mainloop()

def perimetro(a,n):
    perimetro= a*n
    print ('El Perimetro de su Figura es: ',perimetro,'m')
    return perimetro
def trianguloarea(base,altura):   
    area=(base*altura)/2
    print ('El Area de su Figura es: ',area,'m2')  

def cuadradoarea(lado):   
    area=lado*lado
    print ('El Area de su Figura es: ',area, 'm2')      
    
def pentaarea(perimetro,apotema):    
    area=(perimetro*apotema)/2
    print ('El Area de su Figura es: ',area, 'm2')      
    

def primero():
    lados=0
    while lados<3 or lados>5:
        lados= int(input('Ingrese los lados de la figura: '))
        if lados<3:
            print ('Incorrecto figura de pocos lados') 
        if lados>5:
            print ('Incorrecto figura de muchos lados') 
            
    if lados==3:
        print ('USTED ESCOJIO UNA FIGURA DE 3 LADOS')
        lado= int(input('Ingrese el lado del Triangulo: '))
        if lado>640 or lado>480:
            print ('El tamaño excede a la Ventana')
            lado= int(input('Ingrese el lado del Triangulo: '))
        altura= int(input('Ingrese la altura del Triangulo: '))
        perimetro(lado,lados)    
        trianguloarea(lado,altura)
        dibujar(lado,120,lados)
        
    if lados==4:
        print ('USTED ESCOJIO UNA FIGURA DE 4 LADOS')
        lado= int(input('Ingrese el lado del Cuadrado: '))
        if lado>640 or lado>480:
            print ('El tamaño excede a la Ventana')
            lado= int(input('Ingrese el lado del Cuadrado: '))
        perimetro(lado,lados)
        cuadradoarea(lado)
        dibujar(lado,90,lados)
        
    if lados==5:
        print ('USTED ESCOJIO UNA FIGURA DE 5 LADOS')
        lado= int(input('Ingrese el lado del Pentagono: '))
        apotema= int(input('Ingrese el Apotema del Pentagono: '))
        if lado>640 or lado>480:
            print ('El tamaño excede a la Ventana')
            lado= int(input('Ingrese el lado del Pentagono: '))
        perimetro(lado,lados)
        pentaarea(perimetro(lado,lados),apotema)    
        dibujar(lado,72,lados)


ven= Tk()
ven.geometry("640x480+0+0")
lblmenu=Label(text='MENU',fg="black",font= ("arial", 17,"bold")).place(x=300,y=110)
lblnombre=Label(text='DAVID REVELO B',fg="black",font= ("arial", 10,"bold")).place(x=500,y=400)
btn1=Button(ven,fg="green",command=primero,text="1.- CALCULAR EL AREA Y PERIMETRO",font= ("arial", 12,"bold"),width=30).place(x=180,y=190)
btn2=Button(ven,fg="green",text="2.- ANIMACION",font= ("arial", 12,"bold"),width=30).place(x=180,y=250)

    
    
