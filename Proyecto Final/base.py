#Este programa requiere ser ejecutado en la misma carpeta que las imagenes
#La carpeta solo debe contener imagenes, con formatos aceptados desde
#['.jpg','.jpeg','.bmp','png',".gif"] mas algunos otros casos no probados
from Tkinter import *
from PIL import Image, ImageTk
import tkFileDialog as filedialog
import os
carpeta=[]
os.getcwd()
dire = filedialog.askdirectory()
dire=dire.encode("utf-8")
os.chdir(dire)
os.getcwd()
p=os.listdir(dire)
tipos={}
#carpeta= os.getcwd()
#p=os.listdir(carpeta)
#p2=[]
#def conseguir_directorio():
#    dire = filedialog.askdirectory()
#    archivos=os.listdir(dire)
#    for archivo in archivos:
#        print archivo--------------------------------------devuelve los archivos con un nombre erroneo
#        x=archivo
#        p2.append(x)
#    app=Tk()
#    vp=Frame(app)
#    vp.grid(column=0,row=0,padx=(50,50),pady=(10,10))
#    app.mainloop()
#conseguir_directorio()
#print p2
class Imagen:
    def __init__(self,nombre,tipo):
        self.nombre=nombre
        self.tipo=tipo
def hacer_click():
    valor2=entrada_txt.get()
    if valor2 in tipos:
        tipos[valor2].append(foto.nombre)
    else:
        tipos[valor2]=[]
        tipos[valor2].append(foto.nombre)
    #etiqueta.config(text=valor2)
    tipos.keys()
def muestrame(imagen):
    if imagen in p:
        muestra=Tk()
        muestra.geometry("+0+0")
        vp=Frame(muestra)
        vp.grid(column=0,row=0,padx=(50,50),pady=(10,10))
        img=Image.open(imagen)
        img.thumbnail((120,120), Image.ANTIALIAS)
        tkimage = ImageTk.PhotoImage(img)
        vimagen=Label(muestra, image=tkimage)
        vimagen.grid(column=0,row=0)
    else:
        print "Esa imagen no esta en", carpeta
def cuantos_tipos():
    print '''
    Las Clasificaciones Y Sus Cantidades Son:
    '''
    len(tipos.keys())
    for key in tipos:
        print key, len(tipos[key])
def cuantas_img(tipo):
    for valor in tipos[tipo]:
        print valor
for foto in p:
    app = Tk()
    app.title("Prueba Y Error")
    app.geometry("+0+0")
    valor=""
    vp=Frame(app)
    vp.grid(column=0,row=0,padx=(50,50),pady=(10,10))
    try:
        img = Image.open(foto)
        img.thumbnail((400,400), Image.ANTIALIAS)
        foto=Imagen(foto,"")
        tkimage = ImageTk.PhotoImage(img)
        vimagen=Label(app, image=tkimage)
        vimagen.grid(column=0,row=1)
    except:
        x="El archivo" + " " + str(foto) + " " + '''no pudo ser abierto
        esto puede ser por que no es una imagen, puede estar corrupto
        o en un formato no compatible.

        Por favor proceda normalmente'''
        etiqueta3=Label(app,text=x)
        etiqueta3.grid(column=0,row=1)
    #print foto.nombre
    vp.columnconfigure(0,weight=1)
    vp.rowconfigure(0,weight=1)
    etiqueta=Label(vp,text="Cerrado Manual")
    etiqueta.grid(column=4,row=1)
    etiqueta2=Label(vp,text="Que ves?")
    etiqueta2.grid(column=2,row=2)
    entrada_txt=Entry(vp,width=10,textvariable=valor)
    entrada_txt.grid(column=3,row=2)
    valor2=entrada_txt.get()
    boton1=Button(vp,text="Ingresa el Tipo",command=hacer_click)
    boton1.grid(column=4,row=2)
    boton2=Button(vp,text="Abortar",command=quit)
    boton2.grid(column=1,row=1)
    #print foto.tipo
    app.mainloop()
def colage(tipo): #ejemplo
    print "Hola"
    for valor in tipos[tipo]:
        print valor
#posteriormente leera los tipos y abrira el mismo numero
    img2=Image.open("1.jpg")
    img3=Image.open("12.jpg")
    app2=Tk()
    app2.title("Prueba Y Error")
    app2.geometry("480x360+0+0")
    vp2=Frame(app2)
    vp2.grid(column=0,row=0,padx=(0,0),pady=(10,10))
    img2.thumbnail((120,120), Image.ANTIALIAS)
    tkimage2 = ImageTk.PhotoImage(img2)
    vimagen2=Label(app2, image=tkimage2)
    vimagen2.grid(column=0,row=0)
    img3.thumbnail((120,120), Image.ANTIALIAS)
    tkimage3 = ImageTk.PhotoImage(img3)
    vimagen3=Label(app2, image=tkimage3)
    vimagen3.grid(column=1,row=0)
    app2.mainloop()
def protocolage(tipo):
    app2=Tk()
    app2.title("Prueba Y Error")
    app2.geometry("720x480+0+0")
    vp2=Frame(app2)
    vp2.grid(column=0,row=0,padx=(0,0),pady=(10,10))
    boton=Button(vp2,text="Abortar",command=hacer_click).pack
    #boton.grid(column=3,row=2)
    for i in range(len(tipos[tipo])): #temporarl, pasara a ser contar el numero de unidades en tipo
        img=Image.open(tipos[tipo][i])
        img.thumbnail((120,120), Image.ANTIALIAS)
        tkimage = ImageTk.PhotoImage(img)
        vimagen=Label(app2, image=tkimage)
        vimagen.grid(column=i,row=((i)/4))
    app2.mainloop()
print tipos.keys()
cuantos_tipos()
eso=raw_input("Ingrese La categoria a buscar ")
protocolage(eso)
print tipos.keys()
cuantos_tipos()
