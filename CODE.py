from tkinter import *
import math
from pygame import mixer
import speech_recognition
from functools import reduce
mixer.init()

def click(value):
    ex=entryfield.get()
    answer=' '
    try:
        if value=="C":
            
            ex=ex[0:len(ex)-1]
            entryfield.delete(0,END)
            entryfield.insert(0,ex)
            return

        elif value=="CE":
            entryfield.delete(0,END)

        elif value=='√':
            answer=math.sqrt(eval(ex))

        elif value=="π":
            answer=math.pi

        elif value=='cosθ':
            answer=math.cos(math.radians(eval(ex)))

        elif value=='tanθ':
            
            answer=math.tan(math.radians(eval(ex)))

        elif value=='sinθ':
            answer=math.sin(math.radians(eval(ex)))
            
        elif value=="2π":
            answer=(math.pi)*2

        elif value == 'secθ':
            answer = 1/(math.cos(math.radians(eval(ex))))

        elif value == 'cosecθ':
            answer = 1/(math.sin(math.radians(eval(ex))))

        elif value == 'cotθ':
            answer = 1/(math.tan(math.radians(eval(ex))))

        elif value==chr(8731):
            answer=eval(ex)**(1/3)

        elif value=='x\u02B8':
            entryfield.insert(END,'**')
            return

        elif value=='x\u00B3':
            answer=eval(ex)**3

        elif value=='x\u00B2':
            answer=eval(ex)**2

        elif value=='ln':
            answer=math.log(eval(ex))

        elif value=='deg':
            answer=math.degrees(eval(ex))

        elif value=='rad':
            answer=math.radians(eval(ex))
        
        elif value=='e':
            answer=math.e

        elif value=='log₁₀':
            answer=math.log10(eval(ex))
            return
        
        elif value=='X!':
            answer=math.factorial(eval(ex))
        elif value=='%':
            answer=eval(ex)/100
             
            
        elif value==chr(247):
            entryfield.insert(END,'/')
            return
        
        elif value=='=':
            answer=eval(ex)
        
        
        else:
            entryfield.insert(END,value)

            return
        
        entryfield.delete(0,END)
        entryfield.insert(0,answer)

    except SyntaxError:
        pass
#voice input
def add(*a):
    return sum(a)
def sub(*a):
    s=reduce(lambda x,y:x-y,a)
    return s
def mul(*a):
    product=reduce(lambda x,y:x*y,a)
    return product
def div(a,b):
    return a/b
def mod(a,b):
    return a%b
def lcm(*a):
    lc=reduce(lambda x,y:math.lcm(x,y),a)
    return lc
def hcf(*a):
    gc=reduce(lambda x,y:math.gcd(x,y),a)
    return gc


operations={'ADD':add,'ADDITION':add,'SUM':add,'PLUS':add,'+':add,
            'SUBTRACTION':sub , 'DIFFERENCE':sub , 'MINUS':sub , 'SUBTRACT':sub,
            'PRODUCT': mul, 'MULTIPLICATION': mul,'MULTIPLY': mul,'INTO':mul,
            'DIVISION': div, 'DIV': div, 'DIVIDE': div,
            'LCM':lcm , 'HCF':hcf,
            'MOD':mod ,'REMAINDER':mod , 'MODULUS':mod}


def findNumbers(t):
    l=[]
    for num in t:
        try:
            l.append(int(num))
        except ValueError:
            pass
    return l


def audio():
    mixer.music.load('music1.mp3')
    mixer.music.play()
    sr=speech_recognition.Recognizer()
    with speech_recognition.Microphone() as m:
        try:
            sr.adjust_for_ambient_noise(m,duration=0.2)
            voice=sr.listen(m)
            text=sr.recognize_google(voice)
            mixer.music.load('music2.mp3')
            mixer.music.play()
            text_list=text.split()
            for word in text_list:
                if word.upper() in operations.keys():
                    l=findNumbers(text_list)
                    
                    result=operations[word.upper()](*l) #mul(*arg)
                    entryfield.delete(0,END)
                    entryfield.insert(END,result)

                else:
                    pass


        except:
            pass

