from tkinter import *
from youtube import A
import pafy 
import time
from tkinter import messagebox
#############################
#this for window
############################
window =Tk()
window.title('                                                          >>>>>>>> sign in <<<<<<<<')
window.geometry('600x100+310+210')
window.configure(bd=5,relief='groove')
window.resizable(0,0)
window.iconbitmap('m.ico')

##############################
#this part programming 
###############################
vai=IntVar()
vai.set(0)
var=StringVar()
ent=StringVar()
zassw=StringVar()

            


def lang():
      hulk.set('english')
      bt.configure(text='Login')
      bt2.configure(text='Reset')
      bt3.configure(text='Exit')
      ch.configure(text='Check')
      red1.configure(text='Arabic')
      red2.configure(text='English')
      labmail.configure(text='E-mail:')
      labpass.configure(text='Password:')
      red1.configure(state='disable')

def arab():
      hulk.set('arabic')
      bt.configure(text='تسجيل ')
      bt2.configure(text='إعادة ')
      bt3.configure(text='خروج')
      ch.configure(text='تأكيد')
      red1.configure(text='عربية')
      red2.configure(text='إنجليزية')
      labmail.configure(text='الايميل :')
      labpass.configure(text='السر كلمة:')
      red2.configure(state='disable')
def game():
         if vai.get()==1 :
            bt.configure(state='normal')
            red1.configure(state='disable')
            red2.configure(state='disable')
            if hulk.get()=='arabic':
                   mshg=messagebox.showinfo('مروان','تم تطوير هذا البرنامج من قبل مروان ريغي ')
            else:
                  mshg=messagebox.showinfo('maroune','The program was developed by <<<<Righi Maroune>>>>')
         elif vai.get()==0 :
            bt.configure(state='disable')
            red1.configure(state='normal')
            red2.configure(state='normal')
def btn():
            if hulk.get()=='arabic':
                 if ent.get()=='maroune' and zassw.get()=='maroune12345':
                           var.set('بنجاح التسجيل تم')
                           msgb=messagebox.showinfo('Login','Login password=maroune12345 and E-mail=maroune .....')
                           from youtube import A
                           l=A()
                           l.hello()
                           window.destroy()
                 elif ent.get()=='' and zassw.get()=='':
                         labsh.configure(fg='red')
                         var.set('السر وكلمة الايميل ادخال ')

              
                 elif  zassw.get()=='':
                         labsh.configure(fg='yellow')
                         var.set('??? السر كلمة نسيت ')
                 elif  ent.get()=='':
                         labsh.configure(fg='yellow')
                         var.set('??? الايميل نسيت ')
                 else:
                        labsh.configure(fg='red')
                        var.set('??...المرور كلمة او الايميل في خطأ')        
                                
                    
            if hulk.get()=='english':
               
                 try:     
                    if ent.get()=='maroune' and zassw.get()=='maroune12345':
                           labsh.configure(fg='lightgreen')
                           var.set(' Welcome in your account')
                           msgb=messagebox.showinfo('Login','Login password=maroune12345 and E-mail=maroune .....')
                           x=str(ent.get())
                           from youtube import A
                           l=A()
                           l.hello()
                           window.destroy()
                    elif ent.get()=='' and zassw.get()=='':
                         labsh.configure(fg='yellow')
                         var.set('Enter email and password .....???? ')
                    elif  zassw.get()=='':
                         labsh.configure(fg='yellow')
                         var.set('Enter your password .....???? ')
                    elif  ent.get()=='':
                         labsh.configure(fg='yellow')
                         var.set('Enter your E-mail .....???? ')     
                         
                    else:
                        labsh.configure(fg='red')
                        var.set('Invalid email or password .....')
                 except:
                          labsh.configure(fg='red')
                          var.set('Error')
                     
   
