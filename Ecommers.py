# -*- coding: utf-8 -*-
"""
Created on Sun May 12 20:04:57 2019

@author: MG Techno Soft
"""
''' ---------------------------------------------------------------import packages------------------------------------------------'''
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from tkinter import messagebox
import re
from PIL import Image,ImageTk
import ast
import os
import datetime

'''--------------------------------------------------------creating file/connect with db-----------------------------------------'''

open("udata.csv","a")    #creat a file

'''------------------------------------------------------------------product list-------------------------------------------------'''
Men=[
        {'id':1,'name':'T-shirt','cost':498.00},
        {'id':2,'name':'Shirt','cost':999.00},
        {'id':3,'name':'Kurtas','cost':1099.99},
        {'id':4,'name':'Polos','cost':348.00},
        {'id':5,'name':'Jeans','cost':2399.00},
        {'id':6,'name':'Shorts','cost':356.99},
        {'id':7,'name':'Trouser','cost':499.99},
        {'id':8,'name':'Sportswear','cost':709.99}
]
Women=[
        {'id':1,'name':'Top','cost':599.00},
        {'id':2,'name':'Skirt','cost':576.99},
        {'id':3,'name':'Trouser','cost':499.99},
        {'id':4,'name':'Jeans','cost':1399.00},
        {'id':5,'name':'Salwar','cost':498.99},
        {'id':6,'name':'Dupattas','cost':249.99}
]
Kid=[
        {'id':1,'name':'Shirt for baby boy','cost':287.99},
        {'id':2,'name':'Sleepwear for baby boy','cost':200.00},
        {'id':3,'name':'Shorts for baby boy','cost':150.00},
        {'id':4,'name':'Trouser for baby boy','cost':299.99},
        {'id':5,'name':'Skirts for baby girls','cost':349.99},
        {'id':6,'name':'sleepWear for baby girls','cost':176.99},
        {'id':7,'name':'Shorts for baby girls','cost':189.99},
        {'id':8,'name':'Shirt for baby girls','cost':149.99},
        {'id':9,'name':'Shirt for baby boy','cost':199.99},
        {'id':10,'name':'Sleepwear for baby boy','cost':499.99},
        {'id':11,'name':'Shorts for baby boy','cost':269.99},
        {'id':12,'name':'Trouser for baby boy','cost':199.99},
        {'id':13,'name':'Skirts for baby girls','cost':279.99},
        {'id':14,'name':'sleepWear for baby girls','cost':199.99},
        {'id':15,'name':'Shorts for baby girls','cost':299.99},
        {'id':16,'name':'Shirt for baby girls','cost':349.99},
        
]
Electronics=[
               {'id':1,'name':'Yearphone(sony)','cost':549.00},
               {'id':2,'name':'Yearphone(intex)','cost':699.00},
               {'id':3,'name':'Yearphone(mi)','cost':345.00},
               {'id':4,'name':'Yearphone(samsung)','cost':298.00},
               {'id':5,'name':'Headphone(sony)','cost':1149.00},
               {'id':6,'name':'Headphone(mi)','cost':599.00},
               {'id':7,'name':'Headphone(jbl)','cost':400.00},
               {'id':8,'name':'Charger(samsung)','cost':550.00},
               {'id':9,'name':'Charger(nokia)','cost':399.00},
               {'id':10,'name':'Fan(usha)','cost':1500.00},
               {'id':11,'name':'Fan(philips)','cost':1099.00},
               {'id':12,'name':'Fan(orient)','cost':896.00},
               {'id':13,'name':'Ac(philips)','cost':25000.00},
               {'id':14,'name':'Ac(lg)','cost':30500.00},
               {'id':15,'name':'Hometheater(panasonic)','cost':896.00},
               {'id':16,'name':'Hometheater(philips)','cost':2050.00},
               {'id':17,'name':'Tv(lg)','cost':20050.00},
               {'id':18,'name':'Tv(samsung)','cost':34000.00},
               {'id':19,'name':'Solarpannel(dlight)','cost':87450.00},
               {'id':20,'name':'Solarpannel(philips)','cost':100600.00},
               {'id':21,'name':'Samsung','cost':15599.00},
               {'id':22,'name':'Apple','cost':85000.00},
               {'id':23,'name':'Oneplus','cost':17398.00},
               {'id':24,'name':'Redmi','cost':21840.00},
               {'id':25,'name':'Googlepixel','cost':25000.00},
               {'id':26,'name':'Nokia','cost':17708.00},
               {'id':27,'name':'Apple(mac)','cost':120680.00},
               {'id':28,'name':'Hp','cost':61400.00},
               {'id':29,'name':'Lenovo','cost':55000.00},
               {'id':30,'name':'Acer','cost':57900.00}
]
Grocery=[
               {'id':1,'name':'Rice','cost':56.00},
               {'id':2,'name':'Dal','cost':99.00},
               {'id':3,'name':'Mustad-oil','cost':110.00},
               {'id':4,'name':'Ghee','cost':599.00},
               {'id':5,'name':'Atta(5kg)','cost':300.00},
               {'id':6,'name':'Sugar','cost':50.00},
               {'id':7,'name':'Biscuit','cost':156.00}
]
Sportsnfitness=[
               {'id':1,'name':'Sportsshoe','cost':559.00},
               {'id':2,'name':'Sportsshoe','cost':785.00},
               {'id':3,'name':'Dumbels','cost':539.00},
               {'id':4,'name':'Skipingrope','cost':400.00},
               {'id':5,'name':'Bottol','cost':99.00},
               {'id':6,'name':'Sportswatch','cost':699.00},
               {'id':7,'name':'Badminton-full set','cost':600.00},
               {'id':8,'name':'Football','cost':600.00},
               {'id':9,'name':'Backpack','cost':400.00},
]
'''----------------------------------------------------------------payment function----------------------------------------------'''
def pay(cost):
        variable = messagebox.askquestion('Payment','Are you sure you want to pay ' + str(cost)  + '?')
        if variable == messagebox.YES:
                v=messagebox.showinfo('Payment','Successful')
                if v==messagebox.OK:
                    savedata()
        else :
                messagebox.showinfo('Payment','Order Cancelled')
                


