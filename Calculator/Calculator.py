#Calculator

import tkinter as container

from tkinter import *
from tkinter.font import Font
from tkinter import ttk

windObj=container.Tk(className="Calculator",useTk=1)
windObj.title("Calculator")
windObj.grid_columnconfigure((0,1,2,3),weight=1,uniform="column")


menu=["Simplistic","Scienctific","History"]
operators=["/","*","+","-","%"]
number=["1","2","3","4","5","6","7","8","9","0"]
extraChar=["C","=","(",")","x"]
colorPalette=["#ffffff","#f0f8ff","#b0d0ed","#8fd3fe","#6ac5ef","#b5e2ff","#296d98","#FFDF00","#000000"]
fontList=[(Font(family="Calibri",size=12)),(Font(family="Calibri",size=15)),(Font(family="Calibri",size=17,weight="bold"))]

mainFrame=Frame(windObj,bg=colorPalette[1],highlightbackground=colorPalette[1],highlightthickness=0,height=542,width=402)
menuFrame=Frame(windObj,bg=colorPalette[1],highlightbackground=colorPalette[1],highlightthickness=0,height=30,width=4010)

class Windows:
 
  
  def __init__(self):
   self.height=413
   self.width=428

  #Container_Layout Management Code
  def layout(self):
   #windObj.geometry("450x400")
   windObj.minsize(self.width,self.height)
   windObj.maxsize(self.width,self.height)
   windObj.config(bg=colorPalette[1])
  
  def quit(self):
   windObj.destroy()
  
  def mainkeyControls(self):
   windObj.bind("<Control-q>",lambda event: quit())