root=Tk()#main window
root.title('SCIENTIFIC CALCULATOR')
root.config(bg='black')
root.geometry('684x486+100+100')

logo=PhotoImage(file='logo.png')
logolabel=Label(root,image=logo,bg='white')
logolabel.grid(row=0,column=0)

micimage=PhotoImage(file='microphone.png')
micbutton=Button(root,image=micimage,bg='black',bd=0,activebackground='white',command=audio)
micbutton.grid(row=0,column=7)

entryfield=Entry(root,font=('arial',20,'bold'),bg='black',fg='white',bd=10,relief=SUNKEN,width=27)
entryfield.grid(row=0,column=2,columnspan=5)
button_text_list = ["C", "CE", "√", "+", "π", "sinθ", "cosθ", "tanθ",
                    "1", "2", "3", "-", "2π", "cosecθ", "secθ", "cotθ",
                    "4", "5", "6", "*", chr(8731), "x\u02b8", "x\u00B3", "x\u00B2",
                    "7", "8", "9", chr(247), "ln", "deg", "rad", "e",
                    "0", ".", "%", "=", "log₁₀", "(" ,")", "X!"]

rowval=1
columnval=0
for i in button_text_list:  
    button=Button(root,width=5,height=2,relief=SUNKEN,text=i,bg='white',fg='black',font=('arial',18,'bold'),activebackground='white',command= lambda button=i:click(button))
    button.grid(row=rowval,column=columnval,pady=1,padx=1)
    columnval+=1
    if columnval>7:
        rowval+=1
        columnval=0

btn1=Button(root,width=5,height=2,relief=SUNKEN,text='shift',bg='black',fg='white',font=('arial',18,'bold'),activebackground='white',command=lambda btn1='shift':root2())
btn1.grid(row=0,column=0)


btn=Button(root,width=5,height=2,relief=SUNKEN,text='const',bg='black',fg='white',font=('arial',18,'bold'),activebackground='white',command=lambda btn='const':root1())
btn.grid(row=0,column=1)