'''-------------------------------------------------------checking and cnformation pay--------------------------------------------'''
def checkout(crt,crtitem):
        qty1=crt
        total_cost=0.0  
        for i,v in enumerate(qty1):
                total_cost +=crtitem[i]['cost']*int(v.get())
                crtitem[i]['QTY']=v.get()
               
        if total_cost == 0.0:
                return
        
        global payment
        global note
        global k
        note.tab(7,state="normal")
        note.tab(9,state="hidden")
        note.select(payment)
        payment.focus()
        
        load=Image.open("pay.jpg").resize((1340,660),Image.ANTIALIAS)
        render=ImageTk.PhotoImage(load)
        img=Label(payment,image=render)
        img.image=render
        img.place(x=0,y=0)
        
        k=Frame(payment)
        k.pack()
        
        f3=Frame(k)
        f3.pack(side=TOP)
        Label(f3,text='ID',width=5,font=("bold",15)).pack(side=LEFT)
        Label(f3,text='Name',width=30,font=("bold",15)).pack(side=LEFT)
        Label(f3,text='QTY',width=10,font=("bold",15)).pack(side=LEFT)
        Label(f3,text='Cost',width=20,font=("bold",15)).pack(side=LEFT)
        Label(f3,text='TotalCost',width=15,font=("bold",15)).pack(side=RIGHT)
        
        
        f2=Frame(k)
        f2.pack()
        scb=Scrollbar(f2)
        c=Canvas(f2,height=700,width=1020,bg="black",yscrollcommand=scb.set)
        scb.config(command=c.yview)
        scb.pack(side=RIGHT,fill=Y)
        c.pack()
        print(crtitem)
        
        
        n=0
        m=0
        for i,product in enumerate(crtitem):
                f4=Frame(c,height=50,width=1010)
                n=n+1
                l=str(n)
                Label(f4,text=l,font=("bold"),width=3).pack(side=LEFT)
                Label(f4,text=product['name'],width=40,font=("bold")).pack(side=LEFT)
                Label(f4,text=qty1[i].get(),width=10).pack(side=LEFT)
                Label(f4,text=product['cost'],width=30,font=("bold")).pack(side=LEFT)
                Label(f4,text=product['cost']*int(qty1[i].get()),width=15).pack(side=RIGHT)
                c.create_window(0,m,window=f4)
                m+=30
                c.config(scrollregion=c.bbox("all"))
                
        #c.create_image(100,0,image=render,anchor="n")
        
        ca.destroy()
        b=Button(payment)
        b.place(relx=0.896,rely=0.044)
        b.configure(text='Pay',width=13,height=2,command=lambda:pay(total_cost),fg="black",bg="Skyblue",font=("bold"))
        b2=Button(payment)
        b2.place(relx=0.896,rely=0.15)
        b2.configure(text='Back',width=13,height=2,command=directmycart,fg="black",bg="Skyblue",font=("bold"))
        
        
        b=Button(payment)
        b.place(relx=0.001,rely=0.01)
        b.configure(text="Home",width=10,bg="red",fg="black",font=("bold"),command=homepage)
        #b1=Button(f6)'''
        f=open(nam+'mycart.txt','w')
        for produc in crtitem:
            f.write("%s\n" %produc)
        f.close()
            
        
'''--------------------------------------------------------clear page for searchpro ----------------------------------------------'''
def clear1(sitem4,products):
    sear.destroy()
    SearPro(sitem4,products)       
  
'''-----------------------------------------------------------search function----------------------------------------------------'''
        
def SearPro(searp,pro):
    sp=searp
    sitem=sp.get()
    sitem1=sitem.title()
    
    j.destroy()
    
    
    global note
    global search
    global sear
    global products
    global qty
    searp=StringVar()
    
    note.tab(3,state="hidden")
    note.tab(5,state="hidden")
    note.tab(6,state="normal")
    note.select(search)
    
    load=Image.open("search2.jpeg").resize((1340,660),Image.ANTIALIAS)
    render=ImageTk.PhotoImage(load)
    img=Label(search,image=render)
    img.image=render
    img.place(x=0,y=0)
    
    sear=Frame(search)
    sear.pack()
    
    f=Frame(sear)
    f.pack(side=TOP)
    Label(f,text="Showing result for : "+sitem,font=("rome",12,"italic"),fg="blue").pack()
    
    sb=Entry(f,fg="Blue",bg='white',textvariable=searp,width=150,highlightbackground='black',highlightthickness=1)
    sb.pack(side=LEFT)
    load=Image.open("sicon.png").resize((26,16),Image.ANTIALIAS)
    render=ImageTk.PhotoImage(load)
    img=Button(f,image=render)
    img.image=render
    img.pack(side=RIGHT)
    img.configure(command=lambda:clear1(searp,ppp))
    
    f1=Frame(sear)
    f1.pack()
    Label(f1,text='ID',width=15,font=("bold",15)).pack(side=LEFT)
    Label(f1,text='Name',width=30,font=("bold",15)).pack(side=LEFT)
    Label(f1,text='Cost',width=18,font=("bold",15)).pack(side=LEFT)
    Label(f1,text='QTY',width=27,font=("bold",15)).pack(side=RIGHT)
    
    f2=Frame(sear)
    f2.pack()
    scb=Scrollbar(f2)
    c=Canvas(f2,height=700,width=1020,bg="pink",yscrollcommand=scb.set)
    scb.config(command=c.yview)
    scb.pack(side=RIGHT,fill=Y)
    c.pack()
    a=0
    #print('ppp is ',pro)
    if pro==[]:
        products=[]
        l=[Men,Women,Kid,Electronics,Grocery,Sportsnfitness]
        for pr in l:
            for product in pr:
                p=product['name']
                if re.search(sitem1,p):
                    products.append(product)
                    print('a')
                    a+=1
                    
                else:
                    continue
                    #print('not found')
        #print(products)
        if a==0:
           Label(c,text='Oops,Product Not Found...!',bg='pink',fg='red',font=('bold',16,'italic')).pack()   
        else:         
            n=0
            i=0    
            qty=[]
            
            #print(products)
            for product in products:
                f1=Frame(c,height=60,width=1000)
                i=i+1
                l=str(i)
               
                Label(f1,text=l,font=("bold"),width=7,bg='pink').pack(side=LEFT)
                Label(f1,text=product['name'],width=45,font=("bold"),bg='pink').pack(side=LEFT)
                Label(f1,text=product['cost'],width=18,font=("bold"),bg='pink').pack(side=LEFT)
                Label(f1,text="",width=15,bg='pink').pack(side=LEFT)
                s=Spinbox(f1, width=12,foreground='white',background='green',from_ = 0, to = 10,font=("bold"))
                s.pack(side=RIGHT)
                qty.append(s) 
                c.create_window(0,n,window=f1)
                
                n+=100
                c.config(scrollregion=c.bbox("all"))
    else:
        n=0
        i=0    
        qty=[]
        products=pro
        #print(products)
        for product in products:
            f1=Frame(c,height=60,width=1000)
            i=i+1
            l=str(i)
           
            Label(f1,text=l,font=("bold"),width=7,bg='pink').pack(side=LEFT)
            Label(f1,text=product['name'],width=45,font=("bold"),bg='pink').pack(side=LEFT)
            Label(f1,text=product['cost'],width=18,font=("bold"),bg='pink').pack(side=LEFT)
            Label(f1,text="",width=15,bg='pink').pack(side=LEFT)
            s=Spinbox(f1, width=12,foreground='white',background='green',from_ = 0, to = 10,font=("bold"))
            s.pack(side=RIGHT)
            qty.append(s) 
            c.create_window(0,n,window=f1)
            
            n+=100
            c.config(scrollregion=c.bbox("all"))
    
    b1=Button(search)
    b1.place(relx=0.90,rely=0.90)
    b1.configure(text='Add To Cart',width=12,bg="brown",fg="white",command=mycart)
    b2=Button(search)
    b2.place(relx=0.90,rely=0.80)
    b2.configure(text="Clear",width=12,bg="blue",fg="white",command=lambda:clear1(sp,products))
    b1=Button(search)
    b1.place(relx=0.0030,rely=0.01,relwidth=0.10,relheight=0.05)
    b1.configure(text="Home",command=homepage,fg='red',bg='black')
     
    search.option_add('*tearOff',False)
    mb = Menubutton (search) 
    mb.place(relx=0.90,rely=0.01)
    mb.configure(text = 'Sort by')
    mb.menu = Menu ( mb ) 
    mb['menu'] = mb.menu 
    mb.menu.add_command( label = 'Price:Low to High',command=lambda:sorting('low','search',sp)) 
    mb.menu.add_command( label = 'Price:High to Low',command=lambda:sorting('high','search',sp)) 
    
    
    
