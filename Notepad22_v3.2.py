from tkinter import *
import subprocess
p = windown = Tk()
def nachalo():
    subprocess.kill(p)
    root = Tk()
# Настройки Программы
# root.resizable( width = False , height = False )
    root[ 'bg' ] = '#ccc'
    root.geometry( '300x300' )
    root.title( 'Notepad22 | By TOP4IK | Email: olyavyanov15@mail.ru' )
# Сама программа
    def clear():
	    field.delete(1.0, END)
    def ref():
        f=open("DocumentNotepad22.txt","w+")
        f.write(field.get(1.0, END))
        f.close()
    field = Text( font = 'Consolas 10' , bg = '#485460', fg='#d2dae2' )
    field.pack(pady=20, padx=90)
# Кнопки
    btnclearstr = Button( root,text = 'Очистить Абсолютно Все', command = clear , bg = '#485460' , fg = '#d2dae2' )
    btnclearstr.pack(padx=60)
    savebtn = Button( root,text = 'Сохранить', command = ref , bg = '#485460' , fg = '#d2dae2' )
    savebtn.pack()
# defki
    root.mainloop()
b = Button( windown,text='Начать',command = nachalo )
b.pack()
windown.mainloop()