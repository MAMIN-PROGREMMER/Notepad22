import pyautogui
from tkinter import *

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
def opensp()
	fl = open("C:/Users/Senya/Desktop/Справка по Notepad22.txt/","w+")
	fl.close()
field = Text( font = 'Consolas 10'  , bg = '#485460', fg='#d2dae2')
field.pack( pady = 20, padx = 90 )
# Кнопки
sprafka = Button( root, text = 'Справка', command = opensp ,  bg = '#485460' , fg = '#d2dae2' )
btnclearstr = Button( root,text = 'Очистить Абсолютно Все', command = clear , bg = '#485460' , fg = '#d2dae2' )
savebtn = Button( root,text = 'Сохранить', command = ref , bg = '#485460' , fg = '#d2dae2' )
btnclearstr.pack( padx = 60)
savebtn.pack()
sprafka.pack()
# defki
root.mainloop()
