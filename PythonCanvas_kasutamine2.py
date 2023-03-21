from tkinter import *
from tkinter import *
from tkinter import font # vajalik teksti fondi muutmiseks

raam = Tk()
raam.title("Tahvel")
tahvel = Canvas(raam, width=900, height=800, background="white")
tahvel.grid()

# võimalik on muuta joone paksust (width) ja sisu värvi (fill)

tahvel.create_line(110, 690, 110, 500, width=8, fill="#000000")
tahvel.create_line(30, 700, 200, 700, width=4, fill="#202121")


tahvel.create_line(31,50,  300,50, width=52, fill="#037ffc")
tahvel.create_line(31,100,  300,100, width=52, fill="#000000")
tahvel.create_line(31,150,  300,150, width=52, fill="#ced2d6")

tahvel.create_line(31,200,  300,200, width=52, fill="#0d9cbf")
tahvel.create_line(31,250,  300,250, width=52, fill="#dee356")
tahvel.create_line(31,300,  300,300, width=52, fill="#0d9cbf")

tahvel.create_line(31,350,  300,350, width=52, fill="#d63624")
tahvel.create_line(31,400,  300,400, width=52, fill="#f7f5f5")
tahvel.create_line(31,450,  300,450, width=52, fill="#147d2c")

tahvel.create_polygon([30,174],[150,250],[30,325], fill="#000000")
tahvel.create_oval(330, 330, 400, 400, fill="#f7f5f5", activefill="pink", ) 
tahvel.create_oval(330, 335, 400, 405, fill="#0d9cbf", activefill="pink")

tahvel.create_oval(340, 340, 410, 410, fill="#037ffc", activefill="pink")
tahvel.create_line(320,550,  570,550,  width=500 , fill="#a3a7ad")

suur_font = font.Font(family='Algerian', size=20, weight='bold')
tahvel.create_text(370, 310, text="Valgusfoor", font=suur_font, anchor=NW)
tahvel.create_line(420,400,  470,400,  width=45 , fill="red")
tahvel.create_line(420,450,  470,450,  width=45 , fill="yellow")
tahvel.create_line(420,500,  470,500,  width=45 , fill="green")
tahvel.create_line(445 ,530,  445,750,  width=8 , fill="black")
tahvel.create_line(350,760,  530,760,  width=4 , fill="black")



x0=0
y0=0
x1=600
y1=600
a=300
r=(a**2+a**2)**(1/2)
p=(a-r)

for i in range(12):
    x0+=p
    y0+=p
    x1-=p
    y1-=p
    tahvel.create_rectangle(x0,y0,x1,y1,width=1,outline="blue", fill="red")
    tahvel.create_oval(x0,y0,x1,y1,width=1,outline="blue", fill="yellow")
    p=r-a
    r=r-p
    a=((r)*sqrt(2))/2
    tahvel.grid

x1=50
y1=x1*8
for i in range(8):
    for j in range(8):
        x2=i*x1
        y2=j*x1
        if(i+j)%2==0:
            color="white"
        else:
            color="black"
        x=tahvel.create_rectangle(x2,y2,x2+x1,y2+x1,fill=color)

raam.mainloop()
