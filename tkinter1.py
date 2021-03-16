# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import tkinter as tk
import tkinter.messagebox
def click():
    tkinter.messagebox.showinfo(title = '提示',message = '好痛')
window =tk.Tk()
window.title("榆傑的第一個GUI程式")
window.geometry("300x300")
label = tk.Label(window,text = "我的GUI",bg = "#05A",fg = "#AAA")
label.pack()
entry = tk.Entry(window,width = 50)
entry.pack()
button = tk.Button(window,text = "按鈕",command = click)
button.pack()
window.mainloop()