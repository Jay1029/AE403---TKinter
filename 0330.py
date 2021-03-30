import tkinter as tk
window = tk.Tk()
window.geometry('300x300')
window.title('單選按鈕')
t = tk.StringVar()
def selection():
    label.config(text = '我喜歡'+t.get())
label = tk.Label(window, bg='#f00', text='尚未選擇')
label.pack()
radio = tk.Radiobutton(window,text = 'Minecraft Python',variable =t,value = 'MP',command = selection)
radio.pack()
radio = tk.Radiobutton(window,text = 'Minecraft Python',variable =t,value = 'MP',command = selection)
radio.pack()
window.mainloop()