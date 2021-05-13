 
#颜色选择器
from tkinter import *
import tkinter.colorchooser as cc    #给导入的包指定一个别名
 
class App:
	def __init__(self,master):
		frame=Frame(master)
		frame.pack()
		button=Button(frame,text='选择颜色',command=self.ask_color)
		button.grid(row=0,column=0)
	def ask_color(self):
		(rgb,hx)=cc.askcolor()       #************
		print('rgb='+str(rgb)+' hx='+hx)
		
root=Tk()
app=App(root)
root.mainloop()