'''----------------------------------------------------------------clear -------------------------------------------------------'''     
    
def clear(Products):
    j.destroy()
    LoadProducts(Products)
 
'''-----------------------------------------------------------product function---------------------------------------------------'''
def LoadProducts(Products):
    global products
    products=Products
    print("product")
    car.destroy()
    sear.destroy()
    global note
    global item
    global j
    global qty
    searp=StringVar()
    
    
    sitem=StringVar(value="null")
    note.tab(3,state='hidden')
    note.tab(5,state='normal')
    note.tab(9,state='hidden')
    note.tab(10,state='hidden')
    
    note.select(item)
    
    load=Image.open("shopping2.jpg").resize((1340,660),Image.ANTIALIAS)
    render=ImageTk.PhotoImage(load)
    img=Label(item,image=render)
    img.image=render
    img.place(x=0,y=0)
    
    j=Frame(item)
    j.pack()
    
    j1=Frame(j)
    j1.pack(side=TOP)
    sb=Entry(j1,fg="Blue",bg='white',textvariable=searp,width=150,highlightbackground='black',highlightthickness=1)
    sb.pack(side=LEFT)
    load=Image.open("sicon.png").resize((26,16),Image.ANTIALIAS)
    render=ImageTk.PhotoImage(load)
    img=Button(j1,image=render)
    img.image=render
    img.pack(side=RIGHT)
    img.configure(command=lambda:SearPro(searp,ppp))
    
    f1=Frame(j)
    f1.pack()
    Label(f1,text='ID',width=15,font=("bold",15)).pack(side=LEFT)
    Label(f1,text='Name',width=30,font=("bold",15)).pack(side=LEFT)
    Label(f1,text='Cost',width=18,font=("bold",15)).pack(side=LEFT)
    Label(f1,text='QTY',width=27,font=("bold",15)).pack(side=RIGHT)
    
    f2=Frame(j)
    f2.pack()
    scb=Scrollbar(f2)
    c=Canvas(f2,height=700,width=1020,bg="pink",yscrollcommand=scb.set)
    scb.config(command=c.yview)
    scb.pack(side=RIGHT,fill=Y)
    c.pack()
    n=0
    i=0    
    qty=[]
    for product in products:
        f1=Frame(c,height=60,width=1000)
        i=i+1
        l=str(i)
       
        Label(f1,text=l,font=("bold"),width=7,bg='pink').pack(side=LEFT)
        Label(f1,text=product['name'],width=45,font=("bold"),bg='pink').pack(side=LEFT)
        Label(f1,text=product['cost'],width=18,font=("bold"),bg='pink').pack(side=LEFT)
        Label(f1,text="",width=15,bg='pink').pack(side=LEFT)
        s=Spinbox(f1, width=12,foreground='white',background='green',from_ = 0, to = 10,font=("bold"))
        s.pack(side=RIGHT)
        qty.append(s) 
        c.create_window(0,n,window=f1)
        
        n+=100
        c.config(scrollregion=c.bbox("all"))
    
    b1=Button(item)
    b1.place(relx=0.90,rely=0.90)
    b1.configure(text='Add To Cart',width=12,bg="brown",fg="white",command=mycart)
    b2=Button(item)
    b2.place(relx=0.90,rely=0.80)
    b2.configure(text="Clear",width=12,bg="blue",fg="white",command=lambda:clear(Products))
    b1=Button(item)
    b1.place(relx=0.0030,rely=0.01,relwidth=0.10,relheight=0.05)
    b1.configure(text="Home",command=homepage,fg='red',bg='black')
    
    item.option_add('*tearOff',False)
    mb = Menubutton (item) 
    mb.place(relx=0.90,rely=0.01)
    mb.configure(text = 'Sort by')
    mb.menu = Menu ( mb ) 
    mb['menu'] = mb.menu 
    mb.menu.add_command( label = 'Price:Low to High',command=lambda:sorting('low','lodeproduct','null')) 
    mb.menu.add_command( label = 'Price:High to Low',command=lambda:sorting('high','lodeproduct','null')) 
    
'''-----------------------------------------------------------------------sort---------------------------------------------------'''
def sorting(v,fn,sitem4):
    print('sorting')
    p=[]
    ppp=[]
    for pr in products:
            p.append(pr['cost'])
    if v=='low':
        p.sort()
        for p1 in p:
             for product in products:
                 if product['cost']==p1:
                    if product in ppp:
                        continue
                    else:
                        #print(p1,'in',product)
                        ppp.append(product)
                        break
        #j.destroy()
        #LoadProducts(ppp)
    else:
        p.sort(reverse=True)
        for p1 in p:
             for product in products:
                 if product['cost']==p1:
                    if product in ppp:
                        continue
                    else:
                        #print(p1,'in',product)
                        ppp.append(product)
                        break
    if fn=='lodeproduct': 
        j.destroy()
        LoadProducts(ppp)
    else:
        print(sitem4.get())
        sear.destroy()
        SearPro(sitem4,ppp)

'''------------------------------------------------------------------orderd/product----------------------------------------------'''
def prod():
    print("product profile")
    note.tab(5,state="hidden")
    note.tab(6,state="hidden")
    note.tab(10,state="normal")
