from tkinter import *
from tkinter import ttk
import pafy
#import pafy
window = Tk()
window.geometry('500x500+400+100')
window.title('Download Video')
window.iconbitmap('l.ico')

#########################################
# part programing
#####################


def url():

    v = str(var.get())
    url = pafy.new(v)
    down = url.getbest()
    h = down.get_filesize()


def download():
    v = str(var.get())
    url = pafy.new(v)
    down = url.getbest()
    h = down.get_filesize()
    if h < 1073741824:
        bt1.configure(bg='lightgreen', fg='black')
        l1.configure(fg='green')
        lis1.configure(fg='green')
        lis2.configure(fg='green')
        lis3.configure(fg='green')
        c.set(down.extension)
        z = h/1024
        mm = z/1024
        w = h/1024
        m = w//1024
        vv = mm-m
        j = vv*100
        pp = j//1
        p = pp*0.01
        f = m+p
        g = (f, 'MB')
        b.set(g)
        a.set(down.quality)

    else:
        bt1.configure(bg='red', fg='white')
        l1.configure(fg='red')
        z = h/1024
        mm = z/1024
        kl = mm/1024
        n = kl//1
        vv = kl-n
        j = vv*100
        pp = j//1
        p = pp*0.01
        f = n+p

        z = z/1024
        g = (f, 'GB')
        b.set(g)
        a.set(down.quality)
        c.set(down.extension)


def reset():
    a.set('')
    b.set('')
    c.set('')
    var.set('')
    com2.configure(values=(''))
    chek1.configure(state='normal')
    chek2.configure(state='normal')
    bt1.configure(bg='steelblue', fg='white')
    l1.configure(fg='steelblue')
    lis1.configure(fg='steelblue')
    lis2.configure(fg='steelblue')
    lis3.configure(fg='steelblue')


def audio():
    chek2.configure(state='disable')
    h = (var.get())
    url = pafy.new(h)
    lis = []
    streams = url.audiostreams
    # streams=url.streams
    n = 1
    for stream in streams:
        lis.extend([int(n), stream])
        n = n+1
    com2.configure(values=(lis))
    do.set('audio')


def video():
    chek1.configure(state='disable')
    h = (var.get())
    url = pafy.new(h)
    lis = []
    streams = url.streams
    # streams=url.streams
    n = 1
    for stream in streams:
        lis.extend([int(n), stream])
        n = n+1
    com2.configure(values=(lis))
    do.set('video')


def down():
    if do.get == 'audio':
        import pafy
        h = (var.get())
        url = pafy.new(h)
        l = url.audiostreams
        k = com.get()
        k = k-1
        print(l[k])
        print('start Download ', l[k])
        # n=l.index(k)
        # print(n)
        down = url.streams[k]
        # do.set(down)
        # hulk=do.get()
        down.download()
        print(down.download())
    if do.get == 'video':
        import pafy
        h = (var.get())
        url = pafy.new(h)
        l = url.audiostreams
        k = com.get()
        k = k-1
        print(l[k])
        print('start Download ', l[k])
        # n=l.index(k)
        # print(n)
        down = url.streams[k]
        # do.set(down)
        # hulk=do.get()
        down.download()
        print(down.download())


# ""https://www.youtube.com/watch?v=agBuBFbGZAQ https://youtu.be/ttvsn4yDoWA
'''logo=PhotoImage(file='anonimos.png')
label=Label(window,image=logo)
label.pack()'''
#########################
window.configure(bg='white')
# 'https://youtu.be/ttvsn4yDoWA'
label2 = Label(window, text='Download:', bd=2, fg='white', bg='steelblue',
               relief='groove', font=('arial', 20, 'bold', 'italic'))
label4 = Label(window, text='Selection:', bd=2, fg='white',
               bg='steelblue', relief='groove', font=('arial', 20, 'bold', 'italic'))
label3 = Label(window, text='Download Video From Youtube:', bd=2, fg='white',
               bg='steelblue', relief='groove', font=('arial', 20, 'bold', 'italic'))
label3.place(x=48.5, y=0)
label2.place(x=192, y=400)
label4.place(x=192, y=200)
label3 = Label(window, text='URL : ', bd=0, bg='steelblue',
               fg='white', relief='groove', font=('ireal', 11, 'italic'))
label3.place(x=4, y=450)
var = StringVar()
ent = Entry(window, bg='white', fg='steelblue', textvariable=var)
ent.place(x=40, y=450)
############################
# textvariable
###########################
a = StringVar()
b = StringVar()
c = StringVar()
# "
# part style
############################
l1 = Label(window, text='   o-------------o          o----------------o          o--------------o  ',
           bg='white', fg='steelblue',
           font=('arial', 14, 'bold', 'underline'))
l1.place(x=20, y=80)
#############################################
lis1 = Label(window, bg='white', fg='red', textvariable=a)
lis1.place(x=60, y=70)
lis2 = Label(window, bg='white', fg='red', textvariable=b)
lis2.place(x=390, y=70)
lis3 = Label(window, bg='white', fg='red', textvariable=c)
lis3.place(x=230, y=70)
bt1 = Button(window, command=download, text='Submet', bg='steelblue',
             fg='white', activebackground='red', activeforeground='white')
bt1.place(x=208, y=446)
#############################################
li1 = Label(window, text='Quality', bg='steelblue', fg='white',
            font=('arial', 14, 'bold', 'underline', 'italic'))
li1.place(x=50, y=40)
li2 = Label(window, text='Extension', bg='steelblue', fg='white',
            font=('arial', 14, 'bold', 'underline', 'italic'))
li2.place(x=200, y=40)
li3 = Label(window, text='File-Size', bg='steelblue', fg='white',
            font=('arial', 14, 'bold', 'underline', 'italic'))
li3.place(x=370, y=40)
bt2 = Button(window, text='Reset', bg='steelblue', fg='white',
             activebackground='red', activeforeground='white', command=reset)
bt2.place(x=170, y=446)
bt4 = Button(window, text='Download', bg='steelblue', fg='white',
             activebackground='red', activeforeground='white', command=down)
bt4.place(x=260, y=446)

labe5 = Label(window, text='TYPE : ', bd=0, bg='steelblue',
              fg='white', relief='groove', font=('ireal', 11, 'italic'))
labe5.place(x=4, y=300)

labe4 = Label(window, text='Select Quality : ', bd=0, bg='steelblue',
              fg='white', relief='groove', font=('ireal', 11, 'italic'))
labe4.place(x=242, y=300)
sst = StringVar()
chek1 = Checkbutton(window, text='audio',
                    bg='white', fg='steelblue',
                    activebackground='red', activeforeground='white',
                    font=('arial', 11, 'italic', 'bold', 'underline'),
                    command=audio,



                    )
chek1.place(x=60, y=295)
chek2 = Checkbutton(window, text='Video', bg='white', fg='steelblue',
                    activebackground='red',
                    activeforeground='white',
                    font=('arial', 11, 'italic', 'bold', 'underline'),
                    command=video,
                    )

chek2.place(x=130, y=295)
com = IntVar()
com2 = ttk.Combobox(window, textvariable=com)
com2.place(x=350, y=299)
do = StringVar()
labe = Label(window, textvariable=do)
labe.place(x=500, y=500)


window.mainloop()
