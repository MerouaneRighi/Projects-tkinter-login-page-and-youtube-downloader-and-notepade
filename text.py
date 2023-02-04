from tkinter import *
import time
import pafy
import datetime


class TXT():
    def write(self):
        url = "https://youtu.be/ttvsn4yDoWA"
        window = Tk()
        window.geometry('600x500+400+50')
        window.iconbitmap('icon.ico')  # ICON Changed
        window.title('TEXT Editor')
        # "
        sb = Scrollbar(window, bg='black')
        sb.pack(side='right', fill='y')
        bar = Menu(window)
        file = Menu(bar, bg='black', fg='green', activebackground='black',
                    activeforeground='red', font=('times', 11, 'bold', 'italic'))
        edit = Menu(bar)
        form = Menu(bar)
        run = Menu(bar)
        option = Menu(bar)
        windo = Menu(bar)
        hel = Menu(bar)
        # "
        t = datetime.datetime.now().strftime('%x')
        bar.add_cascade(label='File', menu=file)
        bar.add_cascade(label='Edit', menu=edit)
        bar.add_cascade(label='Format', menu=form)
        bar.add_cascade(label='Run', menu=run)
        bar.add_cascade(label='options', menu=option)
        bar.add_cascade(label='Window', menu=windo)
        bar.add_cascade(label='Help', menu=hel)
        bar.add_cascade(label=t)
        #################################################
        file.add_command(label='New file')
        file.add_command(label='Open...')
        file.add_command(label='Open Module...')
        file.add_command(label='Recent Files')
        file.add_command(label='Save')
        file.add_command(label='Save As...')
        file.add_command(label='Save copy As...')
        file.add_command(label='Exit')

        #############################################################

        txt = Text(window, fg='green', bg='black', font=('ireal', 14, 'italic'),
                   highlightbackground='blue',
                   highlightcolor='red',
                   highlightthickness=2,
                   insertbackground='green',
                   insertborderwidth=5,
                   insertontime=100,
                   padx=20, pady=20,
                   spacing1=20,
                   wrap='word',
                   selectbackground='red',
                   selectforeground='white'
                   )
        txt.pack()
        txt.configure(yscrollcommand=sb.set)
        sb.configure(command=txt.yview)
        '''
        insert
        insertbackground='green'
        insertborderwidth=10
        inserttontime=100
        wrap='word',char
        txt.insert(INSERT,'DDos attak play')
        txt.insert(END,'DDos attak play')
        scrollbar
        sb.pack(side='right',fill='y') طوليا
        sb.pack(side='right',fill='y')على العرض 
        '''
        txt.insert(INSERT, url)

        window.configure(menu=bar)

        window.mainloop()


TXT().write()