'''---------------------------------------------------------------------my cart--------------------------------------------------'''
def mycart():
    print("my cart")
    qty1=qty
    
    global note
    global cart
    global car
    
    note.tab(5,state="hidden")
    note.tab(6,state="hidden")
    note.tab(9,state="normal")
    note.tab(10,state="hidden")
    
    note.select(cart)
    
    load=Image.open("cart.jpg").resize((1340,660),Image.ANTIALIAS)
    render=ImageTk.PhotoImage(load)
    img=Label(cart,image=render)
    img.image=render
    img.place(x=0,y=0)
    
    car=Frame(cart)
    car.pack()
    
    fr1=Frame(car)
    fr1.pack(side=TOP)
    Label(fr1,text='ID',width=15,font=("bold",15)).pack(side=LEFT)
    Label(fr1,text='Name',width=30,font=("bold",15)).pack(side=LEFT)
    Label(fr1,text='Cost',width=18,font=("bold",15)).pack(side=LEFT)
    Label(fr1,text='QTY',width=27,font=("bold",15)).pack(side=RIGHT)
    
    fr2=Frame(car)
    fr2.pack()
    scb=Scrollbar(fr2)
    c1=Canvas(fr2,height=700,width=1020,bg="pink",yscrollcommand=scb.set)
    scb.config(command=c1.yview)
    scb.pack(side=RIGHT,fill=Y)
    c1.pack()
    
    n=0
    m=0
    crt=[]
    crtitem=[]
    with open(nam+"mycart.txt",'a')as f:
        for i,product in enumerate(products):
            if qty1[i].get() == '0':
                    continue
            product['QTY']=qty1[i].get()
            f.write("%s\n" % product)
    f=open(nam+"mycart.txt")
    data=f.read()
    dat=data.split('\n')
    g=len(dat)
    if g==1:
            fr4=Frame(c1,height=60,width=1000)
            Label(fr4,text="OOPS!...No Item In Cart",font=("bold",18,"italic"),fg="red",bg="pink").pack()
            c1.create_window(20,30,window=fr4)
            c1.config(scrollregion=c1.bbox("all"))
    for o,da in enumerate(dat):
        if o==g-1:
            break
        else:
            d=ast.literal_eval(da)
            crtitem.append(d)
            fr4=Frame(c1,height=60,width=1000)
            n=n+1
            l=str(n)
            Label(fr4,text=l,font=("bold"),width=7).pack(side=LEFT)
            Label(fr4,text=d['name'],width=45,font=("bold")).pack(side=LEFT)
            Label(fr4,text=d['cost'],width=18,font=("bold")).pack(side=LEFT)
            Label(fr4,text="",width=15).pack(side=LEFT)
            sb=StringVar(value=d['QTY'])
            s1=Spinbox(fr4, width=12,foreground='white',background='green',from_ = 0, to = 10,font=("bold"),textvariable=sb)
            s1.pack(side=RIGHT)
            crt.append(sb) 
            c1.create_window(0,m,window=fr4)
            m+=100
            c1.config(scrollregion=c1.bbox("all"))
        
    f.close()  
    qty1=[]   
    
    '''b0=Button(cart)
    b0.place(relx=0.892,rely=0.01,relwidth=0.10,relheight=0.06)
    b0.configure(text='Delete',fg='yellow',bg='red',command=deleteall)'''
    
    b=Button(cart)
    b.place(relx=0.892,rely=0.70,relwidth=0.10,relheight=0.06)
    b.configure(text="Pay",fg='green',bg='skyblue',command=lambda:checkout(crt,crtitem))
      
    
    b1=Button(cart)
    b1.place(relx=0.0030,rely=0.01,relwidth=0.10,relheight=0.05)
    b1.configure(text="Home",command=homepage,fg='red',bg='black')
    
    j.destroy()
    b2=Button(cart)
    b2.place(relx=0.0030,rely=0.07,relwidth=0.10,relheight=0.05)
    b2.configure(text="Back",fg='red',bg='blue',command=lambda:LoadProducts(products))


'''------------------------------------------------------------mycart for direct access------------------------------------------'''
def directmycart():
    car.destroy()
    k.destroy()
    global note
    global cart
    global ca
    
    note.tab(3,state="hidden")
    note.tab(7,state="hidden")
    note.tab(9,state="normal")
    
    note.select(cart)
    
    load=Image.open("cart.jpg").resize((1340,660),Image.ANTIALIAS)
    render=ImageTk.PhotoImage(load)
    img=Label(cart,image=render)
    img.image=render
    img.place(x=0,y=0)
    
    ca=Frame(cart)
    ca.pack()
    
    fr1=Frame(ca)
    fr1.pack(side=TOP)
    Label(fr1,text='ID',width=15,font=("bold",15)).pack(side=LEFT)
    Label(fr1,text='Name',width=30,font=("bold",15)).pack(side=LEFT)
    Label(fr1,text='Cost',width=18,font=("bold",15)).pack(side=LEFT)
    Label(fr1,text='QTY',width=27,font=("bold",15)).pack(side=RIGHT)
    
    fr2=Frame(ca)
    fr2.pack()
    scb=Scrollbar(fr2)
    c1=Canvas(fr2,height=700,width=1020,bg="pink",yscrollcommand=scb.set)
    scb.config(command=c1.yview)
    scb.pack(side=RIGHT,fill=Y)
    c1.pack()
    
    n=0
    m=0
    crt=[]
    crtitem=[]
    
    f=open(nam+"mycart.txt")
    data=f.read()
    dat=data.split('\n')
    g=len(dat)
    if g==1:
            fr4=Frame(c1,height=60,width=1000)
            Label(fr4,text="OOPS!...No Item In Cart",font=("bold",18,"italic"),fg="red",bg="pink").pack()
            c1.create_window(20,30,window=fr4)
            c1.config(scrollregion=c1.bbox("all"))
    for o,da in enumerate(dat):
        if o==g-1:
            break
        else:
            d=ast.literal_eval(da)
            crtitem.append(d)
            fr4=Frame(c1,height=60,width=1000)
            n=n+1
            l=str(n)
            Label(fr4,text=l,font=("bold"),width=7).pack(side=LEFT)
            Label(fr4,text=d['name'],width=45,font=("bold")).pack(side=LEFT)
            Label(fr4,text=d['cost'],width=18,font=("bold")).pack(side=LEFT)
            Label(fr4,text="",width=15).pack(side=LEFT)
            sb=StringVar(value=d['QTY'])
            s1=Spinbox(fr4, width=12,foreground='white',background='green',from_ = 0, to = 10,font=("bold"),textvariable=sb)
            s1.pack(side=RIGHT)
            crt.append(sb) 
            c1.create_window(0,m,window=fr4)
            m+=100
            c1.config(scrollregion=c1.bbox("all"))
        
    f.close()  
    '''b0=Button(cart)
    b0.place(relx=0.892,rely=0.01,relwidth=0.10,relheight=0.06)
    b0.configure(text='Delete',fg='yellow',bg='red',command=deleteall)'''
    
    
    b=Button(cart)
    b.place(relx=0.892,rely=0.70,relwidth=0.10,relheight=0.06)
    b.configure(text="Pay",fg='green',bg='skyblue',command=lambda:checkout(crt,crtitem))
     
    
    b1=Button(cart)
    b1.place(relx=0.0030,rely=0.01,relwidth=0.10,relheight=0.05)
    b1.configure(text="Home",command=homepage,fg='red',bg='black')
    
