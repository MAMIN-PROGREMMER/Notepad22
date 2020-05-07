import pyautogui
from tkinter import *

root = Tk()
# Настройки Программы
# root.resizable( width = False , height = False )
root.geometry( '300x300' )
root.title( 'Notepad22 | By TOP4IK | Email: olyavyanov15@mail.ru' )
# Сама программа
def clear():
	field.delete(1.0, END)
field = Text( font = 'Consolas 10'  )
field.pack( pady = 20 )
# Кнопки
btnclearstr = Button( root,text = 'Очистить Абсолютно Все', command = clear )
btnclearstr.pack()
# defki
root.mainloop()