class Component:
  
  
  def __init__(self):
   self.objF=[] 
  
  
  def frameGen(self):
   for i in range(6):
    self.objF.append(Frame(mainFrame,bg=colorPalette[1],highlightbackground=colorPalette[1],highlightthickness=0,width=400,height=80))
  
  #Input Controller Code
  def entry(self,wd):
   global eObj
   eObj=Entry(self.objF[0],width=wd,borderwidth=0,font=fontList[1],exportselection=1,bg=colorPalette[1])
   eObj.grid(row=0,column=0,columnspan=4,padx=0,pady=10)
   self.objF[0].grid(row=0,column=0,columnspan=4)

  #Button Controller Code
  def buttonFrame(self):
   obj=[] 

   obj.append(Button(self.objF[1],text=number[0],padx=45,pady=18,command= lambda: self.input(number[0]),bg=colorPalette[1],activebackground=colorPalette[2],font=fontList[0],relief=GROOVE))
   obj.append(Button(self.objF[1],text=number[1],padx=45,pady=18,command= lambda: self.input(number[1]),bg=colorPalette[1],activebackground=colorPalette[2],font=fontList[0],relief=GROOVE))
   obj.append(Button(self.objF[1],text=number[2],padx=45,pady=18,command= lambda: self.input(number[2]),bg=colorPalette[1],activebackground=colorPalette[2],font=fontList[0],relief=GROOVE))
   obj.append(Button(self.objF[1],text=number[9],padx=45,pady=18,command= lambda: self.input(number[9]),bg=colorPalette[1],activebackground=colorPalette[2],font=fontList[0],relief=GROOVE))
   
   obj.append(Button(self.objF[2],text=number[3],padx=45,pady=18,command= lambda: self.input(number[3]),bg=colorPalette[1],activebackground=colorPalette[2],font=fontList[0],relief=GROOVE))
   obj.append(Button(self.objF[2],text=number[4],padx=45,pady=18,command= lambda: self.input(number[4]),bg=colorPalette[1],activebackground=colorPalette[2],font=fontList[0],relief=GROOVE))
   obj.append(Button(self.objF[2],text=number[5],padx=45,pady=18,command= lambda: self.input(number[5]),bg=colorPalette[1],activebackground=colorPalette[2],font=fontList[0],relief=GROOVE))
   obj.append(Button(self.objF[2],text=extraChar[0],padx=45,pady=18,command=lambda: self.clear(),bg=colorPalette[1],activebackground=colorPalette[2],font=fontList[0],relief=GROOVE))
   
   obj.append(Button(self.objF[3],text=number[6],padx=45,pady=18,command= lambda: self.input(number[6]),bg=colorPalette[1],activebackground=colorPalette[2],font=fontList[0],relief=GROOVE))
   obj.append(Button(self.objF[3],text=number[7],padx=45,pady=18,command= lambda: self.input(number[7]),bg=colorPalette[1],activebackground=colorPalette[2],font=fontList[0],relief=GROOVE))
   obj.append(Button(self.objF[3],text=number[8],padx=45,pady=18,command= lambda: self.input(number[8]),bg=colorPalette[1],activebackground=colorPalette[2],font=fontList[0],relief=GROOVE))
   obj.append(Button(self.objF[3],text=operators[0],padx=45,pady=18,command= lambda: self.input(operators[0]),bg=colorPalette[1],activebackground=colorPalette[2],font=fontList[0],relief=GROOVE))
   
   obj.append(Button(self.objF[4],text=operators[1],padx=45,pady=18,command= lambda: self.input(operators[1]),bg=colorPalette[1],activebackground=colorPalette[2],font=fontList[0],relief=GROOVE))
   obj.append(Button(self.objF[4],text=operators[2],padx=45,pady=18,command= lambda: self.input(operators[2]),bg=colorPalette[1],activebackground=colorPalette[2],font=fontList[0],relief=GROOVE))
   obj.append(Button(self.objF[4],text=operators[3],padx=47,pady=18,command= lambda: self.input(operators[3]),bg=colorPalette[1],activebackground=colorPalette[2],font=fontList[0],relief=GROOVE))
   obj.append(Button(self.objF[4],text=extraChar[1],padx=45,pady=18,command= lambda: RPN().output(eObj),bg=colorPalette[1],activebackground=colorPalette[2],font=fontList[0],relief=GROOVE))
   
   obj.append(Button(self.objF[5],text=extraChar[2],padx=47,pady=18,command=lambda: self.input(extraChar[2]),bg=colorPalette[1],activebackground=colorPalette[2],font=fontList[0],relief=GROOVE))   
   obj.append(Button(self.objF[5],text=extraChar[3],padx=47,pady=18,command=lambda: self.input(extraChar[3]),bg=colorPalette[1],activebackground=colorPalette[2],font=fontList[0],relief=GROOVE))
   obj.append(Button(self.objF[5],text=operators[4],padx=43,pady=18,command= lambda: self.input(operators[4]),bg=colorPalette[1],activebackground=colorPalette[2],font=fontList[0],relief=GROOVE))
   obj.append(Button(self.objF[5],text=extraChar[4],padx=45,pady=18,command=lambda: self.cross(),bg=colorPalette[1],activebackground=colorPalette[2],font=fontList[0],relief=GROOVE))   
   t=1
   for i in range(5):
     for j in range(4):
       obj[t-1].grid(row=0,column=j)
       t=t+1
     self.objF[i+1].grid(row=(i+1),column=0,columnspan=3,sticky=W)
   mainFrame.grid(row=1,column=0,columnspan=3,rowspan=6)
   
  def clear(self):
   eObj.delete(0,END)  
  
  def keyControls(self):
   windObj.bind("<Control-x>",lambda event: self.cross())
  
  def input(self,t):
   current=str(eObj.get())
   self.clear() 
   eObj.insert(0,current+t)

  def cross(self):
   current=str(eObj.get())[:-1]
   eObj.delete(0,END)
   eObj.insert(0,current)
    
  def compEvent(self):
   self.frameGen()
   self.entry(40)
   self.buttonFrame()
   self.keyControls()