'''--------------------------------------------------------------------save data-------------------------------------------------'''
def savedata():
        h=open(nam+'myorder.txt')
        h1=h.read()
        h2=h1.split('\n')
        if h2==['']:
            print('null')
        else:
            pp=open(nam+'myorder.txt','a')
            pp.write('%s'%'new')
            pp.close()
        h.close()
    
        with open(nam+"mycart.txt")as f:
            data=f.read()
            dat=data.split("\n")
            g=len(dat)
            with open(nam+"myorder.txt",'a') as gg:
                
               currentDT=datetime.datetime.now()
               time=(currentDT.strftime("%I:%M:%S %p"))
               date=(currentDT.strftime("%a, %b, %d, %Y"))
               gg.write("%s\n"%time)
               gg.write("%s\n"%date)
               
               for i,da in enumerate (dat):
                    if i==g-1:
                       break
                    else:
                        d=ast.literal_eval(da)
                        d.update({'id':i+1})
                        gg.write("%s\n" % d)
            gg.close()
        f.close()
        print("finish")
        f=open(nam+'mycart.txt','w')
        f.close()
        print("file removed")
'''--------------------------------------------------------------------my orderd-------------------------------------------------'''
def myorderd():
        print("my order")
        k.destroy()
        global orderd
        global note
        global y
        note.tab(3,state="hidden")
        note.tab(7,state="hidden")
        note.tab(10,state="normal")
        
        note.select(orderd)
        
        load=Image.open("orderd.jpg").resize((1340,660),Image.ANTIALIAS)
        render=ImageTk.PhotoImage(load)
        img=Label(orderd,image=render)
        img.image=render
        img.place(x=0,y=0)
        
        y=Frame(orderd)
        y.pack()
        
        f=open("login.txt",'r')
        z=f.read()
        a=ast.literal_eval(z)
        y1=Frame(y)
        y1.pack()
        name=a[0].title()
        Label(y1,text='Hello '+name,font=('italic',15,'underline'),fg='green').pack()
        
        scb=Scrollbar(y)
        c=Canvas(y,height=600,width=900,bg="orange",yscrollcommand=scb.set)
        scb.config(command=c.yview)
        scb.pack(side=RIGHT,fill=Y)
        c.pack()
        l=open(nam+'myorder.txt')
        l1=l.read()
        hi8=20
        col=80
        l2=l1.split('new')
        for m,i1 in enumerate (l2):
                print(m)
                y2=Frame(c,width=800,height=70)
                Label(y2,text='Address : '+a[2],font=('italic'),bg='orange').pack(side=TOP)
                Label(y2,text='name',width=20,bg='orange',fg='red').pack(side=LEFT)
                Label(y2,text='price',width=20,bg='orange',fg='red').pack(side=LEFT)  
                Label(y2,text='quantity',width=20,bg='orange',fg='red').pack(side=LEFT)  
                Label(y2,text='total',width=20,bg='orange',fg='red').pack(side=RIGHT)
                c.create_window(470,hi8,window=y2)
                c.config(scrollregion=c.bbox("all"))
                
                dat=i1.split('\n')
                tc=0
                time=''
                date=''
                g=len(dat)
                for i,da in enumerate (dat):
                    if i==g-1:
                       hi8+=40*(i+10)
                       print('break')
                       break
                    else:
                        if i==0:
                           time=da
                           continue
                        elif i==1:
                           date=da
                           continue
                        else:
                            d=ast.literal_eval(da)
                            y3=Frame(c,width=1000,height=10)
                            Label(y3,text=d['name'],width=20,bg='orange').pack(side=LEFT)
                            Label(y3,text=d['cost'],width=20,bg='orange').pack(side=LEFT)
                            Label(y3,text=d['QTY'],width=20,bg='orange').pack(side=LEFT)
                            p=int(d['QTY'])
                            e=d['cost']*p
                            Label(y3,text=e,width=20,bg='orange').pack(side=RIGHT)
                            c.create_window(470,col,window=y3)
                            col+=20
                            tc+=e
                            
                y4=Frame(c,height=30)
                
                Label(y4,text=time ,bg='orange',fg='blue').pack(side=LEFT)
                Label(y4,text=date ,bg='orange',fg='blue').pack(side=LEFT)
                Label(y4,text='',bg='orange',width=36).pack(side=LEFT)
                #Label(y4,text='',bg='orange').pack()
                Label(y4,text='All Total : ',bg='orange',fg='green').pack(side=LEFT)
                Label(y4,text=tc,bg='orange',fg='green').pack(side=RIGHT)
                Label(y4,text='',bg='orange').pack()
                c.create_window(443,col+20,window=y4)
                col=0       
                col+=hi8+60
                c.config(scrollregion=c.bbox("all"))
                        
                        
        
        btn1=Button(orderd)
        btn1.place(relx=0.01,rely=0.01,relwidth=0.10)
        btn1.configure(text="Home",bg='black',fg='red',font=('italic'),command=homepage)

'''-------------------------------------------------------------------notification-----------------------------------------------'''
def noti():
    print("notification")
    global note
    global notification
    
    note.tab(3,state="hidden")
    note.tab(8,state="normal")
    
    note.select(notification)
    
    load=Image.open("notify.jpg").resize((1340,660),Image.ANTIALIAS)
    render=ImageTk.PhotoImage(load)
    img=Label(notification,image=render)
    img.image=render
    img.place(x=0,y=0)
    
    b1=Button(notification)
    b1.place(relx=0.0030,rely=0.01,relwidth=0.10,relheight=0.05)
    b1.configure(text="Home",command=homepage,fg='red',bg='black')
    
'''--------------------------------------------------------------------my account------------------------------------------------'''
def account():
    print("my account")
    global note
    global ac
    global accoun
    note.tab(3,state="hidden")
    note.tab(4,state="normal")
    
    note.select(ac)
    
    
    load=Image.open("emarcket.jpg").resize((1340,660),Image.ANTIALIAS)
    render=ImageTk.PhotoImage(load)
    img=Label(ac,image=render)
    img.image=render
    img.place(x=0,y=0)
    
    accoun=Frame(ac)
    accoun.place(relx=0.20,rely=0.10,relwidth=0.60,relheight=0.80)
    accoun.configure(bg='grey')
    
    log=open('login.txt','r')
    f1=log.read()
    f2=ast.literal_eval(f1)
    log.close()
    
    load=Image.open("img.png").resize((120,120),Image.ANTIALIAS)
    render=ImageTk.PhotoImage(load)
    img=Label(accoun,image=render)
    img.image=render
    img.place(x=370,y=30)
    
    n1=StringVar(value=f2[0])
    n2=StringVar(value=f2[1])
    e=StringVar(value=f2[2])
    pw=StringVar(value=f2[3])
    p=StringVar(value=f2[4])
    
    namee=Label(accoun)
    namee.place(relx=0.20,rely=0.40)
    namee.configure(text="First Name:",font=(11),fg="red",bg='grey')
    
    lname=Label(accoun)
    lname.place(relx=0.20,rely=0.50)
    lname.configure(text="Last Name:",font=(11),fg="red",bg='grey')
    
    email=Label(accoun)
    email.place(relx=0.20,rely=0.60)
    email.configure(text="Email Id:",font=(11),fg="red",bg='grey')
    
    ph=Label(accoun)
    ph.place(relx=0.20,rely=0.70)
    ph.configure(text="Phone no:",font=(11),fg="red",bg='grey')
    
    password=Label(accoun)
    password.place(relx=0.20,rely=0.80)
    password.configure(text="Password:",font=(11),fg="red",bg='grey')
    
    fname=Entry(accoun)
    fname.place(relx=0.40,rely=0.40,relwidth=0.40)
    fname.configure(font=('italic',11),fg='green',textvariable=n1)
    
    lname=Entry(accoun)
    lname.place(relx=0.40,rely=0.50,relwidth=0.40)
    lname.configure(font=('italic',11),fg='green',textvariable=n2)
    
    em=Entry(accoun)
    em.place(relx=0.40,rely=0.60,relwidth=0.40)
    em.configure(font=('italic',11),fg='green',textvariable=e)
    
    pho=Entry(accoun)
    pho.place(relx=0.40,rely=0.70,relwidth=0.40)
    pho.configure(font=('italic',11),fg='green',textvariable=p)
    
    pasw=Entry(accoun)
    pasw.place(relx=0.40,rely=0.80,relwidth=0.40)
    pasw.configure(font=('italic',11),fg='green',textvariable=pw)
    
    b2=Button(accoun)
    b2.place(relx=0.80,rely=0.90,relwidth=0.08,relheight=0.06)
    b2.configure(text="Change",command=lambda:change(n1,n2,e,pw,p),fg='red',bg='green')
    
    
    b1=Button(ac)
    b1.place(relx=0.0030,rely=0.01,relwidth=0.10,relheight=0.05)
    b1.configure(text="Home",command=homepage,fg='red',bg='black')