def root2():#shift window
    
    root2=Toplevel()
    root2.config(bg='black')
    root2.title('SCIENTIFIC CALCULATOR')
    root2.geometry('684x486+100+100')
    
    logo=PhotoImage(file='logo.png')
    logolabel=Label(root2,image=logo,bg='black')
    logolabel.image=logo
    logolabel.grid(row=0,column=0)
    
    
    entryfield=Entry(root2,font=('arial',20,'bold'),bg='black',fg='white',bd=5,relief=SUNKEN,width=30)
    entryfield.grid(row=0,column=1,columnspan=8)
    
    buttons_list = ["C", "CE", "√", "+", "π", "asinθ", "acosθ", "atanθ",
                "7", "8", "9", "*", chr(8731), "acosecθ", "asecθ", "acotθ",
                "4", "5", "6", "-", "2π", "sinh", "cosh", "tanh",
                "1", "2", "3", chr(247), "ln", "deg", "rad", "e",
                "0", ".", "%", "=", "log₁₀", "(" ,")", "X!"]

    def click2(value):
        ex=entryfield.get()
        answer=' '
        try:
            if value=="C":
            
                ex=ex[0:len(ex)-1]
                entryfield.delete(0,END)
                entryfield.insert(0,ex)
                return

            elif value=="CE":
                entryfield.delete(0,END)

            elif value=='√':
                answer=math.sqrt(eval(ex))

            elif value=="π":
                answer=math.pi

            elif value=='acosθ':
                answer=math.degrees(math.acos((eval(ex))))

            elif value=='atanθ':
                answer=math.degrees(math.atan((eval(ex))))

            elif value=='asinθ':
                answer= math.degrees(math.asin((eval(ex))))

            elif value=='acosecθ':
                answer= math.degrees(math.asin(1/(eval(ex))))

            elif value=='asecθ':
                answer= math.degrees(math.acos(1/(eval(ex))))

            elif value=='acotθ':
                answer= math.degrees(math.atan(1/(eval(ex))))

            elif value=='sinh':
                answer=math.sinh(eval(ex))
            
            elif value=='cosh':
                answer=math.cosh(eval(ex))

            elif value=='tanh':
                answer=math.tanh(eval(ex))
            
            elif value=="2π":
                answer=(math.pi)*2

            elif value==chr(8731):
                answer=eval(ex)**(1/3)

            elif value=='x\u02B8':
                entryfield.insert(END,'**')
                return

            elif value=='x\u00B3':
                answer=eval(ex)**3

            elif value=='x\u00B2':
                answer=eval(ex)**2

            elif value=='ln':
                answer=math.log(eval(ex))

            elif value=='deg':
                answer=math.degrees(eval(ex))

            elif value=='rad':
                answer=math.radians(eval(ex))
            
            elif value=='e':
                answer=math.e

            elif value=='log₁₀':
                answer=math.log10(eval(ex))
            
            elif value=='X!':
                answer=math.factorial(eval(ex))
                
            elif value==chr(247):
                entryfield.insert(END,'/')
                return
            
            elif value=='=':
                answer=eval(ex)
            
                

            else:
                entryfield.insert(END,value)

                return
            
            
            
        except SyntaxError:
            pass

        entryfield.delete(0,END)
        entryfield.insert(0,answer)
    
    rowval=1
    columnval=0
    for i in buttons_list:
            button=Button(root2,width=5,height=2,relief=SUNKEN,text=i,bg='black',fg='white',font=('arial',18,'bold'),activebackground='black',command=lambda button=i: click2(button))
            
            button.grid(row=rowval,column=columnval,pady=1,padx=1)
            columnval+=1
            if columnval>7:
                    rowval+=1
                    columnval=0
    

    root2.mainloop()

def root1():#constant window
    
    root1=Toplevel()
    root1.title('CONSTANT VALUES')
    root1.config(bg='black')
    root1.geometry('486x486+100+100')
    logo=PhotoImage(file='logo.png')
    logolabel=Label(root1,image=logo,bg='black')
    logolabel.grid(row=0,column=0)
    
    entryfield=Entry(root1,font=('arial',20,'bold'),bg='black',fg='white',bd=5,relief=SUNKEN,width=25)
    entryfield.grid(row=0,column=1,columnspan=4)
    
    const=['mp','mn','me','R','F','\u03BC','\u03B5','h','q','c']
    
    rowval=1
    columnval=0
    for i in const:
            button=Button(root1,width=5,height=2,relief=SUNKEN,text=i,bg='black',fg='white',font=('arial',18,'bold'),activebackground='black',command=lambda button=i: click1(button))
            button.grid(row=rowval,column=columnval,pady=1,padx=1)
            columnval+=1
            if columnval>4:
                    rowval+=1
                    columnval=0
    def click1(value):
        try:
            entryfield.delete(0,END)
            if value=='mp':
                entryfield.insert(0,'1.6726*10^-27')

            elif value=='mn':
                entryfield.insert(0,'1.6749*10^-27')

            elif value=='me':
                entryfield.insert(0,'9.1093*10^-31')

            elif value=='R':
                entryfield.insert(0,'8.3144')

            elif value=='F':
                entryfield.insert(0,'96485.33')

            elif value=='\u03BC':
                entryfield.insert(0,'4π*10^-7')

            elif value=='\u03B5':
                entryfield.insert(0,'8.854*10^-12')

            elif value=='h':
                entryfield.insert(0,'6.626* 10^-34')
            elif value=='q':
                entryfield.insert(0,'1.62*10^-19')
            elif value=='c':
                entryfield.insert(0,'3*10^8')

        except SyntaxError:
            pass

        
        

    root1.mainloop()
root.mainloop()