class RPN:

  def __init__(self):
   self.tempVar=""
   self.num=[]
   self.st=Stack()

  def output(self,e):
   self.getTokens(e.get()) 
   #print(self.num)
   e.delete(0,END)
   e.insert(0,Evaluation(self.num).result())
   

  def getTokens(self,entry):
   self.parser("(")
   for i in entry:
     self.parser(i)
   self.parser(")")
   

  def parser(self,x):
   if(not self.isWhiteSpace(x)):
     if(self.isPrecedence(x)==1):
        self.tempVar=self.tempVar+x
     elif(self.isPrecedence(x)==5):
       self.st.push(x)
     elif(self.isPrecedence(x)==4):
       if(not self.isNull()):
        self.num.append(self.tempVar)
        self.tempVar=""
       if(self.isLowerPrecedence(self.st,x)):
         self.num.append(self.st.delete())
         self.st.push(x)
       else:
         self.st.push(x)
     elif(self.isPrecedence(x)==3):
       if(not self.isNull()):
        self.num.append(self.tempVar)
        self.tempVar=""
       if(self.isLowerPrecedence(self.st,x)):
         self.num.append(self.st.delete())
         self.st.push(x)
       else:
         self.st.push(x)
     else:
       if(not self.isNull()):
        self.num.append(self.tempVar)
        self.tempVar=""
       self.remove()

  def isNull(self):
   if(self.tempVar==""):
       return True
   return False
  
  def isWhiteSpace(self,x):
    if(x==" "):
     return True
    return False
  
  def isLowerPrecedence(self,st,x):
    if((self.isPrecedence(st.peek())>=self.isPrecedence(x))and(st.peek()!='(')):
     return True
    return False

  def remove(self):
   while((self.st.peek()!=('('))or(self.st.isEmpty())):
     #print(self.st.peek())
     self.num.append(self.st.delete())
   #print(self.st.delete())
  
  def isPrecedence(self,x):
    if(x=='('):
     return 5
    elif((x==operators[1])or(x==operators[0])or(x==operators[4])):
     return 4
    elif((x==operators[2])or(x==operators[3])):
     return 3
    elif(x==')'):
     return 2
    else:
     return 1


class Error:
  
  def mathError(self,exp):
   exp.clear()
   exp.append("NaN")

  def ioError(self,x):
   try:
    return float(x)
   except:
    return int(x)

class Evaluation:
  
  def __init__(self,num):
    self.exp=num
    self.err=Error()

  def isOperator(self,i):
     tempC=0
     for j in operators:
        if(i==j):
          return tempC
        tempC=tempC+1
 
  def result(self):
    i=0
    while(len(self.exp)>1):
        if(self.isOperator(self.exp[i])==0):
          try:
           self.exp[i-2]=str((self.err.ioError(self.exp[i-2]))/(self.err.ioError(self.exp[i-1])))
           self.cleanUp(i)
          except:
           self.err.mathError(self.exp)
           break
          i=0
        elif(self.isOperator(self.exp[i])==1):
          self.exp[i-2]=str((self.err.ioError(self.exp[i-2]))*(self.err.ioError(self.exp[i-1])))
          self.cleanUp(i)
          i=0
        elif(self.isOperator(self.exp[i])==2):
          self.exp[i-2]=str((self.err.ioError(self.exp[i-2]))+(self.err.ioError(self.exp[i-1])))
          self.cleanUp(i)
          i=0
        elif(self.isOperator(self.exp[i])==3):
          self.exp[i-2]=str((self.err.ioError(self.exp[i-2]))-(self.err.ioError(self.exp[i-1])))
          self.cleanUp(i)
          i=0
        elif(self.isOperator(self.exp[i])==4):
          self.exp[i-2]=str((self.err.ioError(self.exp[i-2]))%(self.err.ioError(self.exp[i-1])))
          self.cleanUp(i)
          i=0
        i=i+1
    return self.exp

  def cleanUp(self,i):
   self.exp.pop(i)
   self.exp.pop(i-1)

class Stack:
  
  def __init__(self):
   self.stk=[]
   self.top=-1

  def push(self,x):
   self.top=self.top+1
   self.stk.append(x)

  def delete(self):
   if(self.isEmpty()):
     return "Error"
   self.top=self.top-1
   return self.stk.pop()

  def peek(self):
   if(self.isEmpty()):
     return "Error"
   return self.stk[self.top]
  
  def isEmpty(self):
   if(self.top<0):
    return True
   return False
  
class Menu:
  
  def __init__(self):
    return

  def option(self):
    inp=StringVar()
    om=ttk.OptionMenu(menuFrame,inp,menu[0],*menu)
    style=ttk.Style()
    style.configure("TMenubutton",background=colorPalette[1],selectbackground=colorPalette[2],foreground="#000000",highlightthickness=0,bd=0,font=fontList[2])
    om["menu"].config(relief=FLAT,borderwidth=1,activeborderwidth=2,activebackground=colorPalette[2],bg=colorPalette[1],selectcolor=colorPalette[1],activeforeground=colorPalette[8])
    om.pack(side=LEFT)
      
  def menuEvent(self):
    self.option()
    menuFrame.grid(row=0,column=2,columnspan=3)
    

def mainWindow():
 Windows().layout() 
 Windows().mainkeyControls()
 Menu().menuEvent()
 Component().compEvent()
 windObj.mainloop()


mainWindow()