'''-------------------------------------------------------change----------------------------------------------------------------'''
def change(n1,n2,e,pw,p):
    print('got')
    
    n1=n1.get()
    n2=n2.get()
    e=e.get()
    pw=pw.get()
    p=p.get()
    
    accoun.destroy()
    
    li=[n1,n2,e,pw,p]
    f=open('login.txt','r')
    aa=f.read()
    le=ast.literal_eval(aa)
    f.close()
    f4=[]
    with open('udata.csv','r')as f:
            f1=f.read()
            f2=f1.split('\n')
            #print(len(f2))
            for i,f3 in enumerate (f2):
               # print(le[2],f3)
                if re.search(le[2],f3):
                    print('found')
                    
                else:
                    if len(f2)==i+1:
                        break
                    else:
                        f4.append(f3)
                        
    #print(f4)
    os.remove('udata.csv')
    print('remove successfully')
    for d in f4:
        s=d.split(',')
        with open ('udata.csv','a')as f:
            f.write('{},{},{},{},{}\n'.format(s[0],s[1],s[2],s[3],s[4]))
            f.close()
    with open ('udata.csv','a') as f:
        f.write('{},{},{},{},{}\n'.format(n1,n2,e,pw,p))
        f.close
        
    with open ('login.txt','w')as f:
        f.write('%s\n'%li)
        f.close
    
    account()
    
'''----------------------------------------------------warning for quit from application-----------------------------------------'''
def warningmsg():
    print('quit')
    msg=tkinter.messagebox.askyesno("???","Are you sure, you want to quit from application?" )
    if msg==True:
        root2.destroy()
'''----------------------------------------------------------------------ask-----------------------------------------------------'''
def ask():
    print("ask")
    msg=messagebox.askokcancel('!','Are you sure you want to logout?')
    if msg==True:
        os.remove('login.txt')
        logi()
'''--------------------------------------------------------------------home page-------------------------------------------------'''
def homepage():
    print("homepage")
    y.destroy()
    j.destroy()
    k.destroy()
    sear.destroy()
    ca.destroy()
    global nam
    nam=''
    with open('login.txt','r')as f:
        rd=f.read()
        a1=ast.literal_eval(rd)
        nam=a1[0]
        f.close()
    
    open(nam+'mycart.txt','a')
    open(nam+'myorder.txt','a')
    
    
    global note
    global home
    global hofr
    searp=StringVar()
    
    
    note.tab(0,state='hidden')
    note.tab(1,state='hidden')
    note.tab(3,state='normal')
    note.tab(4,state='hidden')
    note.tab(5,state='hidden')
    note.tab(6,state='hidden')
    note.tab(7,state='hidden')
    note.tab(8,state='hidden')
    note.tab(9,state='hidden')
    note.tab(10,state='hidden')
    
    note.select(home)
    
    load=Image.open("shopping3.jpg").resize((1340,660),Image.ANTIALIAS)
    render=ImageTk.PhotoImage(load)
    img=Label(home,image=render)
    img.image=render
    img.place(x=0,y=0)
    
    
    home.option_add('*tearOff',False)
    mb = Menubutton (home) 
    mb.place(relx=0.001,rely=0.00)
    mb.configure(text = 'Menu')
    mb.menu = Menu ( mb ) 
    mb['menu'] = mb.menu 
    mb.menu.add_command( label = 'My Account',command=account ) 
    mb.menu.add_command( label = 'Notification',command=noti) 
    mb.menu.add_command( label = 'My Cart',command=directmycart)
    mb.menu.add_command( label = 'My Orderd',command=myorderd)
    mb.menu.add_separator()
    mb.menu.add_command( label = 'Setting'  ) 
    mb.menu.add_command( label = 'About'  )
    mb.menu.add_command( label = 'Help' )
    mb.menu.add_separator()
    mb.menu.add_command( label = 'Logout',command=ask) 
    mb.menu.add_command( label = 'Quit' ,command=warningmsg) 
      


    cat = Menubutton (home) 
    cat.place(relx=0.05,rely=0.00)
    cat.configure(text = 'Catagories')
    cat.menu = Menu ( cat ) 
    cat['menu'] = cat.menu 
    
    
    cat.menu.add_command( label = 'Men',command=lambda:LoadProducts(Men))
    cat.menu.add_separator()
    cat.menu.add_command( label = 'Women',command=lambda:LoadProducts(Women))
    cat.menu.add_separator()
    cat.menu.add_command( label = 'kids',command=lambda:LoadProducts(Kid))
    cat.menu.add_separator()
    cat.menu.add_command( label = 'Electronics/Electricals',command=lambda:LoadProducts(Electronics))
    cat.menu.add_separator()
    cat.menu.add_command( label = 'grocery',command=lambda:LoadProducts(Grocery))
    cat.menu.add_separator()
    cat.menu.add_command( label = 'Sports/Fitness',command=lambda:LoadProducts(Sportsnfitness))
    
    sb=Entry(home)
    sb.place(relx=0.150,rely=0.004,relwidth=0.700,relheight=0.040)
    sb.configure(fg="Blue",textvariable=searp)
    load=Image.open("sicon.png").resize((26,21),Image.ANTIALIAS)
    render=ImageTk.PhotoImage(load)
    img=Button(home,image=render)
    img.image=render
    img.place(x=1130,y=3)
    img.configure(command=lambda:SearPro(searp,ppp))
    
    electro=Button(home)
    electro.place(relx=0.300,rely=0.06,width=130)
    electro.configure(text="Electronics",bg="brown",command=lambda:LoadProducts(Electronics))
    
    gro=Button(home)
    gro.place(relx=0.400,rely=0.06,width=130)
    gro.configure(text="Grocery",bg="brown",command=lambda:LoadProducts(Grocery))
    
    fash=Button(home)
    fash.place(relx=0.500,rely=0.06,width=130)
    fash.configure(text="Fashon",bg="brown")
    
    mc=Button(home)
    mc.place(relx=0.600,rely=0.06,width=130)
    mc.configure(text="My Cart",bg="brown",command=directmycart)
    
    