#bt.place(x=533,y=5)
#bt2=Button(window,text='Reset',bg='black',fg='lightgreen',activebackground='lightgreen',activeforeground='black',command=bt2)
#bt2.place(x=533,y=35)
#bt3=Button(window,text='Exit',bg='black',fg='lightgreen',activebackground='red',command=bt3)
#bt3.place(x=538,y=65)
#ch=Checkbutton(window,text='Check',bd=0,fg='green',activeforeground='lightgreen',variable=vai,bg='black',activebackground='black',
#               command=game)
  
v='''def game():
   if vai.get()==1 :
      bt.configure(state='normal')
      red1.configure(state='disable')
      red2.configure(state='disable')
      

   elif vai.get()==0 :
      bt.configure(state='disable')
      red1.configure(state='normal')
      red2.configure(state='normal')
def btn():
   try:
      if  :      
           if ent.get()=='maroune' and zassw.get()=='maroune12345':
                  var.set(' Welcome in your account')
                  x=str(ent.get())
                  window.title('                                                         <<<<<<<Hello maroune>>>>>>        ')
           elif ent.get()=='' and zassw.get()=='':

                var.set('')

           else:
               var.set('Invalid email or password .....')
   except:
                 var.set('Error')'''
def bt2():
        
        var.set('')
        ent.set('')
        zassw.set('')
        red1.configure(state='normal')
        red2.configure(state='normal')
        vai.set(0)
        bt.configure(state='disable')
def bt3():
      if hulk.get()=='english':
            msg=messagebox.askquestion('Warning','Do You Want to Exit The Program ???')
            if msg=='yes':
               window.destroy()
            else:
                  pass
      elif hulk.get()=='arabic':
            msg=messagebox.askquestion('تحذير', 'تريد الخروج من البرنامج ')
            if msg=='yes':
               window.destroy()
            else:
                  pass
################################
#this part for disign 
###############################
logo=PhotoImage(file='anonimos.png')
lab=Label(window,image=logo)
lab.pack()
labmail=Label(window,text='E-mail:',bg='black',font=('times',12,'italic','bold'),fg='green')
labmail.place(x=10,y=20)

entmaile=Entry(window,
               bg='black',
               fg='red',
               font=('times',12,'bold'),textvariable=ent)
entmaile.place(x=70,y=22)


labpass=Label(window,text='Password:',bg='black',font=('times',12,'italic','bold'),fg='green')
labpass.place(x=274,y=20)
############################
labsh=Label(window,bg='black',fg='lightgreen',font=('times',16,'italic','bold'),
            textvariable=var)
labsh.place(x=190,y=60)



#############################"

entpass=Entry(window,
               bg='black',
               fg='red',
               font=('times',12,'bold'),textvariable=zassw,show='*')
entpass.place(x=350,y=22)
######################""
bt=Button(window,text='Login',bg='black',fg='lightgreen',activebackground='lightgreen',activeforeground='black',command=btn,state='disable')
bt.place(x=533,y=5)
bt2=Button(window,text='Reset',bg='black',fg='lightgreen',activebackground='lightgreen',activeforeground='black',command=bt2)
bt2.place(x=533,y=35)
bt3=Button(window,text='Exit',bg='black',fg='lightgreen',activebackground='red',command=bt3)
bt3.place(x=538,y=65)
ch=Checkbutton(window,text='Check',bd=0,fg='green',activeforeground='lightgreen',variable=vai,bg='black',activebackground='black',
               command=game)

ch.place(x=457,y=46)
red1=Radiobutton(window,text='Arabic',bg='black',fg='lightgreen',activebackground='lightgreen',activeforeground='black',command=arab,value=1)
red1.place(x=10,y=65)
red2=Radiobutton(window,text='English',bg='black',fg='lightgreen',activebackground='lightgreen',activeforeground='black',command=lang,value=5)
red2.place(x=68,y=65)
hulk=StringVar()
lab3=Label(window,bg='black',fg='lightgreen',font=('times',16,'italic','bold'),
            textvariable=hulk)
lab3.place(x=200,y=200)

############################"





window.mainloop()