'''------------------------------------------------------------------clean funntion----------------------------------------------'''

def clean(firstname,lastname,email,password,password1,phone):
    print("clean")
    
    firstname.set('')
    lastname.set('')
    email.set('')
    password.set('')
    password1.set('')
    phone.set('')
       
    
'''-----------------------------------------enter all given registerd data  into a file------------------------------------------ '''
def enter(firstname,lastname,email,password,phone):
    print("save")
    
    with open('udata.csv' ,'a') as f:
        f.write('{},{},{},{},{}\n'.format(firstname.get(),lastname.get(),email.get(),password.get(),phone.get()))
        print("file  created...")
        logi()
        
        
'''---------------------------------------------------------checking function----------------------------------------------------'''

def check(firstname,lastname,email,password,password1,phone,chb1):
    print("Start checking...")
    e=email.get()
    p=password.get()
    p1=password1.get()
    cb1=chb1.get()
    t=False
    if not firstname.get():
        messagebox.showinfo("Warning!!!","Please enter firstname(require)!")
    else:
        if not e:
                 messagebox.showinfo("Warning!!!","Please enter E-mail(require)!")
        elif re.search("[-a-zA-Z0-9.`?{}]+@\w+\.\w",e):
            
                f=open("udata.csv")
                data=f.read()
                c=data.split("\n")
                for c1 in c:
                    c2=c1.split(",")
                    for c3 in c2:
                        if c3==e:
                           print("found")
                           t=True
                           messagebox.showinfo("Warning!!!", "This E-mail id is already used")
                           continue
                        else:
                           continue
              
                if not p:
                         messagebox.showinfo("Warning!!!","Please enter password(require)!")
                else:
                        if not p1:
                             messagebox.showinfo("Warning!!!","Please enter conform password(require)!")
                        elif p != p1:   
                             messagebox.showinfo("Warning!!!","Your password is not match!") 
                        else:
                            if not phone.get() :
                                messagebox.showinfo("Warning!!!","Please enter mobile number(require)!")
                            elif len(phone.get())!=10:
                                messagebox.showinfo("Warning!!!","Please enter a valid mobile number(require)!")
                                try:
                                    p = int(phone.get())
                                except ValueError:
                                    print("is not a number, please enter a number only")
                                    messagebox.showinfo("Warning!!!","Please enter number!")
                            elif cb1 != 1:
                                    messagebox.showinfo("Warning!!!","Please accecpt TERMS & CONDITIONS for registration")
                            else:
                                    enter(firstname,lastname,email,password,phone)
   
                                
        else:
            messagebox.showinfo("Warning!!!","Please enter a valid E-mail Id(require)!")
                                
    
'''---------------------------------------------------------------register funntion----------------------------------------------'''

def reg():
    
    print('register')
    global note
    global register
    
    note.tab(2,state="normal")
    note.tab(1,state="hidden")
    
    firstname=StringVar()
    lastname=StringVar(value='')
    email=StringVar()
    password=StringVar()
    password1=StringVar()
    phone=StringVar()
    chb1=IntVar()
    
    load=Image.open("regi.jpeg").resize((1340,660),Image.ANTIALIAS)
    render=ImageTk.PhotoImage(load)
    img=Label(register,image=render)
    img.image=render
    img.place(x=0,y=0)
    
    re=Frame(register)
    re.place(relx=0.12,rely=0.05,height=600,width=1000)
    re.configure(bg="grey")
    
    l=Label(re)
    l.place(relx=0.45,rely=0.05,height=50,width=200)
    l.config(text="**REGISTER**",bg="yellow",font=("times",20))
    
    fname=Label(re)
    fname.place(relx=0.20,rely=0.20)
    fname.configure(text="First Name",font=(11),fg="red",bg="grey")
    
    lname=Label(re)
    lname.place(relx=0.20,rely=0.28)
    lname.configure(text="Last Name",font=(11),fg="red",bg="grey")
    
    em=Label(re)
    em.place(relx=0.20,rely=0.36)
    em.configure(text="E-mail",font=(11),fg="red",bg="grey")
    
    pw=Label(re)
    pw.place(relx=0.20,rely=0.44)
    pw.configure(text="Password",font=(11),fg="red",bg="grey")
    
    pw1=Label(re)
    pw1.place(relx=0.20,rely=0.52)
    pw1.configure(text="ReType\nPassword",font=(11),fg="red",bg="grey")

    ph=Label(re)
    ph.place(relx=0.20,rely=0.62)
    ph.configure(text="Phone",font=(11),fg="red",bg="grey")
    
    
    fn=Entry(re)
    fn.place(relx=0.40,rely=0.20,relwidth=0.40)
    fn.configure(bg="white",fg="green",textvariable=firstname)
    
    
    ln=Entry(re)
    ln.place(relx=0.40,rely=0.28,relwidth=0.40)
    ln.configure(bg="white",fg="green",textvariable=lastname)
    
    em=Entry(re)
    em.place(relx=0.40,rely=0.36,relwidth=0.40)
    em.configure(bg="white",fg="green",textvariable=email)
    
    pw=Entry(re)
    pw.place(relx=0.40,rely=0.44,relwidth=0.40)
    pw.configure(bg="white",fg="green",show="*",textvariable=password)
    
    pw1=Entry(re)
    pw1.place(relx=0.40,rely=0.53,relwidth=0.40)
    pw1.configure(bg="white",fg="green",show="*",textvariable=password1)
    
    ph=Entry(re)
    ph.place(relx=0.40,rely=0.62,relwidth=0.40)
    ph.configure(bg="white",fg="green",textvariable=phone)
    
    
    cb1=Checkbutton(re)
    cb1.place(relx=0.20,rely=0.70)
    cb1.configure(text="T&C",fg="blue",variable=chb1,bg="grey")
    
    save=Button(re)
    save.place(relx=0.60,rely=0.80,height=30,width=65)
    save.configure(text="SAVE",bg="red",fg="black",command=lambda:check(firstname,lastname,email,password,password1,phone,chb1))
    
    clear=Button(re)
    clear.place(relx=0.45,rely=0.80,height=30,width=65)
    clear.configure(text="CLEAR",bg="brown",fg="blue",command=lambda:clean(firstname,lastname,email,password,password1,phone))
    
    cancel=Button(re)
    cancel.place(relx=0.30,rely=0.80,height=30,width=65)
    cancel.configure(text="CANCEL",bg="blue",fg="yellow",command=logi)
    
'''-----------------------------------------------------------warnig message funtion---------------------------------------------'''

def warning():
    print('cancel')
    msg=tkinter.messagebox.askyesno("Login page","Are you sure, youwant to cancel LOGIN?" )
    if msg==True:
        Mainpage()

'''----------------------------------------------------login data conformation  function-----------------------------------------'''
def conform(username,passw):
    p1=[]
    global h
    h=0
    username=username.get()
    password=passw.get()
    if re.search("[-a-zA-Z0-9.`?{}]+@\w+\.\w",username):
        c=open("udata.csv")
        ch=c.read()
        row=ch.split("\n")
        #print(len(row))
        for a in range (len(row)):
           # print("a is now=",a)
            if h==0:
               for row1 in row:
                    if re.search(username,row1):
                        #print(row1)
                        pa=row1.split(",")
                        #print(pa[3])
                        if pa[3]==password or pa[2]==password:
                            print("product loading...")
                            #p1.append(pa[0])
                            #p1.append(pa[1])
                            #p1.append(pa[2])
                            #print(p1)
                            f=open("login.txt",'w')
                            f.write("%s\n"  %pa)
                            f.close()
                    
                            h=1
                            homepage()
                            break
                            
                        else:
                           messagebox.showinfo("404","please enter correct username and password!!!")
                           h=1
                           break
                       
                        
                        
                    else:
                        if len(row)==a+1:
                            messagebox.showinfo("404","username not found!!!")
                            #print("not found username",a)
                            break
                        else:
                            continue
            else:
                break
            
           # messagebox.showinfo("404","please enter correct username and password")
        
    else:
        messagebox.showinfo("404","please enter correct username!!!")

'''-----------------------------------------------------------------login funtion-------------------------------------------------'''

def logi():
    global note
    global login
    global mainpage
    note.select(login)
    note.tab(1,state="normal")
    note.tab(2,state="hidden")
    
   
    load=Image.open("login2.jpg").resize((1340,660),Image.ANTIALIAS)
    render=ImageTk.PhotoImage(load)
    img=Label(login,image=render)
    img.image=render
    img.place(x=0,y=0)
    
    lo=Frame(login)
    lo.place(relx=0.26,rely=0.05,height=600,width=600)
    lo.configure(bg="grey")
    print("login")
    l=Label(lo)
    l.place(relx=0.45,rely=0.05,height=50,width=130)
    l.config(text="__LOG-in__",fg="red",bg="grey",font=("times",20))
    
    username=StringVar()
    passw=StringVar(value="nullhbkhd")
    
    un=Label(lo)
    un.place(relx=0.31,rely=0.25,height=20,width=110)
    un.config(text="User Name",fg="blue",bg="grey",font=(16))
    
    pw=Label(lo)
    pw.place(relx=0.31,rely=0.45,height=20,width=110)
    pw.config(text="Password",fg="blue",bg="grey",font=(16))
    
    user=Entry(lo)
    user.place(relx=0.32,rely=0.33,relwidth=0.35,relheight=0.05)
    user.configure(bg="white",textvariable=username)
    
    
    password=Entry(lo)
    password.place(relx=0.32,rely=0.53,relwidth=0.35,relheight=0.05)
    password.configure(bg="white",show="*",textvariable=passw)
    
    regi=Button(lo)
    regi.place(relx=0.30,rely=0.76,height=30,width=65)
    regi.configure(bg="black",fg="white",text="REGISTER",command=reg)
    
    cancel=Button(lo)
    cancel.place(relx=0.47,rely=0.76,height=30,width=65)
    cancel.configure(bg="red",fg="black",text="CANCEL",command=warning)
    
    log=Button(lo)
    log.place(relx=0.63,rely=0.76,height=30,width=65)
    log.configure(bg="green",fg="yellow",text="LOGIN",command=lambda:conform(username,passw))
    
'''--------------------------------------------------------------mainpage fnction-------------------------------------------------'''

def Mainpage():
    print("MAINPAGE")
    global note
    global mainpage
    global i
    
    note.tab(0,state="normal")
    note.tab(1,state="hidden")
    note.tab(3,state="hidden")
    
    i=Frame(mainpage)
    i.pack(side=TOP)
    note.tab(1,state="hidden")
    
    '''  image loading for main page advertizing'''
    load=Image.open("shopping1.jpeg").resize((1340,210),Image.ANTIALIAS)
    render=ImageTk.PhotoImage(load)
    img=Label(mainpage,image=render)
    img.image=render
    img.place(x=0,y=0)
    load=Image.open("home.png").resize((1340,400),Image.ANTIALIAS)
    render=ImageTk.PhotoImage(load)
    img1=Label(mainpage,image=render)
    img1.image=render
    img1.place(relx=0.0,rely=0.40)
    
    e=Button(mainpage)
    e.place(relx=0.01,rely=0.02,width=80)
    e.configure(text="Exit",bg="black",fg="red",font=("times",17),command=root2.destroy)
    
    ls=Button(mainpage)
    ls.place(relx=0.0,rely=0.33,width=1340)
    ls.configure(text="LOGIN/REGI.>>>",bg="red",fg="black",font=("times",17),command=logi)
    

'''--------------------------------------------------------------window creating--------------------------------------------------'''
global ppp
ppp=[]
root2=Tk()
root2.title("E-commers.")
root2.geometry("1350x680+0+10")

    
note = ttk.Notebook(root2,width=1340,height=670)
mainpage=Frame(note)
login=Frame(note)
register=Frame(note)
home=Frame(note)
ac=Frame(note)
item=Frame(note)
payment=Frame(note)
search=Frame(note)
notification=Frame(note)
cart=Frame(note)
orderd=Frame(note)

j=Frame(item)
j.pack()
k=Frame(payment)
k.pack()
sear=Frame(search)
sear.pack()
car=Frame(cart)
car.pack()
ca=Frame(cart)
ca.pack()
y=Frame(orderd)
y.pack()


note.add(mainpage,text="main", compound=TOP) #0
note.add(login,text="Login")                 #1
note.add(register,text="Register")           #2
note.add(home,text="Home")                   #3
note.add(ac,text="Account")                  #4
note.add(item,text="product")                #5
note.add(search,text="search list")          #6
note.add(payment,text="payment")             #7
note.add(notification,text="Notification")   #8
note.add(cart,text="My-Cart")                #9
note.add(orderd,text="My-Orderd")            #10

note.tab(1,state='hidden')  #loginpage
note.tab(2,state='hidden')  #registerpage
note.tab(3,state='hidden')  #homepage
note.tab(4,state='hidden')  #account
note.tab(5,state='hidden')  #loadproductpage
note.tab(6,state='hidden')  #searchpage
note.tab(7,state='hidden')  #checkoutpage
note.tab(8,state='hidden')  #notificationpage
note.tab(9,state='hidden')  #mycartpage
note.tab(10,state='hidden') #orderd


'''caling mainpage'''

f=os.path.isfile('login.txt')
if f:
    s=open('login.txt')
    a=s.read()
    print(a)
    homepage()
    s.close()
else:
    Mainpage()

#LoadProducts()
#checkout()


note.pack()
root2.mainloop()

